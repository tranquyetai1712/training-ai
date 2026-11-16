---
name: trich-xuat-tin-nhan-zalo
description: "Tự động trích xuất, giải mã và tìm kiếm lịch sử tin nhắn từ cơ sở dữ liệu Zalo PC offline (hỗ trợ đọc tin nhắn dài ngày từ 10 đến 30+ ngày không phụ thuộc vào Zalo Web)."
---

# Kỹ năng: Trích Xuất Tin Nhắn Zalo PC Offline (`trich-xuat-tin-nhan-zalo`)

Kỹ năng này giúp AI Antigravity tự động trích xuất, giải mã và đọc lịch sử trò chuyện trực tiếp từ cơ sở dữ liệu SQLite của ứng dụng Zalo PC trên máy tính Windows.

## Khi nào sử dụng kỹ năng này?
- Người dùng yêu cầu xem/đọc/lấy tin nhắn Zalo của một người bạn hoặc nhóm chat trong một khoảng thời gian (ví dụ: "lấy tin nhắn với brother2 trong 20 ngày", "xem trao đổi nhóm Job WebWP tuần trước").
- Khi Zalo Web bị hết hạn phiên đăng nhập hoặc không hiển thị đầy đủ tin nhắn cũ.
- Người dùng yêu cầu xuất file JSON hoặc báo cáo Markdown lịch sử chat Zalo.

## Cách thức hoạt động
Kỹ năng sử dụng engine `zalo_engine.cjs` đi kèm tại thư mục `scripts/`.
Engine này tự động:
1. Nhận diện phiên bản Zalo PC và nạp runtime 32-bit SQLCipher có sẵn của Zalo.
2. Tự định vị thư mục dữ liệu Zalo Data (hỗ trợ cả ổ C, D, E...).
3. Tự giải mã cơ sở dữ liệu FTSM và SQLite.
4. Xuất kết quả ra file JSON và Markdown sạch, loại bỏ trùng lặp.

## Quy trình thực hiện của Agent

### Bước 1: Xác định mục tiêu và số ngày cần lấy
- Tìm tên người dùng hoặc nhóm (ví dụ: `brother2`, `Job WebWP`).
- Xác định số ngày cần lấy (mặc định là 20 ngày nếu người dùng không chỉ định).

### Bước 2: Chạy lệnh engine qua `run_command`
Đường dẫn engine:
`C:\Users\<Username>\.gemini\config\plugins\q-zalo\skills\trich-xuat-tin-nhan-zalo\scripts\zalo_engine.cjs`

1. **Liệt kê danh sách hội thoại gần đây:**
   ```powershell
   node "C:\Users\SingPC\.gemini\config\plugins\q-zalo\skills\trich-xuat-tin-nhan-zalo\scripts\zalo_engine.cjs" --list
   ```

2. **Tìm kiếm người/nhóm:**
   ```powershell
   node "C:\Users\SingPC\.gemini\config\plugins\q-zalo\skills\trich-xuat-tin-nhan-zalo\scripts\zalo_engine.cjs" --search "<tên>"
   ```

3. **Trích xuất tin nhắn:**
   ```powershell
   node "C:\Users\SingPC\.gemini\config\plugins\q-zalo\skills\trich-xuat-tin-nhan-zalo\scripts\zalo_engine.cjs" --target "<tên/ID>" --days <số_ngày> --out "<thư_mục_lưu>"
   ```

### Bước 3: Đọc file báo cáo Markdown và phản hồi cho người dùng
- Sau khi engine chạy xong, đọc file Markdown đã tạo trong thư mục `--out`.
- Trình bày tóm tắt cho người dùng theo từng mốc thời gian rõ ràng, lịch sự và chính xác.
