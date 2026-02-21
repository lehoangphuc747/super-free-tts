from typing import Dict

# Danh sách ngôn ngữ giao diện được hỗ trợ
SUPPORTED_LANGUAGES = ["en", "vi"]

# Bảng chuỗi cho từng ngôn ngữ.
# Lưu ý: nếu thêm key mới, cần thêm cho cả "en" và "vi".
STRINGS: Dict[str, Dict[str, str]] = {
    "en": {
        # Menus / dialog titles
        "menu_services_configuration": "Super Free TTS: Services Configuration",
        "menu_preferences": "Super Free TTS: Preferences",
        "dialog_services_title": "Super Free TTS: Services Configuration",
        "dialog_preferences_title": "Super Free TTS: Preferences",
        "dialog_easy_title": "Super Free TTS: Add Audio (Easy)",
        "dialog_collection_title": "Super Free TTS: Add Audio (Collection)",
        "dialog_realtime_title": "Super Free TTS: Add Audio (Realtime)",
        "dialog_preset_rules_title": "Super Free TTS: Preset Rules",
        "dialog_main_title": "Super Free TTS",
        "tab_services": "Services",
        "tab_preferences": "Preferences",

        # Generic buttons
        "button_save": "Save",
        "button_cancel": "Cancel",
        "button_close": "Close",
        "generic_enable": "Enable",
        "generic_enable_all": "Enable All",
        "button_open": "Open",
        "button_duplicate": "Duplicate",
        "button_rename": "Rename",
        "button_delete": "Delete",
        "button_save_and_close": "Save and Close",
        "button_advanced": "Advanced",
        "dialog_save_changes": "Save changes to current preset?",
        "dialog_enter_new_name": "Enter new preset name",
        "dialog_rename_title": "Rename Preset",
        "dialog_delete_confirm": "Delete Preset {0}?",
        "dialog_choose_preset_open": "Choose a preset to open",
        "dialog_choose_preset_duplicate": "Choose a preset to duplicate",

        # Easy mode buttons
        "easy_button_preview_audio": "Preview Audio",
        "easy_button_previewing": "Playing Preview...",
        "easy_button_add_audio": "Add Audio",
        "easy_button_adding_audio": "Adding Audio...",
        "easy_button_more_settings": "More Settings...",
        "easy_button_hide_settings": "Hide Settings...",

        # Collection / batch buttons
        "batch_button_preset": "Preset:",
        "batch_button_preview_sound": "Preview Sound",
        "batch_button_apply_to_notes": "Apply To Notes",
        "batch_button_apply_to_note": "Apply To Note",
        "batch_button_loading": "Loading...",
        "batch_button_save_and_close": "Save and Close",
        "batch_button_open": "Open",
        "batch_button_duplicate": "Duplicate",
        "batch_button_rename": "Rename",
        "batch_button_delete": "Delete",
        "batch_button_done": "Done",
        "batch_button_select_note_to_preview": "Select Note to Preview Sound",

        # Realtime buttons / tabs
        "realtime_button_apply_to_note": "Apply To Note",
        "realtime_tab_front": "Front Side",
        "realtime_tab_back": "Back Side",

        # Preset mapping rules
        "preset_rules_group_note_info": "Note Info",
        "preset_rules_group_need_help": "Need Help?",
        "preset_rules_group_settings": "Settings",
        "preset_rules_group_preset_rules": "Preset Rules",
        "preset_rules_button_preview_all": "Preview All",
        "preset_rules_button_run_all": "Run All",
        "preset_rules_button_add_rule": "Add Rule",
        "preset_rules_button_save_and_close": "Save and Close",

        # Voice selection
        "voice_filters_group_title": "Voice Filters",
        "voice_label_language": "Language",
        "voice_label_locale": "Locale",
        "voice_label_service": "Service",
        "voice_label_gender": "Gender",
        "voice_button_reset_filters": "Reset Filters",
        "voice_group_voice": "Voice",
        "voice_button_play_sample": "Play Sample",
        "voice_button_play_sample_wait": "Select note to play sample",
        "voice_group_selection_mode": "Selection Mode",
        "voice_radio_single": "Single: a single voice will be used for all notes.",
        "voice_radio_random": "Random: select randomly from a list of voices.",
        "voice_radio_priority": "Priority: try first voice, then move to second if not found.",
        "voice_group_voice_list": "Voice List",
        "voice_button_add_voice": "Add Voice",
        "voice_button_remove_voice": "Remove",
        "voice_button_move_up": "Up",
        "voice_button_move_down": "Down",

        # Services configuration
        "services_header_title": "Services",
        "services_header_description": "Choose which free text-to-speech services you want to use. You can enable multiple services at once.",
        "services_button_enable_all_free": "Enable All Free Services",
        "services_button_disable_all": "Disable All Services",
        "config_toc_title": "Configuration",
        "config_toc_services": "Services",
        "config_toc_about": "About",
        "config_search_placeholder": "Search service…",

        # Service fee / type descriptions
        "service_fee_free": "Free",
        "service_fee_paid": "Paid",
        "service_type_dictionary_description": "Dictionary, contains recordings of words.",
        "service_type_tts_description": "Text To Speech, can generate audio for full sentences.",

        # Specific service descriptions
        "service_description_GoogleTranslate": "Uses Google's free translation API. Multilingual support. (Online)",
        "service_description_EdgeTTS": "High quality, natural sounding AI voices from Microsoft Edge. (Online)",
        "service_description_Windows": "Standard Windows voices (SAPI 5). Fast and works offline.",
        "service_description_MacOS": "Standard MacOS voices. High quality and works offline.",
        "service_description_ESpeakNg": "Open source synthesizer. Robotic voice but very fast and supports many languages. (Offline)",

        # Tabs (batch dialog)
        "tab_source": "Source",
        "tab_target": "Target",
        "tab_voice_selection": "Voice Selection",
        "tab_text_processing": "Text Processing",

        # Batch dialog extra buttons
        "batch_button_show_settings": "Show Settings",
        "batch_button_hide_settings": "Hide Settings",

        # Preferences - language
        "preferences_group_language_title": "Language / Ngôn ngữ",
        "preferences_label_interface_language": "Interface Language / Ngôn ngữ giao diện",
        "preferences_option_language_en": "English",
        "preferences_option_language_vi": "Tiếng Việt",
        "preferences_language_tooltip": "Choose the language for Super Free TTS buttons and dialogs.",

        # Choose Easy/Advanced dialog
        "choose_mode_title": "How would you like to add audio?",
        "choose_mode_subtitle": "Pick the mode that fits your workflow. You can change this later.",
        "choose_mode_easy_title": "Easy Mode",
        "choose_mode_easy_desc": "Simple interface for adding audio manually. Just choose the field and the voice. Similar to AwesomeTTS.",
        "choose_mode_advanced_title": "Advanced Mode",
        "choose_mode_advanced_desc": "Full interface with presets, batch processing, and mapping rules. Offers complete control.",
        "choose_mode_footer": "You can change this later in the editor button bar (Configure preset rules).",

        # Service badges
        "service_badge_recommended": "Recommended",
        "service_badge_free": "Free",
        "service_badge_enabled": "Enabled",

        # Category labels (no emoji)
        "config_category_tts": "TTS Services",
        "config_category_dictionary": "Dictionary Services",
        "about_header_title": "About SuperFreeTTS",
        "about_contributor": "Honorable Contributor",
        "about_author": "Author",
        "about_version": "Version",
        "about_website": "Website",
        "about_facebook": "Facebook",
        "about_description": "SuperFreeTTS is a 100% free text-to-speech addon for Anki, designed to make language learning more accessible and effective.",
        "about_footer": "SuperFreeTTS is documentation-driven and built for the community.",

        # Source component
        "source_group_mode": "Source Mode",
        "source_group_configuration": "Source Configuration",
        "source_label_additional_settings": "Additional Settings:",

        # Target component
        "target_radio_sound_only": "Sound Tag only",
        "target_radio_text_and_sound": "Text and Sound Tag",
        "target_radio_remove_sound": "Remove other sound tags",
        "target_radio_keep_sound": "Keep other sound tags (append)",
        "target_group_field": "Target Field",
        "target_group_text_sound_handling": "Text and Sound Tag Handling",
        "target_group_existing_sound_handling": "Existing Sound Tag Handling",

        # Target easy component
        "target_easy_radio_same_field": "Into same field",
        "target_easy_radio_different_field": "Into different field (choose which)",
        "target_easy_radio_at_end": "At the end",
        "target_easy_radio_after_cursor": "After cursor (not supported)",
        "target_easy_label_which_field": "<i>Which field to insert the audio into?</i>",
        "target_easy_label_where_insert": "<i>Where inside the field to insert the audio?</i>",

        # Shortcuts component
        "shortcuts_group_editor_add_audio": "Editor Add Audio",
        "shortcuts_group_editor_preview_audio": "Editor Preview Audio",
        "button_clear": "Clear",

        # Error handling component
        "errorhandling_checkbox_usage_stats": "Send anonymous usage statistics and error reports to help improve Super Free TTS",
        "errorhandling_checkbox_disable_ssl": "Disable SSL certificate verification (not recommended)",
        "errorhandling_group_realtime_errors": "Realtime TTS Errors",
        "errorhandling_group_reporting": "Error Reporting",
        "errorhandling_group_network": "Network Connection",
        "errorhandling_label_ssl_description": "Only disable SSL verification if you are behind a corporate proxy or firewall that intercepts HTTPS connections.",

        # Mapping rule component
        "mappingrule_button_preview": "Preview",
        "mappingrule_tooltip_preview": "Hear audio for this preset",
        "mappingrule_button_run": "Run",
        "mappingrule_tooltip_run": "Add audio to the note for this preset",
        "mappingrule_label_preset": "Preset:",
        "mappingrule_button_edit": "Edit",
        "mappingrule_tooltip_edit": "Edit this preset (to change voice or other settings)",
        "mappingrule_radio_note_type": "Note Type",
        "mappingrule_radio_deck_note_type": "Deck and Note Type",
        "mappingrule_checkbox_enabled": "Enabled",
        "mappingrule_button_delete": "Delete",

        # Choose preset component
        "choosepreset_radio_new": "New Preset",
        "choosepreset_radio_existing": "Existing Preset",
        "button_ok": "Ok",

        # Text processing component
        "textproc_label_blank_text": "<i>Enter sample text to verify text processing settings.</i>",
        "textproc_header_type": "Type",
        "textproc_header_pattern": "Pattern",
        "textproc_header_replacement": "Replacement",
        "textproc_group_preview": "Preview Text Processing Settings",
        "textproc_label_verify_settings": "You may verify your settings by entering sample text below:",
        "textproc_label_enter_sample": "Enter sample text:",
        "textproc_label_transformed": "Transformed Text:",
        "textproc_group_rules": "Text Processing Rules",
        "textproc_checkbox_html_to_text": "Process HTML tags, convert into single line",
        "textproc_checkbox_strip_brackets": "Remove text in brackets (), [], {}, <>",
        "textproc_checkbox_strip_cloze": "Remove Cloze brackets {{c1::text}}",
        "textproc_checkbox_ssml_convert": "Convert SSML characters (like <, &&, etc)",
        "textproc_checkbox_run_replace_last": "Run text replacement rules last (uncheck to run first)",
        "textproc_checkbox_ignore_case": "Ignore case (Regex rules only)",
        "textproc_group_replacement_rules": "Text Replacement Rules",
        "textproc_label_add_rules": "Add replacement rules and double click to edit pattern / replacements",
        "textproc_button_add_simple": "Add Simple Rule",
        "textproc_button_add_regex": "Add Regex Rule",
        "textproc_button_remove_rule": "Remove Selected Rule",

        # Batch tooltips (remaining hardcoded)
        "batch_tooltip_open": "Open a different preset",
        "batch_tooltip_duplicate": "Duplicate an existing preset",
        "batch_tooltip_save": "Save current preset",
        "batch_tooltip_rename": "Rename the current preset",
        "batch_tooltip_delete": "Delete the current preset",
        "batch_tooltip_save_and_close": "Save current preset and close dialog",
        "batch_tooltip_show_advanced": "Show advanced text processing options",
        "batch_tooltip_hide_advanced": "Hide advanced text processing options",
        "batch_button_preview": "Preview",
        "batch_button_apply": "Apply",
        "batch_button_save_close": "Save & Close",
        "button_apply": "Apply",

        # Easy component
        "easy_group_source_text": "\u2460 Source Text",
        "easy_group_voice_selection": "\u2461 Voice Selection",
        "easy_group_target_field": "\u2462 Target Field",
        "easy_tooltip_preview_with_shortcut": "Preview the audio that will be generated ({0})",
        "easy_tooltip_preview": "Preview the audio that will be generated",
        "easy_tooltip_add_with_shortcut": "Add the audio to your note ({0})",
        "easy_tooltip_add": "Add the audio to your note",

        # Voice selection easy
        "voiceselection_easy_label_language": "Language:",
        "voiceselection_easy_label_service": "Service:",
        "voiceselection_easy_label_voice": "Voice:",

        # Realtime side component
        "realtime_checkbox_enable_side": "Enable Realtime TTS for {0} side",
        "realtime_button_preview_sound": "Preview Sound",
        "realtime_group_preview": "Preview",
        "realtime_label_text_pronounced": "Text to be pronounced:",
        "realtime_button_playing_preview": "Playing Preview...",

        # Preferences component
        "preferences_tab_keyboard_shortcuts": "Keyboard Shortcuts",
        "preferences_tab_error_handling": "Error Handling",

        # GUI menus and tooltips
        "menu_add_audio_collection": "Add Audio (Collection)...",
        "menu_add_audio_collection_preset": "Add Audio (Collection): {0}...",
        "menu_add_audio_realtime": "Add Audio (Realtime)...",
        "menu_remove_audio_realtime": "Remove Audio (Realtime) / TTS Tag...",
        "editor_tooltip_add_audio": "Super Free TTS: Add Audio to your note (based on your preset rules)",
        "editor_tooltip_preview_audio": "Super Free TTS: Preview Audio (Hear the audio before adding it)",
        "editor_tooltip_configure_presets": "Super Free TTS: Configure Preset Rules for this Note (do this before being able to add audio)",

        # Piper Manager
        "piper_title": "Piper Model Manager",
        "piper_label_language": "Language:",
        "piper_all_languages": "All Languages",
        "piper_status_loading": "Loading voice list from Hugging Face...",
        "piper_button_download": "Download Selected",
        "piper_status_loaded": "Loaded {0} voices.",
        "piper_status_load_error": "Failed to load voices: {0}",
        "piper_warning_load_error": "Error loading Piper voices list: {0}",
        "piper_label_installed": "[Installed]",
        "piper_status_download_complete": "Download complete!",
        "piper_info_download_success": "Model downloaded successfully!",
        "piper_status_error": "Error: {0}",
        "piper_warning_download_failed": "Download failed: {0}",
        "piper_button_download_models": "Download Models...",
        "piper_info_select_dir": "Please select a models directory first.",

        # Welcome message
        "welcome_important": "Important",
        "welcome_configure_desc": "you have to configure services before adding audio.",
        "welcome_configure_title": "Configure Services",
        "welcome_configure_subtitle": "Click here before adding audio",
        "welcome_no_audio_yet": "It looks like you haven't added audio yet.",
        "welcome_add_audio_title": "Adding Audio",
        "welcome_add_audio_subtitle": "Click to learn how to add audio",
        "welcome_heading": "Super Free TTS - Add Audio to your Flashcards",
        "welcome_close": "× Close",
    },
    "vi": {
        # Menus / dialog titles
        "menu_services_configuration": "Super Free TTS: Cấu hình dịch vụ",
        "menu_preferences": "Super Free TTS: Tùy chọn",
        "dialog_services_title": "Super Free TTS: Cấu hình dịch vụ",
        "dialog_preferences_title": "Super Free TTS: Tùy chọn",
        "dialog_easy_title": "Super Free TTS: Thêm âm thanh (Dễ)",
        "dialog_collection_title": "Super Free TTS: Thêm âm thanh (Nhiều thẻ)",
        "dialog_realtime_title": "Super Free TTS: Âm thanh tự phát (Realtime)",
        "dialog_preset_rules_title": "Super Free TTS: Quy tắc preset",
        "dialog_main_title": "Super Free TTS",
        "tab_services": "Nguồn âm thanh",
        "tab_preferences": "Cấu hình",

        # Generic buttons
        "button_save": "Lưu",
        "button_cancel": "Hủy",
        "button_close": "Đóng",
        "generic_enable": "Bật",
        "generic_enable_all": "Bật tất cả",
        "button_open": "Mở",
        "button_duplicate": "Sao chép",
        "button_rename": "Đổi tên",
        "button_delete": "Xóa",
        "button_save_and_close": "Lưu và Đóng",
        "button_advanced": "Nâng cao",

        # Easy mode buttons
        "easy_button_preview_audio": "Nghe thử",
        "easy_button_previewing": "Đang phát thử...",
        "easy_button_add_audio": "Thêm âm thanh",
        "easy_button_adding_audio": "Đang thêm âm thanh...",
        "easy_button_more_settings": "Tùy chọn nâng cao...",
        "easy_button_hide_settings": "Ẩn bớt tùy chọn...",

        # Collection / batch buttons
        "batch_button_preset": "Preset:",
        "batch_button_preview_sound": "Nghe thử",
        "batch_button_apply_to_notes": "Áp dụng cho nhiều thẻ",
        "batch_button_apply_to_note": "Áp dụng cho thẻ",
        "batch_button_loading": "Đang xử lý...",
        "batch_button_save_and_close": "Lưu và đóng",
        "batch_button_open": "Mở",
        "batch_button_duplicate": "Nhân bản",
        "batch_button_rename": "Đổi tên",
        "batch_button_delete": "Xóa",
        "batch_button_done": "Hoàn tất",
        "batch_button_select_note_to_preview": "Chọn thẻ để nghe thử",

        # Realtime buttons / tabs
        "realtime_button_apply_to_note": "Áp dụng cho thẻ",
        "realtime_tab_front": "Mặt trước",
        "realtime_tab_back": "Mặt sau",

        # Preset mapping rules
        "preset_rules_group_note_info": "Thông tin thẻ",
        "preset_rules_group_need_help": "Cần trợ giúp?",
        "preset_rules_group_settings": "Cài đặt",
        "preset_rules_group_preset_rules": "Quy tắc preset",
        "preset_rules_button_preview_all": "Nghe thử tất cả",
        "preset_rules_button_run_all": "Chạy tất cả",
        "preset_rules_button_add_rule": "Thêm quy tắc",
        "preset_rules_button_save_and_close": "Lưu và đóng",

        # Voice selection
        "voice_filters_group_title": "Bộ lọc giọng đọc",
        "voice_label_language": "Ngôn ngữ",
        "voice_label_locale": "Giọng (vùng)",
        "voice_label_service": "Dịch vụ",
        "voice_label_gender": "Giới tính",
        "voice_button_reset_filters": "Đặt lại bộ lọc",
        "voice_group_voice": "Giọng đọc",
        "voice_button_play_sample": "Nghe mẫu",
        "voice_button_play_sample_wait": "Chọn thẻ để nghe mẫu",
        "voice_group_selection_mode": "Chế độ chọn giọng",
        "voice_radio_single": "Một giọng: dùng cùng một giọng cho mọi thẻ.",
        "voice_radio_random": "Ngẫu nhiên: chọn ngẫu nhiên từ danh sách giọng.",
        "voice_radio_priority": "Ưu tiên: thử giọng 1, lỗi thì chuyển giọng 2, v.v.",
        "voice_group_voice_list": "Danh sách giọng đã chọn",
        "voice_button_add_voice": "Thêm giọng",
        "voice_button_remove_voice": "Xóa",
        "voice_button_move_up": "Lên",
        "voice_button_move_down": "Xuống",

        # Services configuration
        "services_header_title": "Dịch vụ TTS",
        "services_header_description": "Chọn các dịch vụ đọc văn bản thành giọng nói miễn phí bạn muốn dùng. Có thể bật nhiều dịch vụ cùng lúc.",
        "services_button_enable_all_free": "Bật tất cả dịch vụ miễn phí",
        "services_button_disable_all": "Tắt tất cả dịch vụ",
        "config_toc_title": "Cấu hình",
        "config_toc_services": "Dịch vụ",
        "config_toc_about": "Thông tin",
        "config_search_placeholder": "Tìm dịch vụ…",

        # Service fee / type descriptions
        "service_fee_free": "Miễn phí",
        "service_fee_paid": "Trả phí",
        "service_type_dictionary_description": "Từ điển, chứa các bản ghi âm từ vựng.",
        "service_type_tts_description": "Text To Speech, có thể đọc trọn câu/văn bản.",
        
        # Specific service descriptions
        "service_description_GoogleTranslate": "Sử dụng API miễn phí của Google Translate. Hỗ trợ đa ngôn ngữ. (Online)",
        "service_description_EdgeTTS": "Giọng đọc AI tự nhiên, chất lượng cao từ Microsoft Edge. (Online)",
        "service_description_Windows": "Giọng đọc có sẵn trên Windows (SAPI 5). Nhanh và hoạt động offline.",
        "service_description_MacOS": "Giọng đọc có sẵn trên MacOS. Chất lượng cao và hoạt động offline.",
        "service_description_ESpeakNg": "Trình tổng hợp mã nguồn mở. Giọng hơi máy nhưng rất nhanh và hỗ trợ nhiều ngôn ngữ. (Offline)",

        # Tabs (batch dialog)
        "tab_source": "Nguồn",
        "tab_target": "Trường nhận âm thanh",
        "tab_voice_selection": "Chọn giọng",
        "tab_text_processing": "Xử lý text",

        # Batch dialog extra buttons
        "batch_button_show_settings": "Hiện cài đặt",
        "batch_button_hide_settings": "Ẩn cài đặt",

        # Preferences - language
        "preferences_group_language_title": "Language / Ngôn ngữ",
        "preferences_label_interface_language": "Interface Language / Ngôn ngữ giao diện",
        "preferences_option_language_en": "English",
        "preferences_option_language_vi": "Tiếng Việt",
        "preferences_language_tooltip": "Chọn ngôn ngữ cho nút bấm và hộp thoại của Super Free TTS.",

        # Choose Easy/Advanced dialog
        "choose_mode_title": "Bạn muốn thêm âm thanh theo cách nào?",
        "choose_mode_subtitle": "Chọn chế độ phù hợp. Bạn có thể đổi lại sau.",
        "choose_mode_easy_title": "Chế độ Dễ",
        "choose_mode_easy_desc": "Giao diện đơn giản để thêm âm thanh. Chỉ cần chọn trường và giọng đọc. Tương tự AwesomeTTS.",
        "choose_mode_advanced_title": "Chế độ Nâng cao",
        "choose_mode_advanced_desc": "Giao diện đầy đủ với preset, xử lý hàng loạt và quy tắc ánh xạ. Kiểm soát hoàn toàn.",
        "choose_mode_footer": "Bạn có thể đổi lại sau ở thanh nút trên trình soạn thẻ (Cấu hình quy tắc preset).",

        # Service badges
        "service_badge_recommended": "Gợi ý",
        "service_badge_free": "Miễn phí",
        "service_badge_enabled": "Đã bật",

        # Category labels (no emoji)
        "config_category_tts": "Dịch vụ TTS",
        "config_category_dictionary": "Dịch vụ Từ điển",
        "about_header_title": "Thông tin SuperFreeTTS",
        "about_contributor": "Người đóng góp danh dự",
        "about_author": "Tác giả",
        "about_version": "Phiên bản",
        "about_website": "Trang web",
        "about_facebook": "Facebook",
        "about_description": "SuperFreeTTS là một addon chuyển văn bản thành giọng nói hoàn toàn miễn phí cho Anki, được thiết kế để giúp việc học ngôn ngữ trở nên dễ dàng và hiệu quả hơn.",
        "about_footer": "SuperFreeTTS được phát triển theo hướng tài liệu và xây dựng cho cộng đồng.",

        # Source component
        "source_group_mode": "Chế độ nguồn",
        "source_group_configuration": "Cấu hình nguồn",
        "source_label_additional_settings": "Cài đặt thêm:",

        # Target component
        "target_radio_sound_only": "Chỉ thẻ âm thanh",
        "target_radio_text_and_sound": "Văn bản và thẻ âm thanh",
        "target_radio_remove_sound": "Xóa các thẻ âm thanh khác",
        "target_radio_keep_sound": "Giữ các thẻ âm thanh khác (nối thêm)",
        "target_group_field": "Trường đích",
        "target_group_text_sound_handling": "Xử lý văn bản và thẻ âm thanh",
        "target_group_existing_sound_handling": "Xử lý thẻ âm thanh hiện có",

        # Target easy component
        "target_easy_radio_same_field": "Vào cùng trường",
        "target_easy_radio_different_field": "Vào trường khác (chọn trường)",
        "target_easy_radio_at_end": "Ở cuối",
        "target_easy_radio_after_cursor": "Sau vị trí con trỏ (chưa hỗ trợ)",
        "target_easy_label_which_field": "<i>Chèn âm thanh vào trường nào?</i>",
        "target_easy_label_where_insert": "<i>Chèn âm thanh vào vị trí nào trong trường?</i>",

        # Shortcuts component
        "shortcuts_group_editor_add_audio": "Phím tắt Thêm âm thanh",
        "shortcuts_group_editor_preview_audio": "Phím tắt Nghe thử",
        "button_clear": "Xóa",

        # Error handling component
        "errorhandling_checkbox_usage_stats": "Gửi thống kê sử dụng ẩn danh và báo cáo lỗi để cải thiện Super Free TTS",
        "errorhandling_checkbox_disable_ssl": "Tắt xác minh chứng chỉ SSL (không khuyến nghị)",
        "errorhandling_group_realtime_errors": "Lỗi TTS thời gian thực",
        "errorhandling_group_reporting": "Báo cáo lỗi",
        "errorhandling_group_network": "Kết nối mạng",
        "errorhandling_label_ssl_description": "Chỉ tắt xác minh SSL nếu bạn đang dùng proxy hoặc tường lửa chặn kết nối HTTPS.",

        # Mapping rule component
        "mappingrule_button_preview": "Xem trước",
        "mappingrule_tooltip_preview": "Nghe thử âm thanh cho preset này",
        "mappingrule_button_run": "Chạy",
        "mappingrule_tooltip_run": "Thêm âm thanh vào thẻ cho preset này",
        "mappingrule_label_preset": "Preset:",
        "mappingrule_button_edit": "Sửa",
        "mappingrule_tooltip_edit": "Sửa preset này (đổi giọng hoặc cài đặt khác)",
        "mappingrule_radio_note_type": "Loại thẻ",
        "mappingrule_radio_deck_note_type": "Bộ thẻ và Loại thẻ",
        "mappingrule_checkbox_enabled": "Đã bật",
        "mappingrule_button_delete": "Xóa",

        # Choose preset component
        "choosepreset_radio_new": "Preset mới",
        "choosepreset_radio_existing": "Preset có sẵn",
        "button_ok": "Ok",

        # Text processing component
        "textproc_label_blank_text": "<i>Nhập văn bản mẫu để kiểm tra cài đặt xử lý text.</i>",
        "textproc_header_type": "Loại",
        "textproc_header_pattern": "Mẫu",
        "textproc_header_replacement": "Thay thế",
        "textproc_group_preview": "Xem trước cài đặt xử lý text",
        "textproc_label_verify_settings": "Bạn có thể kiểm tra cài đặt bằng cách nhập văn bản mẫu bên dưới:",
        "textproc_label_enter_sample": "Nhập văn bản mẫu:",
        "textproc_label_transformed": "Văn bản đã xử lý:",
        "textproc_group_rules": "Quy tắc xử lý text",
        "textproc_checkbox_html_to_text": "Xử lý thẻ HTML, chuyển thành một dòng",
        "textproc_checkbox_strip_brackets": "Xóa text trong ngoặc (), [], {}, <>",
        "textproc_checkbox_strip_cloze": "Xóa ngoặc Cloze {{c1::text}}",
        "textproc_checkbox_ssml_convert": "Chuyển đổi ký tự SSML (như <, &&, v.v.)",
        "textproc_checkbox_run_replace_last": "Chạy quy tắc thay thế cuối cùng (bỏ chọn để chạy trước)",
        "textproc_checkbox_ignore_case": "Bỏ qua hoa thường (chỉ dành cho Regex)",
        "textproc_group_replacement_rules": "Quy tắc thay thế text",
        "textproc_label_add_rules": "Thêm quy tắc thay thế và nhấp đúp để sửa mẫu / thay thế",
        "textproc_button_add_simple": "Thêm quy tắc đơn giản",
        "textproc_button_add_regex": "Thêm quy tắc Regex",
        "textproc_button_remove_rule": "Xóa quy tắc đã chọn",

        # Batch tooltips
        "batch_tooltip_open": "Mở preset khác",
        "batch_tooltip_duplicate": "Nhân bản preset có sẵn",
        "batch_tooltip_save": "Lưu preset hiện tại",
        "batch_tooltip_rename": "Đổi tên preset hiện tại",
        "batch_tooltip_delete": "Xóa preset hiện tại",
        "batch_tooltip_save_and_close": "Lưu preset và đóng hộp thoại",
        "batch_tooltip_show_advanced": "Hiện tùy chọn xử lý text nâng cao",
        "batch_tooltip_hide_advanced": "Ẩn tùy chọn xử lý text nâng cao",
        "batch_button_preview": "Xem trước",
        "batch_button_apply": "Áp dụng",
        "batch_button_save_close": "Lưu & Đóng",
        "button_apply": "Áp dụng",

        # Easy component
        "easy_group_source_text": "\u2460 Văn bản nguồn",
        "easy_group_voice_selection": "\u2461 Chọn giọng đọc",
        "easy_group_target_field": "\u2462 Trường đích",
        "easy_tooltip_preview_with_shortcut": "Nghe thử âm thanh sẽ được tạo ({0})",
        "easy_tooltip_preview": "Nghe thử âm thanh sẽ được tạo",
        "easy_tooltip_add_with_shortcut": "Thêm âm thanh vào thẻ của bạn ({0})",
        "easy_tooltip_add": "Thêm âm thanh vào thẻ của bạn",

        # Voice selection easy
        "voiceselection_easy_label_language": "Ngôn ngữ:",
        "voiceselection_easy_label_service": "Dịch vụ:",
        "voiceselection_easy_label_voice": "Giọng đọc:",

        # Realtime side component
        "realtime_checkbox_enable_side": "Bật TTS thời gian thực cho mặt {0}",
        "realtime_button_preview_sound": "Nghe thử",
        "realtime_group_preview": "Xem trước",
        "realtime_label_text_pronounced": "Văn bản sẽ được đọc:",
        "realtime_button_playing_preview": "Đang phát thử...",

        # Preferences component
        "preferences_tab_keyboard_shortcuts": "Phím tắt",
        "preferences_tab_error_handling": "Xử lý lỗi",

        # GUI menus and tooltips
        "menu_add_audio_collection": "Thêm âm thanh (Nhiều thẻ)...",
        "menu_add_audio_collection_preset": "Thêm âm thanh (Nhiều thẻ): {0}...",
        "menu_add_audio_realtime": "Thêm âm thanh (Realtime)...",
        "menu_remove_audio_realtime": "Xóa âm thanh (Realtime) / TTS Tag...",
        "editor_tooltip_add_audio": "Super Free TTS: Thêm âm thanh vào thẻ (dựa trên quy tắc preset)",
        "editor_tooltip_preview_audio": "Super Free TTS: Nghe thử (Nghe âm thanh trước khi thêm)",
        "editor_tooltip_configure_presets": "Super Free TTS: Cấu hình quy tắc Preset cho thẻ này (cần làm trước khi thêm âm thanh)",

        # Piper Manager
        "piper_title": "Quản lý mô hình Piper",
        "piper_label_language": "Ngôn ngữ:",
        "piper_all_languages": "Tất cả ngôn ngữ",
        "piper_status_loading": "Đang tải danh sách giọng đọc từ Hugging Face...",
        "piper_button_download": "Tải về giọng đã chọn",
        "piper_status_loaded": "Đã tải {0} giọng đọc.",
        "piper_status_load_error": "Không tải được danh sách giọng: {0}",
        "piper_warning_load_error": "Lỗi khi tải danh sách giọng Piper: {0}",
        "piper_label_installed": "[Đã cài]",
        "piper_status_download_complete": "Tải xong!",
        "piper_info_download_success": "Tải mô hình thành công!",
        "piper_status_error": "Lỗi: {0}",
        "piper_warning_download_failed": "Tải thất bại: {0}",
        "piper_button_download_models": "Tải mô hình...",
        "piper_info_select_dir": "Vui lòng chọn thư mục mô hình trước.",

        # Welcome message
        "welcome_important": "Quan trọng",
        "welcome_configure_desc": "bạn cần cấu hình dịch vụ trước khi thêm âm thanh.",
        "welcome_configure_title": "Cấu hình dịch vụ",
        "welcome_configure_subtitle": "Nhấp vào đây trước khi thêm âm thanh",
        "welcome_no_audio_yet": "Có vẻ như bạn chưa thêm âm thanh nào.",
        "welcome_add_audio_title": "Thêm âm thanh",
        "welcome_add_audio_subtitle": "Nhấp để tìm hiểu cách thêm âm thanh",
        "welcome_heading": "Super Free TTS - Thêm âm thanh vào thẻ ghi nhớ",
        "welcome_close": "× Đóng",
    },
}


def _normalize_language(lang: str) -> str:
    """
    Chuẩn hóa mã ngôn ngữ. Nếu không hỗ trợ thì fallback về 'en'.
    """
    if lang not in SUPPORTED_LANGUAGES:
        return "en"
    return lang


def get_text(key: str, lang: str) -> str:
    """
    Lấy chuỗi giao diện theo key và ngôn ngữ.
    - Nếu lang không hợp lệ: dùng 'en'.
    - Nếu thiếu key trong lang hiện tại: fallback về 'en'.
    - Nếu vẫn thiếu: trả lại chính key (giúp debug).
    """
    lang = _normalize_language(lang)
    lang_dict = STRINGS.get(lang, STRINGS["en"])
    if key in lang_dict:
        return lang_dict[key]
    # fallback sang en nếu key không có trong lang hiện tại
    if key in STRINGS["en"]:
        return STRINGS["en"][key]
    # cuối cùng trả lại chính key
    return key

