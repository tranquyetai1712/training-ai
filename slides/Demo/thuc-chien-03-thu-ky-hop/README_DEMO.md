# 🎙️ DEMO MẪU: THƯ KÝ HỌP AI — NGHE GHI ÂM, VIẾT BIÊN BẢN & ĐỒNG BỘ TRELLO / SLACK (BÀI 26–28)

Thư mục này cung cấp bộ dữ liệu Demo hoàn chỉnh cho **Phần 11 (Bài 11.1 – 11.3)**, kết hợp với Plugin **`q-thu-ky-hop`** (`.agents/plugins/q-thu-ky-hop/`) gồm kỹ năng `thu-ky-hop-tu-dong` và 2 file quy chuẩn (`quy-chuan-bien-ban-hop.md`, `quy-chuan-trello-slack.md`).

---

## 📁 1. File Ghi Âm Mẫu Có Sẵn

* **`cuoc_hop_giao_ban_tuan.mp3`**: Đoạn ghi âm cuộc họp giao ban đầu tuần nhiều giọng nói (Giám đốc Nguyễn Văn An, Trưởng phòng Marketing Hoàng Anh, Kế toán trưởng Thu Trang) — có cả vài câu chuyện phiếm đầu giờ về kẹt xe/trời mưa để AI tự lọc bỏ khi trích xuất biên bản!

### Đáp án chuẩn trong file ghi âm:
* **Quyết định đã chốt:**
  1. Ngày mở bán chính thức: **25/10/2026**
  2. Ngân sách marketing tối đa: **100.000.000 VNĐ**
* **Bảng phân công việc (Action Items):**
  | Công Việc Cụ Thể | Người Phụ Trách | Hạn Chót (Deadline) | Kết Quả Cần Bàn Giao |
  | :--- | :---: | :---: | :--- |
  | Thiết kế xong Landing Page giới thiệu sản phẩm | Hoàng Anh | 18/10/2026 (17h00) | Đường link trang web chạy thử nghiệm |
  | Lên kịch bản quảng cáo Facebook & TikTok | Thu Trang | 20/10/2026 (12h00) | File kế hoạch nội dung và ngân sách |
  | Kiểm kê số lượng tồn kho sản phẩm mẫu | Tuấn Vũ | 22/10/2026 (17h00) | Báo cáo kiểm kho có chữ ký thủ kho |

---

## 🎬 2. Câu Lệnh Mẫu Khi Quay Video

### Bài 11.2 (Nghe file ghi âm ➔ Xuất `bien_ban_hop_giao_ban.md`)
> *"Hãy dùng kỹ năng thư ký họp để lắng nghe file ghi âm `thuc-chien-03-thu-ky-hop/cuoc_hop_giao_ban_tuan.mp3`, lọc bỏ chuyện phiếm và lập biên bản cuộc họp chuẩn 3 phần (Tổng quan, Quyết định đã chốt, Bảng Action Items 4 cột) lưu thành `thuc-chien-03-thu-ky-hop/bien_ban_hop_giao_ban.md`. Không tự suy diễn thông tin ngoài bản ghi âm."*

### Bài 11.3 (Tạo thẻ Trello & Bắn thông báo Slack)
*(Yêu cầu đã bật kết nối Trello MCP và Slack MCP trong Antigravity)*
> *"Dựa trên bảng phân công việc trong biên bản cuộc họp vừa lập, hãy tạo 3 thẻ việc tương ứng trên bảng Trello `Chiến Dịch Tháng 10` tại cột `Cần Làm (To Do)` (gắn đúng người phụ trách và hạn chót), đồng thời gửi tin nhắn tóm tắt vào kênh Slack `#thong-bao-chung` cho toàn công ty nắm bắt."*
