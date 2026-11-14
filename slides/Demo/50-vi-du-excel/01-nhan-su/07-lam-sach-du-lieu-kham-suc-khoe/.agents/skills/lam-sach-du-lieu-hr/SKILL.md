---
name: lam-sach-du-lieu-hr
description: "Use this skill to clean up messy user-submitted forms, fixing capitalization, phone numbers, and dates."
---

# QUY TRÌNH LÀM SẠCH DỮ LIỆU ĐĂNG KÝ NHÂN SỰ

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:

## Bước 1: Đọc file form thô
Nạp file `dang_ky_kham_suc_khoe_raw.xlsx`.

## Bước 2: Xử lý chuỗi & Format
Sử dụng các quy tắc regex và xử lý chuỗi để chuẩn hóa tên, SĐT, CCCD và ngày sinh.

## Bước 3: Phát hiện trùng lặp
Đánh dấu các dòng trùng lặp số CCCD nếu có.

## Bước 4: Lưu file chuẩn
Lưu thành `danh_sach_chuan_gui_benh_vien.xlsx`.
