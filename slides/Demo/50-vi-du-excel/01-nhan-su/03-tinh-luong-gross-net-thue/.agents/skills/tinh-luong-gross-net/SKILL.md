---
name: tinh-luong-gross-net
description: "Use this skill to calculate payroll, insurance deductions, and 7-tier progressive personal income tax."
---

# QUY TRÌNH LẬP BẢNG TÍNH LƯƠNG & THUẾ TNCN

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:

## Bước 1: Đọc bảng công & mức lương
Nạp file `du_lieu_luong_thang.xlsx` chứa lương cơ bản, phụ cấp, OT và số người phụ thuộc.

## Bước 2: Tính bảo hiểm bắt buộc
Tính trích BHXH/BHYT/BHTN 10.5% trên mức lương đóng bảo hiểm.

## Bước 3: Tính thuế TNCN lũy tiến
Áp dụng biểu thuế 7 bậc lũy tiến tính số thuế phải nộp.

## Bước 4: Tính lương Net thực nhận
Lương Net = Tổng thu nhập - Bảo hiểm - Thuế TNCN.
