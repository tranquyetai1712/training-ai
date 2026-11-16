---
name: q-kiem-tra-lan-cuoi-truoc-khi-tao-pull-request
description: "Gate kiểm tra chất lượng mã nguồn lần cuối trước khi tạo Pull Request. Tự động quét dead code, naming, comment, Rubocop, RSpec, Security, Brakeman, Performance, HTML Tag Balance, Pagination Guard và PR Description — xuất 1 báo cáo artifact markdown duy nhất."
---

# 🚦 Gate Kiểm Tra Lần Cuối Trước Khi Tạo Pull Request

Đây là **bước gate bắt buộc cuối cùng** trước khi tạo PR. Mục tiêu: phát hiện mọi vấn đề còn sót lại trong code đã thay đổi và xuất 1 báo cáo tổng hợp duy nhất.

> **Không bỏ qua bước nào.** Mỗi mục phải được kiểm tra và có kết quả rõ ràng trong báo cáo.

---

## ⚡ QUY TRÌNH THỰC THI (Tự Động)

Thực thi tuần tự theo 10 bước sau. Sau khi hoàn tất tất cả, tổng hợp kết quả vào **1 artifact markdown duy nhất**.

---

### 📌 Bước 0: Xác định phạm vi thay đổi

Trước khi bắt đầu, lấy danh sách file đã thay đổi so với nhánh gốc (thường là `main` hoặc `develop`):

```bash
# Lấy danh sách file thay đổi trong branch hiện tại
git diff --name-only origin/main...HEAD

# Xem nội dung diff chi tiết để phân tích
git diff origin/main...HEAD
```

> Chỉ kiểm tra **các file đã thay đổi trong branch**, không kiểm tra toàn bộ codebase.

---

### 🪦 Bước 1: Dead Code (Quy Trình Rà Soát 2 Chiều)

**Mục tiêu**: Phát hiện triệt để code không còn được sử dụng (bao gồm cả code mới thừa và code cũ bị mồ côi khi xóa/sửa HTML, JS, CSS, Ruby, YML).

**Phạm vi file quét**: Quét trên TẤT CẢ các định dạng file (`.rb`, `.erb`, `.haml`, `.slim`, `.js`, `.ts`, `.jsx`, `.tsx`, `.vue`, `.scss`, `.css`, `.yml`). TUYỆT ĐỐI không giới hạn chỉ quét trong file `*.rb`.

```bash
# Cấu trúc grep quét đa định dạng file:
grep -rn "search_term" app/ config/ spec/ --include="*.{rb,erb,haml,slim,js,ts,jsx,tsx,vue,scss,css,yml}"
```

**Thực thi theo 2 chiều (2-Way Audit)**:

#### 🅰️ Hướng 1: Quét Code Mới Thêm (Forward Scan)
Đọc các dòng **thêm mới** (`+`) trong `git diff`:
1. **Ruby Backend**: Method/Class/Constant/Interaction/Route mới $\rightarrow$ Grep xem có ít nhất 1 nơi gọi trong `app/`, `config/`, `spec/`.
2. **HTML / Templates**: Partial mới (`_form.html.erb`), Component mới $\rightarrow$ Grep xem có nơi `render` / `import` không.
3. **JS / TS / Stimulus**:
   - **BẮT BUỘC ĐỐI SOÁT 1:1 STIMULUS TARGETS, VALUES & METHODS**:
     Trích xuất **tất cả** phần tử trong `static targets = [...]`, `static values = { ... }` và **các class methods** của các file `.js` mới/sửa, chạy lệnh đối soát 1:1 với `app/views/` và `app/javascript/`:
     ```bash
     # 1. Quét Unused Stimulus Targets
     for target in $(grep -oP 'static targets = \[\K[^\]]+' $(git diff --name-only origin/main...HEAD | grep '\.js$') 2>/dev/null | tr -d '",' | tr ' ' '\n'); do
       [ -z "$target" ] && continue
       count=$(grep -rn --include="*.erb" --include="*.html" --include="*.haml" "$target" app/views/ | wc -l)
       if [ "$count" -eq 0 ]; then
         echo "❌ DEAD CODE - UNUSED STIMULUS TARGET: $target (Khai báo trong JS nhưng không có nơi dùng trong app/views/)"
       fi
     done

     # 2. Quét Unused Stimulus Methods (Khai báo method trong Controller nhưng không được gọi trong JS và không có data-action nào trong views)
     for js_file in $(git diff --name-only origin/main...HEAD | grep '\.js$'); do
       [ -f "$js_file" ] || continue
       methods=$(grep -oP '^\s*(async\s+)?\K[a-zA-Z0-9_]+(?=\s*\([^)]*\)\s*\{)' "$js_file" | grep -vE '^(if|else|for|while|switch|catch|connect|disconnect|initialize|constructor)$')
       for method in $methods; do
         [ -z "$method" ] && continue
         view_count=$(grep -rn --include="*.erb" --include="*.html" --include="*.haml" -P "#${method}\b" app/views/ | wc -l)
         js_count=$(grep -rn --include="*.js" --include="*.ts" -P "(this\.${method}\b|#${method}\b)" app/javascript/ | wc -l)
         if [ "$((view_count + js_count))" -eq 0 ]; then
           echo "❌ DEAD CODE - UNUSED STIMULUS METHOD: $method in $js_file (Method được khai báo nhưng không có nơi dùng trong JS và không có data-action nào trong views)"
         fi
       done
     done
     ```
   - Function, Exported module $\rightarrow$ Grep xem có nơi call hoặc import trong JS/TS khác không.
4. **CSS / SCSS**: Class/ID selector mới $\rightarrow$ Grep xem có xuất hiện trong HTML/ERB/JS không.
5. **I18n Locales**: Translation Key mới trong `config/locales/*.yml` $\rightarrow$ Grep xem có gọi qua `t(...)` / `I18n.t(...)` không.

#### 🅱️ Hướng 2: Quét Code Mồ Côi Do Xóa/Sửa (Reverse Scan)
Đọc các dòng **bị xóa** (`-`) hoặc **bị sửa** trong `git diff`:
1. **Khi xóa/sửa thẻ HTML / ERB**:
   - BẮT BUỘC kiểm tra các Stimulus Action (`data-action="...#methodName"`) vừa bị gỡ khỏi View. Tự động quét xem `methodName` trong Stimulus Controller tương ứng có trở thành mồ côi (dead code) hay không:
     ```bash
     for removed_action in $(git diff origin/main...HEAD | grep -E '^\-[^-]' | grep -oP '#[a-zA-Z0-9_]+' | tr -d '#' | sort -u 2>/dev/null); do
       [ -z "$removed_action" ] && continue
       view_count=$(grep -rn --include="*.erb" --include="*.html" --include="*.haml" -P "#${removed_action}\b" app/views/ | wc -l)
       js_count=$(grep -rn --include="*.js" --include="*.ts" -P "(this\.${removed_action}\b|#${removed_action}\b)" app/javascript/ | wc -l)
       if [ "$((view_count + js_count))" -eq 0 ]; then
         echo "❌ DEAD CODE - ORPHANED STIMULUS METHOD: $removed_action (Action data-action=\"...#$removed_action\" vừa bị xóa khỏi Views khiến method $removed_action trong JS Controller thành mồ côi!)"
       fi
     done
     ```
   - Helper, Partial, CSS Class, hoặc I18n Key bị mồ côi do xóa HTML.
2. **Khi xóa/sửa Javascript / TypeScript**: Route/Controller action, JS Helper mồ côi.
3. **Khi xóa/sửa Ruby Code**: View file, JS data attribute, hay Translation Key mồ côi.

#### 🔤 Hướng 3: Quét Bất Đồng Bộ Ngữ Nghĩa giữa UI và Văn Bản Hướng Dẫn Locale (UI-Locale Semantic Consistency) [CC-09]
- **Khi gỡ bỏ nút/action/tính năng khỏi HTML/ERB**:
  - BẮT BUỘC rà soát các văn bản hướng dẫn (`*_tip_*`, `*_help_*`, `*_description`, `*_instructions`) trong `config/locales/` thuộc trang đó ở cả 3 ngôn ngữ (`en`, `ja`, `vi`).
  - Kiểm tra xem nội dung văn bản hướng dẫn có còn chứa các từ ngữ nhắc đến tính năng vừa bị gỡ khỏi UI hay không (ví dụ "or search", "や検索", "hoặc tìm kiếm").
  - NẾU CÓ, báo lỗi **`❌ I18N SEMANTIC DESYNCHRONIZATION [CC-09]`** yêu cầu cập nhật lại đồng bộ tất cả các tệp locale.

---

### 🏷️ Bước 2: Kiểm Tra Tên (Naming)

- Method: Động từ hoặc cụm động từ (`process_payment`).
- Variable/Attribute: Danh từ (`user_count`).
- Boolean: Prefix `is_`, `has_`, `can_`, `should_` hoặc suffix `?` trong Ruby.
- Không dùng từ viết tắt khó hiểu (`tmp`, `mgr`, `val`, `res`).

---

### 💬 Bước 3: Kiểm Tra Comment

```bash
# Tìm code đang bị comment-out
grep -n "^[[:space:]]*#[[:space:]]*[a-z]" <file_changed>
```
- Không có code bị comment-out (`# old_method(...)`).
- Comment giải thích "tại sao" (why), không giải thích "làm gì" (what).

---

### 🧱 Bước 4: Kiểm Tra Cấu Trúc HTML / ERB (HTML Tag Balance Check)

**Mục tiêu**: Đảm bảo các file View `.erb`/`.html` bị chỉnh sửa không bị mất thẻ đóng (`</div>`, `</form>`, `</table>`), làm vỡ layout giao diện.

```bash
# Tự động đếm cân bằng thẻ <div> trong các file ERB thay đổi:
for file in $(git diff --name-only origin/main...HEAD | grep '\.erb$'); do
  [ -f "$file" ] || continue
  open_divs=$(grep -o '<div' "$file" | wc -l)
  close_divs=$(grep -o '</div>' "$file" | wc -l)
  if [ "$open_divs" -ne "$close_divs" ]; then
    echo "❌ MARKUP ERROR: File $file bị lệch thẻ div (Mở <div: $open_divs, Đóng </div>: $close_divs)"
  fi
done
```

---

### 🔧 Bước 5: Rubocop

```bash
git diff --name-only origin/main...HEAD | grep "\.rb$" | xargs docker compose exec -T web bundle exec rubocop -f github
```
**Kết quả mong đợi**: `0 offenses detected`.

---

### 🧪 Bước 6: RSpec & Multi-Page Rigor Test Guard

**Mục tiêu**: 
1. 100% test liên quan pass.
2. **Rigor Test Guard cho Phân Trang**: Nếu PR có tính năng phân trang (`pagy` / `limit` / `offset`), BẮT BUỘC phải có test case cho:
   - Trang 1 (`page=1`).
   - Trang 2 (`page=2`) $\rightarrow$ Khẳng định các bản ghi trang 2 khác trang 1, không duplicate/lost.
   - Helper sinh URL phân trang với query parameters.

```bash
docker compose exec -T web bundle exec rspec spec/path/to/changed_spec.rb --format documentation
```

---

### 🔒 Bước 7: Security Checklist & URL Parameter Allowlisting

- **SQL Injection**: No string interpolation in `where`/`order`. Dynamic sort columns must be whitelisted.
- **XSS**: No `.html_safe`/`raw` on unescaped user input.
- **Open Redirect / URL Sanitization**: `pagination_url_for` hoặc helper sinh URL **KHÔNG ĐƯỢC** dùng `request.query_parameters` thô. BẮT BUỘC phải qua allowlist (ví dụ `slice(:q, :sort, :month, :tab)`).
- **IDOR & Mass Assignment**: Scope qua current user / Strong params `.permit(...)`.

---

### 🛡️ Bước 8: Brakeman (Static Security Scan)

```bash
docker compose exec -T web bundle exec brakeman --no-pager -q || true
```

---

### ⚡ Bước 9: Performance & Pagination Rules Audit (RR-49 Compliance)

**Checklist Bắt Buộc Đối Với PR Có Phân Trang (RR-49 Compliance)**:
- [ ] **[RR-49 / PAG-01] Explicit Deterministic Order**: mọi query `pagy(...)` BẮT BUỘC phải có `.order(...)` và kết thúc bằng tie-break `.order(:id)` (tránh nhảy vị trí trên Postgres SQL).
- [ ] **[RR-49 / PAG-02] Pre-Pagination Aggregations**: mọi phép tính tổng (totals, badge count, footer summary) BẮT BUỘC được tính toán trên Full Relation TRƯỚC KHI gọi `pagy(relation)`.
- [ ] **[RR-49 / PAG-04] Native Gem API**: Sử dụng API chuẩn `pagy.series`, không tự viết lại logic window thủ công. Gem mới được pin version operator (`gem 'pagy', '~> 43.4'`).
- [ ] N+1 Query: Sử dụng `includes`, `preload`, `eager_load` đúng chỗ.

---

### 🖼️ Bước 10: Kiểm Tra & Đồng Bộ Mô Tả Pull Request (PR Description 2-Way & Scope Verification)

**Mục tiêu**: Đảm bảo nội dung mô tả Pull Request (PR body) hiện tại trên GitHub phản ánh chính xác các thay đổi mới (`git diff`), không chứa thông tin khẳng định sai lệch (False Claims), và bao phủ đầy đủ kịch bản kiểm thử End-to-End theo yêu cầu Ticket.

```bash
PR_INFO=$(gh pr view --json number,title,body,baseRefName 2>/dev/null)
```

#### 🅰️ Pillar 1: Purpose Alignment Check (Kiểm tra sự phù hợp Mục đích)
- Rà soát phần `## Changes` / `## Summary` trong PR Body. Đảm bảo mô tả rõ ràng mục đích của PR và tóm tắt khái quát các mảng thay đổi chính bằng ngôn ngữ tự nhiên (không yêu cầu liệt kê danh sách file hay trùng khớp 100% tên file).

#### 🅱️ Pillar 2: Reverse Check (Kiểm tra Nghịch - Chống False Claims)
- Bóc tách toàn bộ Class Name (`Kpi::Criteria::Base`), Module Name, và File Path xuất hiện trong các câu khẳng định sửa đổi (`## Summary`, `## Key Changes`), ngoại trừ khối code mẫu trong `## How to Test`.
- Kiểm tra đối soát trực tiếp với `git diff origin/main...HEAD`:
  - NẾU PR Body khẳng định "Guarded/Fixed/Refactored Class $X$", nhưng `git diff` **không hề chạm vào file source của Class $X$** (do logic đã có sẵn trên `main` hoặc ghi nhầm), BẮT BUỘC báo lỗi:  
    `🔴 [blocking] PR Description Mismatch: Khẳng định sửa Class '$X' nhưng git diff không hề có file này!`
  - Tự động chạy `gh pr edit <PR_NUMBER> --body "..."` để loại bỏ/sửa lại thông tin sai lệch trước khi cấp chứng nhận PASS (bảo toàn 100% phần `## Screenshots` / ảnh demo, link JIRA, và checklist).

#### 🆂 Pillar 3: E2E Test Scope Check (Kiểm tra bao phủ luồng Test)
- Đọc mô tả vấn đề/lỗi trong Ticket Jira (ví dụ "crash HTTP 500 khi xuất Excel hoặc xem Web UI Dashboard").
- So sánh với mục `## How to Test` trong PR Body:
  - NẾU Ticket đề cập đến trải nghiệm người dùng trên Web UI / Export Excel, nhưng `How to Test` chỉ ghi test `Rails Console` / `RSpec` $\rightarrow$ Đánh dấu:  
    `⚠️ WARNING: How to Test thiếu kịch bản E2E (Web UI / Export Excel) theo Ticket AC`
  - Tự động bổ sung mục **`### End-to-End / Web UI & Export Test`** với các bước thao tác thực tế trên trình duyệt vào PR Body.

---

### 🔁 Bước 11: Recurring Review Patterns — 7 Quy Tắc Trừu Tượng Chống Lặp Lỗi (RR-01 → RR-07)

> **Nguồn gốc**: Phân tích 55 PRs trong 3 tháng (halo_web, quyetchasqui) cho thấy các nhóm lỗi lặp đi lặp lại qua nhiều tuần. 7 quy tắc dưới đây được viết ở **cấp độ nguyên lý (principle-level)** để bắt trọn **gia đình lỗi tương tự**, bất kể ngôn ngữ hay loại file.
>
> **Phạm vi quét**: Tất cả file đã thay đổi trong diff: `.rb`, `.js`, `.ts`, `.erb`, `.haml`, `.slim`, `.yml`, `.css`, `.scss`, `Dockerfile`, `docker-compose*.yml`.

---

#### 🔢 RR-01: Giá Trị Literal Trong Logic Nghiệp Vụ (Literal Values in Business Logic)

**Nguyên lý**: Bất kỳ giá trị số (`42`, `10000`, `0.8`), thời lượng (`sleep 5`, `setTimeout(50)`, `wait: 30.seconds`, `timeout: 10000`), ngưỡng giới hạn (`limit: 3`, `max_retries: 5`, `batch_size: 500`), hoặc chuỗi cấu hình/URL (`"https://..."`, `"application/json"`) được viết **trực tiếp (hardcode) bên trong thân hàm/method/block** của logic nghiệp vụ — chứ không phải ở đầu module/class dưới dạng **Named Constant** hoặc trong file cấu hình — là vi phạm.

**Phạm vi áp dụng**: Ruby (`.rb`), JavaScript/TypeScript (`.js`, `.ts`), YAML config, Docker files, ERB templates.

**Cách quét**: Đọc từng dòng mới (`+`) trong `git diff`. Nếu dòng đó nằm trong thân method/function/block và chứa một giá trị literal (số, chuỗi cấu hình, duration) không thuộc một trong các ngoại lệ hợp lệ bên dưới → báo lỗi.

**Ngoại lệ hợp lệ (KHÔNG báo lỗi)**:
- Giá trị `0`, `1`, `-1`, `true`, `false`, `nil`, `null`, `""` (neutral/sentinel values).
- Giá trị nằm trong dòng khai báo hằng số (`TIMEOUT_MS = 10000`, `MAX_RETRIES = 5`, `freeze`).
- Giá trị nằm trong file config/initializer/seed/migration nơi bản chất là khai báo cấu hình.
- Giá trị trong RSpec/Test assertions (`expect(...).to eq(42)`).
- HTTP status codes chuẩn (`200`, `404`, `500`) khi dùng inline trong controller response.

**Ví dụ phát hiện**:
```
❌ RR-01 (Ruby):   sleep 5                      → Dùng const RETRY_DELAY_SECONDS = 5
❌ RR-01 (Ruby):   .limit(100)                   → Dùng const DEFAULT_PAGE_SIZE = 100
❌ RR-01 (JS):     setTimeout(callback, 50)      → Dùng const RENDER_DELAY_MS = 50
❌ RR-01 (JS):     timeout: 10000                → Dùng const GEOLOCATION_TIMEOUT_MS = 10000
❌ RR-01 (Ruby):   retry_count < 3               → Dùng const MAX_RETRY_ATTEMPTS = 3
❌ RR-01 (Docker): --workers 4                   → Dùng biến ENV hoặc ARG
```

---

#### 🔇 RR-02: Thất Bại Im Lặng & Che Giấu Thông Tin (Silent Failure & Information Hiding)

**Nguyên lý**: Bất kỳ đoạn code nào **triệt tiêu, nuốt, hoặc làm mờ** một lỗi/exception/trạng thái bất thường mà **không phát ra tín hiệu có thể quan sát được** (observable signal: log level ≥ `warn`, metric, user notification, `raise`/`throw`) → BẮT BUỘC xem xét và có lý do chính đáng.

**Các mẫu vi phạm (bao gồm nhưng không giới hạn)**:
- `rescue => nil` / `rescue StandardError` không ghi log hoặc re-raise.
- `return if x.nil?` trên biến nội bộ vốn **phải tồn tại** theo invariant của hàm (→ nên `raise ArgumentError` hoặc fail-fast).
- `catch(e) { }` hoặc `catch(e) { console.log(e) }` rồi tiếp tục chạy như không có gì.
- `Rails.logger.debug(...)` cho exception cần quan sát ở Production (debug level bị tắt trên prod → vô hình).
- Guard im lặng `return` trên trạng thái "không thể xảy ra" do bug nội bộ (thay vì fail-fast).
- Guard trùng lặp ở nhiều hàm liền kề cùng điều kiện (dấu hiệu che giấu root cause).
- `rescue` rộng rồi fallback giá trị mặc định mà **không ghi log nguyên nhân** → hệ thống chạy nhầm im lặng.

**Ngoại lệ hợp lệ**:
- Guard ở Boundary tiếp nhận dữ liệu không tin cậy (HTTP params, External API response, User input, localStorage).
- Prototype/tool nội bộ với scope cực nhỏ có ghi rõ TODO follow-up.
- `discard_on` trong ActiveJob cho lỗi không thể phục hồi (đã có hệ thống giám sát job failures).

**Câu hỏi tự kiểm tra**: Nếu guard/rescue/catch này kích hoạt trên Production, team có biết ngay trong vòng 5 phút để điều tra không? Nếu **không** → vi phạm.

---

#### 📝 RR-03: Bất Đồng Bộ Giữa Tuyên Bố và Triển Khai (Declaration ≠ Implementation)

**Nguyên lý**: Bất kỳ **tuyên bố** (PR Description, code comment, tên biến/method, spec ticket, README) mà **không phản ánh chính xác** những gì code thực tế đang làm → BẮT BUỘC phát hiện và yêu cầu đồng bộ.

**Các mẫu vi phạm (bao gồm nhưng không giới hạn)**:
- **PR Description ↔ Code**: Mô tả ghi dùng giải pháp A (ví dụ: `touch: true` trên `belongs_to`) nhưng code triển khai giải pháp B (`after_save :touch_tag`).
- **PR Description ↔ Scope**: Mô tả ghi tính năng chạy toàn hệ thống nhưng code bọc guard môi trường (`Rails.env.development?`).
- **Comment ↔ Code**: Comment giải thích logic cũ không còn đúng sau khi refactor.
- **Tên biến/method ↔ Hành vi**: Method tên `validate_and_save!` nhưng thực tế chỉ validate mà không save.
- **Spec Ticket ↔ Implementation**: Ticket AC yêu cầu "preload 2 rows, cancel on fast scroll" nhưng code không implement 2 yêu cầu này.

**Cách quét**:
1. Lấy nội dung PR Body hiện tại (`gh pr view --json body`).
2. Bóc tách mọi khẳng định sửa đổi (class name, method name, behavior description) trong PR Body.
3. Đối chiếu từng khẳng định với `git diff origin/main...HEAD`: nếu diff không chạm vào file/class/method được claim → `🔴 [blocking] RR-03: Declaration ≠ Implementation`.
4. Kiểm tra mọi comment trong diff: comment mô tả logic cũ mà code bên dưới đã thay đổi → `⚠️ RR-03: Stale comment`.

---

#### 🧪 RR-04: Hợp Đồng Hành Vi Không Có Kiểm Chứng (Uncovered Behavioral Contracts)

**Nguyên lý**: Bất kỳ **hợp đồng hành vi mới** (new behavioral contract) — bao gồm Model mới, association, validation, scope, sort order, API endpoint, callback, state transition — mà **không có automated test tương ứng** kiểm chứng hành vi đó → BẮT BUỘC bổ sung.

**Các mẫu vi phạm (bao gồm nhưng không giới hạn)**:
- Tạo Model/Schema mới (`Tag`, `FaceTag`) mà **không có file spec** tại `spec/models/`.
- Thêm scope sort theo nhiều tiêu chí (`updated_at DESC, created_at DESC`) nhưng test chỉ verify tiêu chí chính, **thiếu test tiebreaker** khi tiêu chí chính trùng nhau.
- Thêm `belongs_to :tag, dependent: :destroy` nhưng **không test** cascade destroy hoạt động đúng.
- Thêm `uniqueness` validation nhưng **không test** DB constraint khi bypass ActiveRecord (`insert_all`, `update_column`).
- Thêm tính năng/logic mới nằm ngoài scope PR ban đầu nhưng **không viết test đi kèm**.
- Ticket spec yêu cầu N kịch bản UX nhưng test chỉ cover < N kịch bản.

**Cách quét**:
1. Đọc diff: tìm mọi file `db/migrate/`, `app/models/`, `app/interactions/`, `app/controllers/` mới hoặc sửa.
2. Với mỗi hành vi mới (validation, scope, association, method, endpoint), kiểm tra xem trong diff hoặc trong codebase có test tương ứng không.
3. Nếu **không** → `❌ RR-04: Behavioral contract without test coverage`.

---

#### 🔄 RR-05: Logic Trùng Lặp Thiếu Trừu Tượng Chia Sẻ (Duplicated Logic Without Shared Abstraction)

**Nguyên lý**: Bất kỳ **mẫu logic** (pattern) nào xuất hiện **≥ 2 nơi** trong codebase mà không được trích xuất thành helper/utility/concern/component chia sẻ → vi phạm DRY và cần đánh giá refactor.

**Các mẫu vi phạm (bao gồm nhưng không giới hạn)**:
- Cùng khối `try { await response.json() } catch(e) { ... }` lặp lại ở 3+ file JS controllers.
- Cùng đoạn CSS/Tailwind utility class pattern copy-paste qua nhiều views.
- Cùng khối Ruby code xử lý error response/rescue lặp lại ở nhiều Interaction/Service.
- Cùng cấu trúc query/scope Ruby lặp lại ở nhiều controllers thay vì đặt trong Model scope.

**Cách quét**:
1. Đọc các dòng mới (`+`) trong diff.
2. Với mỗi block code ≥ 3 dòng liên tiếp, tìm kiếm trong codebase xem block tương tự đã tồn tại ở nơi khác chưa.
3. Nếu **có** → `⚠️ RR-05: Duplicated logic — consider extracting to shared helper/utility`.

---

#### 🌐 RR-06: Thay Đổi Cục Bộ Gây Tác Động Toàn Cục (Local Change, Global Side Effect)

**Nguyên lý**: Bất kỳ thay đổi nào **có ý định phục vụ một trang/controller/feature cụ thể** nhưng **vô tình ảnh hưởng** đến toàn bộ hệ thống hoặc các trang/feature không liên quan → BẮT BUỘC phát hiện và cô lập.

**Các mẫu vi phạm (bao gồm nhưng không giới hạn)**:
- Sửa CSS class/selector ở file stylesheet toàn cục → vỡ layout ở các trang Admin/khác.
- Thêm initializer/monkey-patch chạy ở **tất cả môi trường** mà không có guard `Rails.env.development?` hoặc `Rails.env.production?` khi chỉ cần chạy ở một môi trường.
- Sửa migration/index trên bảng chung → ảnh hưởng write performance toàn bảng.
- Sửa `ApplicationController` / `application.html.erb` cho một feature cụ thể → ảnh hưởng mọi trang.
- Thêm `before_action` / `after_action` ở parent controller mà chỉ cần cho child controller.

**Cách quét**:
1. Kiểm tra xem diff có chạm vào các file "toàn cục" không: `application_controller.rb`, `application.html.erb`, `application.css`, `config/initializers/`, `config/routes.rb` (root level), stylesheet chung, shared partial.
2. Nếu **có** và purpose chỉ phục vụ một feature/page cụ thể → `⚠️ RR-06: Local intent, global impact — consider scoping`.

---

#### 🌍 RR-07: Nội Dung Người Dùng Nhìn Thấy Không Qua Hệ Thống Dịch (User-Facing Content Bypassing i18n)

**Nguyên lý**: Bất kỳ chuỗi văn bản nào mà **người dùng cuối có thể nhìn thấy** (trên UI, trong email, trong thông báo lỗi, trong flash message, trong JS alert/confirm/toast) mà **không được định tuyến qua hệ thống i18n** (`t()`, `I18n.t()`, Stimulus Values từ `data-*-value`) → BẮT BUỘC báo lỗi.

**Phạm vi quét**: ERB/HAML views, JavaScript/TypeScript controllers, Ruby controller flash messages, Mailer templates, ActiveInteraction error messages.

**Cách quét**:
```bash
# Quét chuỗi tiếng Anh/Việt/Nhật hardcode trong ERB views mới/sửa
for file in $(git diff --name-only origin/main...HEAD | grep -E '\.(erb|haml|slim)$'); do
  [ -f "$file" ] || continue
  # Tìm chuỗi literal trong thẻ HTML (không nằm trong <%= t(...) %> hoặc comment)
  grep -nP '(?<!<%=\s)(?<!#)\b[A-Z][a-z]+(?:\s[a-z]+){1,}' "$file" | grep -vP '(class=|id=|data-|href=|src=|<%|%>)' | head -20
done
```

**Ngoại lệ hợp lệ**:
- Nội dung kỹ thuật thuần túy: tên biến, class name, log message (không phải user-facing).
- Nội dung trong comment HTML / code comment.
- Nội dung trong file seed/migration/config không phải UI.

---

## 📊 ĐỊNH DẠNG BÁO CÁO ĐẦU RA

Tổng hợp kết quả vào **1 artifact markdown**:

```markdown
# 🚦 Báo Cáo Kiểm Tra Chất Lượng Trước PR

> **Branch**: `<tên branch>`
> **Ngày kiểm tra**: `<ngày giờ>`
> **Files thay đổi**: `<số lượng file>`

---

## Tổng Kết

| Mục Kiểm Tra | Kết Quả | Ghi Chú |
|---|---|---|
| 🪦 Dead Code | ✅ / ❌ | ... |
| 🏷️ Naming | ✅ / ❌ | ... |
| 💬 Comment | ✅ / ⚠️ / ❌ | ... |
| 🧱 HTML Tag Balance | ✅ / ❌ | `X files checked` |
| 🔧 Rubocop | ✅ / ❌ | `X offenses` |
| 🧪 RSpec & Rigor Guard | ✅ / ❌ | `X examples, Y failures` |
| 🔒 Security & URL Sanitization | ✅ / ❌ | ... |
| 🛡️ Brakeman | ✅ / ❌ | ... |
| ⚡ Performance & RR-49 Pagination | ✅ / ⚠️ / ❌ | `Deterministic order & Pre-aggregations checked` |
| 🖼️ PR Description | ✅ / ⚠️ / N/A | Matches git diff / Auto-updated (Preserved Screenshots) |
| 🔁 RR-01 Literal Values | ✅ / ⚠️ / ❌ | `X magic numbers found in Y files` |
| 🔁 RR-02 Silent Failure | ✅ / ⚠️ / ❌ | `X silent guards/rescues found` |
| 🔁 RR-03 Declaration ≠ Implementation | ✅ / ⚠️ / ❌ | `PR Body vs Diff alignment` |
| 🔁 RR-04 Uncovered Contracts | ✅ / ⚠️ / ❌ | `X new behaviors without tests` |
| 🔁 RR-05 Duplicated Logic | ✅ / ⚠️ / ❌ | `X duplicated patterns found` |
| 🔁 RR-06 Local→Global Side Effect | ✅ / ⚠️ / ❌ | `X global files modified for local purpose` |
| 🔁 RR-07 i18n Bypass | ✅ / ⚠️ / ❌ | `X hardcoded strings found in Y files` |

**🎯 Kết luận tổng thể**: ✅ PASS — Sẵn sàng tạo PR / ❌ FAIL — Cần sửa trước
```
