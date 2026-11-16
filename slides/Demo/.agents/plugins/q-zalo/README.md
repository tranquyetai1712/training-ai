# Plugin `q-zalo` - Trích Xuất Dữ Liệu Zalo PC Cho Antigravity

Plugin tự động trích xuất, giải mã và tìm kiếm lịch sử tin nhắn từ cơ sở dữ liệu SQLite của ứng dụng Zalo PC (hỗ trợ đọc tin nhắn dài ngày từ 10 đến 30+ ngày không phụ thuộc vào Zalo Web).

---

## 🚀 Hướng Dẫn Cài Đặt Sang Máy Mới (1 Bước)

Giả sử bạn có một máy tính mới đã cài đặt **Zalo PC** và **Antigravity**:

1. **Copy thư mục `q-zalo`**:
   Copy toàn bộ thư mục `q-zalo` vào đường dẫn sau trên máy mới:
   ```
   C:\Users\<Tên_User_Máy_Mới>\.gemini\config\plugins\q-zalo\
   ```

2. **Khởi động lại Antigravity** (hoặc mở session mới):
   Antigravity sẽ tự động nhận diện skill `trich-xuat-tin-nhan-zalo`.

> [!TIP]
> **Không cần cài đặt thêm thư viện (Zero npm install)**! Script tự động tận dụng runtime Node.js và module SQLite 32-bit có sẵn bên trong Zalo PC.

---

## 🛠 Cách Sử Dụng Trực Tiếp Qua Dòng Lệnh (CLI)

Bạn hoặc AI có thể chạy trực tiếp bằng lệnh:

```bash
# 1. Xem danh sách các cuộc trò chuyện gần nhất
node scripts/zalo_engine.cjs --list

# 2. Tìm kiếm ID người dùng hoặc nhóm theo tên
node scripts/zalo_engine.cjs --search "brother2"
node scripts/zalo_engine.cjs --search "Job WebWP"

# 3. Trích xuất tin nhắn theo số ngày (mặc định 20 ngày)
node scripts/zalo_engine.cjs --target "brother2" --days 20
node scripts/zalo_engine.cjs --target "Job WebWP" --days 20
```

Hoặc dùng file `run.bat`:
```cmd
run.bat --target "brother2" --days 20
```

---

## 📁 Kết Quả Đầu Ra
Dữ liệu trích xuất sẽ được tự động lưu vào thư mục `zalo_output/`:
- `<tên>_messages.json`: File JSON chứa toàn bộ dữ liệu tin nhắn chi tiết.
- `<tên>_report.md`: File Markdown tổng hợp lịch sử chat theo từng ngày.
