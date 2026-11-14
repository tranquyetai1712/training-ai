# CẨM NANG HƯỚNG DẪN DEMO: 10-DOI-SOAT-SAO-KE-SO-QUY

## 1. Nỗi Đau & Bài Toán Thực Tế
Dò sao kê ngân hàng với sổ thu chi cực kỳ mất thời gian vì nội dung chuyển khoản viết tắt, dính chữ, hoặc khách trả gộp 2 hóa đơn một lúc.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu khách hàng chuyển khoản 28 triệu với nội dung vỏn vẹn 'Hoang Gia ck', làm thế nào bạn biết món tiền này trả cho hóa đơn nào nếu công ty đang có 2 hóa đơn 18tr và 10tr?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đối soát 2 file sao_ke_vcb.xlsx và so_thu_chi.xlsx. Hãy khớp các giao dịch dựa trên Số tiền, Ngày giao dịch (cho phép lệch tối đa 1 ngày) và nhận diện mờ Mã hóa đơn/Tên khách trong nội dung CK. Tìm ra cả các trường hợp 1 lệnh chuyển khoản bằng tổng của 2 hóa đơn cùng khách hàng. Xuất file Ket_qua_doi_soat_T10.xlsx gồm 3 sheet: Đã khớp 1-1, Khớp gộp đơn, và Chưa khớp.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không dặn AI tìm kiếm tổ hợp gộp tiền (Subset Sum), AI sẽ báo khoản 28 triệu là 'Không tìm thấy hóa đơn tương ứng'.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Ket_qua_doi_soat_T10.xlsx` bóc tách chuẩn xác các khoản đã khớp 1-1, chỉ ra trường hợp trả gộp đơn và khoanh vùng khoản tiền lạ.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Khả năng Fuzzy Matching kết hợp tìm tổ hợp tiền gộp đơn giải phóng kế toán khỏi hàng nghìn dòng dò mắt thủ công.
