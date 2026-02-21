# CHANGES — Lịch sử thay đổi Super Free TTS

File này ghi lại **các thay đổi theo phiên bản / theo thời gian**: đã sửa gì, thêm gì, để người dùng (kể cả không rành kỹ thuật) đọc được và AI có thể hiểu cấu trúc khi đọc file.

**Cách đọc:** Mỗi mục có phần *Cho người dùng* (giải thích đơn giản) và *Cho AI / kỹ thuật* (từ khóa, commit, file liên quan).

---

## [Chưa phát hành / Unreleased]

*Các thay đổi đã làm trong code nhưng chưa gộp vào bản phát hành chính thức.*

### Cho người dùng

- **Menu AnkiVN trong Tools**  
  Trong menu **Tools** giờ có menu **AnkiVN**, và **Super Free TTS** nằm bên trong menu AnkiVN này (dạng submenu). Bấm vào **AnkiVN → Super Free TTS** để mở cửa sổ cấu hình.

- **Một cửa sổ cấu hình duy nhất (Super Free TTS)**  
  Thay vì hai cửa sổ riêng (Cấu hình dịch vụ, Tùy chọn), giờ chỉ có **một cửa sổ** tên **Super Free TTS** với **hai tab lớn**:  
  - **Nguồn âm thanh** (Services): bật/tắt và cấu hình các nguồn TTS.  
  - **Cấu hình** (Preferences): ngôn ngữ giao diện, phím tắt, xử lý lỗi, v.v.  
  Cửa sổ mở **giữa màn hình**, có thể **kéo thanh title** và **co giãn** kích thước (không mở full màn hình mặc định).

### Cho AI / kỹ thuật

- **Menu: AnkiVN menu with Super Free TTS submenu.** Tools menu contains QMenu "AnkiVN" (objectName `ankivn_menu`). Inside this menu is QAction "Super Free TTS" (objectName `sf_action_main`) which opens `launch_superfreetss_dialog(hypertts)`. On init, removes old actions (`sf_action_services`, `sf_action_preferences`) if exist. Creates AnkiVN menu if not found, then adds Super Free TTS action as submenu item. Text from i18n `dialog_main_title`. File: `superfreetss_addon/gui.py`. Commit: `feat: Add AnkiVN menu with Super Free TTS as submenu item` (76f0b97).

- **Single config dialog (SuperFreeTTSMainDialog / SuperFreeTTSDialog):** One dialog replaces ConfigurationDialog and PreferencesDialog. Contains QTabWidget with two tabs: (0) Services — `component_configuration.Configuration`; (1) Preferences — `component_preferences.ComponentPreferences`. Opened via `launch_superfreetss_dialog(hypertts, initial_tab=0|1)`. Dialog opens **centered** on screen (`primaryScreen().availableGeometry()`, then `move()` to center); no `showMaximized()` so title bar is draggable and window is resizable. Alias: `SuperFreeTTSDialog = SuperFreeTTSMainDialog`. Files: `superfreetss_addon/gui.py`, `superfreetss_addon/i18n.py` (added `dialog_main_title`, `tab_services`, `tab_preferences`; en: "Services", "Preferences"; vi: "Nguồn âm thanh", "Cấu hình"). Commits: `feat: single Super Free TTS dialog (2 tabs), Tools menu submenu, open maximized; update CHANGES.md` (c03210e), `fix: single Tools menu item (no submenu), dialog centered and resizable; update CHANGES` (62a4fac).

---

## [1.0] — 2025-02-14

### Cho người dùng

- **Sửa thông báo welcome bị hiện hai lần**  
  Khi mở màn hình bộ thẻ (Deck Browser), thông báo “Super Free TTS - Add Audio to your Flashcards” (với nút Cấu hình dịch vụ) trước đây có thể hiện **hai khung giống hệt nhau**. Đã sửa để chỉ hiện **một khung**.

- **README**  
  Thêm file README.md chuyên nghiệp cho dự án.

- **Piper TTS**  
  Thêm và tối ưu hỗ trợ Piper TTS.

### Cho AI / kỹ thuật

- **Duplicate welcome fix:** `deck_browser_will_render_content` can be called multiple times; guard added so welcome HTML is appended only when `"superfreetss-welcome-message"` not already in `content.stats`. File: `superfreetss_addon/gui.py`.
- **Commit:** `fix: prevent duplicate welcome message in deck browser (hook called multiple times)` (3bafbca).
- **Other commits:** Add professional README.md (3b7f98a); Add and optimize pipertts (42924ed).
- **Version in code:** `superfreetss_addon/version.py` → `ANKI_SUPER_FREE_TTS_VERSION='1.0'`.

---

## Cấu trúc file (để AI parse)

- Mỗi phiên bản nằm trong section `## [số phiên bản hoặc Unreleased]`.
- Trong mỗi section: **Cho người dùng** (plain language, có thể tiếng Việt + tiếng Anh); **Cho AI / kỹ thuật** (keywords, file paths, commit messages).
- Có thể bổ sung thêm mục **Commit**, **Files changed**, **Breaking changes** tùy từng bản.
