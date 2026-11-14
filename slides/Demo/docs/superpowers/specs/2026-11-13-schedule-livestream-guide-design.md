# Thiết Kế Kịch Bản Livestream: Ứng Dụng Lệnh `/schedule` Trong Công Việc & Học Tập

- **Ngày tạo:** 2026-11-13
- **Chủ đề:** Làm chủ tính năng `/schedule` (Lên lịch hẹn giờ & Tự động hóa định kỳ) trong Google Antigravity
- **Thời lượng:** 60 phút
- **Đối tượng khán giả:** Dân văn phòng, sinh viên, người tự học, quản lý dự án, freelancer và người dùng AI muốn tối ưu hóa năng suất.

---

## 1. Bối Cảnh & Mục Tiêu

### 1.1. Nỗi đau thực tế (Problem Statement)
Hầu hết người dùng AI hiện nay chỉ sử dụng theo cơ chế đồng bộ thụ động (Synchronous & Passive):
1. Người dùng gõ câu lệnh (Prompt).
2. Người dùng phải ngồi chờ AI sinh câu trả lời trước màn hình.
3. Nếu cần làm tác vụ sau đó 30 phút hoặc mỗi ngày lúc 9h sáng, người dùng phải tự nhớ và gõ lại bằng tay.
4. Chuông báo thức hoặc ứng dụng nhắc việc (Google Calendar, Reminders) chỉ kêu "bíp bíp" rồi người dùng vẫn phải tự tay vào làm.

### 1.2. Giải pháp đột phá từ Google Antigravity `/schedule`
Lệnh `/schedule` cung cấp khả năng tự động hóa nền (Background Scheduling) với các ưu điểm vượt trội:
- **Tự động thức dậy làm việc:** Không chỉ nhắc nhở tĩnh mà AI thực sự kích hoạt các công cụ (Tools: đọc file, duyệt web, gửi email, tạo bảng tính, nhắn tin) để hoàn thành tác vụ.
- **Non-blocking (Không gián đoạn):** Agent giải phóng phiên chat ngay lập tức, người dùng tiếp tục giao tiếp bình thường mà không bị treo phiên làm việc.
- **Tương tác linh hoạt:** Hỗ trợ cả ngôn ngữ tự nhiên (`in 15 minutes`, `every weekday at 9am`) lẫn biểu thức Cron tiêu chuẩn 5 trường.

---

## 2. Kiến Trúc Kỹ Thuật Của `/schedule`

### 2.1. Hai chế độ vận hành chính

| Đặc tính | One-shot Timers (Hẹn 1 lần) | Recurring Cron Schedules (Định kỳ) |
|---|---|---|
| **Cơ chế** | Đếm ngược khoảng thời gian cố định rồi chạy đúng 1 lần | Lặp lại theo biểu thức chu kỳ 5 trường Cron |
| **Tham số chính** | `DurationSeconds`, `Prompt`, `TimerCondition` | `CronExpression`, `Prompt`, `MaxIterations`, `IsDaemon` |
| **Hủy sớm** | Hỗ trợ `TimerCondition` (`any`, `never`, `<sender-id>`) | Hủy thủ công qua `/tasks` hoặc khi chạm `MaxIterations` |
| **Ứng dụng điển hình**| Chờ tiến trình nền hoàn tất, nhắc chuẩn bị họp, kiểm tra kết quả | Báo cáo đầu ngày, quét dọn file cuối tuần, nhắc nộp báo cáo |

### 2.2. Vòng đời tác vụ & Bảng điều khiển `/tasks`
- Khi lệnh `/schedule` được gọi, một background task được tạo trong session hiện tại.
- Trạng thái chuyển đổi: `Pending` (Đang chờ) $\rightarrow$ `Fired / Active` (Đang chạy) $\rightarrow$ `Completed` (Hoàn thành).
- Quản lý qua giao diện `/tasks`:
  - Phím `k` (Kill): Hủy một lịch trình đang chờ.
  - Phím `x` (Prune): Xóa các tác vụ đã hoàn tất khỏi bảng danh sách.
  - Phím `Enter`: Xem chi tiết thông số và log tác vụ.

---

## 3. Kho Dữ Liệu 30 Ví Dụ Thực Chiến

### Nhóm A: Dân Văn Phòng, Hành Chính, Kế Toán & Nhân Sự (8 ví dụ)
1. **Tóm tắt Email quan trọng đầu ngày:**
   `/schedule every weekday at 08:30 "Quét các email mới chưa đọc trong Gmail, lọc ra các email từ sếp và khách hàng, tóm tắt 3 đầu việc khẩn cấp nhất"`
2. **Nhắc nhở và chuẩn bị tài liệu trước cuộc họp 15 phút:**
   `/schedule in 45 minutes "Kiểm tra Google Calendar xem cuộc họp lúc 14:00 nội dung là gì, đọc file tài liệu đính kèm và tóm tắt nhanh 3 ý chính để tôi nắm trước khi vào họp"`
3. **Tự động nhắc nộp Báo cáo tuần vào chiều Thứ 6:**
   `/schedule every Friday at 16:00 "Kiểm tra thư mục Google Drive 'Báo cáo tuần', xem phòng ban nào chưa nộp file và soạn sẵn bản nháp thông báo nhắc nhở lên kênh Slack chung"`
4. **Theo dõi nhân sự sắp hết hạn thử việc / hợp đồng lao động:**
   `/schedule every Monday at 09:00 "Mở file Google Sheet 'Danh sách nhân sự', lọc những ai sắp hết hạn thử việc trong vòng 7 ngày tới và gửi danh sách cho HR Manager"`
5. **Nhắc chốt order cơm trưa cho phòng ban:**
   `/schedule every weekday at 10:45 "Đăng tin nhắn bình chọn quán ăn trưa hôm nay vào kênh #lunch trên Slack và nhắc mọi người chốt trước 11:15"`
6. **Tổng hợp hóa đơn điện tử cuối tuần gửi kế toán:**
   `/schedule every Friday at 17:00 "Tìm trong Gmail các email có file hóa đơn/VAT gửi về trong tuần, tải PDF về thư mục 'Hoa_don_tuan' trên máy và thống kê tổng tiền ra file Excel"`
7. **Cảnh báo công nợ / gửi email nhắc thanh toán cuối tháng:**
   `/schedule on the 28th of every month at 09:30 "Kiểm tra danh sách công nợ khách hàng, tạo danh sách các đơn vị quá hạn và soạn sẵn email lịch sự nhắc thanh toán"`
8. **Tự động quét dọn và sắp xếp thư mục `Downloads`:**
   `/schedule every Sunday at 21:00 "Quét thư mục Downloads trên máy tính, gom các file đã tải quá 7 ngày vào các thư mục phân loại: Ảnh, Tài liệu PDF, Bộ cài đặt, File nén"`

### Nhóm B: Học Tập, Ôn Thi & Nghiên Cứu (8 ví dụ)
9. **Trợ lý Pomodoro ngắt quãng (Active Recall):**
   `/schedule in 25 minutes "Nhắc tôi đứng dậy uống nước, hỏi tôi vừa học được khái niệm cốt lõi nào và ghi câu trả lời vào sổ tay 'learn_log.md'"`
10. **Luyện từ vựng theo phương pháp Lặp lại ngắt quãng (Spaced Repetition):**
    `/schedule every day at 12:00, 18:00, 21:00 "Lấy ngẫu nhiên 3 từ vựng trong file 'tu_vung_ielts.txt', đặt câu đố trắc nghiệm ngữ cảnh để tôi trả lời"`
11. **Canh điểm thi / Thông báo mới trên cổng thông tin trường học:**
    `/schedule every 2 hours "Truy cập trang cổng đào tạo sinh viên, kiểm tra xem đã có điểm thi môn Kinh tế vi mô chưa, nếu có thông báo ngay"`
12. **Cảnh báo Deadline bài tập trong vòng 48 giờ:**
    `/schedule every morning at 07:30 "Đọc danh sách bài tập trên Trello/Calendar, cảnh báo những bài tập có deadline trong vòng 48h tới kèm độ ưu tiên"`
13. **Theo dõi bài báo khoa học mới trên arXiv / Google Scholar:**
    `/schedule every Monday at 08:00 "Tìm kiếm các nghiên cứu mới xuất bản về chủ đề 'Agentic AI Workflows', tóm tắt abstract 3 bài nổi bật nhất vào file Research.md"`
14. **Hẹn giờ ôn tập bài cũ theo đường cong quên lãng Ebbinghaus:**
    `/schedule in 3 days "Nhắc tôi ôn lại sơ đồ tư duy môn Giải tích đã học hôm nay, tạo sẵn 5 câu hỏi trắc nghiệm kiểm tra nhanh"`
15. **Tự động đóng phiên học và sao lưu tài liệu (Auto Git Backup):**
    `/schedule at 23:00 "Nhắc tôi dừng học đi ngủ, tự động lưu toàn bộ các ghi chú trong ngày và tạo commit đẩy lên GitHub"`
    *(Cron: `0 23 * * *`)*
16. **Tóm tắt các bản tin công nghệ / tài chính học thuật cuối tuần:**
    `/schedule every Sunday at 09:00 "Đọc 3 trang blog công nghệ xem tuần qua có bài viết nổi bật nào, tổng hợp các điểm tin chính thành 1 trang A4"`

### Nhóm C: Marketing, Bán Hàng & Chăm Sóc Khách Hàng (7 ví dụ)
17. **Theo dõi biến động giá của đối thủ cạnh tranh:**
    `/schedule every 4 hours "Vào link sản phẩm của đối thủ X trên sàn thương mại điện tử, ghi nhận giá và số lượng tồn kho vào Google Sheet, cảnh báo nếu giá giảm hơn 10%"`
18. **Theo dõi phản hồi & thương hiệu trên mạng xã hội (Social Listening):**
    `/schedule every weekday at 15:00 "Tìm kiếm các bài đăng hoặc thảo luận mới nhất có từ khóa [Tên sản phẩm] trong ngày, phân tích cảm xúc khách hàng (khen/chê)"`
19. **Tự động nhắc nhở Follow-up khách hàng tiềm năng:**
    `/schedule in 2 days "Kiểm tra xem khách hàng [Nguyen Van A] đã trả lời email báo giá chưa. Nếu chưa có phản hồi, gợi ý cho tôi 1 mẫu email follow-up khéo léo"`
20. **Gợi ý & soạn trước bài đăng định kỳ cho Fanpage / LinkedIn:**
    `/schedule every Tuesday and Thursday at 09:00 "Lấy 1 ý tưởng trong bảng kế hoạch content, viết bản nháp bài chia sẻ chuyên môn cho LinkedIn và lưu vào thư mục drafts/"`
21. **Thống kê số lượng Lead / Form đăng ký cuối ngày:**
    `/schedule every day at 21:00 "Kiểm tra Google Form đăng ký khóa học hôm nay, đếm số lượng người mới đăng ký và báo cáo số liệu tổng kết qua tin nhắn"`
22. **Nhắc chúc mừng sinh nhật khách hàng VIP:**
    `/schedule every morning at 08:00 "Tra cứu danh sách khách hàng xem hôm nay có sinh nhật của ai không, soạn sẵn tin nhắn chúc mừng cá nhân hóa"`
23. **Kiểm tra thứ hạng từ khóa SEO định kỳ:**
    `/schedule every Monday at 07:00 "Tìm kiếm vị trí thứ hạng của 5 từ khóa SEO chiến lược trên Google, so sánh với thứ hạng tuần trước"`

### Nhóm D: Năng Suất Cá Nhân, Freelancer & Quản Lý Dự Án (7 ví dụ)
24. **Rà soát Task bị tắc nghẽn (Blocker) trước giờ Daily Standup:**
    `/schedule every weekday at 09:15 "Đọc bảng Trello/Jira của dự án, liệt kê các task đang ở cột 'In Progress' quá 3 ngày hoặc chưa có người phụ trách để chuẩn bị họp lúc 09:30"`
25. **Chờ tiến trình nền dài (Render video, xuất file lớn, train model, CI build):**
    `/schedule in 20 minutes "Kiểm tra xem tiến trình export video / build code đã hoàn thành chưa, nếu xong thì báo cho tôi biết kết quả và dung lượng file"`
26. **Phản tư cuối ngày (Daily Evening Review):**
    `/schedule every day at 17:30 "Gửi cho tôi 3 câu hỏi đánh giá ngày: 1. Việc quan trọng nhất đã làm xong? 2. Điều gì làm mất thời gian? 3. Ba ưu tiên cho ngày mai? Lưu lại vào nhật ký"`
27. **Nhắc vận động, bảo vệ mắt và cột sống (Ergonomics Reminder):**
    `/schedule every 60 minutes "Nhắc tôi đứng lên uống một cốc nước, nhìn ra xa 20 giây và làm 2 động tác xoay cổ vai gáy"`
28. **Giám sát trạng thái hoạt động của Website cá nhân / Portfolio:**
    `/schedule every 30 minutes "Gửi request kiểm tra trang web cá nhân xem có phản hồi HTTP 200 không, nếu có lỗi 500 hoặc timeout thì lập tức cảnh báo"`
29. **Cảnh báo kỳ gia hạn các gói dịch vụ thuê bao (Subscriptions):**
    `/schedule on the 1st of every month at 09:00 "Kiểm tra danh sách các gói dịch vụ định kỳ (Hosting, Domain, Spotify, Netflix, ChatGPT...) xem tháng này dịch vụ nào đến hạn trừ tiền"`
30. **Tổng kết tuần KPT (Keep - Problem - Try) và lên lịch tuần mới:**
    `/schedule every Sunday at 20:00 "Đọc lại lịch trình tuần qua trên Calendar, tự động tạo khung báo cáo KPT và gợi ý danh sách mục tiêu cho tuần tới"`

---

## 4. Kịch Bản Chi Tiết Livestream (Timeline 60 Phút)

### Giai đoạn 1: Mở đầu & Khơi gợi nỗi đau (00:00 – 12:00)
- **00:00 – 04:00 | Intro & Bẻ gãy tư duy cũ:**
  - Nêu sự khác biệt giữa "Nhắc nhở tĩnh" (Alarm kêu bíp bíp) và "Trợ lý hành động" (AI thức dậy làm việc).
  - Tuyên bố giá trị: Sau 60 phút này, bạn sẽ sở hữu một trợ lý cá nhân biết tự động làm việc kể cả khi bạn đang bận họp.
- **04:00 – 07:00 | Giới thiệu cơ chế Non-blocking:**
  - Giải thích tại sao lệnh `sleep` truyền thống là tệ hại (treo máy) và `/schedule` giải phóng luồng chat ra sao.
  - Giới thiệu 2 chế độ: One-shot timer & Recurring cron.
- **07:00 – 12:00 | Hero Demo 1 (Hiệu ứng Wow sau 2 phút):**
  - Gõ: `/schedule in 2 minutes "Quét thư mục dự án và kiểm tra xem có tài liệu nào mới cập nhật không"`.
  - Trong lúc chờ, quay sang chat về 1 chủ đề khác.
  - Đúng 2 phút sau: Agent tự động chen ngang hiển thị thông báo kết quả kiểm tra.

### Giai đoạn 2: Trình diễn thực chiến (12:00 – 35:00)
- **12:00 – 22:00 | Hero Demo 2 (Ứng dụng Văn phòng & Quản lý):**
  - Đọc file `danh_sach_hop_dong.xlsx`.
  - Thiết lập cron kiểm tra hạn hợp đồng / công nợ định kỳ.
  - Demo rút ngắn thời gian kích hoạt (sau 30 giây) để khán giả thấy AI đọc file, xử lý logic ngày tháng và xuất bảng markdown cùng email soạn sẵn.
- **22:00 – 35:00 | Hero Demo 3 (Ứng dụng Học tập & Trắc nghiệm phản xạ):**
  - Đọc file `tu_vung_ielts.txt`.
  - Thiết lập lịch đố vui định kỳ theo chu kỳ ngắt quãng.
  - Tương tác với khán giả trên khung chat live: Mời khán giả chọn đáp án A, B, C, D cho câu hỏi AI vừa tạo ra.

### Giai đoạn 3: Quản trị tác vụ & Xử lý tình huống (35:00 – 50:00)
- **35:00 – 43:00 | Bảng điều khiển `/tasks`:**
  - Hướng dẫn mở giao diện Task Manager.
  - Kiểm tra các tác vụ đang `Active`, `Pending`, `Completed`.
  - Hướng dẫn hủy tác vụ bằng phím `k` (Kill) hoặc câu lệnh giao tiếp.
- **43:00 – 50:00 | Bí quyết Prompt & Phân biệt với `/automation`:**
  - Viết câu lệnh bằng ngôn ngữ tự nhiên thay vì cố nhớ cú pháp Cron.
  - Giải đáp câu hỏi: "Tắt máy thì có chạy không?" $\rightarrow$ Phân định giữa `/schedule` (phiên làm việc) và `/automation` / Sidecars (chạy độc lập trên máy chủ nền).

### Giai đoạn 4: Tổng kết & Quà tặng (50:00 – 60:00)
- Tóm tắt công thức 3 bước áp dụng.
- Chia sẻ đường link tải file Cheat Sheet 30 Prompt mẫu.
- Giải đáp thắc mắc (Q&A) và kết thúc buổi live.

---

## 5. Dữ Liệu Mẫu (Mock Data) Cho Buổi Live

### 5.1. File `danh_sach_hop_dong.xlsx` (Demo 2)
Cấu trúc các cột:
- `Mã NV`: NV001, NV002, NV003, NV004, NV005
- `Họ và Tên`: Nguyễn Văn An, Trần Thị Bích, Lê Hoàng Nam, Phạm Thu Thảo, Vũ Minh Quân
- `Phòng Ban`: Marketing, Kỹ thuật, Kinh doanh, Nhân sự, Thiết kế
- `Loại Hợp Đồng`: Thử việc 2 tháng, Thử việc 2 tháng, Chính thức 1 năm, Thử việc 2 tháng, Chính thức 1 năm
- `Ngày Hết Hạn`: *(Ghi chú: Đặt 2 nhân viên có ngày hết hạn cách ngày livestream 3 đến 5 ngày để AI lọc ra chính xác)*

### 5.2. File `tu_vung_ielts.txt` (Demo 3)
Cấu trúc mẫu:
```text
1. Ubiquitous /juːˈbɪk.wə.təs/ (adj): Có mặt ở khắp mọi nơi (present, appearing, or found everywhere).
2. Procrastinate /prəʊˈkræs.tɪ.neɪt/ (verb): Trì hoãn công việc (delay or postpone action).
3. Resilience /rɪˈzɪl.jəns/ (noun): Khả năng phục hồi, kiên cường (the capacity to recover quickly from difficulties).
4. Streamline /ˈstriːm.laɪn/ (verb): Tinh gọn hóa quy trình (make an organization or system more efficient).
5. Paradigm /ˈpær.ə.daɪm/ (noun): Mô hình, hình mẫu mẫu mực (a typical example or pattern of something).
```

---

## 6. Kế Hoạch Dự Phòng Kỹ Thuật (Failsafe)

| Rủi ro | Giải pháp dự phòng |
|---|---|
| **Mạng chập chờn / Agent phản hồi lâu** | Chuẩn bị sẵn 1 file text chứa sẵn output mẫu để copy-paste trình diễn ngay lập tức, không để thời gian chết trên live |
| **Lỗi đường dẫn file khi đọc Excel** | Đặt toàn bộ file mock data ngay tại thư mục gốc workspace để câu lệnh chỉ cần ghi tên file |
| **Khán giả hỏi cú pháp cron phức tạp** | Khẳng định thế mạnh của Antigravity là khả năng chuyển hóa ngôn ngữ tự nhiên thành cron biểu thức chuẩn |
