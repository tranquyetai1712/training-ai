---
name: q-sync-storage
description: Đồng bộ hóa toàn bộ thư mục storage giữa các dự án có chung prefix trong thư mục /var/www/html.
---

# 🔄 Đồng bộ hóa thư mục storage (sync_storage)

Skill này hỗ trợ đồng bộ hóa đệ quy toàn bộ thư mục `storage/` từ dự án hiện tại sang các dự án khác có chung tiền tố (prefix) tên thư mục (ví dụ: `halo_web`, `halo_web_v2`, `halo_api` có chung prefix là `halo`).

## ⚙️ Cách hoạt động

Skill thực hiện chạy script `sync_storage.sh` nằm trong thư mục của skill. 
Script tự động phát hiện tiền tố của dự án hiện tại, quét các thư mục đích trong `/var/www/html` có cùng tiền tố và thực hiện sao chép đệ quy thư mục `storage/`.

> [!IMPORTANT]
> Mặc định, thư mục `storage/events/` (thường chứa các file cơ sở dữ liệu SQLite3 của từng tenant) sẽ **bị bỏ qua (skipped/excluded)** trong quá trình đồng bộ để tối ưu hiệu năng và tránh sao chép dữ liệu database cồng kềnh.

## 🛠️ Tham số hỗ trợ

- **Không truyền tham số (Mặc định):** Chỉ đồng bộ thêm mới hoặc cập nhật các file từ nguồn sang đích. Các file chỉ tồn tại ở đích (ví dụ file `B.md`) sẽ **không bị xóa**.
- **`--delete` hoặc `-d`:** Đồng bộ hai thư mục giống hệt nhau. Bất kỳ file nào chỉ tồn tại ở đích mà không có ở nguồn sẽ **bị xóa**.

## 🚀 Cách sử dụng

Bạn có thể kích hoạt skill bằng cách chạy script trực tiếp trên terminal của dự án hiện tại:

```bash
# Run synchronization without deleting target-only files
bash /home/tranquyet/.gemini/config/plugins/quyetchasqui/skills/q-sync-storage/sync_storage.sh

# Run synchronization and delete target-only files
bash /home/tranquyet/.gemini/config/plugins/quyetchasqui/skills/q-sync-storage/sync_storage.sh --delete
```
