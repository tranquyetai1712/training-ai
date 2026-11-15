# Quy Tắc Phân Loại & Gán Nhãn Email

Tài liệu này định nghĩa hệ thống phân loại nhãn (Label Taxonomy) và các quy tắc kiểm soát gán nhãn cho toàn bộ các quy trình xử lý email thuộc plugin `q-email`.

---

## I. BỘ DIỆN NHÃN NGHIỆP VỤ (LABEL TAXONOMY)

Khi phân tích từng email, Agent BẮT BUỘC xếp loại vào một hoặc nhiều nhãn phù hợp theo danh sách bên dưới:

1. **`KinhDoanh/BaoGia`**: Email hỏi giá, yêu cầu gửi báo giá, tư vấn chi phí sản phẩm/dịch vụ.
2. **`KinhDoanh/HopTac`**: Email liên hệ hợp tác kinh doanh, đề xuất hợp tác B2B, tài trợ, đối tác.
3. **`KeToan/HoaDon`**: Email đính kèm hoặc chứa hóa đơn điện tử (VAT), chứng từ thanh toán, biên lai, sao kê.
4. **`NhanSu/Tuyendung`**: Email ứng tuyển, gửi CV, hồ sơ xin việc, liên hệ tuyển dụng.
5. **`CongNo/ThanhToan`**: Email nhắc nợ, thông báo hết hạn thanh toán, xác nhận đã chuyển khoản.
6. **`HanhChinh/ThongBao`**: Email thông báo hệ thống, thông báo gia hạn dịch vụ, bản tin nội bộ.
7. **`KhanCap`**: Email phàn nàn, khiếu nại gay gắt của khách hàng, sự cố hệ thống nghiêm trọng.
8. **`QuangCao_Spam`**: Email quảng cáo không mong muốn, tiếp thị hàng loạt, thư rác.

---

## II. QUY TẮC BẢO TOÀN VÀ CHỐNG TRÙNG LẶP

1. **Nhãn kiểm soát `AI_DaPhanLoai`:**
   - Mọi email sau khi được phân loại thành công **BẮT BUỘC** phải được gắn thêm nhãn `AI_DaPhanLoai`.
   - Nhãn này đóng vai trò là cờ đánh dấu (flag) giúp Agent nhận biết email đã qua xử lý.

2. **Điều kiện lọc email cần xử lý:**
   - Luôn truy vấn với bộ lọc: `-label:AI_DaPhanLoai`.
   - Không xử lý lại các email đã có nhãn này để tránh spam thông báo và lãng phí tài nguyên.

3. **Đảm bảo tồn tại nhãn trước khi gán:**
   - Trước khi gán bất kỳ nhãn nào, Agent phải kiểm tra danh sách nhãn hiện hữu trên Gmail qua Gmail MCP.
   - Nếu nhãn chưa tồn tại, Agent phải tạo nhãn mới trước khi thực hiện thao tác gán nhãn.
