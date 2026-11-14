# 📋 HƯỚNG DẪN KẾT NỐI & THỰC HÀNH TRELLO MCP TỪ CON SỐ 0

Sổ tay hướng dẫn nhanh kích hoạt cổng kết nối **Trello MCP** cho Google Antigravity, giúp bạn thao tác trọn gói trên Trello (tạo bảng, tạo cột, thêm mới, chỉnh sửa, sắp xếp và báo cáo) ngay trong khung chat Antigravity mà không cần bấm tay trên trình duyệt.

---

## 🚀 3 Bước Thiết Lập Nhanh

### Bước 1: Lấy API Key & Token Trên Trello (Miễn Phí 100%)
1. Đăng nhập tài khoản Trello của bạn trên trình duyệt (có thể dùng tài khoản mới tinh, chưa có bảng hay thẻ nào).
2. Truy cập trang cấp khóa chính thức của Trello: [https://trello.com/app-key](https://trello.com/app-key).
3. Copy chuỗi **Personal Key (API Key)** hiển thị trên màn hình.
4. Nhấp vào liên kết **Token** (nằm ngay bên dưới mục API Key), bấm **Allow (Cho phép)** và copy chuỗi **Token** được cấp.

### Bước 2: Cấu Hình File `mcp_config.json`
Mở file `~/.gemini/config/mcp_config.json` (hoặc file `mcp_config.json` trong thư mục demo) và điền khóa của bạn:

```json
{
  "mcpServers": {
    "trello": {
      "command": "npx",
      "args": [
        "-y",
        "@delorenj/mcp-server-trello"
      ],
      "env": {
        "TRELLO_API_KEY": "<DÁN_TRELLO_API_KEY_CỦA_BẠN>",
        "TRELLO_TOKEN": "<DÁN_TRELLO_TOKEN_CỦA_BẠN>"
      }
    }
  }
}
```

### Bước 3: Kiểm Tra Trạng Thái Kết Nối Trong Antigravity
* Lưu file `mcp_config.json` và tải lại cổng MCP trong Antigravity Desktop.
* Khi biểu tượng server `trello` chuyển sang trạng thái **Connected**, bạn có thể bắt đầu ra lệnh ngay từ Antigravity!

---

## 🎯 Bộ 6 Câu Lệnh Thực Hành Từ Tài Khoản Trello Trống Trơn

Bạn chỉ cần copy/gõ lần lượt 6 câu lệnh dưới đây vào khung chat Antigravity:

1. **Khởi tạo bảng & cột mới:**
   > *Dùng Trello MCP tạo bảng mới tên "Vận Hành Văn Phòng Q4", bên trong tạo 3 cột theo thứ tự: "Cần Làm (To Do)", "Đang Thực Hiện" và "Hoàn Thành".*
2. **Thêm mới 5 thẻ công việc:**
   > *Thêm 5 thẻ vào cột "Cần Làm (To Do)": (1) Chốt báo giá thiết bị văn phòng, (2) Soạn dự thảo hợp đồng thuê mặt bằng, (3) Đối chiếu hóa đơn VAT tháng 10, (4) Lên lịch họp giao ban đầu tuần, (5) Đặt vé máy bay công tác Đà Nẵng — kèm mô tả ngắn cho từng thẻ.*
3. **Chỉnh sửa tiêu đề, mô tả & hạn chót:**
   > *Chỉnh sửa thẻ "Chốt báo giá thiết bị văn phòng": đổi tên thành "[KHẨN] Chốt báo giá thiết bị văn phòng", cập nhật mô tả "Cần duyệt trước 17h hôm nay để kịp đặt hàng" và gắn hạn chót là ngày mai.*
4. **Sắp xếp thứ tự & di chuyển thẻ giữa các cột:**
   > *Đẩy thẻ "[KHẨN] Chốt báo giá thiết bị văn phòng" lên vị trí đầu cột, đồng thời chuyển thẻ "Soạn dự thảo hợp đồng thuê mặt bằng" sang cột "Đang Thực Hiện" và thẻ "Đặt vé máy bay công tác Đà Nẵng" sang cột "Hoàn Thành".*
5. **Thêm ghi chú bình luận & checklist tiến độ:**
   > *Vào thẻ "Soạn dự thảo hợp đồng thuê mặt bằng", thêm bình luận "Đã gửi phòng pháp chế rà soát Điều 4, chờ phản hồi" và tạo checklist 2 mục: Kiểm tra điều khoản cọc, Trình ký Giám đốc.*
6. **Quét lại toàn bảng & lập báo cáo tổng hợp:**
   > *Quét toàn bộ bảng "Vận Hành Văn Phòng Q4" và xuất bảng Markdown tóm tắt trạng thái từng thẻ việc theo từng cột.*

---

## 🛠️ Các Công Cụ Chính AI Tự Động Sử Dụng
* `create_board` / `add_list_to_board`: Tạo bảng và các cột Kanban mới từ đầu.
* `add_card_to_list`: Thêm thẻ công việc mới kèm mô tả vào cột chỉ định.
* `update_card_details`: Sửa tên thẻ, mô tả, nhãn hoặc ngày hết hạn (Deadline).
* `move_card`: Di chuyển thẻ giữa các cột và sắp xếp lại vị trí thẻ.
* `list_boards` / `get_lists` / `get_cards_by_list_id`: Đọc dữ liệu bảng, cột và thẻ để tổng hợp báo cáo.
