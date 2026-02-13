import sys
import io
import asyncio
import edge_tts
from typing import List

from superfreetss_addon import voice
from superfreetss_addon import service
from superfreetss_addon import errors
from superfreetss_addon import constants
from superfreetss_addon import languages
from superfreetss_addon import logging_utils

logger = logging_utils.get_child_logger(__name__)

class EdgeTTS(service.ServiceBase):
    def __init__(self):
        service.ServiceBase.__init__(self)

    @property
    def service_type(self) -> constants.ServiceType:
        return constants.ServiceType.tts

    @property
    def service_fee(self) -> constants.ServiceFee:
        return constants.ServiceFee.free

    def configuration_options(self):
        return {}

    def _get_loop(self):
        try:
            return asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            return loop

    def voice_list(self) -> List[voice.TtsVoice_v3]:
        # EdgeTTS voices are hardcoded or fetched. For robustness, we'll try to fetch or use a reasonable static list.
        try:
            loop = self._get_loop()
            if loop.is_running():
                # If we're already in a running loop (unlikely for this sync call), 
                # we'd need another strategy, but for Anki background tasks, this is usually okay.
                import threading
                result = []
                def _run():
                    nonlocal result
                    new_loop = asyncio.new_event_loop()
                    try:
                        result = new_loop.run_until_complete(edge_tts.VoicesManager.create())
                    finally:
                        new_loop.close()
                t = threading.Thread(target=_run)
                t.start()
                t.join()
                voices_data = result
            else:
                voices_data = loop.run_until_complete(edge_tts.VoicesManager.create())

            voices = []
            for v in voices_data.voices:
                # Map EdgeTTS locale to AudioLanguage
                lang_key = v['Locale'].replace('-', '_')
                audio_lang = None
                try:
                    audio_lang = languages.AudioLanguage[lang_key]
                except KeyError:
                    # Fuzzy matching
                    for al in languages.AudioLanguage:
                        if al.name.startswith(v['Locale'].split('-')[0]):
                            audio_lang = al
                            break
                
                if audio_lang:
                    gender = constants.Gender.Male if v['Gender'] == 'Male' else constants.Gender.Female
                    voices.append(voice.build_voice_v3(
                        name=v['FriendlyName'],
                        gender=gender,
                        language=audio_lang,
                        service=self,
                        voice_key=v['ShortName'],
                        options={}
                    ))
            return voices
        except Exception as e:
            logger.error(f"EdgeTTS: Error fetching voice list: {e}")
            return []

    def get_tts_audio(self, source_text, voice: voice.TtsVoice_v3, options):
        try:
            loop = self._get_loop()
            audio_data = io.BytesIO()
            
            async def _stream():
                communicate = edge_tts.Communicate(source_text, voice.voice_key)
                async for chunk in communicate.stream():
                    if chunk["type"] == "audio":
                        audio_data.write(chunk["data"])

            if loop.is_running():
                import threading
                def _run():
                    new_loop = asyncio.new_event_loop()
                    try:
                        new_loop.run_until_complete(_stream())
                    finally:
                        new_loop.close()
                t = threading.Thread(target=_run)
                t.start()
                t.join()
            else:
                loop.run_until_complete(_stream())
                
            return audio_data.getvalue()
        except Exception as e:
            logger.warning(f'EdgeTTS: exception while retrieving sound for {source_text}: {e}')
            raise errors.RequestError(source_text, voice, str(e))
