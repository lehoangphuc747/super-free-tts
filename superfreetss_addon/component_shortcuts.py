import sys
import aqt.qt

from . import component_common
from . import config_models
from . import constants
from . import gui_utils
from . import logging_utils
from . import i18n
logger = logging_utils.get_child_logger(__name__)


class Shortcuts(component_common.ConfigComponentBase):

    def __init__(self, hypertts, dialog, model_change_callback):
        self.hypertts = hypertts
        self.dialog = dialog
        self.model = config_models.KeyboardShortcuts()
        self.model_change_callback = model_change_callback
        self.propagate_model_change = True

        self.editor_add_audio_key_sequence = aqt.qt.QKeySequenceEdit()
        self.editor_preview_audio_key_sequence = aqt.qt.QKeySequenceEdit()        

    def get_model(self):
        return self.model

    def load_model(self, model):
        self.model = model
        self.propagate_model_change = False
        self.editor_add_audio_key_sequence.setKeySequence(aqt.qt.QKeySequence(self.model.shortcut_editor_add_audio))
        self.editor_preview_audio_key_sequence.setKeySequence(aqt.qt.QKeySequence(self.model.shortcut_editor_preview_audio))
        self.propagate_model_change = True


    def notify_model_update(self):
        if self.propagate_model_change == True:
            self.model_change_callback(self.model)

    def draw(self):
        lang = self.hypertts.get_ui_language()
        layout_widget = aqt.qt.QWidget()
        layout = aqt.qt.QVBoxLayout(layout_widget)

        # editor add audio
        # ================

        groupbox = aqt.qt.QGroupBox(i18n.get_text('shortcuts_group_editor_add_audio', lang))
        vlayout = aqt.qt.QVBoxLayout()

        editor_add_audio_label = aqt.qt.QLabel(constants.GUI_TEXT_SHORTCUTS_EDITOR_ADD_AUDIO)
        editor_add_audio_label.setWordWrap(True)
        vlayout.addWidget(editor_add_audio_label)

        hlayout = aqt.qt.QHBoxLayout()

        hlayout.addWidget(self.editor_add_audio_key_sequence)

        self.editor_add_audio_clear_button = aqt.qt.QPushButton(i18n.get_text('button_clear', lang))
        hlayout.addWidget(self.editor_add_audio_clear_button)
        
        vlayout.addLayout(hlayout)

        groupbox.setLayout(vlayout)
        layout.addWidget(groupbox)

        # editor preview audio
        # ====================

        groupbox = aqt.qt.QGroupBox(i18n.get_text('shortcuts_group_editor_preview_audio', lang))
        vlayout = aqt.qt.QVBoxLayout()

        editor_preview_audio_label = aqt.qt.QLabel(constants.GUI_TEXT_SHORTCUTS_EDITOR_PREVIEW_AUDIO)
        editor_preview_audio_label.setWordWrap(True)
        vlayout.addWidget(editor_preview_audio_label)

        hlayout = aqt.qt.QHBoxLayout()

        hlayout.addWidget(self.editor_preview_audio_key_sequence)

        self.editor_preview_audio_clear_button = aqt.qt.QPushButton(i18n.get_text('button_clear', lang))
        hlayout.addWidget(self.editor_preview_audio_clear_button)

        vlayout.addLayout(hlayout)

        groupbox.setLayout(vlayout)
        layout.addWidget(groupbox)

        # warning label
        note_label = aqt.qt.QLabel(constants.GUI_TEXT_SHORTCUTS_ANKI_RESTART)
        note_label.setWordWrap(True)
        layout.addWidget(note_label)

        layout.addStretch()

        # wire events
        self.editor_add_audio_clear_button.pressed.connect(self.editor_add_audio_clear)
        self.editor_preview_audio_clear_button.pressed.connect(self.editor_preview_audio_clear)
        
        self.editor_add_audio_key_sequence.keySequenceChanged.connect(self.editor_add_audio_changed)
        self.editor_preview_audio_key_sequence.keySequenceChanged.connect(self.editor_preview_audio_changed)

        return layout_widget


    def editor_add_audio_clear(self):
        self.editor_add_audio_key_sequence.clear()

    def editor_preview_audio_clear(self):
        self.editor_preview_audio_key_sequence.clear()

    def convert_shortcut(self, key_sequence):
        shortcut_str = key_sequence.toString()
        if shortcut_str == '':
            return None
        return shortcut_str

    def editor_add_audio_changed(self, key_sequence):
        logger.info(f'editor_add_audio_changed {key_sequence}')
        logger.info(f'key_sequence.toString(): {key_sequence.toString()}')
        self.model.shortcut_editor_add_audio = self.convert_shortcut(key_sequence)
        self.notify_model_update()

    def editor_preview_audio_changed(self, key_sequence):
        logger.info(f'editor_preview_audio_changed')
        logger.info(f'key_sequence.toString(): {key_sequence.toString()}')        
        self.model.shortcut_editor_preview_audio = self.convert_shortcut(key_sequence)
        self.notify_model_update()
