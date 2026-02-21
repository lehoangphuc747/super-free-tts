# Plan: Super Free TTS — Code & UI/UX Improvement

**TL;DR**: Nâng cấp toàn diện addon Super Free TTS qua 5 phase: (1) Fix critical bugs gây crash, (2) Dọn dead code ~730+ dòng thừa từ HyperTTS Pro, (3) Thống nhất design system và fix styling bugs, (4) Hoàn thiện i18n cho 100% strings, (5) Cải thiện UX/UI components. Tổng cộng ~40 thay đổi cụ thể, ưu tiên theo severity. Mọi thay đổi đều backward-compatible, không break config hiện có của user.

---

## Phase 1: Critical Bug Fixes (Priority: CRITICAL)

**1.1** Fix night mode crash — Add `GREEN_COLOR_NIGHTMODE` và `RED_COLOR_NIGHTMODE` vào `constants.py` (line 153-154), giá trị phù hợp dark theme (e.g., lighter green/red). Hiện tại `anki_utils.get_green_css_color()` / `get_red_css_color()` sẽ **crash với `AttributeError`** khi Anki ở night mode.

**1.2** Fix wrong import — Xóa dòng `from asyncio.proactor_events import constants` tại `component_target.py` line 1. Đây là import sai module, bị shadow bởi dòng 7 `from . import constants`. Trên macOS/Linux sẽ gây lỗi nếu dòng shadow bị xóa.

**1.3** Fix `setStyleSheet(None)` — 5 chỗ truyền `None` thay vì `""`, có thể gây TypeError trên một số Qt version:
   - `component_realtime.py` line 134
   - `component_presetmappingrules.py` line 293
   - `component_presetmappingrules.py` line 304
   - `component_batch.py` line 200
   - `component_batch.py` line 546

**1.4** Fix duplicate class — `component_text_processing.py`: `TextProcessing` class defined twice (line 14 incomplete, line ~152 complete). Xóa class stub ở line 14-17.

---

## Phase 2: Dead Code Cleanup (~730+ lines)

**2.1** Xóa 3 file entirely dead:
   - `cloudlanguagetools.py` (226 lines) — CLT API client cho HyperTTS Pro, kèm **HMAC secret key hardcoded** (security risk)
   - `component_trialsignup.py` (375 lines) — Trial signup flow cho vocab.ai Pro
   - `component_services_configuration.py` (~130 lines) — Dialog chọn trial vs manual config

**2.2** Clean dead code trong active files:

| File | What to Remove |
|------|----------------|
| `superfreetss.py` | `save_superfreetss_pro_api_key()` (line 796), `superfreetss_pro_enabled()` (line 820), `config_register_added_audio()` (line 810) |
| `servicemanager.py` | `configure_cloudlanguagetools()`, `use_cloud_language_tools()`, `hypertts_pro_mode` flag, dead CLT routing branch in `get_tts_audio_implementation()` |
| `config_models.py` | `HyperTTSProAccountConfig`, dead `TrialRegistrationStep` values, `TrialRequestReponse`, `ServicesConfigurationMode`, `EasyAdvancedMode`, vestigial Pro fields (`hypertts_pro_api_key`, `use_vocabai_api`, `vocabai_api_url_override`) |
| `constants.py` | ~15 empty Pro string constants (lines 367-375), Pro trial text constants (lines 340-360), `CLOUDLANGUAGETOOLS_API_BASE_URL`, `VOCABAI_API_BASE_URL` |
| `component_configuration.py` | `hyperttspro_account_config_change()`, `cloud_language_tools_enabled()` |
| `gui_utils.py` | `get_vocab_ai_url()` (line 174), dead `variant == 'white'` branch in `get_superfreetss_label_header()` |
| `gui.py` | Dead trial registration checks in `should_show_welcome_message()` (lines 460-480) |
| `__init__.py` | Dead Sentry/Pro key checks (line 112), dead stats fields (line 168) |

**2.3** Fix test logger in production — Thay `get_test_child_logger()` bằng `get_child_logger()` tại:
   - `component_services_configuration.py` line 10 (file sẽ bị xóa ở 2.1)
   - `component_choose_easy_advanced.py` line 11

---

## Phase 3: Design System Unification

**3.1** Thống nhất button styling — Migrate tất cả từ legacy `get_green_stylesheet()` / `get_red_stylesheet()` sang modern `configure_primary_button()` / `configure_secondary_button()` từ `gui_utils.py`. Files cần migrate:
   - `component_realtime.py`
   - `component_presetmappingrules.py`
   - `component_preferences.py`
   - `component_easy.py`
   - `component_configuration.py`

**3.2** Xóa alias confusing — Xóa `configure_purple_button = configure_primary_button` trong `gui_utils.py`. Update mọi caller dùng `configure_purple_button` → `configure_primary_button`.

**3.3** Tạo font size tokens — Thêm vào `constants.py`:
   - `FONT_SIZE_TITLE = 16` (thống nhất từ 12-20pt hiện tại)
   - `FONT_SIZE_SUBTITLE = 13`
   - `FONT_SIZE_BODY = 11`
   - `FONT_SIZE_SMALL = 9`
   Refactor 57 chỗ `setPointSize()` hardcoded trong codebase.

**3.4** Centralize inline styles — Di chuyển ~58 inline `setStyleSheet()` calls vào `STYLESHEET_DIALOG` hoặc tạo named style constants. Đặc biệt:
   - `component_about.py`: 5 inline styles → tạo `ABOUT_*` style constants
   - `component_configuration.py`: 10 inline styles cho TOC/cards → tạo `CONFIG_*` style constants
   - `component_choose_easy_advanced.py`: 4 inline styles

**3.5** Night mode support cho custom colors — Đảm bảo tất cả `COLOR_*` tokens có bản night mode tương ứng, sử dụng `Palette` system hoặc explicit night mode check. Tạo `COLOR_PRIMARY_DARK`, `COLOR_SURFACE_DARK`, etc.

---

## Phase 4: i18n Completion

**4.1** Audit & add ~120+ missing keys vào `i18n.py` cho cả EN và VI. Chia theo component:

| Component | ~Keys cần thêm |
|-----------|----------------|
| `component_source.py` | 3 (`source_mode`, `source_configuration`, `additional_settings`) |
| `component_target.py` | 7 (sound tag modes, field labels) |
| `component_target_easy.py` | 4+ (field/position options) |
| `component_shortcuts.py` | 3 (`editor_add_audio`, `editor_preview_audio`, `clear`) |
| `component_errorhandling.py` | 5 (error handling labels) |
| `component_mappingrule.py` | 8 (preview/run/edit/delete, preset labels) |
| `component_choosepreset.py` | 4 (new/existing/ok/cancel) |
| `component_text_processing.py` | 7 (processing rules labels) |
| `component_batch.py` | 8+ (advanced, preview, apply, save, tooltips) |
| `component_easy.py` | 3 (①②③ group titles) |
| `component_voiceselection_easy.py` | 3 (language/service/voice) |
| `component_about.py` | full about text |
| `component_realtime_side.py` | 3 (tab labels) |
| `component_preferences.py` | 2 (tab labels) |
| `gui.py` | 4+ (browser menu items) |
| `gui.py` | 3 (editor button tooltips) |
| `errors.py` | ~25 error messages |

**4.2** Replace tất cả hardcoded strings bằng `i18n.get_text()` calls trong từng component tương ứng.

**4.3** Fix wrong product name references:
   - `component_errorhandling.py`: `"help improve HyperTTS"` → `"help improve Super Free TTS"`
   - `errors.py` line 115: `vocab.ai/tutorials/hypertts-getting-started` → link đúng
   - `gui.py` line 540: welcome message links to `vocab.ai` → link đúng
   - `__init__.py` line 36: `HYPER_TTS_DEBUG_LOGGING` → `SUPER_FREE_TTS_DEBUG_LOGGING`

**4.4** Fix typo: `component_about.py` — `"build for the community"` → `"built for the community"`

---

## Phase 5: UX/UI Improvements

**5.1** Extract welcome message — Di chuyển ~120 dòng inline HTML/CSS/JS từ `gui.py` (lines 460-590) ra file template riêng (e.g., `templates/welcome.html`). Sử dụng string templating thay vì f-string concatenation. Đảm bảo support night mode qua CSS variables thay vì inline color.

**5.2** Cải thiện Piper Manager UX (`component_piper_manager.py`):
   - Thêm download timeout (hiện không có)
   - Thêm cancel button cho download đang chạy
   - Cleanup thread on dialog close
   - Xóa hardcoded `vi_VN` preference (line 186)

**5.3** Cải thiện Easy mode UX (`component_easy.py`):
   - Thêm visual progress indicator cho wizard steps (highlight active step)
   - Thêm validation feedback — disable nút "Apply" khi thiếu selection, kèm tooltip giải thích

**5.4** Cải thiện error UX:
   - Thay `raise Exception` generic bằng specific `HyperTTSError` subclasses
   - Thêm user-friendly error dialog thay vì raw exception display
   - Add timeout cho EdgeTTS async calls (hiện hang vô thời hạn)
   - Add retry logic cho network failures (dictionary services)

**5.5** Cải thiện Service Configuration UX (`component_configuration.py`):
   - Thêm loading indicator khi scan services
   - Thêm service status badges (available/unavailable/error)
   - Cải thiện search filter — highlight matching text trong service cards

**5.6** Rename internal variable `hyper_tts` / `hypertts` → `superfreetss` hoặc `sftts` xuyên suốt codebase (~30+ files). Đây là cosmetic nhưng quan trọng cho maintainability.

**5.7** Standardize comments — Chuyển Vietnamese comments sang English hoặc xóa (files: `component_piper_manager.py`, `component_presetmappingrules.py`, `component_preferences.py`).

**5.8** Fix `component_realtime_source.py` bug — Line 39: `load_model` set `source_type_combobox` twice thay vì set `source_field_type_combobox`. Verify và fix logic.

---

## Verification

| Phase | How to Test |
|-------|-------------|
| Phase 1 | Bật Anki night mode → mở Super Free TTS dialog → confirm no crash. Test tất cả button states. |
| Phase 2 | `grep -r "cloudlanguagetools\|TrialSignup\|ServicesConfiguration\|hypertts_pro" superfreetss_addon/` → should return 0 results. Mở addon → tất cả features still work. |
| Phase 3 | Visual inspection: tất cả buttons cùng style, font sizes consistent. Test night mode styling. |
| Phase 4 | Chuyển language sang VI trong Preferences → mọi string hiển thị tiếng Việt. Grep `"'[A-Z].*'"` trong component files → no hardcoded English UI strings. |
| Phase 5 | Test Piper download + cancel. Test Easy mode workflow. Test Edge TTS timeout. Test realtime source loading. |

---

## Decisions & Notes

- **Giữ lại `sentry_utils.py` và `stats.py`**: Dù disabled, đây là infrastructure files có thể re-enable. Chỉ clean dead *Pro-specific* code.
- **Không xóa `component_superfreettpro.py`**: File này có thể đã được reference từ chỗ khác, cần verify trước khi xóa (low priority).
- **Variable rename `hyper_tts` → Phase 5.6**: Đặt cuối vì scope lớn (~30 files) và chỉ cosmetic, không ảnh hưởng functionality.
- **Config migration**: Khi xóa vestigial Pro fields từ `config_models.py`, cần bump schema version (4→5) và add migration logic để không break existing user configs.
