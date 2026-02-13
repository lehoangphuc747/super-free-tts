import os
import requests
import threading
import json
import aqt
from aqt.qt import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QProgressBar, QPushButton, pyqtSignal, QObject, Qt, QComboBox
from dataclasses import dataclass
from typing import List, Optional, Dict

from . import logging_utils
from . import gui_utils

logger = logging_utils.get_child_logger(__name__)

# Official voices.json URL
VOICES_JSON_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/main/voices.json"
HF_BASE_URL = "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0"

@dataclass
class PiperModelInfo:
    key: str
    name: str
    language_code: str
    quality: str
    url_onnx: str
    url_json: str

class DownloadWorkerSignals(QObject):
    progress = pyqtSignal(int, str)
    finished = pyqtSignal()
    error = pyqtSignal(str)
    voices_loaded = pyqtSignal(list)

class PiperDownloadWorker(QObject):
    def __init__(self, model: Optional[PiperModelInfo] = None, dest_dir: str = ""):
        super().__init__()
        self.model = model
        self.dest_dir = dest_dir
        self.signals = DownloadWorkerSignals()
        self.is_cancelled = False

    def fetch_voices(self):
        try:
            response = requests.get(VOICES_JSON_URL)
            if response.status_code == 200:
                voices_data = response.json()
                models = []
                for voice_key, info in voices_data.items():
                    # Format: key is e.g. "en_US-amy-low"
                    # We need to construct download URLs
                    # Piper HF structure: {lang}/{lang_region}/{voice_name}/{quality}/{filename}
                    
                    files = info.get('files', {})
                    onnx_rel_path = ""
                    for f_path in files.keys():
                        if f_path.endswith('.onnx'):
                            onnx_rel_path = f_path
                            break
                    
                    if not onnx_rel_path:
                        continue
                        
                    # Hugging Face resolve URL: HF_BASE_URL + path (path already starts with lang/...)
                    # Actually voices.json paths are relative to the repo root v1.0.0 folder
                    
                    models.append(PiperModelInfo(
                        key=voice_key,
                        name=info.get('name', voice_key),
                        language_code=info.get('language', {}).get('code', 'unknown'),
                        quality=info.get('quality', 'medium'),
                        url_onnx=f"{HF_BASE_URL}/{onnx_rel_path}?download=true",
                        url_json=f"{HF_BASE_URL}/{onnx_rel_path}.json?download=true"
                    ))
                
                # Sort models: language first, then name
                models.sort(key=lambda x: (x.language_code, x.name))
                self.signals.voices_loaded.emit(models)
            else:
                self.signals.error.emit(f"Failed to fetch voices.json: HTTP {response.status_code}")
        except Exception as e:
            self.signals.error.emit(str(e))

    def run(self):
        if not self.model: return
        try:
            if not os.path.exists(self.dest_dir):
                os.makedirs(self.dest_dir)
            
            self._download_file(self.model.url_onnx, self.model.key + ".onnx")
            if self.is_cancelled: return

            self._download_file(self.model.url_json, self.model.key + ".onnx.json")
            if self.is_cancelled: return
            
            self.signals.finished.emit()
        except Exception as e:
            self.signals.error.emit(str(e))

    def _download_file(self, url, filename):
        filepath = os.path.join(self.dest_dir, filename)
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024 * 1024
        wrote = 0
        
        with open(filepath, 'wb') as f:
            for data in response.iter_content(block_size):
                if self.is_cancelled: return
                wrote = wrote + len(data)
                f.write(data)
                if total_size > 0:
                    percent = int((wrote / total_size) * 100)
                    self.signals.progress.emit(percent, f"Downloading {filename} ({int(wrote/1024/1024)}MB / {int(total_size/1024/1024)}MB)")

class PiperManagerDialog(QDialog):
    def __init__(self, parent, dest_dir):
        super().__init__(parent)
        self.dest_dir = dest_dir
        self.all_models: List[PiperModelInfo] = []
        
        self.setWindowTitle("Piper Model Manager")
        self.setMinimumWidth(600)
        self.setMinimumHeight(500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        # Filter Row
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Language:"))
        self.lang_combo = QComboBox()
        self.lang_combo.addItem("All Languages", "all")
        self.lang_combo.currentIndexChanged.connect(self.filter_models)
        filter_layout.addWidget(self.lang_combo, 1)
        self.layout.addLayout(filter_layout)
        
        self.model_list = QListWidget()
        self.layout.addWidget(self.model_list)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.layout.addWidget(self.progress_bar)
        
        self.status_label = QLabel("Loading voice list from Hugging Face...")
        self.layout.addWidget(self.status_label)
        
        btn_layout = QHBoxLayout()
        self.download_btn = QPushButton("Download Selected")
        self.download_btn.setEnabled(False)
        self.download_btn.clicked.connect(self.download_selected)
        gui_utils.configure_primary_button(self.download_btn)
        
        self.close_btn = QPushButton("Close")
        self.close_btn.clicked.connect(self.reject)
        
        btn_layout.addStretch()
        btn_layout.addWidget(self.download_btn)
        btn_layout.addWidget(self.close_btn)
        self.layout.addLayout(btn_layout)
        
        self.worker = None
        self.load_voices()

    def load_voices(self):
        self.worker = PiperDownloadWorker()
        self.worker.signals.voices_loaded.connect(self.on_voices_loaded)
        self.worker.signals.error.connect(self.on_load_error)
        threading.Thread(target=self.worker.fetch_voices).start()

    def on_voices_loaded(self, models):
        self.all_models = models
        languages = sorted(list(set(m.language_code for m in models)))
        
        # Populate language combo
        self.lang_combo.blockSignals(True)
        for lang in languages:
            self.lang_combo.addItem(lang, lang)
        
        # Try to pre-select vi_VN or en_US
        idx = self.lang_combo.findData("vi_VN")
        if idx == -1: idx = self.lang_combo.findData("en_US")
        if idx != -1: self.lang_combo.setCurrentIndex(idx)
        
        self.lang_combo.blockSignals(False)
        
        self.status_label.setText(f"Loaded {len(models)} voices.")
        self.download_btn.setEnabled(True)
        self.filter_models()

    def on_load_error(self, err):
        self.status_label.setText(f"Failed to load voices: {err}")
        aqt.utils.showWarning(f"Error loading Piper voices list: {err}")

    def filter_models(self):
        self.model_list.clear()
        selected_lang = self.lang_combo.currentData()
        
        for model in self.all_models:
            if selected_lang == "all" or model.language_code == selected_lang:
                item = QListWidgetItem(f"{model.name} [{model.quality}] ({model.language_code})")
                if model_exists(self.dest_dir, model):
                    item.setText(item.text() + " [Installed]")
                    item.setForeground(Qt.GlobalColor.gray)
                
                item.setData(Qt.ItemDataRole.UserRole, model)
                self.model_list.addItem(item)

    def download_selected(self):
        selected_items = self.model_list.selectedItems()
        if not selected_items: return
            
        model = selected_items[0].data(Qt.ItemDataRole.UserRole)
        
        self.download_btn.setEnabled(False)
        self.lang_combo.setEnabled(False)
        self.model_list.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        
        self.worker = PiperDownloadWorker(model, self.dest_dir)
        self.worker.signals.progress.connect(self.update_progress)
        self.worker.signals.finished.connect(self.download_finished)
        self.worker.signals.error.connect(self.download_error)
        
        threading.Thread(target=self.worker.run).start()

    def update_progress(self, percent, msg):
        self.progress_bar.setValue(percent)
        self.status_label.setText(msg)

    def download_finished(self):
        self.status_label.setText("Download complete!")
        self.progress_bar.setValue(100)
        self.download_btn.setEnabled(True)
        self.lang_combo.setEnabled(True)
        self.model_list.setEnabled(True)
        aqt.utils.showInfo("Model downloaded successfully!")
        self.filter_models()

    def download_error(self, err):
        self.status_label.setText(f"Error: {err}")
        self.download_btn.setEnabled(True)
        self.lang_combo.setEnabled(True)
        self.model_list.setEnabled(True)
        aqt.utils.showWarning(f"Download failed: {err}")

def model_exists(dest_dir, model):
    onnx_path = os.path.join(dest_dir, model.key + ".onnx")
    return os.path.exists(onnx_path)

