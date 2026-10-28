# 📘 TÀI LIỆU NỘI DUNG CHI TIẾT & KỊCH BẢN GIẢNG DẠY
## PHẦN 04: KHO VŨ KHÍ KỸ THUẬT – 7 TRỤ CỘT GOOGLE ANTIGRAVITY
### *Dành riêng cho người học không chuyên về kỹ thuật (Non-Coders, Dân Văn Phòng, Quản Lý)*

---

> **MỤC TIÊU CỐT LÕI CỦA PHẦN 4:**  
> Giúp học viên hiểu cặn kẽ bản chất của 7 "món vũ khí" cốt lõi trong Google Antigravity bằng các hình tượng thực tế gần gũi nhất, nắm vững **cấu trúc thư mục**, **đường dẫn lưu trữ** (Global vs Workspace) theo chuẩn tài liệu chính thức (`https://antigravity.google/docs/`), và **quy tắc đặt tên chuẩn xác** để tự tay tổ chức, quản lý và nhân bản các trợ lý AI mà không bao giờ gặp lỗi kỹ thuật.

---

## 🗺️ TỔNG QUAN KHUNG 23 SLIDE BÀI GIẢNG

```
TRỤ CỘT 01: SUBAGENTS ENGINE (Đội Ngũ Nhân Sự Song Song)
  ├─ Slide 01: Khái Niệm Subagent
  ├─ Slide 02: 3 Chế Độ Workspace Của Subagent
  └─ Slide 03: Cấu Trúc File Subagent

TRỤ CỘT 02: RULES ENGINE (Sổ Tay Nội Quy & Định Hình Chuẩn Mực)
  ├─ Slide 04: Khái Niệm Rules
  ├─ Slide 05: Sổ Tay Quy Tắc AGENTS.md
  ├─ Slide 06: Cấu Trúc Thư Mục Rules & 4 Trigger
  └─ Slide 07: Giới Hạn 24KB & Mini-Project 1

TRỤ CỘT 03: AGENT SKILLS (Bằng Nghề & Cẩm Nang Nghiệp Vụ)
  ├─ Slide 08: Khái Niệm Agent Skill
  ├─ Slide 09: 3 Thành Phần Của Một Skill
  ├─ Slide 10: Cấu Trúc Thư Mục & Tên File SKILL.md
  └─ Slide 11: Cơ Chế Tiết Kiệm Token (Progressive Disclosure)

TRỤ CỘT 04: LIFECYCLE HOOKS (Trạm Gác An Ninh Vòng Đời)
  ├─ Slide 12: Khái Niệm Lifecycle Hook
  ├─ Slide 13: 5 Trạm Gác Vòng Đời Của Hook
  └─ Slide 14: Cấu Hình hooks.json & Mini-Project 6

TRỤ CỘT 05: MODEL CONTEXT PROTOCOL - MCP (Cổng Cắm USB Mở Rộng Giác Quan)
  ├─ Slide 15: Khái Niệm Model Context Protocol (MCP)
  └─ Slide 16: Cấu Hình mcp_config.json & Mini-Project 4

TRỤ CỘT 06: PLUGINS ECOSYSTEM (Vali Đồ Nghề Đóng Gói All-in-One)
  ├─ Slide 17: Khái Niệm Plugin
  ├─ Slide 18: Cấu Trúc Thư Mục Plugin & plugin.json
  └─ Slide 19: Quản Lý & Bật/Tắt Plugin 1-Click

TRỤ CỘT 07: SIDECARS & TASK SCHEDULE (Cỗ Máy Vận Hành Ngầm 24/7)
  ├─ Slide 20: Khái Niệm Task Schedule
  ├─ Slide 21: Khái Niệm Sidecar Daemon
  └─ Slide 22: Cấu Trúc File sidecar.json & Tự Hồi Sinh

TỔNG KẾT & TRA CỨU NHANH
  └─ Slide 23: Bản Đồ Tra Cứu Toàn Năng (Cheatsheet)
```

---

# CHI TIẾT NỘI DUNG TỪNG SLIDE & KỊCH BẢN GIẢNG DẠY

---

## 📍 SLIDE 01: KHÁI NIỆM SUBAGENT
* **Thuộc trụ cột:** TRỤ CỘT 01: SUBAGENTS ENGINE
* **Huy hiệu đầu trang:** `TRỤ CỘT 01: SUBAGENTS ENGINE` | `ĐỘI NGŨ NHÂN SỰ SONG SONG`
* **Mục tiêu học viên cần đọng lại:** Hiểu vì sao không nên bắt một AI duy nhất ôm đồm tất cả công việc; nắm được bản chất Subagent là những nhân sự AI phụ chạy ngầm độc lập với bộ nhớ riêng biệt.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Khái Niệm **Subagent**
2. **Mô tả ngắn:** Ủy quyền tác vụ chuyên sâu cho các nhân sự AI phụ hoạt động độc lập, không làm tắc nghẽn bộ nhớ của AI chính.
3. **Bảng so sánh Đối kháng (Vs Matrix):**
   * **Bên trái (Vấn đề - 1 AI ôm đồm):** Bắt 1 con AI vừa cào web, vừa phân tích bảng tính Excel, vừa viết báo cáo. Hậu quả: Bàn làm việc bộ nhớ ngắn hạn bị quá tải giấy tờ, câu trả lời bắt đầu nhầm lẫn số liệu, rớt ý quan trọng.
   * **Bên phải (Giải pháp - Đội ngũ Subagents):** AI chính làm Giám đốc điều hành. Khi có tác vụ nặng, Giám đốc triệu hồi Subagent nghiên cứu và Subagent tính toán chạy song song trong phòng làm việc riêng biệt. Bàn làm việc của Giám đốc luôn sạch sẽ.
4. **Chân trang:** `HIỆU NĂNG VƯỢT TRỘI:` Cho 3-5 Subagents cùng làm việc song song giúp giải quyết khối lượng công việc gấp 3 đến 5 lần.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Một lỗi kinh điển của người mới dùng AI là bắt một con AI duy nhất phải ôm đồm tất cả mọi thứ: vừa tìm tài liệu, vừa cào web, vừa tính toán số liệu, vừa viết báo cáo. Hậu quả là bàn làm việc bộ nhớ ngắn hạn của AI bị quá tải giấy tờ, và nó bắt đầu lẫn lộn giữa các nhiệm vụ.*
>
> *Antigravity giải quyết bài toán này bằng hệ thống Subagents (Tác tử phụ). Bạn hãy hình dung AI chính đóng vai trò như một người Giám đốc điều hành. Khi gặp một khối lượng công việc lớn, Giám đốc sẽ triệu hồi các Trợ lý chuyên môn làm việc song song: một bạn chuyên đi tìm tài liệu trên mạng, một bạn chuyên ngồi tính toán số liệu Excel.*
>
> *Mỗi trợ lý phụ có phòng làm việc riêng biệt, không làm bẩn bàn làm việc của Giám đốc. Nhờ vậy, nhiều nhân sự AI có thể cùng làm việc một lúc, giúp hoàn thành dự án nhanh gấp 3 đến 5 lần mà AI không bao giờ bị lẫn lộn!"*

---

## 📍 SLIDE 02: 3 CHẾ ĐỘ WORKSPACE CỦA SUBAGENT
* **Thuộc trụ cột:** TRỤ CỘT 01: SUBAGENTS ENGINE
* **Huy hiệu đầu trang:** `TRỤ CỘT 01: SUBAGENTS ENGINE` | `KHÔNG GIAN LÀM VIỆC AN TOÀN`
* **Mục tiêu học viên cần đọng lại:** Hiểu cách bảo vệ dữ liệu gốc an toàn thông qua 3 chế độ không gian làm việc (`inherit`, `branch`, `share`), và biết cách lựa chọn chế độ an toàn cho công việc văn phòng.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** 3 Chế Độ **Workspace Của Subagent**
2. **Mô tả ngắn:** Bảo vệ dữ liệu gốc tuyệt đối: Lựa chọn linh hoạt giữa làm việc tại chỗ, tạo phòng thí nghiệm riêng hoặc chia sẻ kho tài nguyên.
3. **3 Thẻ Chế Độ Không Gian:**
   * **01. Làm việc tại chỗ (`inherit`):** Subagent dùng chung thư mục làm việc hiện tại với AI chính. Thích hợp nhất cho tác vụ đọc tài liệu tra cứu, phân tích nhanh, không chỉnh sửa trực tiếp vào file gốc.
   * **02. Phòng thí nghiệm riêng (`branch`):** Tự động tạo một không gian cô lập riêng biệt (Git worktree). Subagent tha hồ thử nghiệm, chỉnh sửa; chỉ khi bạn duyệt ưng ý thì mới lưu đè vào file gốc. Bảo vệ an toàn 100%!
   * **03. Dùng chung kho dữ liệu (`share`):** Dành cho các dự án dung lượng lớn; chia sẻ tài nguyên nền tảng nhưng kết quả xuất ra vẫn được giữ riêng biệt.
4. **Chân trang:** `KHUYÊN DÙNG CHO DÂN VĂN PHÒNG:` 99% công việc văn phòng hàng ngày chỉ cần chọn `inherit` (để tra cứu nhanh) hoặc `branch` (để thử nghiệm an toàn, không lo hỏng file gốc)!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Khi cho các trợ lý phụ làm việc, điều dân văn phòng lo lắng nhất là: 'Lỡ trợ lý phụ sửa nhầm làm hỏng file gốc của tôi thì sao?'. Đừng lo, Antigravity trang bị 3 chế độ bảo vệ không gian làm việc rất rõ ràng:*
>
> *1. Chế độ `inherit` (Làm việc tại chỗ / Dùng chung): Trợ lý ngồi chung bàn với bạn, dùng chung file hiện tại. Thích hợp nhất cho việc nhờ AI đọc tài liệu tra cứu, phân tích nhanh.*
>
> *2. Chế độ `branch` (Phòng thí nghiệm riêng / An toàn 100%): Giống như việc bạn copy một bản sao tài liệu ra phòng riêng cho thực tập sinh tha hồ sửa thử. Chỉ khi nào bạn duyệt ưng ý thì mới lưu đè vào file gốc. Không bao giờ sợ mất dữ liệu!*
>
> *3. Chế độ `share` (Dùng chung kho dữ liệu lớn): Dành cho các dự án dung lượng nặng, chia sẻ tài nguyên nền nhưng kết quả vẫn tách biệt.*
>
> *Lời khuyên cho bạn: Trong công việc văn phòng hàng ngày, 99% bạn chỉ cần chọn giữa `inherit` (để tra cứu nhanh) và `branch` (để thử nghiệm an toàn)!"*

---

## 📍 SLIDE 03: CẤU TRÚC FILE SUBAGENT
* **Thuộc trụ cột:** TRỤ CỘT 01: SUBAGENTS ENGINE
* **Huy hiệu đầu trang:** `TRỤ CỘT 01: SUBAGENTS ENGINE` | `THIẾT LẬP NHÂN SỰ`
* **Mục tiêu học viên cần đọng lại:** Nắm vững cấu trúc 1 file Subagent duy nhất (định dạng Markdown), phân biệt vị trí lưu trữ (Dự án vs Toàn máy), và quy tắc thụt lề bằng phím cách Space.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Cấu Trúc **File Subagent**
2. **Mô tả ngắn:** Tạo nhân viên AI mới chỉ bằng 1 file văn bản duy nhất: Phân định nơi lưu trữ toàn máy vs dự án và quy cách viết hồ sơ nhân sự chuẩn.
3. **Khối Đường Dẫn & Vị Trí:**
   * **Workspace (Chỉ dùng cho dự án này):** `.agents/agents/<ten-subagent>.md`
   * **Global (Dùng chung cho toàn bộ máy tính):** `~/.gemini/config/agents/<ten-subagent>.md`
4. **Khối Thẻ Thông Tin Đầu Trang (YAML Frontmatter + Prompt):**
   * Phần thẻ đầu trang (giữa hai hàng `---`):
     * `name`: Tên định danh (chữ thường, gạch nối, ví dụ: `tro-ly-van-thu`)
     * `description`: Mô tả năng lực và khi nào AI chính nên gọi trợ lý này
     * `role`: Chức danh công việc (ví dụ: `Senior Office Secretary`)
     * `workspace`: Chế độ làm việc (`inherit`, `branch`, hoặc `share`)
     * `model`: Bộ não AI (`inherit`, `flash`, hoặc `pro`)
   * Phần chỉ dẫn bên dưới: Ghi rõ nhiệm vụ chi tiết và tiêu chuẩn bàn giao bằng tiếng Việt tự nhiên.
5. **Chân trang:** `LƯU Ý VÀNG:` Tên file viết thường `kebab-case.md`. Mẹo sống còn: Trong thẻ thông tin đầu trang, chỉ thụt dòng bằng phím Dấu Cách (Space), không dùng phím Tab kẻo lỗi cú pháp!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Để tạo ra một nhân viên AI mới, bạn không cần phải biết lập trình một dòng nào cả! Bản chất của một Subagent chỉ là MỘT FILE VĂN BẢN DUY NHẤT có đuôi `.md`.*
>
> *Nơi cất file rất rõ ràng:*
> *- Dùng cho riêng dự án này: Cất vào `.agents/agents/<tên>.md` ngay trong thư mục dự án.*
> *- Dùng cho toàn bộ máy tính: Cất vào `~/.gemini/config/agents/<tên>.md`.*
>
> *Nội dung file gồm 2 phần trực quan:*
> *1. Thẻ Thông Tin Đầu Trang (Frontmatter nằm giữa hai hàng dấu ---): Ghi Tên nhân sự, Mô tả khi nào nên gọi, Vai trò và Chế độ workspace.*
> *2. Lời Dặn Dò Nhiệm Vụ: Viết bằng tiếng Việt tự nhiên ngay bên dưới.*
>
> *Một mẹo sống còn cho dân văn phòng: Trong thẻ thông tin đầu trang, khi thụt dòng chỉ bấm phím Dấu Cách (Space), tuyệt đối KHÔNG bấm phím Tab kẻo file bị lỗi cấu trúc!"*

---

## 📍 SLIDE 04: KHÁI NIỆM RULES
* **Thuộc trụ cột:** TRỤ CỘT 02: RULES ENGINE
* **Huy hiệu đầu trang:** `TRỤ CỘT 02: RULES ENGINE` | `TIÊU CHUẨN BẮT BUỘC`
* **Mục tiêu học viên cần đọng lại:** Hiểu rõ bản chất Rules là quy tắc kỷ luật và tiêu chuẩn bắt buộc; phân biệt rạch ròi giữa Rules và Skills mà không nhầm lẫn.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Khái Niệm **Rules**
2. **Mô tả ngắn:** Bộ quy tắc và tiêu chuẩn bắt buộc định hình phong cách, chuẩn mực đầu ra: Viết 1 lần, AI tuân thủ mãi mãi.
3. **Bảng Phân Biệt Sống Còn: Rules vs Skills:**
   * **Cột Rules (Nội quy kỷ luật & Tiêu chuẩn bắt buộc):**
     * Bản chất: Như Nội quy cơ quan & Tiêu chuẩn nghiệp vụ bắt buộc.
     * Trả lời câu hỏi: *"Tôi ĐƯỢC PHÉP và KHÔNG ĐƯỢC PHÉP làm gì? Chuẩn mực đầu ra thế nào?"*
     * Ví dụ văn phòng: Luôn xưng hô lịch sự; không tự ý xóa dữ liệu khách hàng; bảng tính tiền tệ phải định dạng VND.
     * Cơ chế: Tự động nạp vào bộ nhớ trước khi AI bắt đầu làm việc.
   * **Cột Skills (Bằng nghề & Cẩm nang nghiệp vụ từng bước):**
     * Bản chất: Như Sách dạy nghề / Cẩm nang thao tác chuẩn SOP.
     * Trả lời câu hỏi: *"Tôi phải làm theo các BƯỚC THAO TÁC CỤ THỂ nào để ra kết quả?"*
     * Ví dụ văn phòng: Quy trình 5 bước xuất hóa đơn điện tử; quy trình lọc báo cáo tồn kho.
     * Cơ chế: Chỉ nạp khi gặp đúng nghiệp vụ cần dùng đến (tiết kiệm bộ nhớ).
4. **Chân trang:** `NGUYÊN TẮC VÀNG:` Rules là quy tắc kỷ luật & tiêu chuẩn bắt buộc; Skills là cẩm nang thao tác từng bước.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Các bạn có thấy mệt mỏi khi lần nào mở ChatGPT hay Claude lên cũng phải gõ lại một câu dặn dò quen thuộc: 'Nhớ trả lời bằng tiếng Việt lịch sự, đừng dài dòng, số liệu tiền tệ phải định dạng VND'?*
>
> *Hôm nay gõ, ngày mai quên, ngày kia AI lại trả lời lan man. Rules trong Antigravity sinh ra để giải phóng bạn: Bạn viết quy tắc ra MỘT LẦN DUY NHẤT, và AI sẽ tuân thủ mãi mãi!*
>
> *Để dễ nhớ, các bạn hãy phân biệt rạch ròi:*
> *- Rules là Sổ tay quy tắc kỷ luật & Tiêu chuẩn bắt buộc. Nó trả lời: 'Tôi ĐƯỢC PHÉP và KHÔNG ĐƯỢC PHÉP làm gì? Chuẩn mực đầu ra thế nào?'.*
> *- Còn Skills là Bằng nghề & Cẩm nang nghiệp vụ. Nó trả lời: 'Tôi phải làm theo các BƯỚC THAO TÁC CỤ THỂ nào để ra kết quả?'.*
>
> *Quy tắc kỷ luật vững chắc giúp AI luôn làm việc chuẩn mực, an toàn và nhất quán!"*

---

## 📍 SLIDE 05: SỔ TAY QUY TẮC AGENTS.MD
* **Thuộc trụ cột:** TRỤ CỘT 02: RULES ENGINE
* **Huy hiệu đầu trang:** `TRỤ CỘT 02: RULES ENGINE` | `NỘI QUY PHÂN TẦNG`
* **Mục tiêu học viên cần đọng lại:** Hiểu cách hoạt động của cuốn sổ tay quy tắc `AGENTS.md` và cơ chế phân tầng thông minh giữa quy chuẩn toàn máy và quy chuẩn dự án.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Sổ Tay Quy Tắc **AGENTS.md**
2. **Mô tả ngắn:** Phân tầng quy tắc thông minh: Phân định rạch ròi giữa quy chuẩn phong cách & chuẩn mực chung toàn máy tính và nội quy nghiệp vụ riêng của từng dự án.
3. **Sơ đồ Cấu Trúc 2 Cấp Phân Tầng:**
   * **Cấp 1 - Quy tắc Toàn máy (Global Rules):**
     * Vị trí: `~/.gemini/config/AGENTS.md` (hoặc thư mục `~/.gemini/config/rules/`)
     * Ý nghĩa: Quy chuẩn phong cách áp dụng cho mọi dự án. Ví dụ: *"Luôn chào hỏi lịch sự, văn phong chuẩn mực công sở, luôn xuất kết quả bằng tiếng Việt."*
   * **Cấp 2 - Quy tắc Dự án (Workspace Rules):**
     * Vị trí: File `AGENTS.md` đặt ngay tại thư mục gốc của dự án bạn đang mở.
     * Ý nghĩa: Nội quy nghiệp vụ đặc thù của dự án đó. Ví dụ: *"Mọi hóa đơn công tác phải tuân thủ Nghị định 30, tệp ảnh lưu vào thư mục storage/."*
4. **Chân trang:** `TÊN FILE BẮT BUỘC:` File `AGENTS.md` bắt buộc phải viết HOA toàn bộ. Quy tắc tại dự án luôn được ưu tiên áp dụng song hành cùng quy tắc toàn máy.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Nội quy trong Antigravity được chia làm 2 cấp phân tầng rất thông minh:*
>
> *1. **Global Rules (Quy tắc toàn máy):** Nằm ở thư mục gốc của máy tính bạn (`~/.gemini/config/AGENTS.md`). Đây là những chuẩn mực chung nhất, ví dụ: 'Tôi là người Việt Nam, AI luôn phản hồi bằng tiếng Việt trang trọng, tôn trọng bản quyền'. Bất kể bạn mở dự án nào trên máy tính, AI đều tự động tuân thủ.*
>
> *2. **Workspace Rules (Quy tắc dự án):** Là file `AGENTS.md` đặt ngay tại thư mục công việc bạn đang làm. Ví dụ dự án Kế toán thì dặn: 'Chỉ xuất file Excel định dạng tiền tệ VND'; dự án Marketing thì dặn: 'Văn phong trẻ trung, dùng icon bắt mắt'.*
>
> *Tên file bắt buộc phải viết HOA: `AGENTS.md`. Nhờ cơ chế 2 cấp này, bạn không bao giờ phải mất công copy paste lại các yêu cầu cơ bản mỗi khi bắt đầu một công việc mới!"*

---

## 📍 SLIDE 06: CẤU TRÚC THƯ MỤC RULES & 4 TRIGGER
* **Thuộc trụ cột:** TRỤ CỘT 02: RULES ENGINE
* **Huy hiệu đầu trang:** `TRỤ CỘT 02: RULES ENGINE` | `QUY CHUẨN KỸ THUẬT RULES`
* **Mục tiêu học viên cần đọng lại:** Nắm vững cấu trúc thư mục rules, 4 kiểu kích hoạt thông minh (hiểu rõ `glob` là quy tắc theo đuôi file), và tránh bẫy thư mục con.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Cấu Trúc Thư Mục **Rules & 4 Trigger**
2. **Mô tả ngắn:** Tổ chức thư mục quy tắc chuẩn xác và làm chủ 4 cơ chế kích hoạt thông minh để AI không bị quá tải bộ nhớ.
3. **Khối Thư Mục & Bẫy Kỹ Thuật Cần Tránh:**
   * **Vị trí chuẩn:** `.agents/rules/*.md` (Workspace) hoặc `~/.gemini/config/rules/*.md` (Global).
   * **Bẫy thư mục con (Cực kỳ quan trọng):** Antigravity chỉ quét các file `.md` nằm trực tiếp trong thư mục `rules/`. Nếu bạn tạo thư mục con (ví dụ: `rules/ke-toan/hoa-don.md`), AI sẽ **BỎ QUA HOÀN TOÀN** trừ khi bạn đăng ký thủ công qua file `rules.json`! Hãy để toàn bộ file quy tắc phẳng ngay trong `rules/`.
4. **Khối 4 Cơ Chế Kích Hoạt (Triggers):**
   * **`always_on`:** Luôn bật trong mọi cuộc hội thoại (dành cho quy tắc an toàn cốt lõi).
   * **`model_decision`:** AI tự động đọc khi thấy ngữ cảnh câu hỏi liên quan đến chủ đề đó.
   * **`glob` (Quy tắc theo đuôi file):** Chỉ tự động bật khi bạn mở hoặc thao tác trên đúng loại tệp tin (ví dụ: `*.xlsx` cho bảng tính Excel, `*.docx` cho văn bản Word).
   * **`manual`:** Chỉ nạp khi bạn chủ động gắn thẻ nhắc tên quy tắc trong ô chat.
5. **Chân trang:** `KHUYÊN DÙNG:` Đặt quy tắc phẳng trực tiếp trong thư mục `rules/` và dùng trigger `model_decision` để tối ưu chi phí bộ nhớ.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Khi viết quy tắc, có một CÁI BẪY mà tài liệu của Google Antigravity đặc biệt cảnh báo: Antigravity chỉ quét các file nằm TRỰC TIẾP trong thư mục `rules/`. Nếu bạn tạo thư mục con (ví dụ: `rules/ke-toan/hoa-don.md`), AI sẽ BỎ QUA HOÀN TOÀN! Do vậy, hãy để toàn bộ file `.md` nằm phẳng trực tiếp trong thư mục `rules/`.*
>
> *Bên cạnh đó, bạn làm chủ 4 cơ chế kích hoạt thông minh:*
> *- `always_on`: Luôn luôn bật trong mọi cuộc hội thoại.*
> *- `model_decision`: AI tự giác mở ra khi thấy câu hỏi của bạn nhắc tới chủ đề đó.*
> *- `glob` (Quy tắc theo đuôi tệp tin): Đây là tính năng rất hay! Ví dụ bạn đặt glob là `*.xlsx` thì chỉ khi nào bạn mở bảng tính Excel, quy tắc định dạng số liệu mới bật lên; bình thường nó ngủ yên để tiết kiệm bộ nhớ.*
> *- `manual`: Chỉ mở khi nào bạn chủ động nhắc tên quy tắc.*
>
> *Nhờ 4 cơ chế này, bộ nhớ của AI luôn gọn gàng và không bao giờ bị nghẽn!"*

---

## 📍 SLIDE 07: GIỚI HẠN 24KB & MINI-PROJECT 1
* **Thuộc trụ cột:** MINI-PROJECT 01: QUY TẮC NGHỊ ĐỊNH 30
* **Huy hiệu đầu trang:** `MINI-PROJECT 01: QUY TẮC NGHỊ ĐỊNH 30` | `QUY TẮC CÔNG NGHỆ CỐT LÕI`
* **Mục tiêu học viên cần đọng lại:** Hiểu rõ trần dung lượng 24KB cho từng file đơn lẻ và ngân sách 20.000 tokens; thực hành tạo Bộ Quy Tắc thẩm định thể thức văn bản hành chính theo Nghị định 30/2020/NĐ-CP.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Giới Hạn 24KB & **Mini-Project 1**
2. **Mô tả ngắn:** Nắm vững trần dung lượng 24KB/file và thực hành thiết lập Bộ Quy Tắc thẩm định thể thức văn bản hành chính chuẩn Nghị định 30.
3. **Cảnh báo Kỹ thuật Chuẩn Xác:**
   * **Giới hạn từng file:** Tối đa **24 KB** (~24.000 ký tự / khoảng 4.000 - 6.000 từ) cho mỗi file rule riêng lẻ. Nếu vượt quá, hệ thống sẽ tự động cắt dòng (truncate).
   * **Ngân sách tổng:** Tối đa **20.000 tokens** cho toàn bộ các quy tắc nạp cùng lúc.
   * *Bí quyết văn phòng:* Viết quy tắc cô đọng, gạch đầu dòng rõ ràng, chia nhỏ theo từng nghiệp vụ thay vì nhét tất cả vào 1 file!
4. **Khối Thực Hành Mini-Project 1 (Bộ Quy Tắc Nghị Định 30):**
   * Tệp tin: `.agents/rules/the-thuc-cong-van.md`
   * Trigger: `model_decision` | Mô tả: Kiểm tra thể thức văn bản hành chính
   * Nội dung quy tắc mẫu:
     * Quốc hiệu: Chữ in hoa đứng đậm, cỡ chữ 12-13.
     * Tiêu ngữ: Chữ in hoa và chữ thường đứng đậm, cỡ 13-14.
     * Địa danh và ngày tháng: Chữ in nghiêng, cỡ 13-14.
     * Thẩm định lỗi: Tự động chỉ ra các điểm sai lệch so với Nghị định 30/2020/NĐ-CP.
5. **Chân trang:** `KẾT QUẢ THỰC TẾ:` Mọi văn bản bạn soạn thảo qua Antigravity đều được tự động rà soát thể thức chuẩn chỉnh 100% trước khi in ấn trình sếp!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Nhiều bạn hỏi tôi: 'Tôi viết một cuốn quy tắc dài 100 trang như sách giáo khoa nhét vào cho AI đọc có được không?'. Câu trả lời là: TUYỆT ĐỐI KHÔNG!*
>
> *Tài liệu Antigravity quy định trần kỹ thuật rất rõ:*
> *- Giới hạn từng file đơn lẻ là 24KB (khoảng 4.000 đến 6.000 từ). Nếu một file dài hơn mức này, hệ thống sẽ tự động cắt ngắn bớt.*
> *- Tổng ngân sách nạp cùng lúc cho các quy tắc là 20.000 tokens.*
> *Vì vậy, bí quyết vàng cho dân văn phòng là: Viết quy tắc ngắn gọn, đanh thép, chia nhỏ thành từng file theo từng chủ đề.*
>
> *Để thực hành, chúng ta cùng làm Mini-Project 1: Thiết lập Bộ Quy Tắc Thẩm Định Thể Thức Công Văn chuẩn Nghị định 30/2020/NĐ-CP tại `.agents/rules/the-thuc-cong-van.md`.*
>
> *Từ nay về sau, cứ khi nào bạn nhờ AI soạn văn bản hành chính, AI sẽ tự động căn chỉnh đúng chuẩn: Quốc hiệu cỡ chữ mấy, tiêu ngữ in hoa thế nào, số ký hiệu đặt ở đâu. Văn bản trình ký lúc nào cũng chuẩn chỉ 100%!"*

---

## 📍 SLIDE 08: KHÁI NIỆM AGENT SKILL
* **Thuộc trụ cột:** TRỤ CỘT 03: AGENT SKILLS
* **Huy hiệu đầu trang:** `TRỤ CỘT 03: AGENT SKILLS` | `DẠY NGHỀ CHUYÊN MÔN`
* **Mục tiêu học viên cần đọng lại:** Nắm vững khái niệm Skill là cẩm nang dạy nghề chuyên môn theo từng bước chuẩn hóa SOP; hiểu sự khác biệt cốt lõi giữa Rules và Skills.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Khái Niệm **Agent Skill**
2. **Mô tả ngắn:** Gói cẩm nang dạy cho AI cách làm một nghiệp vụ chuyên sâu theo từng bước chuẩn hóa SOP, biến AI thành chuyên viên thạo việc.
3. **So sánh Hình tượng Đời thực:**
   * **Rules (Kỷ luật & Tiêu chuẩn):** Cho AI biết ranh giới không được vượt qua (Ví dụ: *"Phải trung thực, không được làm rò rỉ giá vốn"*).
   * **Skill (Bằng nghề & Hướng dẫn SOP):** Cầm tay chỉ việc cho AI từng thao tác cụ thể (Ví dụ: *"Bước 1: Tải hóa đơn; Bước 2: Quét mã số thuế; Bước 3: Đối chiếu ngân hàng; Bước 4: Xuất báo cáo"*).
4. **3 Năng lực cốt lõi khi trang bị Skill:**
   * **Chuyên môn hóa sâu:** Biến AI phổ thông thành chuyên gia xử lý báo cáo thuế, chuyên viên SEO, hay trợ lý thẩm định hợp đồng.
   * **Tính lặp lại hoàn hảo:** Dù làm 100 lần, AI vẫn tuân thủ chính xác từng bước như một cỗ máy, không bao giờ bỏ sót công đoạn.
   * **Tự kích hoạt thông minh:** Bạn không cần nhớ tên lệnh, chỉ cần yêu cầu công việc là AI tự nhận diện và lôi Skill tương ứng ra làm.
5. **Chân trang:** `ĐỊNH NGHĨA:` Skill là quy trình thao tác chuẩn (SOP) được số hóa để AI tự động thực thi trọn vẹn từ đầu đến cuối.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Nếu như Rules là 'Quy tắc kỷ luật & Tiêu chuẩn bắt buộc', thì Skills chính là 'Bằng Nghề Chuyên Môn'.*
>
> *Một nhân viên mới có thể rất ngoan ngoãn, tuân thủ nghiêm ngặt mọi nội quy cơ quan (đó là Rules). Nhưng nếu bạn không dạy nghề, không đưa cho bạn ấy cẩm nang hướng dẫn công việc từng bước (SOP), thì bạn ấy vẫn không thể tự làm báo cáo quyết toán thuế được!*
>
> *Skills trong Antigravity chính là cẩm nang nghề nghiệp đóng gói sẵn. Khi bạn giao việc: 'Hãy làm báo cáo doanh thu tuần', AI sẽ tự động mở Skill 'Báo cáo doanh thu' ra, làm đúng theo quy trình 4 bước đã được bạn huấn luyện.*
>
> *Nhờ có Skills, từ một AI trả lời chung chung, bạn đã đào tạo nó trở thành một nhân viên nghiệp vụ lành nghề của riêng phòng ban mình!"*

---

## 📍 SLIDE 09: 3 THÀNH PHẦN CỦA MỘT SKILL
* **Thuộc trụ cột:** TRỤ CỘT 03: AGENT SKILLS
* **Huy hiệu đầu trang:** `TRỤ CỘT 03: AGENT SKILLS` | `CẤU TẠO BỘ ĐỒ NGHỀ`
* **Mục tiêu học viên cần đọng lại:** Hiểu cấu tạo một gói Skill gồm 3 thành phần; nhận thức rõ `scripts/` là hộp đen tự động hóa (không cần biết code), người dùng chỉ cần tập trung vào `SKILL.md`.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** 3 Thành Phần **Của Một Skill**
2. **Mô tả ngắn:** Đóng gói kỹ năng thành các module chuyên biệt: Có hướng dẫn từng bước, công cụ thực thi tự động và mẫu tham khảo chuẩn.
3. **Chi Tiết 3 Món Đồ Nghề:**
   * **01. File `SKILL.md` (Trái tim - Bắt buộc):** Chứa bản hướng dẫn SOP từng bước bằng tiếng Việt tự nhiên, các kịch bản xử lý sự cố và thẻ mô tả đón khách.
   * **02. Thư mục `scripts/` (Hộp đen tự động hóa - Tùy chọn):** Chứa công cụ tính toán tự động. Dân văn phòng không cần biết code, chỉ cần nhờ AI viết hộ script rồi thả vào đây!
   * **03. Thư mục `references/` (Kho tài liệu tra cứu - Tùy chọn):** Chứa biểu mẫu Excel, quy chế công ty, tài liệu tra cứu chuyên sâu để AI mở ra đối chiếu khi cần.
4. **Chân trang:** `CẤU TRÚC TINH GỌN:` Trong thực tế văn phòng, bạn chỉ cần tạo duy nhất file `SKILL.md` là AI đã đủ thông minh để hoàn thành 90% công việc thường nhật!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Cấu tạo của một Skill trong Google Antigravity là một bộ đồ nghề đóng gói gồm 3 món:*
>
> *1. **File `SKILL.md` (Trái tim - Bắt buộc):** Chứa quy trình hướng dẫn từng bước SOP viết bằng tiếng Việt tự nhiên.*
> *2. **Thư mục `scripts/` (Hộp đen tự động hóa - Tùy chọn):** Chứa các công cụ tự động hóa hoặc công thức xử lý. Người dùng văn phòng KHÔNG CẦN biết lập trình, bạn chỉ cần copy script có sẵn hoặc nhờ chính AI viết hộ script rồi thả vào đây!*
> *3. **Thư mục `references/` (Kho tài liệu tra cứu - Tùy chọn):** Chứa bảng biểu Excel mẫu, quy chế công ty để AI mở ra đối chiếu khi cần.*
>
> *Tin vui cho dân văn phòng: Trong thực tế, bạn CHỈ CẦN viết duy nhất file `SKILL.md` bằng tiếng Việt là AI đã đủ thông minh để hoàn thành xuất sắc 90% công việc!"*

---

## 📍 SLIDE 10: CẤU TRÚC THƯ MỤC & TÊN FILE SKILL.MD
* **Thuộc trụ cột:** TRỤ CỘT 03: AGENT SKILLS
* **Huy hiệu đầu trang:** `TRỤ CỘT 03: AGENT SKILLS` | `CHUẨN MỰC TẠO SKILL`
* **Mục tiêu học viên cần đọng lại:** Nắm vững quy tắc vàng viết hoa `SKILL.md`, vị trí lưu trữ Workspace vs Global, và cách viết trường `description` ở ngôi thứ ba.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Cấu Trúc Thư Mục & **Tên File SKILL.md**
2. **Mô tả ngắn:** Đóng gói kỹ năng theo chuẩn Antigravity: Nắm vững quy tắc viết hoa sống còn và cách viết trường description để AI tự giác kích hoạt.
3. **Cây Thư Mục & Vị Trí Lưu Trữ:**
   * **Workspace (Chỉ dùng trong dự án hiện tại):** `.agents/skills/<ten-skill>/SKILL.md`
   * **Global (Dùng chung cho toàn máy tính):** `~/.gemini/config/skills/<ten-skill>/SKILL.md`
4. **Quy Tắc Vàng Đặt Tên (Bắt buộc tuân thủ):**
   * **Tên file bắt buộc viết HOA 100%:** `SKILL.md`. Nếu viết thường dạng `skill.md`, hệ thống sẽ **BỎ QUA HOÀN TOÀN** và xem như không tồn tại!
   * **Tên thư mục bọc ngoài:** Viết thường dạng `kebab-case` (ví dụ: `xuat-bao-cao-thue`, `phan-tich-hop-dong`).
5. **Thẻ Bảng Hiệu Đón Khách (YAML Description):**
   * Trường `description` ở đầu file là "bảng hiệu đón khách". Viết bằng **ngôi thứ ba**: *"Dùng kỹ năng này khi người dùng yêu cầu..."* để AI kích hoạt chuẩn xác nhất.
6. **Chân trang:** `LƯU Ý VÀNG:` Tên file `SKILL.md` bắt buộc viết hoa toàn bộ; thụt lề bằng phím cách Space, không dùng phím Tab!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Tại sao nhiều bạn sau khi tạo Skill xong, ra chat với AI bảo làm mà AI lại không chịu dùng Skill đó? 90% trường hợp rơi vào 2 lỗi sau:*
>
> *Lỗi thứ nhất: Tên file viết thường! Tài liệu Antigravity quy định: File cẩm nang bắt buộc PHẢI VIẾT HOA TOÀN BỘ là `SKILL.md`. Nếu viết `skill.md` chữ thường, AI xem như file không tồn tại!*
>
> *Lỗi thứ hai: Trường `description` trong Thẻ Căn Cước đầu trang viết sai ngôi. Trường này giống như bảng hiệu đón khách, bạn nên viết bằng NGÔI THỨ BA: 'Sử dụng kỹ năng này khi người dùng yêu cầu bóc tách hóa đơn VAT sang Excel...'. Đừng viết 'Tôi là skill...', AI đọc ngôi thứ ba sẽ kích hoạt cực kỳ nhạy bén!*
>
> *Và một mẹo nhỏ nữa: Trong phần thẻ đầu trang, luôn thụt lề bằng phím Dấu Cách (Space), không dùng phím Tab nhé!"*

---

## 📍 SLIDE 11: CƠ CHẾ TIẾT KIỆM TOKEN (PROGRESSIVE DISCLOSURE)
* **Thuộc trụ cột:** TỐI ƯU HÓA TÀI NGUYÊN: PROGRESSIVE DISCLOSURE
* **Huy hiệu đầu trang:** `TỐI ƯU HÓA TÀI NGUYÊN` | `BÍ QUYẾT TỐI ƯU HÓA TÀI NGUYÊN`
* **Mục tiêu học viên cần đọng lại:** Hiểu Token là đơn vị đếm từ của AI và nắm vững nguyên tắc "Đọc mục lục trước — Lật từng trang sau" giúp tiết kiệm 95% chi phí bộ nhớ.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Cơ Chế Tiết Kiệm Token **(Progressive Disclosure)**
2. **Mô tả ngắn:** "Nguyên tắc Đọc Mục Lục trước — Lật từng trang sau": Chỉ nạp thông tin khi thực sự cần, tiết kiệm đến 95% chi phí bộ nhớ token của AI.
3. **Sơ Đồ 3 Tầng Tải Dữ Liệu:**
   * **Tầng 1 (Đọc bảng hiệu/mục lục - Siêu nhẹ):** Lúc khởi động, AI chỉ đọc lướt Tên và Mô tả của các Skill (~100 tokens, chỉ như đọc mục lục bìa sách). Máy chạy siêu nhẹ! Dù bạn cài 50 Skills khác nhau, máy vẫn chạy mượt mà.
   * **Tầng 2 (Mở cẩm nang khi có việc - Vừa phải):** Khi bạn yêu cầu làm báo cáo thuế, AI mới rút cuốn `SKILL.md` về thuế ra đọc từng bước (~2.000 tokens).
   * **Tầng 3 (Rút đồ nghề trong hộp đen - Tiết kiệm tối đa):** Chỉ khi gặp bài toán tính toán phức tạp, AI mới nạp thêm các script trong thư mục `scripts/`.
4. **Chân trang:** `SO SÁNH HIỆU QUẢ:` Tiết kiệm 95% chi phí bộ nhớ so với việc nhét toàn bộ hướng dẫn vào System Prompt ngay từ đầu.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Nếu bạn cài đặt hàng chục Skill khác nhau trong máy tính, liệu bộ nhớ của AI có bị nghẽn không?*
>
> *Câu trả lời là hoàn toàn KHÔNG! Antigravity áp dụng một cơ chế cực kỳ thông minh gọi là Progressive Disclosure — hay dân dã gọi là: 'Nguyên Tắc Đọc Mục Lục Trước — Lật Từng Trang Sau':*
>
> *1. Token là gì? Token đơn giản là đơn vị đếm từ của AI (khoảng 3/4 từ tiếng Việt). Bộ nhớ AI có giới hạn số lượng token.*
> *2. Tầng 1 (Đọc bảng hiệu): Lúc mở máy, AI chỉ liếc qua Tên và Mô tả ngắn của các Skill (~100 tokens, nhẹ như sợi lông hồng). Dù bạn cài 50 Skills thì máy vẫn chạy mượt mà.*
> *3. Tầng 2 (Mở cẩm nang khi có việc): Khi bạn yêu cầu làm báo cáo thuế, AI mới rút cuốn `SKILL.md` về thuế ra đọc từng bước.*
> *4. Tầng 3 (Rút đồ nghề trong hộp đen): Chỉ khi gặp bài toán tính toán phức tạp, AI mới nạp thêm các script tính toán.*
>
> *Nhờ nguyên tắc này, bạn tha hồ trang bị kho vũ khí kỹ năng đồ sộ mà AI lúc nào cũng nhẹ tênh và phản hồi nhanh như chớp!"*

---

## 📍 SLIDE 12: KHÁI NIỆM LIFECYCLE HOOK
* **Thuộc trụ cột:** TRỤ CỘT 04: LIFECYCLE HOOKS
* **Huy hiệu đầu trang:** `TRỤ CỘT 04: LIFECYCLE HOOKS` | `LÁ CHẮN AN NINH TỰ ĐỘNG`
* **Mục tiêu học viên cần đọng lại:** Hiểu Lifecycle Hook đóng vai trò như chốt chặn an ninh tự động, giám sát và kiểm soát mọi hành vi của AI trước khi tác động vào máy tính.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Khái Niệm **Lifecycle Hook**
2. **Mô tả ngắn:** Vệ sĩ bảo vệ máy tính vô điều kiện: Kiểm soát và can thiệp tự động trước và sau mỗi hành vi của AI để triệt tiêu mọi rủi ro an ninh.
3. **Tại sao bạn cần Lifecycle Hook?**
   * **Rủi ro AI quá đà:** AI đôi khi quá nhiệt tình, vô tình chạy lệnh xóa nhầm tệp tin quan trọng, hoặc đọc trộm file bảng lương cá nhân.
   * **Giải pháp Lá chắn:** Hook đóng vai trò như trạm kiểm soát an ninh tự động. Mọi hành động của AI (đọc file, ghi file, chạy lệnh) đều phải xuất trình giấy phép qua trạm gác.
4. **3 Năng lực kiểm soát của Hook:**
   * **Chặn đứng tức thì:** Từ chối ngay lập tức nếu AI chạm vào vùng cấm (ví dụ: các file chứa mật khẩu `.env`, file `bang_luong.xlsx`).
   * **Ghi nhật ký kiểm toán:** Tự động ghi chép lại mọi hành động mà AI đã thực hiện trên máy tính của bạn.
   * **Tiền xử lý thông minh:** Tự động dọn dẹp hoặc định dạng lại dữ liệu trước khi gửi cho AI xử lý.
5. **Chân trang:** `AN TOÀN LÀ TRÊN HẾT:` Hook là quyền lực kiểm soát tối cao của con người, đảm bảo AI không bao giờ vượt quyền kiểm soát.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Chào mừng các bạn đến với Trụ Cột số 4: Lifecycle Hooks — Lá chắn an ninh tự động của bạn.*
>
> *Nhiều người sợ dùng AI tự động vì lo ngại: 'Nếu con AI lỡ tay xóa mất thư mục tài liệu của công ty tôi thì sao? Hoặc nó vô tình gửi dữ liệu mật ra ngoài thì ai chịu trách nhiệm?'.*
>
> *Đó chính là lý do Lifecycle Hooks ra đời! Bạn hãy hình dung Hook giống như một anh Vệ sĩ hay Chốt bảo vệ an ninh đứng ngay tại cổng ra vào.*
>
> *Mỗi khi AI định mở một tệp tin, anh bảo vệ sẽ chặn lại hỏi: 'Tệp tin này có nằm trong danh sách cấm không?'. Nếu AI định đụng vào file mật khẩu, Hook sẽ dứt khoát giật nút dừng khẩn cấp và báo hiệu cho bạn ngay lập tức.*
>
> *Có Hook bảo vệ, bạn có thể hoàn toàn yên tâm ngủ ngon khi giao việc cho AI tự động chạy thâu đêm!"*

---

## 📍 SLIDE 13: 5 TRẠM GÁC VÒNG ĐỜI CỦA HOOK
* **Thuộc trụ cột:** TRỤ CỘT 04: LIFECYCLE HOOKS
* **Huy hiệu đầu trang:** `TRỤ CỘT 04: LIFECYCLE HOOKS` | `KIẾN TRÚC TRẠM GÁC`
* **Mục tiêu học viên cần đọng lại:** Nắm vững 5 sự kiện Hook theo tên chuẩn PascalCase của Antigravity (`SessionStart`, `PreToolUse`, `PostToolUse`, `PreInvocation`, `Stop`).

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** 5 Trạm Gác **Vòng Đời Của Hook**
2. **Mô tả ngắn:** Điểm mặt 5 thời khắc quyết định trong vòng đời phiên làm việc mà bạn có thể cài cắm bảo vệ an ninh và tối ưu hóa dữ liệu.
3. **Chi Tiết 5 Trạm Gác Vòng Đời (Chuẩn PascalCase):**
   * **Trạm 1: `SessionStart` (Cổng vào phiên):** Kích hoạt một lần duy nhất khi mở phiên chat. Thích hợp để nạp môi trường, kiểm tra kết nối mạng.
   * **Trạm 2: `PreToolUse` (Trạm gác tiền trảm - QUAN TRỌNG NHẤT):** Đứng ngay trước khi AI bấm nút chạy bất kỳ công cụ nào (đọc file, xóa file, chạy lệnh). Chốt chặn cốt lõi để bảo vệ dữ liệu mật!
   * **Trạm 3: `PostToolUse` (Trạm nghiệm thu kết quả):** Kích hoạt ngay sau khi công cụ chạy xong. Tự động kiểm tra chất lượng kết quả đầu ra trước khi AI trả lời.
   * **Trạm 4: `PreInvocation` (Kiểm duyệt đầu vào):** Quét câu hỏi của người dùng trước khi gửi cho mô hình để lọc bỏ số thẻ tín dụng hoặc thông tin nhạy cảm.
   * **Trạm 5: `Stop` (Cổng đóng phiên):** Kích hoạt khi kết thúc công việc. Tự động lưu trữ nhật ký báo cáo hoặc dọn dẹp file tạm.
4. **Chân trang:** `ĐIỂM THEN CHỐT:` `PreToolUse` là chốt chặn phòng thủ cốt lõi nhất để ngăn AI đụng vào file mật hoặc tự ý sửa đổi dữ liệu quan trọng!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Đi sâu vào kiến trúc an ninh: Antigravity bảo vệ máy tính của bạn thông qua 5 trạm gác vòng đời (Lưu ý: Tên sự kiện chính thức viết theo dạng PascalCase):*
>
> *1. `SessionStart`: Chốt kiểm soát khi mở cửa phiên chat đầu ngày.*
> *2. `PreToolUse` (Trạm gác tiền trảm - QUAN TRỌNG NHẤT): Đứng ngay trước khi AI bấm nút chạy bất kỳ công cụ nào (như đọc file, xóa file, chạy lệnh). Đây là chốt chặn phòng thủ cốt lõi để ngăn AI đụng vào dữ liệu mật!*
> *3. `PostToolUse`: Trạm nghiệm thu sản phẩm ngay sau khi công cụ chạy xong.*
> *4. `PreInvocation`: Trạm kiểm duyệt câu hỏi và dữ liệu đầu vào trước khi chuyển cho bộ não AI suy nghĩ.*
> *5. `Stop`: Chốt cổng đóng phiên làm việc, tự động xuất báo cáo nhật ký.*
>
> *Hãy nhớ đúng tên gọi `PreToolUse` và `PostToolUse` để khi cấu hình file máy tính hiểu và kích hoạt chính xác 100%!"*

---

## 📍 SLIDE 14: CẤU HÌNH HOOKS.JSON & MINI-PROJECT 6
* **Thuộc trụ cột:** MINI-PROJECT 06: SECURITY SHIELD
* **Huy hiệu đầu trang:** `MINI-PROJECT 06: SECURITY SHIELD` | `THIẾT LẬP LÁ CHẮN BẢO MẬT`
* **Mục tiêu học viên cần đọng lại:** Nắm vững cấu trúc file `hooks.json` theo chuẩn Object của Antigravity, vị trí lưu trữ và thực hành cấu hình lá chắn bảo vệ file nhạy cảm.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Cấu Hình hooks.json & **Mini-Project 6**
2. **Mô tả ngắn:** Thiết lập file hooks.json tại .agents/hooks.json hoặc ~/.gemini/config/hooks.json chặn đứng hành vi đọc file nhạy cảm.
3. **Đường Dẫn & Tên File Cấu Hình:**
   * **Workspace:** `.agents/hooks.json`
   * **Global:** `~/.gemini/config/hooks.json`
   * Tên file bắt buộc viết thường: `hooks.json`.
4. **Cấu Trúc Khai Báo Chuẩn Antigravity:**
   ```json
   {
     "la-chan-file-mat": {
       "PreToolUse": [
         {
           "matcher": "read_file",
           "hooks": [
             {
               "type": "command",
               "command": "python ./scripts/chan_file_mat.py"
             }
           ]
         }
       ]
     }
   }
   ```
5. **Thực Hành Mini-Project 6 (Lá Chắn File Mật):**
   * Tự động phát hiện khi AI định đọc file `.env`, `passwords.txt`, hoặc `bang_luong.xlsx`.
   * Lập tức hủy bỏ lệnh và cảnh báo: *"Truy cập bị từ chối: Tệp tin nhạy cảm đã được bảo vệ bởi Lifecycle Hook!"*.
6. **Chân trang:** `BẢO VỆ 100%:` Không còn nỗi lo dữ liệu cá nhân hay tiền lương công ty bị AI đọc trộm hoặc tải lên mạng!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Để các bạn không cảm thấy Hooks là khái niệm xa vời, slide này hướng dẫn cấu hình trực tiếp file `hooks.json`:*
>
> *Vị trí lưu trữ:*
> *- Riêng cho dự án: `.agents/hooks.json`*
> *- Dùng cho toàn máy: `~/.gemini/config/hooks.json`*
>
> *Cấu trúc file cực kỳ dễ hiểu: Mỗi trạm gác có một tên định danh bọc ngoài, ví dụ `la-chan-file-mat`, bên trong khai báo sự kiện `PreToolUse`. Khi AI định gọi công cụ đọc file (`read_file`), hệ thống sẽ tự động kích hoạt lệnh kiểm tra an ninh.*
>
> *Nếu phát hiện AI định mở file bảng lương (`bang_luong.xlsx`) hoặc file mật khẩu `.env`, lá chắn lập tức ngắt lệnh ngay tại chỗ! Dân văn phòng hoàn toàn có thể yên tâm giao việc cho AI mà dữ liệu cơ quan luôn được bảo vệ an toàn 100%!"*

---

## 📍 SLIDE 15: KHÁI NIỆM MODEL CONTEXT PROTOCOL (MCP)
* **Thuộc trụ cột:** TRỤ CỘT 05: MCP ECOSYSTEM
* **Huy hiệu đầu trang:** `TRỤ CỘT 05: MCP ECOSYSTEM` | `CHUẨN KẾT NỐI MỞ VẠN NĂNG`
* **Mục tiêu học viên cần đọng lại:** Hiểu Model Context Protocol (MCP) là "cổng cắm USB vạn năng" giúp AI kết nối với mọi phần mềm văn phòng bên ngoài.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Khái Niệm **Model Context Protocol (MCP)**
2. **Mô tả ngắn:** Chuẩn kết nối mở đóng vai trò như "Cổng cắm USB" giúp AI cắm rút tự do vào hàng ngàn phần mềm văn phòng.
3. **Hình Tượng "Cổng Cắm USB":**
   * **Trước khi có MCP:** AI bị nhốt trong một căn phòng kín, muốn nối với Gmail phải viết code riêng cho Gmail, muốn nối với Slack lại phải viết code riêng cho Slack. Rất phức tạp và tốn kém.
   * **Khi có MCP (Chuẩn USB-C thế hệ mới):** Mọi phần mềm chỉ cần trang bị một đầu cắm chuẩn MCP. AI chỉ việc "cắm cáp" vào là ngay lập tức có thêm giác quan và quyền năng điều khiển phần mềm đó!
4. **Hệ Sinh Thái Cắm Rút Phổ Biến:**
   * **Giao tiếp & Trao đổi:** Cắm vào Gmail (đọc/gửi thư), Slack (bắn thông báo kênh), Zalo PC (đọc tin nhắn offline).
   * **Dữ liệu & Quản trị:** Cắm vào Google Sheets/Excel, Notion, Trello, Google Drive.
   * **Tra cứu & Nghiên cứu:** Cắm vào Google Search, trình duyệt web tự động.
5. **Chân trang:** `TIÊU CHUẨN MỞ TOÀN CẦU:` MCP là chuẩn công nghệ mở do toàn ngành công nghệ chung tay phát triển, không bị trói buộc vào một công ty duy nhất.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Chào mừng các bạn đến với Trụ Cột số 5: Model Context Protocol (MCP). Đây có thể xem là một cuộc cách mạng công nghệ quan trọng nhất đối với người dùng AI!*
>
> *Trước đây, con AI giống như một bộ não bị nhốt trong lọ thủy tinh: Nó rất thông minh nhưng không có tay chân, không thể tự mở Gmail đọc thư, không thể tự mở Slack nhắn tin cho đồng nghiệp.*
>
> *MCP chính là 'Cổng cắm USB Type-C vạn năng' cho AI! Chuột hay bàn phím của bất kỳ hãng nào chỉ cần có đầu cắm USB là cắm vào máy tính dùng được ngay. Tương tự như vậy, Gmail, Slack, Excel hay Google Drive đã có sẵn cổng cắm MCP.*
>
> *Antigravity chỉ cần 'cắm cáp' vào là AI lập tức có tay chân để thao tác trực tiếp trên các ứng dụng văn phòng của bạn!"*

---

## 📍 SLIDE 16: CẤU HÌNH MCP_CONFIG.JSON & MINI-PROJECT 4
* **Thuộc trụ cột:** MINI-PROJECT 04: GMAIL & SLACK
* **Huy hiệu đầu trang:** `MINI-PROJECT 04: GMAIL & SLACK` | `GIAO THỨC TRUYỀN THÔNG MCP`
* **Mục tiêu học viên cần đọng lại:** Nắm vững vị trí và cấu trúc file `mcp_config.json`, phân biệt kết nối Stdio (cắm USB trực tiếp) vs HTTP (cáp mạng Internet), và thực hành trợ lý đọc Gmail báo Slack.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Cấu Hình mcp_config.json & **Mini-Project 4**
2. **Mô tả ngắn:** Cấu hình cổng cắm tại ~/.gemini/config/mcp_config.json và thực chiến trợ lý tự động lọc email khẩn báo tin Slack.
3. **Vị Trí & Tên File Cấu Hình MCP:**
   * Vị trí lưu trữ duy nhất: `~/.gemini/config/mcp_config.json`
   * Tên file bắt buộc viết thường: `mcp_config.json`.
4. **2 Cơ Chế Kết Nối Cổng:**
   * **`stdio` (Cắm USB trực tiếp vào máy):** Chạy phần mềm cục bộ ngay trên máy tính của bạn. Tốc độ phản hồi tức thì và bảo mật tuyệt đối.
   * **`http / sse` (Cắm cáp mạng qua Internet):** Kết nối tới các ứng dụng đám mây từ xa thông qua đường dẫn URL web an toàn.
5. **Thực Hành Mini-Project 4 (Bộ Đôi Gmail + Slack):**
   * Khai báo server `gmail` và server `slack` trong `mcp_config.json`.
   * Giao nhiệm vụ tự nhiên: *"Hãy kiểm tra hòm thư Gmail, tìm các email có tiêu đề 'Khẩn cấp' trong sáng nay, tóm tắt nội dung và gửi tin nhắn báo động vào kênh #thong-bao trên Slack!"*.
6. **Chân trang:** `KẾT QUẢ THỰC TẾ:` AI tự động kết nối dữ liệu giữa 2 ứng dụng độc lập hoàn toàn mà bạn không cần phải sao chép qua lại thủ công một chữ nào!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Toàn bộ cấu hình MCP nằm gọn trong một file duy nhất mang tên `mcp_config.json` tại kho Global `~/.gemini/config/mcp_config.json`.*
>
> *Trong file này, bạn phân biệt 2 kiểu cắm rất dễ hiểu:*
> *1. Giao thức `stdio` (Cắm USB trực tiếp vào máy): Chạy các gói ứng dụng ngay trên máy tính của bạn, tốc độ phản hồi nhanh như chớp và cực kỳ bảo mật.*
> *2. Giao thức `http / sse` (Cắm cáp mạng qua Internet): Kết nối tới các dịch vụ đám mây từ xa qua một đường link web.*
>
> *Và đây là điều kỳ diệu của Mini-Project 4: Bạn chỉ cần yêu cầu: 'AI ơi, quét hòm thư Gmail, tìm email khẩn sáng nay rồi bắn tin tóm tắt sang kênh Slack cho cả phòng!'. AI tự cắm vào Gmail lấy thư, rồi tự cắm sang Slack gửi tin. Hai phần mềm riêng biệt kết nối mượt mà như một dòng chảy tự nhiên!"*

---

## 📍 SLIDE 17: KHÁI NIỆM PLUGIN
* **Thuộc trụ cột:** TRỤ CỘT 06: PLUGINS ECOSYSTEM
* **Huy hiệu đầu trang:** `TRỤ CỘT 06: PLUGINS ECOSYSTEM` | `ĐÓNG GÓI VẠN NĂNG ALL-IN-ONE`
* **Mục tiêu học viên cần đọng lại:** Hiểu Plugin là chiếc vali đồ nghề đóng gói All-in-One gom toàn bộ Rules, Skills, Subagents, Hooks để nhân bản năng suất cho toàn đội ngũ.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Khái Niệm **Plugin**
2. **Mô tả ngắn:** Chiếc vali đồ nghề All-in-One: Gom toàn bộ Rules, Skills, Subagents và Hooks vào 1 thư mục để chia sẻ và nhân bản năng suất cho toàn team.
3. **Vấn Đề & Giải Pháp Đóng Gói:**
   * **Vấn đề phân tán:** Sau khi bạn đã dày công thiết lập 3 Rules, 5 Skills, 2 Subagents và 1 Hook an ninh; nếu muốn đồng nghiệp cùng phòng dùng được, bạn phải gửi từng file lẻ tẻ rất dễ nhầm lẫn.
   * **Giải pháp Chiếc Vali Plugin:** Plugin đóng gói tất cả các món vũ khí trên vào MỘT THƯ MỤC DUY NHẤT. Đồng nghiệp chỉ cần nhận chiếc vali này về máy là có ngay một bộ trợ lý hoàn chỉnh 100%.
4. **Lợi Ích Doanh Nghiệp Cốt Lõi:**
   * **Nhân bản năng suất tức thì:** Toàn bộ nhân viên phòng ban dùng chung một tiêu chuẩn chất lượng cao nhất.
   * **Cập nhật tập trung:** Khi có thay đổi quy định, người quản lý chỉ cần sửa trong gói Plugin và chia sẻ lại cho toàn team.
5. **Chân trang:** `SỨC MẠNH TO LỚN:` Plugin biến năng lực cá nhân của bạn thành tài sản số của cả doanh nghiệp!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Bây giờ hãy cùng nhau ghép các mảnh ghép lại! Bạn đã có Rules (nội quy), bạn có Skills (tay nghề), bạn có Hooks (trạm gác) và Subagents (nhân sự).*
>
> *Giả sử bạn vừa mất 1 tuần để huấn luyện ra một bộ trợ lý Kế toán quá xuất sắc. Bây giờ bạn muốn chia sẻ cho 10 người đồng nghiệp trong phòng cùng dùng, bạn sẽ làm thế nào? Lẽ nào đi gửi từng file lẻ tẻ rồi hướng dẫn họ copy từng chỗ? Rất mất thời gian và dễ nhầm!*
>
> *Plugin chính là chiếc Vali Đồ Nghề All-in-One! Bạn gom tất cả các file đó vào một thư mục duy nhất gọi là Plugin. Bạn nén lại gửi cho đồng nghiệp qua Zalo hoặc Google Drive.*
>
> *Đồng nghiệp nhận về, chỉ cần thả vào máy tính là lập tức sở hữu trọn vẹn sức mạnh của bộ trợ lý Kế toán y hệt như trên máy bạn. Năng suất cả phòng tăng vọt!"*

---

## 📍 SLIDE 18: CẤU TRÚC THƯ MỤC PLUGIN & PLUGIN.JSON
* **Thuộc trụ cột:** TRỤ CỘT 06: PLUGINS ECOSYSTEM
* **Huy hiệu đầu trang:** `TRỤ CỘT 06: PLUGINS ECOSYSTEM` | `QUY CHUẨN ĐÓNG GÓI PLUGIN`
* **Mục tiêu học viên cần đọng lại:** Nắm vững cấu trúc thư mục tự nhận diện của Plugin, vị trí lưu trữ và quy cách viết file `plugin.json`.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Cấu Trúc Thư Mục **Plugin & plugin.json**
2. **Mô tả ngắn:** Thư mục plugin tự động nhận diện kỹ năng và quy tắc bên trong; file bắt buộc duy nhất là plugin.json viết thường.
3. **Cấu Trúc Cây Thư Mục Plugin:**
   * **Đường dẫn thư mục chứa:**
     * Workspace: `.agents/plugins/<ten-plugin>/`
     * Global: `~/.gemini/config/plugins/<ten-plugin>/`
   * **Các ngăn đồ nghề bên trong:**
     * `plugin.json` *(Bắt buộc - Viết thường)*: Tờ giấy khai sinh và thông tin phiên bản.
     * `skills/`: Chứa các thư mục Skill con (`<skill-name>/SKILL.md`).
     * `rules/`: Chứa các file quy tắc (`*.md` hoặc `AGENTS.md`).
     * `agents/`: Chứa các hồ sơ nhân sự phụ (`*.md`).
     * `hooks.json`: Tệp lá chắn an ninh đi kèm gói plugin.
4. **Quy Tắc Tự Nhận Diện Kỳ Diệu:**
   * Antigravity tự động quét các thư mục con tiêu chuẩn (`skills/`, `rules/`, `agents/`) mà không cần bạn phải khai báo thủ công danh sách file vào `plugin.json`!
5. **Chân trang:** `LƯU Ý ĐẶT TÊN:` Tên file khai sinh bắt buộc viết thường: `plugin.json`. Tên thư mục bọc ngoài dạng `kebab-case`.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Cấu trúc bên trong của một Plugin trong Antigravity được thiết kế thông minh đến mức kinh ngạc!*
>
> *Trong thư mục plugin, file bắt buộc duy nhất là `plugin.json` viết thường. Nó giống như một tờ giấy khai sinh ghi tên gói, phiên bản (ví dụ 1.0.0), tác giả và mô tả ngắn.*
>
> *Và điều tuyệt vời nhất là: Bạn chỉ cần xếp các món đồ vào đúng các ngăn có tên chuẩn: Kỹ năng thì nhét vào ngăn `skills/`, nội quy nhét vào `rules/`, nhân sự nhét vào `agents/`.*
>
> *Hệ thống sẽ TỰ ĐỘNG NHẬN DIỆN tất cả mọi thứ bên trong mà bạn không cần phải khai báo danh sách từng file một! Thao tác đóng gói cực kỳ đơn giản, trực quan và chuẩn hóa cao độ!"*

---

## 📍 SLIDE 19: QUẢN LÝ & BẬT/TẮT PLUGIN 1-CLICK
* **Thuộc trụ cột:** QUẢN TRỊ PLUGIN: MANIFEST & CLI
* **Huy hiệu đầu trang:** `QUẢN TRỊ PLUGIN` | `CƠ CHẾ ĐIỀU HÀNH PLUGIN`
* **Mục tiêu học viên cần đọng lại:** Nắm vững cơ chế quản lý vòng đời plugin tương tự như Extension trình duyệt; cách bật/tắt linh hoạt để tối ưu hiệu năng máy tính.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Quản Lý & **Bật/Tắt Plugin 1-Click**
2. **Mô tả ngắn:** Quản lý tập trung vòng đời plugin tương tự như kho tiện ích mở rộng Chrome Extension: Bật khi cần, tắt khi xong.
3. **Cơ Chế Bật/Tắt Tương Tự Chrome Extension:**
   * **Cài đặt độc lập:** Bạn có thể cài 10 gói plugin khác nhau (Kế toán, Marketing, Pháp chế, Nhân sự) mà không sợ chúng xung đột lẫn nhau.
   * **Bật/Tắt linh hoạt:**
     * Khi đến kỳ báo cáo tài chính cuối tháng: Bật plugin Kế Toán lên.
     * Khi hết kỳ: Bấm tắt plugin đi để giải phóng hoàn toàn bộ nhớ cho AI.
4. **Các Cách Điều Khiển Thao Tác:**
   * Sử dụng lệnh gạch chéo trực tiếp trong khung chat: `/plugin` để mở bảng điều khiển.
   * Chỉnh sửa trạng thái `"enabled": true / false` trong file cấu hình.
5. **Chân trang:** `GỌN GÀNG & LINH HOẠT:` Quản trị plugin theo nhu cầu thực tế giúp môi trường làm việc luôn tinh gọn và nhẹ nhàng.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Việc quản lý các gói Plugin dễ dàng hệt như bạn bật/tắt các tiện ích mở rộng trên trình duyệt web vậy.*
>
> *Hôm nay là kỳ quyết toán thuế cuối tháng, bạn chỉ cần gõ `/plugin` và bấm BẬT gói 'Kế Toán & Thuế'. Ngay lập tức, AI của bạn sở hữu toàn bộ kỹ năng soi hóa đơn, biểu mẫu thuế và các quy định mới nhất.*
>
> *Sang tuần sau bạn chuyển sang làm chiến dịch tiếp thị, bạn tắt gói Kế toán và bấm BẬT gói 'Marketing Content'. Bàn làm việc của AI lại biến thành một phòng truyền thông sáng tạo!*
>
> *Không bao giờ bị lẫn lộn giữa các chuyên môn, và máy tính của bạn lúc nào cũng được giữ sạch sẽ, tối ưu!"*

---

## 📍 SLIDE 20: KHÁI NIỆM TASK SCHEDULE
* **Thuộc trụ cột:** TRỤ CỘT 07: SIDECARS & SCHEDULE
* **Huy hiệu đầu trang:** `TRỤ CỘT 07: SIDECARS & SCHEDULE` | `TỰ ĐỘNG HÓA HẸN GIỜ`
* **Mục tiêu học viên cần đọng lại:** Hiểu Task Schedule là chiếc đồng hồ báo thức thông minh giúp AI tự động thức dậy làm việc định kỳ qua lệnh `/schedule` mà không cần viết file phức tạp.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Khái Niệm **Task Schedule**
2. **Mô tả ngắn:** Đồng hồ báo thức thông minh cho AI: Đặt lịch hẹn giờ định kỳ qua lệnh /schedule để AI tự động thức dậy làm việc ngầm.
3. **Hình Tượng "Đồng Hồ Báo Thức":**
   * **Trước đây:** Bạn phải ngồi trực trước màn hình, gõ lệnh thì AI mới làm việc.
   * **Với Task Schedule:** Bạn hẹn giờ trước bằng lệnh `/schedule`: Đúng 7:00 sáng mỗi ngày, hoặc 17:00 chiều thứ Sáu hàng tuần; AI tự động thức dậy, thực hiện công việc và gửi kết quả sẵn sàng chờ bạn!
4. **2 Chế Độ Hẹn Giờ Cơ Bản:**
   * **Hẹn giờ một lần (Timer đếm lùi):** Ví dụ: *"Sau 30 phút nữa hãy kiểm tra lại trạng thái tệp tin và thông báo cho tôi"*.
   * **Lịch trình lặp lại (Cron Expression):** Ví dụ: *"Cứ 8:00 sáng từ thứ Hai đến thứ Sáu, hãy tổng hợp tin tức thị trường gửi vào hòm thư"*.
5. **Chân trang:** `LỢI ÍCH VƯỢT TRỘI:` Không cần viết file phức tạp: Chỉ cần dùng lệnh `/schedule` bằng tiếng Việt là AI tự động hẹn giờ làm việc ngầm!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Từ đầu buổi học đến giờ, bạn luôn phải ngồi trước máy tính gõ lệnh thì AI mới làm. Nhưng nếu bạn muốn: 'Ban đêm tôi đi ngủ, AI tự động thức dậy lúc 2 giờ sáng để quét dọn tệp tin rác', thì sao?*
>
> *Đó là lúc chúng ta dùng đến Task Schedule — Chiếc Đồng Hồ Báo Thức thông minh cho AI!*
>
> *Một điểm tuyệt vời: Bạn KHÔNG CẦN phải tạo file cấu hình phức tạp nào cả! Trong Antigravity, bạn chỉ cần dùng lệnh `/schedule` và gõ yêu cầu bằng tiếng Việt tự nhiên:
> - 'Đúng 7:00 sáng mỗi ngày, hãy đọc tin tức thị trường và gửi email tóm tắt cho tôi'.
> - 'Cứ 17:00 chiều thứ Sáu, tự động xuất báo cáo tuần từ thư mục dự án'.*
>
> *AI sẽ tự động nhận lịch hẹn, đến đúng giờ tự thức dậy làm việc và gửi báo cáo về cho bạn!"*

---

## 📍 SLIDE 21: KHÁI NIỆM SIDECAR DAEMON
* **Thuộc trụ cột:** TRỤ CỘT 07: SIDECARS DAEMON
* **Huy hiệu đầu trang:** `TRỤ CỘT 07: SIDECARS DAEMON` | `CỖ MÁY VẬN HÀNH 24/7`
* **Mục tiêu học viên cần đọng lại:** Hiểu Sidecar Daemon là cỗ máy chạy ngầm độc lập 24/7 như chiếc thùng xe phụ gắn bên hông xe máy, duy trì hoạt động không phụ thuộc cửa sổ chat.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Khái Niệm **Sidecar Daemon**
2. **Mô tả ngắn:** Cỗ máy vận hành nền độc lập như chiếc thùng xe phụ gắn bên hông xe máy: Âm thầm chạy 24/7 kể cả khi tắt khung chat.
3. **Hình Tượng "Thùng Xe Phụ Bên Hông Mô Tô" (Sidecar):**
   * Trong thực tế, xe mô tô gắn thêm một thùng xe phụ bên hông để chở thêm hàng nặng. Xe chính vẫn chạy bon bon phía trước.
   * Trong Antigravity, giao diện chat chính là chiếc mô tô. Còn Sidecar là chiếc thùng xe phụ âm thầm chạy song song phía sau hậu trường. Dù bạn tắt cửa sổ chat, thùng xe phụ vẫn tiếp tục vận hành các tác vụ ngầm 24/7!
4. **Các Ứng Dụng Thực Tế Tuyệt Vời:**
   * Canh gác hòm thư khách hàng hoặc tin nhắn Zalo 24/7.
   * Theo dõi biến động giá cổ phiếu hoặc tỷ giá hối đoái liên tục.
   * Quét và phân loại tự động mọi tệp tin tải về trong thư mục Downloads.
5. **Chân trang:** `HOẠT ĐỘNG BỀN BỈ:` Chạy độc lập hoàn toàn, không phụ thuộc vào trạng thái mở hay tắt của cửa sổ làm việc Antigravity!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Và bây giờ, chúng ta chạm tay vào Mảnh ghép đỉnh cao hoàn thiện toàn bộ bức tranh kiến trúc Antigravity: Sidecars!*
>
> *Từ 'Sidecar' trong tiếng Anh nghĩa là chiếc xe máy có gắn thêm một thùng xe phụ bên hông để chở đồ. Trong máy tính, Sidecar là một cỗ máy chạy ngầm độc lập 24/7.*
>
> *Nó có đặc điểm gì đặc biệt? Dù bạn tắt cửa sổ chat Antigravity, thậm chí thu nhỏ máy tính đi làm việc khác, cỗ máy Sidecar vẫn âm thầm thức canh gác:*
>
> *- Nó có thể theo dõi xem hòm thư có khiếu nại của khách hàng không để gửi chuông báo.*
> *- Nó có thể canh thư mục Downloads xem bạn vừa tải file hóa đơn nào về là tự động đổi tên và cất vào kho ngay lập tức.*
>
> *Một trợ lý chạy ngầm 24/7 không biết mệt mỏi và không bao giờ đòi nghỉ phép!"*

---

## 📍 SLIDE 22: CẤU TRÚC FILE SIDECAR.JSON & TỰ HỒI SINH
* **Thuộc trụ cột:** TÍNH BỀN BỈ: RESTART POLICY
* **Huy hiệu đầu trang:** `TÍNH BỀN BỈ` | `CƠ CHẾ TỰ HỒI SINH`
* **Mục tiêu học viên cần đọng lại:** Nắm vững cấu trúc file `sidecar.json`, vị trí lưu trữ và cơ chế tự hồi sinh đảm bảo hệ thống tự động hóa không bao giờ bị gián đoạn.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Cấu Trúc File sidecar.json & **Tự Hồi Sinh**
2. **Mô tả ngắn:** Bảo đảm tính bền bỉ tuyệt đối của hệ thống tự động hóa: Tự động hồi sinh khi gặp sự cố mạng hoặc lỗi đột xuất.
3. **Đường Dẫn & Tên File Bắt Buộc:**
   * Vị trí lưu trữ: `~/.gemini/config/sidecars/<ten-sidecar>/sidecar.json`
   * Tên file bắt buộc viết thường: `sidecar.json`.
4. **Chính Sách Tự Hồi Sinh (`restart_policy`):**
   * **`always` (Luôn luôn hồi sinh):** Nếu tiến trình gặp lỗi ngắt quãng hoặc bị tắt đột ngột, Antigravity sẽ tự động khởi động lại ngay lập tức.
   * **`on-failure` (Chỉ hồi sinh khi gặp sự cố):** Tự động khởi động lại khi gặp lỗi bất ngờ; chỉ dừng hẳn khi hoàn thành đúng nhiệm vụ.
   * **`never` (Không tự hồi sinh):** Chỉ chạy một lần duy nhất rồi tắt.
5. **Chân trang:** `BẢO CHỨNG VẬN HÀNH:` Hệ thống tự động đứng dậy sau sự cố, đảm bảo các quy trình nghiệp vụ quan trọng vận hành liên tục 365 ngày/năm.

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Một tiến trình chạy ngầm thì điều gì quan trọng nhất? Đó là Tính Bền Bỉ (Resilience) — nó không được phép chết giữa chừng!*
>
> *Mỗi Sidecar được định nghĩa bằng một file duy nhất mang tên `sidecar.json` nằm trong thư mục `~/.gemini/config/sidecars/<tên-sidecar>/`.*
>
> *Trong file này có một dòng thiết lập cực kỳ quyền lực mang tên `restart_policy: always` (Chính sách tự hồi sinh). Nếu chẳng may máy tính của bạn bị rớt mạng chập chờn hoặc hệ điều hành gặp trục trặc khiến Sidecar bị văng ra, thì chỉ vài giây sau, Antigravity sẽ TỰ ĐỘNG BẬT NÓ DẬY NGAY LẬP TỨC!*
>
> *Không cần bạn phải ra tay khởi động lại. Đây chính là tiêu chuẩn vàng của hệ thống tự động hóa cấp doanh nghiệp!"*

---

## 📍 SLIDE 23: BẢN ĐỒ TRA CỨU TOÀN NĂNG (CHEATSHEET)
* **Thuộc trụ cột:** TỔNG KẾT VŨ KHÍ: CHEATSHEET TOÀN NĂNG
* **Huy hiệu đầu trang:** `TỔNG KẾT VŨ KHÍ` | `BẢN ĐỒ TRA CỨU NHANH`
* **Mục tiêu học viên cần đọng lại:** Nắm trọn bản đồ tra cứu 1 trang tổng kết toàn bộ vị trí thư mục, đường dẫn lưu trữ và quy tắc vàng của cả 7 Trụ Cột để áp dụng hàng ngày.

### 🖼️ Khung hiển thị trực quan trên Slide
1. **Tiêu đề:** Bản Đồ Tra Cứu **Toàn Năng (Cheatsheet)**
2. **Mô tả ngắn:** Bảng một trang tổng hợp toàn bộ vị trí cất file, đường dẫn lưu trữ và quy tắc vàng đặt tên để học viên lưu lại tra cứu hàng ngày.
3. **Bảng Tra Cứu Toàn Năng 7 Trụ Cột:**

| Trụ Cột | Khái Niệm Đời Thực | Đường Dẫn Workspace (Dự Án) | Đường Dẫn Global (Toàn Máy) | Tên File Bắt Buộc & Quy Tắc Vàng |
| :--- | :--- | :--- | :--- | :--- |
| **01. Subagents** | Đội ngũ nhân sự phụ song song | `.agents/agents/<name>.md` | `~/.gemini/config/agents/<name>.md` | Chữ thường `kebab-case.md`, khai báo `name`, `role`, `workspace`. Thụt lề bằng Space, không dùng Tab! |
| **02. Rules** | Sổ tay quy tắc & Tiêu chuẩn | `AGENTS.md` hoặc `.agents/rules/*.md` | `~/.gemini/config/AGENTS.md` hoặc `~/.gemini/config/rules/*.md` | `AGENTS.md` viết HOA; tối đa 24KB/file; ngân sách 20.000 tokens; để phẳng trong `rules/`! |
| **03. Skills** | Bằng nghề & Cẩm nang nghiệp vụ | `.agents/skills/<name>/SKILL.md` | `~/.gemini/config/skills/<name>/SKILL.md` | File bắt buộc viết HOA `SKILL.md`; viết `description` ngôi thứ ba để tự kích hoạt. |
| **04. Hooks** | Trạm gác an ninh tự động | `.agents/hooks.json` | `~/.gemini/config/hooks.json` | File bắt buộc `hooks.json`; sự kiện PascalCase (`PreToolUse`, `PostToolUse`). |
| **05. MCP** | Cổng cắm USB mở rộng phần mềm | *Thường dùng cấu hình Global* | `~/.gemini/config/mcp_config.json` | File bắt buộc viết thường `mcp_config.json`; cắm USB trực tiếp qua giao thức `stdio`. |
| **06. Plugins** | Vali đồ nghề All-in-One | `.agents/plugins/<name>/` | `~/.gemini/config/plugins/<name>/` | Chứa `plugin.json` viết thường; tự động nhận diện các thư mục `skills/`, `rules/`, `agents/`. |
| **07. Sidecars & Schedule** | Thùng xe phụ chạy ngầm 24/7 | *Hẹn giờ nhanh bằng lệnh `/schedule`* | `~/.gemini/config/sidecars/<name>/sidecar.json` | Lệnh `/schedule` không cần file; Sidecar dùng `sidecar.json` với `restart_policy: always`. |

4. **Chân trang:** `LƯU BẢN ĐỒ NÀY LẠI:` Đây là tài liệu gối đầu giường giá trị nhất, giúp bạn làm chủ 100% hệ sinh thái Google Antigravity!

### 🎙️ Kịch bản giảng dạy chi tiết (Speaker Notes)
> *"Kính thưa các bạn học viên, đây chính là Slide đắt giá nhất trong toàn bộ Phần 4 — Tấm Bản Đồ Chỉ Đường quý giá mà tôi muốn các bạn chụp ảnh màn hình hoặc lưu lại làm cẩm nang gối đầu giường!*
>
> *Từ nay về sau, mỗi khi chuẩn bị tạo một trợ lý mới, bạn chỉ cần mở bảng này ra đối chiếu:*
> *- Muốn đặt quy tắc kỷ luật: Tìm dòng Rules.*
> *- Muốn truyền tay nghề SOP: Tìm dòng Skills, nhớ file phải viết hoa `SKILL.md`.*
> *- Muốn bảo vệ file an toàn: Tìm dòng Hooks với trạm gác `PreToolUse`.*
> *- Muốn cắm vào Gmail, Slack: Tìm dòng MCP.*
> *- Muốn đóng gói vali tặng đồng nghiệp: Tìm dòng Plugins.*
> *- Muốn hẹn giờ chạy ngầm 24/7: Tìm dòng Task Schedule (`/schedule`) và Sidecars.*
>
> *Nắm vững tấm bản đồ này, các bạn đã chính thức bước lên một tầm cao mới: Không còn là người dùng AI đơn thuần, mà là Kiến Trúc Sư Điều Hành toàn bộ hệ thống trí tuệ nhân tạo phục vụ cho công việc và doanh nghiệp của mình. Chúc mừng tất cả các bạn đã làm chủ trọn vẹn 7 Trụ Cột Vũ Khí của Google Antigravity!"*

---

*Tài liệu được biên soạn và cập nhật theo tài liệu kỹ thuật chuẩn xác nhất của Google Antigravity (https://antigravity.google/docs/).*
