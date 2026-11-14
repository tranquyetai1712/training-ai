---
name: dinh-khoan-no-co
description: "Use this skill to parse natural language transaction descriptions and map them to standard debit/credit accounting accounts."
---

# QUY TRÌNH TỰ ĐỘNG ĐỊNH KHOẢN KẾ TOÁN

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:

## Bước 1: Đọc sổ nhật ký giao dịch
Nạp file `giao_dich_raw.xlsx` chứa ngày, diễn giải và số tiền.

## Bước 2: Phân tích ngữ nghĩa diễn giải
Nhận diện bản chất kinh tế của giao dịch (chi phí, thu nợ, trả nợ, lương, thuế).

## Bước 3: Gán TK Nợ / TK Có
Ánh xạ sang hệ thống tài khoản theo Thông tư 200.

## Bước 4: Xuất file MISA Import
Lưu file `Giao_dich_da_dinh_khoan_import_misa.xlsx`.
