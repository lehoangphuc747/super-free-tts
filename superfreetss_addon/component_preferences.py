import sys
import aqt.qt

from . import component_common
from . import component_shortcuts
from . import component_errorhandling
from . import config_models
from . import constants
from . import errors
from . import gui_utils
from . import logging_utils
from . import i18n
logger = logging_utils.get_child_logger(__name__)

class ComponentPreferences(component_common.ConfigComponentBase):
    def __init__(self, superfreetss, dialog):
        self.superfreetss = superfreetss
        self.dialog = dialog
        self.model = config_models.Preferences()
        self.shortcuts = component_shortcuts.Shortcuts(self.superfreetss, self.dialog, self.shortcuts_updated)
        self.error_handling = component_errorhandling.ErrorHandling(self.superfreetss, self.dialog, self.error_handling_updated)

        lang = self.superfreetss.get_ui_language()
        # Nút lưu / hủy
        self.save_button = aqt.qt.QPushButton(i18n.get_text('button_apply', lang))
        self.cancel_button = aqt.qt.QPushButton(i18n.get_text('button_cancel', lang))

        # Chọn ngôn ngữ giao diện
        self.language_combobox = aqt.qt.QComboBox()

    def load_model(self, model):
        logger.info('load_model')
        self.model = model
        self.shortcuts.load_model(self.model.keyboard_shortcuts)
        self.error_handling.load_model(self.model.error_handling)
        # thiết lập ngôn ngữ ban đầu cho combobox
        current_lang = getattr(self.model, "ui_language", "en") or "en"
        # ánh xạ giá trị nội bộ -> index
        language_values = ["en", "vi"]
        if current_lang in language_values:
            self.language_combobox.setCurrentIndex(language_values.index(current_lang))
        else:
            self.language_combobox.setCurrentIndex(0)

    def get_model(self):
        return self.model

    def shortcuts_updated(self, model):
        self.model.keyboard_shortcuts = model
        self.model_part_updated_common()

    def error_handling_updated(self, model):
        self.model.error_handling = model
        self.model_part_updated_common()

    def model_part_updated_common(self):
        self.save_button.setEnabled(True)
        gui_utils.configure_primary_button(self.save_button)        

    def draw(self, layout):
        lang = self.superfreetss.get_ui_language()
        vlayout = aqt.qt.QVBoxLayout()

        # dialog header 
        # =============

        hlayout = aqt.qt.QHBoxLayout()
        hlayout.addStretch()
        # logo header
        hlayout.addLayout(gui_utils.get_superfreetss_label_header())
        vlayout.addLayout(hlayout)                

        # nhóm chọn ngôn ngữ giao diện
        language_groupbox = aqt.qt.QGroupBox(i18n.get_text("preferences_group_language_title", lang))
        language_layout = aqt.qt.QVBoxLayout()
        language_label = aqt.qt.QLabel(i18n.get_text("preferences_label_interface_language", lang))
        language_layout.addWidget(language_label)

        # đổ dữ liệu cho combobox ngôn ngữ
        self.language_combobox.clear()
        self.language_combobox.addItem(i18n.get_text("preferences_option_language_en", lang), "en")
        self.language_combobox.addItem(i18n.get_text("preferences_option_language_vi", lang), "vi")
        self.language_combobox.setToolTip(i18n.get_text("preferences_language_tooltip", lang))
        language_layout.addWidget(self.language_combobox)
        language_groupbox.setLayout(language_layout)
        vlayout.addWidget(language_groupbox)

        layout.addLayout(vlayout)

        # preferences tabs
        # ====================

        self.tabs = aqt.qt.QTabWidget()
        self.tabs.addTab(self.shortcuts.draw(), i18n.get_text('preferences_tab_keyboard_shortcuts', lang))
        self.tabs.addTab(self.error_handling.draw(), i18n.get_text('preferences_tab_error_handling', lang))
        layout.addWidget(self.tabs)

        # setup bottom buttons
        # ====================

        hlayout = aqt.qt.QHBoxLayout()
        hlayout.addStretch()

        # apply button — primary style, consistent with Configuration dialog
        self.save_button.setEnabled(False)
        gui_utils.configure_primary_button(self.save_button, min_height=40, min_width=100, font_size=11)
        hlayout.addWidget(self.save_button)
        # cancel button — secondary outlined style
        gui_utils.configure_secondary_button(self.cancel_button, min_height=40, min_width=100, font_size=11)
        hlayout.addWidget(self.cancel_button)

        # sự kiện thay đổi ngôn ngữ
        self.language_combobox.currentIndexChanged.connect(self.language_changed)
        self.save_button.pressed.connect(self.save_button_pressed)
        self.cancel_button.pressed.connect(self.cancel_button_pressed)

        layout.addLayout(hlayout)        

    def language_changed(self, index: int):
        """
        Khi user đổi ngôn ngữ trong combobox, cập nhật model.ui_language
        và bật nút Apply.
        """
        data_lang = self.language_combobox.itemData(index)
        if data_lang is None:
            # fallback an toàn
            data_lang = "en"
        self.model.ui_language = data_lang
        self.model_part_updated_common()

    def save_button_pressed(self):
        with self.superfreetss.error_manager.get_single_action_context('Saving Preferences'):
            self.superfreetss.save_preferences(self.model)
            self.dialog.close()

    def cancel_button_pressed(self):
        self.dialog.close()    