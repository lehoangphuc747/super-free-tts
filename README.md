# Super Free TTS

**Super Free TTS** là một addon (tiện ích mở rộng) **100% MIỄN PHÍ** cho [Anki](https://apps.ankiweb.net/) giúp người dùng tự động thêm âm thanh text-to-speech (TTS) vào thẻ học một cách nhanh chóng và hiệu quả.

---

## ✨ Tính Năng Nổi Bật

- **100% Miễn phí**: Tuyệt đối không yêu cầu API key trả phí hay thuê bao hàng tháng.
- **Hỗ trợ đa dịch vụ**:
    - **EdgeTTS** (Microsoft): Chất lượng cao, giọng đọc tự nhiên (Khuyên dùng).
    - **Google Translate TTS**: Đơn giản, ổn định.
    - **Windows SAPI / macOS TTS**: Sử dụng giọng đọc có sẵn trong hệ điều hành.
    - **Từ điển trực tuyến**: Cambridge, Oxford, Naver, Youdao...
- **Linh hoạt**: 
    - Thêm audio cho từng thẻ riêng lẻ trong Editor.
    - Thêm audio hàng loạt (Batch) cho hàng ngàn thẻ cùng lúc.
    - **Realtime TTS**: Tự động phát âm thanh khi review mà không cần tạo file cứng.
- **Tự động hóa**: Thiết lập "Preset Mapping Rules" để tự động áp dụng giọng đọc dựa trên Deck hoặc Note Type.

## 🚀 Hướng Dẫn Cài Đặt

1. Copy thư mục dự án vào thư mục `addons21` của Anki.
2. Khởi động lại Anki.
3. Vào menu `Tools` → `Super Free TTS: Services Configuration` để bật các dịch vụ bạn muốn sử dụng (nên bật **EdgeTTS**).

## 🛠 Công Nghệ Sử Dụng

- **Ngôn ngữ**: Python 3.x
- **UI Framework**: PyQt5 / PyQt6
- **Thư viện chính**: `edge-tts`, `gtts`, `aiohttp`, `requests`.

## 👨‍💻 Tác giả

Dự án được phát triển bởi **Daniel from AnkiVN**.
- **Website**: [ankivn.com](https://ankivn.com)
- **Hỗ trợ**: Cộng đồng Anki Việt Nam.

---
*Cảm ơn bạn đã sử dụng Super Free TTS! Nếu thấy hữu ích, hãy để lại 1 star cho repo nhé!* ⭐
