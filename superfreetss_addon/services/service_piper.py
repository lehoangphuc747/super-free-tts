import sys
import os
import subprocess
import json
import io
import threading
import time
from typing import List, Optional

from superfreetss_addon import voice
from superfreetss_addon import service
from superfreetss_addon import errors
from superfreetss_addon import constants
from superfreetss_addon import languages
from superfreetss_addon import logging_utils

logger = logging_utils.get_child_logger(__name__)

class PiperProcessManager:
    def __init__(self):
        self._process = None
        self._current_model = None
        self._lock = threading.Lock()
        self._timer = None
        self._timeout = 120 # 2 minutes

    def get_process(self, executable_path, model_path):
        with self._lock:
            # If model changed, or binary changed, kill existing process
            if self._process and self._current_model != model_path:
                self.stop_locked()
            
            # Start process if not running
            if self._process is None or self._process.poll() is not None:
                startupinfo = None
                if os.name == 'nt':
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                
                cwd = os.path.dirname(executable_path)
                # We do NOT specify --output_file here, we will specify it per-request in JSON
                cmd = [executable_path, '--model', model_path, '--json-input']
                
                logger.info(f"Starting persistent Piper process: {' '.join(cmd)}")
                self._process = subprocess.Popen(
                    cmd,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    startupinfo=startupinfo,
                    cwd=cwd,
                    bufsize=1, # Line buffered
                    text=False # We handle encoding manually
                )
                self._current_model = model_path
                
                # Drain stderr in a separate thread to prevent deadlock
                def drain_stderr(pipe):
                    try:
                        while True:
                            line = pipe.readline()
                            if not line: break
                            logger.debug(f"Piper Stderr: {line.decode('utf-8', errors='ignore').strip()}")
                    except: pass
                
                t = threading.Thread(target=drain_stderr, args=(self._process.stderr,), daemon=True)
                t.start()

            self._reset_timer_locked()
            return self._process

    def _reset_timer_locked(self):
        if self._timer:
            self._timer.cancel()
        self._timer = threading.Timer(self._timeout, self.stop)
        self._timer.start()

    def stop(self):
        with self._lock:
            self.stop_locked()

    def stop_locked(self):
        if self._process:
            logger.info(f"Stopping persistent Piper process for model: {self._current_model}")
            try:
                self._process.stdin.close()
                self._process.terminate()
                # Wait a bit then kill if necessary
                # self._process.wait(timeout=2)
            except:
                try: self._process.kill()
                except: pass
            self._process = None
            self._current_model = None
        if self._timer:
            self._timer.cancel()
            self._timer = None

# Global manager instance
_piper_manager = PiperProcessManager()

class PiperTTS(service.ServiceBase):
    CONFIG_EXECUTABLE_PATH = 'executable_path'
    CONFIG_MODELS_PATH = 'models_path'

    def __init__(self):
        service.ServiceBase.__init__(self)

    @property
    def service_type(self) -> constants.ServiceType:
        return constants.ServiceType.tts

    @property
    def service_fee(self) -> constants.ServiceFee:
        return constants.ServiceFee.free

    def configuration_options(self):
        return {
            self.CONFIG_EXECUTABLE_PATH: ('file', 'Piper Executable (*.exe);;All Files (*)'),
            self.CONFIG_MODELS_PATH: ('directory', 'Select Models Directory')
        }

    def voice_list(self) -> List[voice.TtsVoice_v3]:
        models_path = self.get_configuration_value_optional(self.CONFIG_MODELS_PATH, '')
        if not models_path or not os.path.exists(models_path):
            return []

        voices = []
        try:
            # Scan for .onnx.json files
            for filename in os.listdir(models_path):
                if filename.endswith('.onnx.json'):
                    json_path = os.path.join(models_path, filename)
                    onnx_filename = filename.replace('.json', '')
                    onnx_path = os.path.join(models_path, onnx_filename)
                    
                    if not os.path.exists(onnx_path):
                        continue
                        
                    try:
                        with open(json_path, 'r', encoding='utf-8') as f:
                            config = json.load(f)
                        
                        lang_code = config.get('language', {}).get('code', '')
                        if not lang_code:
                            parts = filename.split('-')
                            if len(parts) > 0:
                                lang_code = parts[0]
                        
                        audio_lang = None
                        try:
                            safe_key = lang_code.replace('-', '_')
                            if safe_key in languages.AudioLanguage.__members__:
                                audio_lang = languages.AudioLanguage[safe_key]
                        except:
                            pass
                        
                        if audio_lang:
                            voice_name = onnx_filename.replace('.onnx', '')
                            friendly_name = voice_name
                            if 'espeak' in config:
                                friendly_name = f"Piper - {voice_name}"

                            voices.append(voice.build_voice_v3(
                                name=friendly_name,
                                gender=constants.Gender.Female,
                                language=audio_lang,
                                service=self,
                                voice_key=voice_name,
                                options={}
                            ))
                            
                    except Exception as e:
                        logger.error(f"Error parsing model config {json_path}: {e}")
                        
        except Exception as e:
            logger.error(f"Error listing piper models: {e}")
            
        return voices

    def get_tts_audio(self, source_text, voice: voice.TtsVoice_v3, options):
        executable_path = self.get_configuration_value_optional(self.CONFIG_EXECUTABLE_PATH, '')
        models_path = self.get_configuration_value_optional(self.CONFIG_MODELS_PATH, '')
        
        if not executable_path or not os.path.exists(executable_path):
            raise errors.RequestError(source_text, voice, "Piper executable not found. Please configure path.")
            
        model_file = os.path.join(models_path, voice.voice_key + ".onnx")
        if not os.path.exists(model_file):
            raise errors.RequestError(source_text, voice, f"Model file not found: {model_file}")

        import tempfile
        fd, temp_path = tempfile.mkstemp(suffix='.wav')
        os.close(fd) 
        
        try:
            # Get or start the persistent process
            process = _piper_manager.get_process(executable_path, model_file)
            
            # Send JSON request with output_file
            request = {
                "text": source_text,
                "output_file": temp_path
            }
            payload = json.dumps(request) + "\n"
            
            # Thread-safe write and read
            with _piper_manager._lock:
                process.stdin.write(payload.encode('utf-8'))
                process.stdin.flush()
                
                # Wait for JSON response on stdout
                response_line = process.stdout.readline()
                if not response_line:
                    raise Exception("Piper process died unexpectedly")
                
                _piper_manager._reset_timer_locked()

            # Read the generated audio file
            if os.path.exists(temp_path):
                with open(temp_path, 'rb') as f:
                    audio_data = f.read()
                return audio_data
            else:
                raise Exception("Piper did not create output file.")
            
        except Exception as e:
            logger.warning(f'exception while generating piper audio: {e}')
            # On error, it's safer to stop the process as it might be in an inconsistent state
            _piper_manager.stop()
            raise errors.RequestError(source_text, voice, str(e))
        finally:
            if os.path.exists(temp_path):
                try: os.remove(temp_path)
                except: pass
