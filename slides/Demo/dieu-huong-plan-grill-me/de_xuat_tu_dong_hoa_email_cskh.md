# ĐỀ XUẤT TRIỂN KHAI: TỰ ĐỘNG HÓA GỬI EMAIL CHĂM SÓC KHÁCH HÀNG DỊP CUỐI NĂM

**Người lập đề xuất:** Nguyễn Minh Tuấn — Chuyên viên Chăm sóc Khách hàng  
**Thời gian dự kiến chạy:** 08:00 sáng Thứ Hai tuần tới  
**Mục tiêu:** Tự động gửi email tri ân kèm mã giảm giá 20% cho toàn bộ danh sách khách hàng cũ của công ty.

---

## 1. Quy trình thực hiện dự kiến
1. Lấy danh sách toàn bộ **5.000 khách hàng** từ file `danh_sach_khach_hang_2024_2026.xlsx` (gồm cột `Ten_Khach_Hang`, `Email`, `Hang_The`).
2. Dùng AI trộn nội dung theo mẫu:
   > *"Chào anh/chị [Ten_Khach_Hang], cảm ơn anh/chị đã đồng hành cùng công ty. Gửi tặng anh/chị mã giảm giá VIP20 giảm ngay 20% cho mọi đơn hàng trong tháng này!"*
3. Kết nối tài khoản Gmail công ty (`cskh@congty.vn`) và bấm chạy tự động gửi một lượt hết 5.000 email trong buổi sáng.

---

## 2. Các điểm còn đang bỏ ngỏ (Chưa có phương án xử lý)
- Chưa kiểm tra xem trong 5.000 dòng Excel có khách hàng nào bị trống tên (`Ten_Khach_Hang` bị bỏ trống) hoặc sai định dạng email hay không.
- Chưa lọc danh sách những khách hàng từng phàn nàn hoặc đã yêu cầu ngừng nhận email quảng cáo (Unsubscribe) trước đây.
- Chưa tính đến giới hạn gửi mail của Gmail (gửi 5.000 mail cùng lúc có nguy cơ bị khóa tài khoản hoặc rơi vào hộp thư Rác/Spam).
- Mã giảm giá `VIP20` đang dùng chung cho mọi khách hàng, chưa giới hạn số lần nhập hoặc giá trị đơn hàng tối thiểu.
- Chưa có bước chạy thử (Test) trên 3–5 email nội bộ trước khi bắn hàng loạt.
