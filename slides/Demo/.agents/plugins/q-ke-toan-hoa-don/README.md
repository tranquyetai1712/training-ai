# Plugin `q-ke-toan-hoa-don` — Kế Toán Số: Đọc Ảnh Hóa Đơn & Xuất Excel Chuẩn Công Thức

Plugin giúp trợ lý AI đọc hiểu hàng loạt ảnh chụp hóa đơn (kể cả ảnh nghiêng hoặc giấy in nhiệt hơi mờ), bóc tách chuẩn xác số tiền trước thuế, thuế VAT, tổng thanh toán và xuất ra bảng kê Excel `.xlsx` có sẵn công thức `=SUM(...)` đúng chuẩn doanh nghiệp.

---

## 📁 Cấu Trúc Thư Mục

```text
q-ke-toan-hoa-don/
├── plugin.json
├── README.md
├── rules/
│   └── quy-chuan-bang-ke-excel.md
└── skills/
    └── boc-tach-hoa-don-excel/
        ├── SKILL.md
        └── scripts/
            └── tao_bang_ke_excel.py
```

---

## 🚀 Cách Sử Dụng Nhanh

1. Đặt toàn bộ ảnh chụp hóa đơn (`.png`, `.jpg`, `.jpeg`) vào một thư mục (ví dụ: `HoaDon_CongTac`).
2. Nhắn yêu cầu bằng tiếng Việt tự nhiên:
   > *"Hãy đọc toàn bộ ảnh hóa đơn trong thư mục `HoaDon_CongTac`, lập bảng đối chiếu chi tiết rồi xuất thành file `bang_ke_chi_phi_cong_tac.xlsx` chuẩn công thức `=SUM()` giúp tôi."*
