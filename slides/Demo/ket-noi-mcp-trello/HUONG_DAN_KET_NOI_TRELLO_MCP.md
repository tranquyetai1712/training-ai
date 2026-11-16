# 📋 HƯỚNG DẪN KẾT NỐI & THỰC HÀNH TRELLO MCP TỪ CON SỐ 0

Sổ tay hướng dẫn nhanh kích hoạt cổng kết nối **Trello MCP** cho Google Antigravity qua giao diện **Customization (1-Click OAuth)**, kết hợp cùng **Skill chuẩn hóa thẻ việc** để dựng bảng, thêm sửa, bóc tách tài liệu từ máy tính và điều phối công việc hoàn toàn tự động ngay trong khung chat Antigravity mà không cần chạm tay vào trình duyệt Trello.

---

## 🚀 3 Bước Thiết Lập 1-Click (Không Cần Code, Không Cần API Key/Token)

### Bước 1: Mở Mục Customization Trong Antigravity
1. Khởi động **Antigravity Desktop** trên máy tính của bạn.
2. Nhấp vào biểu tượng hoặc menu **Customization** (khu vực quản lý Plugins & MCP Servers).

### Bước 2: Kết Nối Cổng Trello 1-Chạm
1. Trong danh sách các cổng kết nối / plugins, tìm đến mục **Trello**.
2. Nhấp vào nút **Connect** (hoặc **Sign In with Trello**).
3. Một cửa sổ trình duyệt an toàn sẽ mở ra để bạn xác thực tài khoản Trello: nhấp chọn **Allow (Cho phép)** để cấp quyền truy cập.

### Bước 3: Kiểm Tra Trạng Thái Kết Nối
* Khi biểu tượng server Trello chuyển sang màu xanh với trạng thái **Connected**, cổng MCP đã sẵn sàng hoạt động!
* Bạn có thể mở khung chat Antigravity và bắt đầu ra lệnh điều phối công việc ngay lập tức.

---

## 🎯 Bộ 8 Câu Lệnh Thực Chiến Từ Con Số 0 Đến Bảng Việc Chuyên Nghiệp

### Nhóm A: 5 Thao Tác Nền Tảng (Làm Chủ Trello Không Chạm Chuột)

1. **Khởi tạo bảng & cột mới:**
   > *Dùng Trello MCP tạo bảng mới tên "Vận Hành Văn Phòng Q4", bên trong tạo 3 cột theo đúng thứ tự: "Cần Làm (To Do)", "Đang Thực Hiện" và "Hoàn Thành".*
2. **Thêm nhanh các thẻ công việc:**
   > *Thêm giúp tôi 3 thẻ việc vào cột "Cần Làm (To Do)": (1) Chốt báo giá thiết bị văn phòng, (2) Soạn dự thảo hợp đồng thuê mặt bằng, (3) Đặt vé máy bay công tác Đà Nẵng — kèm mô tả ngắn cho từng thẻ.*
3. **Chỉnh sửa tiêu đề, mô tả & hạn chót:**
   > *Chỉnh sửa thẻ "Chốt báo giá thiết bị văn phòng": đổi tên thành "[KHẨN] Chốt báo giá thiết bị văn phòng", cập nhật mô tả "Cần duyệt trước 17h hôm nay để kịp đặt hàng" và gắn hạn chót là ngày mai.*
4. **Sắp xếp thứ tự & di chuyển thẻ giữa các cột:**
   > *Đẩy thẻ "[KHẨN] Chốt báo giá thiết bị văn phòng" lên vị trí đầu cột, đồng thời chuyển thẻ "Soạn dự thảo hợp đồng thuê mặt bằng" sang cột "Đang Thực Hiện" và thẻ "Đặt vé máy bay công tác Đà Nẵng" sang cột "Hoàn Thành".*
5. **Thêm ghi chú bình luận & checklist tiến độ:**
   > *Vào thẻ "Soạn dự thảo hợp đồng thuê mặt bằng", thêm bình luận "Đã gửi phòng pháp chế rà soát Điều 4, chờ phản hồi" và tạo checklist 2 mục: Kiểm tra điều khoản cọc, Trình ký Giám đốc.*

---

### Nhóm B: 3 Kịch Bản Đột Phá (Thao Tác Tay Chào Thua Sức Mạnh AI)

6. **Cú hích Skill: Biến văn bản thô cộc lốc thành Thẻ Trello chuẩn Doanh nghiệp:**
   *(Yêu cầu có Skill `trello-task-standardizer` trong thư mục demo)*
   > *Thêm thẻ Trello: làm hợp đồng thuê xe 29 chỗ chở nhân viên đi du lịch hè, ngân sách dưới 15 triệu, liên hệ 3 nhà xe, xong trước thứ 5.*
   *(AI sẽ tự động chuẩn hóa tiêu đề thành `[HÀNH CHÍNH] Ký hợp đồng thuê xe du lịch hè 29 chỗ`, format mô tả chuẩn Agile: 🎯 Mục tiêu, 👤 PIC & Deadline, 📋 Checklist 4 bước, ✅ Tiêu chí hoàn thành DoD, ⚠️ Ràng buộc ngân sách).*

7. **Cầu nối đa nguồn: Bóc tách file ghi chú họp lộn xộn trên máy lên Trello:**
   > *Đọc tệp ghi chú cuộc họp "ghi_chu_cuoc_hop_tho.txt" trong thư mục này: tự động bóc tách các đầu việc của từng phòng ban, phân loại việc khẩn đưa lên đầu và nạp thành các thẻ việc ngay ngắn vào cột "Cần Làm"!*
   *(AI đọc file văn bản trên máy tính, trích xuất việc của Hành chính, Kế toán, Nhân sự và tự động tạo thẻ trên Trello mà không cần copy-paste thủ công).*

8. **Trợ lý kiểm toán & Quét báo cáo tiến độ thông minh:**
   > *Hãy quét toàn bộ bảng "Vận Hành Văn Phòng Q4": thẻ nào có chữ [KHẨN] hoặc deadline trong hôm nay thì tự gắn nhãn Đỏ và thêm bình luận nhắc nhở tiến độ. Sau đó, lập bảng Markdown tóm tắt tiến độ toàn bộ dự án.*

---

## 🛠️ Các Công Cụ & Skill AI Tự Động Phối Hợp Sử Dụng
* **Skill `trello-task-standardizer`:** Khuôn mẫu chuyên môn tự động cấu trúc hóa nội dung thô thành thẻ chuẩn Agile/Scrum.
* **Trello MCP Tools:**
  * `create_board` / `add_list_to_board`: Tạo bảng và các cột Kanban mới từ đầu.
  * `add_card_to_list`: Thêm thẻ công việc mới kèm mô tả và checklist vào cột chỉ định.
  * `update_card_details`: Sửa tên thẻ, mô tả, nhãn hoặc ngày hết hạn (Deadline).
  * `move_card`: Di chuyển thẻ giữa các cột và sắp xếp lại vị trí thẻ.
  * `get_lists` / `get_cards_by_list_id`: Đọc dữ liệu thẻ để kiểm toán và lập báo cáo tổng hợp.
