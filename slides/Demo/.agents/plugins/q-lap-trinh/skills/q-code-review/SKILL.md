---
name: q-code-review
description: Quy trình tự động đánh giá (code review) Pull Request đa góc nhìn bằng các Subagents song song trong Antigravity, quét tác động liên file (cross-file caller tracing), soi logic thời gian (temporal invariants), kiểm tra bản chất unit test, chấm điểm độ tin cậy lọc nhiễu, phân loại MUST/IMO/NITS và xuất báo cáo lên GitHub PR.
---

# 🔍 Quy Trình Code Review Pull Request Đa Góc Nhìn (Antigravity AI)

Tài liệu này hướng dẫn Antigravity Agent thực hiện đánh giá mã nguồn (Code Review) cho một Pull Request (PR) trên GitHub. Quy trình sử dụng các Subagents chạy song song để soi xét mã nguồn từ nhiều khía cạnh khác nhau, quét tác động liên file (cross-file caller tracer), soi logic thời gian, lọc bỏ cảnh báo giả (false positives) bằng thang điểm tin cậy và báo cáo kết quả theo chuẩn **MUST / IMO / NITS**.

---

## 🛠️ CÁC BƯỚC THỰC HIỆN CHI TIẾT

Để đánh giá một PR, hãy thực hiện chính xác theo thứ tự sau:

### 1. Kiểm Tra Sơ Bộ Điều Kiện PR (Model: `flash`)
Sử dụng một subagent với `Model: 'flash'` dùng lệnh `gh` để kiểm tra PR:
* (a) Đã bị đóng (closed) hoặc đã merged chưa?
* (b) Có đang ở trạng thái bản nháp (draft) không?
* (c) Có phải là PR tự động (như Dependabot/Renovate) hoặc thay đổi quá đơn giản không cần review không?
* (d) Đã từng được Antigravity Code Reviewer nhận xét trước đó chưa?

👉 **Nếu thuộc một trong các trường hợp trên: Dừng quy trình, không tiến hành review.**

---

### 2. Thu Thập Hệ Thống Quy Tắc Mã Nguồn (Model: `flash`)
Sử dụng subagent đọc và liệt kê danh sách đường dẫn các file quy tắc áp dụng cho dự án (chỉ lấy đường dẫn, chưa lấy nội dung):
* File `AGENTS.md` tại gốc dự án (nếu có) và các file `AGENTS.md` nằm trong thư mục chứa file bị sửa đổi.
* Các file quy tắc kiến trúc & bảo mật trong thư mục `storage/rules/` và `rules/` của dự án.
* Các quy tắc global của Antigravity tại `/home/tranquyet/.gemini/config/plugins/chasqui/rules/` và `/home/tranquyet/.gemini/config/`.

---

### 3. Xem Thay Đổi & Tóm Tắt PR (Model: `flash`)
Sử dụng subagent lấy thông tin diff của PR (`gh pr diff`) và trả về bản tóm tắt ngắn gọn các thay đổi chính.

---

### 4. Phân Tích Đa Góc Nhìn Bằng 6 Subagents Chuyên Sâu Song Song (Model: `pro`)
Khởi chạy đồng thời **6 Subagents song song** với `Model: 'pro'` qua tool `invoke_subagent` để đánh giá mã nguồn độc lập. Mỗi subagent trả về danh sách vấn đề phát hiện được cùng căn cứ cụ thể:

* **Subagent #1 (Kiểm tra Quy tắc Dự án, Dead Code & Bản Chất Unit Test - Rule, Dead Code & Test Intent Compliance)**:
  - Đối chiếu các file sửa đổi với hệ thống quy tắc đã thu thập ở Bước 2 (`AGENTS.md`, `storage/rules/`, v.v.). Đặc biệt thực hiện **Dead Code Audit 2 Chiều**:
    - Forward Scan: Kiểm tra code mới tạo có callsite hay chưa.
    - Reverse Scan: Khi gỡ nút/action UI, quét dọn dẹp các method JS Stimulus controller, Ruby helper/private method, Interaction class mồ côi. Kiểm tra tệp locale (`en`, `ja`, `vi`) xem câu văn hướng dẫn (`*_tip_*`, `*_help_*`, `*_description`) có bị outdated do hướng dẫn thao tác vừa bị gỡ hay không [CC-09].
    - Bảo vệ Binding: Đảm bảo không xóa hàm nếu vẫn còn nơi khác gọi đến.
  - **Review The Test (Test Assertion Intent Audit)**: Khi PR có sửa đổi hoặc thêm mới test (`spec/`, `test/`), không chỉ kiểm tra test pass hay fail, mà phải soi ngữ nghĩa của dữ liệu mock: *"Dữ liệu mock/factory trong test (ví dụ ngày tháng `future_date`, giá trị biên) có phản ánh đúng thực tế nghiệp vụ không? Test có đang cố tình `expect` một kết quả sai lệch để hợp pháp hóa bug logic trong code không?"*

* **Subagent #2 (Quét Lỗi Logic, Bugs Sơ Bộ & Temporal Invariants - Shallow Bug & Temporal Audit)**:
  - Đọc diff của PR và quét nhanh các lỗi logic, bug tiềm ẩn lớn (N+1 query, race condition, broken action bindings). Bỏ qua các vấn đề nhỏ nhặt (nitpicks), ưu tiên các lỗi có nguy cơ gây bug ở runtime.
  - **Checklist Temporal & Domain Invariants**: Đối với mọi query hoặc tính toán liên quan đến thời gian (`Date`, `Time`, `created_at`, `effective_from`, `period_start`, `period_end`):
    - Phép so sánh/fallback thời gian có bị **lệch chiều** không (ví dụ: lấy benchmark/dữ liệu TƯƠNG LAI áp cho kỳ QUÁ KHỨ)?
    - Dữ liệu fallback có bị thiếu giới hạn trên/dưới (`<= Date.current` hoặc `<= period_end`) hay không?

* **Subagent #3 (Phân Tích Lịch Sử Commit & Git Blame - Historical Context)**:
  - Kiểm tra `git blame` và lịch sử commit của các đoạn code bị sửa đổi để phát hiện nguy cơ phá vỡ logic cũ hoặc tái diễn bug cũ trong lịch sử.

* **Subagent #4 (Rà Soát Thảo Luận Trên các PR Cũ - Past PR Context)**:
  - Đọc các PR trước đây từng can thiệp vào các file này, kiểm tra các comment lưu ý cũ xem có áp dụng cho PR hiện tại không.

* **Subagent #5 (Tuân Thủ Comment & Đồng Bộ YARD Docstrings - Code Comments & Docstrings Compliance)**:
  - Đọc các comment/docstrings sẵn có trong các file bị sửa đổi và đảm bảo code mới viết tuân thủ đúng chỉ dẫn trong comment đó.
  - Kiểm tra tính nhất quán hai chiều giữa **Public Docstrings** (`@raise`, `@return`, `@param` ở public method/class) và **Private Implementation**: Nếu private method thay đổi ngoại lệ hoặc điều kiện trả về, public method docstring BẮT BUỘC phải được cập nhật đồng bộ, không được để mâu thuẫn.

* **Subagent #6 (MỚI - Quét Tác Động Xuyên File & Khối Gọi Lên - Cross-File Caller & Unreachable Code Tracer)**:
  - Khi một Service, Model, Helper hoặc Utility bị thay đổi chữ ký (signature), thay đổi danh sách ngoại lệ ném ra (`raise`), hoặc thay đổi điều kiện trả về (như thêm fallback):
  - **BẮT BUỘC dùng công cụ tìm kiếm code (`grep_search`) quét toàn bộ codebase** để tìm tất cả các vị trí gọi (callsites: Controllers, Jobs, Mailers, Rake tasks, Services khác).
  - Phân tích xem các khối `rescue`, `case/when`, `if/else` hoặc giả định tại các file caller có bị trở thành **Mã chết (Unreachable Code)** hoặc **Nuốt lỗi thầm lặng (Silent Failure)** hay không.

---

### 5. Chấm Điểm Độ Tin Cậy Để Lọc Nhiễu (Model: `flash`)
Đối với **mỗi vấn đề** tìm thấy ở Bước 4, kích hoạt một subagent song song (`Model: 'flash'`) nhận ngữ cảnh (mô tả lỗi, PR diff, danh sách file quy tắc) và chấm điểm độ tin cậy trên thang **0 - 100** nhằm loại bỏ cảnh báo giả (False Positives):

* **0**: Hoàn toàn không tin cậy. Là cảnh báo giả hoặc lỗi đã tồn tại từ trước khi tạo PR.
* **25**: Ít tin cậy. Có thể là lỗi nhưng chưa xác minh được, hoặc là vấn đề phong cách code không được quy định trong quy tắc.
* **50**: Tin cậy trung bình. Lỗi có thực nhưng ít khả năng xảy ra trong thực tế, hoặc chỉ là nitpick nhỏ.
* **75**: Độ tin cậy cao. Đã xác minh lỗi rất dễ xảy ra trong thực tế, hoặc vi phạm trực tiếp quy tắc trong `storage/rules/` / `AGENTS.md`.
* **100**: Chắc chắn 100%. Lỗi logic/bảo mật nghiêm trọng chắc chắn xảy ra thường xuyên khi chạy ứng dụng.

⚡ **Cơ Chế Điểm Thưởng Ưu Tiên (+15 đến +20 điểm)**:
Tự động cộng thêm điểm tin cậy cho các phát hiện thuộc nhóm:
1. **Unreachable Error Handling / Rescue**: Khối `rescue`/`catch` ở upstream caller bị vô hiệu hóa hoặc biến thành unreachable code do thay đổi trong downstream service.
2. **Temporal Invariant Violation**: Dữ liệu/benchmark tương lai bị lọt vào tính toán cho kỳ quá khứ do thiếu ràng buộc thời gian.
3. **Public vs Private Docstring Inconsistency**: Thẻ docstring `@raise`/`@return` của API public mâu thuẫn trực tiếp với logic thực tế bên dưới.

---

### 6. Lọc Nhiễu & Phân Loại MUST / IMO / NITS
1. **Lọc loại bỏ**: Loại bỏ tất cả các phát hiện có điểm tin cậy **< 80**.
2. **Dừng lại nếu sạch lỗi**: Nếu không còn phát hiện nào đạt điểm >= 80 -> **Dừng lại** (hoặc báo cáo PR sạch lỗi).
3. **Phân loại vấn đề giữ lại**:
   * 🔴 **MUST (Bắt buộc sửa)**: Điểm tin cậy 85–100. Các lỗi logic nghiêm trọng, nguy cơ bảo mật, hỏng chức năng, vi phạm temporal invariants, hoặc vi phạm quy tắc dự án được ghi rõ trong `storage/rules/`.
   * 🟡 **IMO (In My Opinion - Ý kiến đóng góp)**: Điểm tin cậy 80–84. Các đề xuất cải tiến kiến trúc, tối ưu hiệu năng, giảm độ phức tạp mà không làm hỏng app.
   * 🟢 **NITS (Góp ý nhỏ)**: Các nits nhỏ đạt điểm tin cậy >= 80 liên quan đến docstring/naming.

---

### 7. Tái Kiểm Tra Điều Kiện (Model: `flash`)
Trước khi đăng nhận xét, dùng subagent check lại trạng thái PR ở Bước 1 để đảm bảo PR vẫn đang mở và đủ điều kiện nhận review.

---

### 8. Đăng Báo Cáo Kết Quả Lên GitHub PR (`gh pr comment`)
Sử dụng lệnh `gh` đăng comment lên PR với định dạng chuẩn như sau:

#### 📌 Mẫu Báo Cáo Khi Tìm Thấy Lỗi:

```markdown
### 🔍 Báo cáo Đánh giá Mã nguồn (Code Review)

Đã rà soát và phát hiện **[Số lượng]** vấn đề cần lưu ý:

#### 🔴 MUST (Bắt buộc sửa)
1. **[Tóm tắt ngắn gọn lỗi]** *(Độ tin cậy: 95/100)*
   - **Chi tiết**: Mô tả lỗi và nguyên nhân... (Quy tắc liên quan: `storage/rules/security_guidelines.md`)
   - **Vị trí**: https://github.com/OWNER/REPO/blob/COMMIT_SHA/PATH/TO/FILE.rb#L10-L15

#### 🟡 IMO (Ý kiến đóng góp)
2. **[Tóm tắt ngắn gọn đề xuất]** *(Độ tin cậy: 80/100)*
   - **Chi tiết**: Đề xuất cải tiến...
   - **Vị trí**: https://github.com/OWNER/REPO/blob/COMMIT_SHA/PATH/TO/FILE.rb#L40-L45

---
🤖 Generated by Antigravity AI Code Reviewer
<sub>- Nếu nhận xét này hữu ích, vui lòng thả cảm xúc 👍. Nêu chưa hài lòng, hãy phản hồi 👎.</sub>
```

#### 📌 Mẫu Báo Cáo Khi Không Có Lỗi (< 80 điểm):

```markdown
### 🔍 Báo cáo Đánh giá Mã nguồn (Code Review)

✅ **Không phát hiện lỗi đáng quan ngại.** Codebase tuân thủ tốt các quy tắc kiến trúc và không có bug logic lớn.

---
🤖 Generated by Antigravity AI Code Reviewer
```

---

## ⛔ NHỮNG TRƯỜNG HỢP CẢNH BÁO GIẢ (FALSE POSITIVES NÊN TRÁNH)

Khi chấm điểm ở Bước 5, các subagent cần loại bỏ (cho điểm thấp):
* Lỗi đã tồn tại từ trước trong codebase (Pre-existing issues).
* Lỗi mà linter, typechecker hoặc compiler sẽ bắt được (RuboCop, TypeScript, RSpec...) - giả định CI sẽ tự chạy.
* Thay đổi về hành vi nhưng là cố ý và phù hợp với yêu cầu tính năng.
* Lỗi nằm ở dòng code mà tác giả PR **không sửa đổi**.
* Các bắt bẻ hình thức (pedantic nitpicks) mà Senior Engineer không bắt lỗi trên PR.

⚠️ **LƯU Ý NGOẠI LỆ (KHÔNG BỎ QUA):** Thay đổi hành vi làm vô hiệu hóa khối error handling/rescue ở upstream caller hoặc vi phạm logic thời gian (temporal invariant) **KHÔNG ĐƯỢC COI LÀ CẢNH BÁO GIẢ**. Đây là lỗi logic kiến trúc thực sự cần được báo cáo.

---

## 📌 QUY TRẮC ĐỊNH DẠNG LINK GITHUB CODE

Khi chèn link code trong comment review:
1. Phải dùng **Full Commit SHA** (Ví dụ: `https://github.com/owner/repo/blob/1d54823877c4de72b2316a64032a54afc404e619/app/models/user.rb#L10-L15`). Tuyệt đối không dùng biến bash hay relative path.
2. Tên repo phải khớp chính xác với repo đang review.
3. Ký tự `#` đứng liền sau tên file, dòng bắt đầu và kết thúc dạng `L[start]-L[end]`.
4. Bao gồm ít nhất 1 dòng ngữ cảnh trước và sau dòng bị lỗi (ví dụ: dòng lỗi là L5-L6 -> đặt link `#L4-L7`).
