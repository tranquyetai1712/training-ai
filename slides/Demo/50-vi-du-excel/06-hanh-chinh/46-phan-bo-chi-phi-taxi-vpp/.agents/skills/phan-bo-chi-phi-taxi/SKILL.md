---
name: phan-bo-chi-phi-taxi
description: "Use this skill to map corporate ride-hailing/utility invoices to department cost centers and flag policy exceptions."
---

# QUY TRÌNH PHÂN BỔ CHI PHÍ TAXI VÀ KIỂM SOÁT NGOÀI GIỜ

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:

## Bước 1: Đọc bảng kê Grab và nhân sự
Nạp file `bang_ke_taxi.xlsx` và `nhan_su.xlsx`.

## Bước 2: Gán phòng ban & Lọc giờ
Ánh xạ Cost Center và lọc chuyến đi sau 22h hoặc ngày nghỉ.

## Bước 3: Xuất báo cáo chi phí
Lưu file `Phan_bo_chi_phi_Grab_T10.xlsx`.
