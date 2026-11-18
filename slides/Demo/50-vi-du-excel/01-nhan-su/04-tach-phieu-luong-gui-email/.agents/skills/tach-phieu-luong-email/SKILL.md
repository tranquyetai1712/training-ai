---
name: tach-phieu-luong-email
description: "Use this skill to split a master payroll spreadsheet into individual payslips matching the Chasqui template and prepare personalized Gmail drafts."
---

# QUY TRÌNH TÁCH PHIẾU LƯƠNG VÀ TẠO EMAIL NHÁP

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:

## Bước 1: Đọc bảng lương tổng
Nạp file `bang_luong_chot.xlsx` gồm 15 cột dữ liệu nhân viên, lương cơ bản, trợ cấp, OT, bảo hiểm, giảm trừ, thuế và thực lĩnh.

## Bước 2: Tách phiếu lương Excel chuẩn mẫu
Lặp qua từng nhân viên, tạo file `.xlsx` riêng trong `Phieu_Luong_Ca_Nhan/` theo đúng format PAYROLL SLIP của `_ket_qua_mau_chuan.xlsx` với công thức sống.

## Bước 3: Tạo bản nháp Gmail
Sử dụng trực tiếp công cụ Gmail tích hợp sẵn trong Antigravity để tạo các bản nháp email chứa bảng lương HTML cá nhân hóa.
