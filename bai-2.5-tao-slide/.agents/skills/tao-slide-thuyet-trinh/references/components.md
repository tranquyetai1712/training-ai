# THƯ VIỆN BỐ CỤC SLIDE CHUẨN (COMPONENTS REFERENCE)
## (Starter Kit Bài 2.5 - Khóa Học Antigravity AI)

Tài liệu này cung cấp **6 mẫu khối bố cục Lego chuẩn hóa** bằng mã nguồn HTML5/CSS, được thiết kế tương thích 100% với khung gầm động cơ `templates/engine.html`. 

---

## 📌 QUY TẮC CẤU TRÚC KHUNG BAO (WRAPPER SYNTAX)

Mỗi slide độc lập bên trong `engine.html` (tại vị trí token `{{SLIDES_CONTENT}}`) bắt buộc phải tuân theo cấu trúc thẻ bao chuẩn sau:

```html
<!-- Slide đầu tiên (Bắt buộc có class "active"): -->
<div class="slide active" data-slide="01" data-notes="Kịch bản lời thoại người nói cho slide 1...">
  <!-- Nội dung component của slide 1 -->
</div>

<!-- Các slide tiếp theo từ slide 2 trở đi (KHÔNG có class "active"): -->
<div class="slide" data-slide="02" data-notes="Kịch bản lời thoại người nói cho slide 2...">
  <!-- Nội dung component của slide 2 -->
</div>
```

### Các nguyên tắc cốt lõi:
1. **Quy tắc class `active`:** Duy nhất **Slide đầu tiên** (Slide 01) được gán class `class="slide active"`. Tất cả các slide từ số 02 trở đi chỉ mang `class="slide"`. Khi người dùng bấm phím chuyển slide, JavaScript của `engine.html` sẽ tự động chuyển class `active`.
2. **Thuộc tính `data-notes`:** Chứa toàn bộ kịch bản lời thoại của người thuyết trình.
   - Khi bấm phím <kbd>S</kbd>, ngăn kéo lời thoại (Speaker Notes Drawer) sẽ tự động mở ra và trích xuất nội dung từ thuộc tính này.
   - *Lưu ý về dấu nháy:* Trong giá trị của `data-notes="..."`, nếu muốn trích dẫn câu từ, hãy dùng dấu nháy đơn (`'`) hoặc thực thể HTML `&quot;` để tránh lỗi đóng sớm thuộc tính HTML.
3. **Cân bằng thẻ HTML:** Đảm bảo mọi thẻ mở `<div>`, `<section>`, `<ul>`, `<table>` đều có thẻ đóng `</div>`, `</section>`, `</ul>`, `</table>` tương ứng.

---

## 1. Component 1: Cover / Hero Slide (Tiêu Đề Lớn Gradient + Thực Trạng vs Mục Tiêu)

- **Mục đích sử dụng:** Dùng cho slide mở màn (Slide 01). Giới thiệu ấn tượng tên đề án/bài học, đặt ngay vấn đề nhức nhối hiện tại và giải pháp đột phá mục tiêu để gây tò mò cho khán giả.
- **Vị trí phù hợp:** Slide 01.

```html
<!-- COMPONENT 1: HERO COVER SLIDE -->
<div class="slide active" data-slide="01" data-notes="Chào mừng quý anh chị và các bạn đến với buổi thuyết trình hôm nay! Chúng ta đều biết quy trình làm báo cáo thủ công hiện nay đang ngốn tới 12 giờ làm việc mỗi tuần và tỷ lệ sai sót số liệu lên đến 15%. Hôm nay, tôi xin giới thiệu giải pháp tự động hóa toàn diện giúp cắt giảm 65% thời gian xử lý và nâng cao hiệu suất làm việc gấp 3 lần. Hãy cùng tôi khám phá chi tiết nhé!">
  <span class="slide-eyebrow eyebrow-indigo">⚡ KHỞI ĐỘNG DỰ ÁN</span>
  <h1 class="slide-title" style="font-size: 2.5rem; background: linear-gradient(135deg, #ffffff 40%, #818cf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
    TỰ ĐỘNG HÓA BÁO CÁO KINH DOANH VỚI AI
  </h1>
  <p class="slide-subtitle">
    Giải pháp chuyển đổi số thông minh giúp tối ưu hóa thời gian xử lý dữ liệu và gia tăng hiệu suất làm việc cho phòng ban
  </p>

  <div class="grid-2">
    <!-- Hộp Thực trạng / Nỗi đau hiện tại -->
    <div class="box-card">
      <span class="card-header-icon">⚠️</span>
      <h3 class="card-heading" style="color: #f87171;">Thực Trạng Hiện Nay</h3>
      <p class="card-desc">
        • Tốn 10 - 12 giờ/tuần để thu thập và đối soát số liệu từ 5 phần mềm rời rạc.<br>
        • Sai lệch dữ liệu phát sinh thường xuyên do nhập liệu thủ công bằng tay.<br>
        • Báo cáo thường xuyên nộp chậm hạn, ảnh hưởng đến quyết định của ban điều hành.
      </p>
    </div>

    <!-- Hộp Mục tiêu đột phá mới -->
    <div class="box-card box-card-highlight">
      <span class="card-header-icon">🚀</span>
      <h3 class="card-heading" style="color: #38bdf8;">Mục Tiêu Đột Phá Đề Xuất</h3>
      <p class="card-desc">
        • Tự động gom và hợp nhất dữ liệu đa kênh theo thời gian thực (Realtime).<br>
        • Cắt giảm 65% thời gian lập báo cáo, bàn giao số liệu chỉ trong 15 phút.<br>
        • Đảm bảo độ chính xác 99.9%, tự động cảnh báo số liệu bất thường bằng AI.
      </p>
    </div>
  </div>
</div>
```

---

## 2. Component 2: Split 2 Cột (So Sánh Cũ/Sai vs Mới/Chuẩn)

- **Mục đích sử dụng:** Đặt 2 phương pháp tiếp cận cạnh nhau để so sánh trực quan (Thủ công vs Tự động, Sai lầm phổ biến vs Chuẩn thực chiến).
- **Vị trí phù hợp:** Slide 02 hoặc 03.

```html
<!-- COMPONENT 2: SPLIT COMPARISON 2 CỘT -->
<div class="slide" data-slide="02" data-notes="Ở slide này, chúng ta cùng nhìn nhận thẳng thắn sự khác biệt giữa hai phương pháp. Cột bên trái là cách làm truyền thống: phân mảnh, phụ thuộc con người và cực kỳ căng thẳng mỗi kỳ báo cáo. Trong khi đó, cột bên phải là mô hình tự động hóa mới: luồng dữ liệu thông suốt, có kiểm tra chéo tự động và nhân sự có thể tập trung vào việc phân tích chiến lược thay vì copy paste dữ liệu.">
  <span class="slide-eyebrow eyebrow-rose">⚖️ ĐỐI CHIẾU THỰC TẾ</span>
  <h2 class="slide-title">So Sánh Phương Pháp Tiếp Cận</h2>
  <p class="slide-subtitle">
    Sự khác biệt căn bản giữa mô hình xử lý phân mảnh truyền thống và nền tảng dữ liệu tự động
  </p>

  <div class="grid-2">
    <!-- Cột Cách làm cũ / Sai lầm -->
    <div class="box-card" style="border-left: 4px solid #ef4444;">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
        <span class="card-header-icon" style="margin: 0;">❌</span>
        <span class="badge-pill pill-red">CÁCH CŨ / THỦ CÔNG</span>
      </div>
      <h3 class="card-heading">Quy Trình Thủ Công Rời Rạc</h3>
      <p class="card-desc">
        <strong>1. Nhập liệu lặp lại:</strong> Sao chép dữ liệu thủ công từ ERP sang các bảng tính Excel riêng lẻ.<br><br>
        <strong>2. Rủi ro sai lệch:</strong> Dễ nhầm lẫn công thức, trùng lặp dòng và không truy vết được lịch sử chỉnh sửa.<br><br>
        <strong>3. Lãng phí nhân lực:</strong> Nhân sự cấp cao bị chôn vùi vào thao tác kỹ thuật cơ bản thay vì phân tích thị trường.
      </p>
    </div>

    <!-- Cột Cách làm mới / Chuẩn hóa -->
    <div class="box-card box-card-highlight" style="border-left: 4px solid #10b981;">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
        <span class="card-header-icon" style="margin: 0;">✅</span>
        <span class="badge-pill pill-green">CÁCH MỚI / CHUẨN HÓA</span>
      </div>
      <h3 class="card-heading">Nền Tảng AI Tự Động Hóa</h3>
      <p class="card-desc">
        <strong>1. Đồng bộ luồng dữ liệu:</strong> Kết nối API trực tiếp, tự động làm sạch và hợp nhất dữ liệu trong 30 giây.<br><br>
        <strong>2. Kiểm tra chéo thông minh:</strong> AI tự động phát hiện số liệu ngoại lai và gắn cờ cảnh báo trước khi xuất báo cáo.<br><br>
        <strong>3. Giải phóng thời gian:</strong> Tiết kiệm hàng trăm giờ lao động mỗi tháng, chuyển trọng tâm sang tư vấn quyết định.
      </p>
    </div>
  </div>
</div>
```

---

## 3. Component 3: Grid 3 Cột (Quy Trình 3 Bước / 3 Trụ Cột)

- **Mục đích sử dụng:** Trình bày quy trình theo từng giai đoạn thời gian (Giai đoạn 1 ➔ 2 ➔ 3) hoặc 3 trụ cột chiến lược cốt lõi của đề xuất.
- **Vị trí phù hợp:** Slide 03 hoặc 04.

```html
<!-- COMPONENT 3: GRID 3 CỘT (QUY TRÌNH / TRỤ CỘT) -->
<div class="slide" data-slide="03" data-notes="Để hiện thực hóa mục tiêu trên, chúng tôi xây dựng lộ trình triển khai gồm 3 giai đoạn rõ ràng trong vòng 6 tuần. Giai đoạn 1 tập trung chuẩn hóa nguồn dữ liệu và thiết lập luồng kết nối API. Giai đoạn 2 là giai đoạn cốt lõi với việc huấn luyện mô hình AI và chạy thử nghiệm song song. Giai đoạn 3 sẽ hoàn tất chuyển giao, đào tạo nội bộ và đưa vào vận hành thực tế toàn công ty.">
  <span class="slide-eyebrow eyebrow-cyan">🔄 LỘ TRÌNH THỰC HIỆN</span>
  <h2 class="slide-title">Lộ Trình Triển Khai 3 Giai Đoạn</h2>
  <p class="slide-subtitle">
    Quy trình từng bước đảm bảo tính khả thi, an toàn dữ liệu và không làm gián đoạn vận hành
  </p>

  <div class="grid-3">
    <!-- Bước 1 -->
    <div class="box-card">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
        <span class="card-header-icon" style="margin: 0;">🔌</span>
        <span class="badge-pill pill-blue">BƯỚC 01</span>
      </div>
      <h3 class="card-heading">Chuẩn Hóa Dữ Liệu</h3>
      <p class="card-desc">
        • Rà soát cấu trúc cơ sở dữ liệu hiện hữu.<br>
        • Xây dựng đường ống kết nối API an toàn.<br>
        • Định hình danh mục chỉ số đo lường (KPI).<br>
        <em>Thời gian dự kiến: Tuần 1 - Tuần 2</em>
      </p>
    </div>

    <!-- Bước 2 -->
    <div class="box-card box-card-highlight">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
        <span class="card-header-icon" style="margin: 0;">⚙️</span>
        <span class="badge-pill pill-green">BƯỚC 02</span>
      </div>
      <h3 class="card-heading">Thiết Lập Động Cơ AI</h3>
      <p class="card-desc">
        • Cấu hình các kịch bản tổng hợp tự động.<br>
        • Kiểm thử song song với phương pháp cũ.<br>
        • Hiệu chỉnh độ chính xác đạt ngưỡng 99%.<br>
        <em>Thời gian dự kiến: Tuần 3 - Tuần 4</em>
      </p>
    </div>

    <!-- Bước 3 -->
    <div class="box-card">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
        <span class="card-header-icon" style="margin: 0;">🎓</span>
        <span class="badge-pill pill-amber">BƯỚC 03</span>
      </div>
      <h3 class="card-heading">Chuyển Giao & Vận Hành</h3>
      <p class="card-desc">
        • Tổ chức 2 buổi đào tạo sử dụng cho nhân sự.<br>
        • Bàn giao tài liệu hướng dẫn và video mẫu.<br>
        • Thiết lập kênh hỗ trợ kỹ thuật liên tục.<br>
        <em>Thời gian dự kiến: Tuần 5 - Tuần 6</em>
      </p>
    </div>
  </div>
</div>
```

---

## 4. Component 4: KPI Stats Slide (3 Số Liệu Đột Phá Lớn)

- **Mục đích sử dụng:** Trình bày các cam kết số liệu định lượng, kết quả tài chính, tỷ lệ tăng trưởng hoặc ROI thuyết phục người nghe.
- **Vị trí phù hợp:** Slide 04 hoặc 05.

```html
<!-- COMPONENT 4: KPI STATS SLIDE -->
<div class="slide" data-slide="04" data-notes="Kính thưa các anh chị, đây chính là các con số cam kết cụ thể mà dự án sẽ mang lại. Thứ nhất, chúng ta tiết kiệm được 65% thời gian xử lý sự vụ hàng tuần. Thứ hai, hệ số hoàn vốn đầu tư đạt 3.2 lần chỉ sau 4 tháng vận hành nhờ cắt giảm chi phí làm thêm giờ và tối ưu hóa quy trình. Và cuối cùng, độ chuẩn xác dữ liệu đạt trên 99.8%, triệt tiêu hoàn toàn các lỗi sai sót do con người.">
  <span class="slide-eyebrow eyebrow-emerald">📊 HIỆU QUẢ ĐO LƯỜNG</span>
  <h2 class="slide-title">Các Chỉ Số Đột Phá Cam Kết (KPIs)</h2>
  <p class="slide-subtitle">
    Định lượng giá trị cụ thể dự án mang lại cho tổ chức sau khi hoàn thành triển khai
  </p>

  <div class="grid-3">
    <!-- Stat 1 -->
    <div class="box-card" style="text-align: center; justify-content: center; padding: 32px 20px;">
      <div style="font-size: 3.5rem; font-weight: 800; font-family: var(--font-mono); color: #38bdf8; line-height: 1; margin-bottom: 10px;">
        -65%
      </div>
      <h3 class="card-heading" style="justify-content: center; font-size: 1.15rem; color: #f8fafc;">
        Thời Gian Xử Lý
      </h3>
      <p class="card-desc" style="margin-top: 6px;">
        Rút ngắn thời gian lập báo cáo định kỳ từ 12 giờ xuống còn dưới 4 giờ làm việc mỗi tuần.
      </p>
    </div>

    <!-- Stat 2 -->
    <div class="box-card box-card-highlight" style="text-align: center; justify-content: center; padding: 32px 20px;">
      <div style="font-size: 3.5rem; font-weight: 800; font-family: var(--font-mono); color: #34d399; line-height: 1; margin-bottom: 10px;">
        3.2x
      </div>
      <h3 class="card-heading" style="justify-content: center; font-size: 1.15rem; color: #f8fafc;">
        Tỷ Suất ROI Dự Kiến
      </h3>
      <p class="card-desc" style="margin-top: 6px;">
        Thu hồi vốn đầu tư công nghệ hoàn toàn sau 4 tháng nhờ tiết giảm chi phí vận hành.
      </p>
    </div>

    <!-- Stat 3 -->
    <div class="box-card" style="text-align: center; justify-content: center; padding: 32px 20px;">
      <div style="font-size: 3.5rem; font-weight: 800; font-family: var(--font-mono); color: #a855f7; line-height: 1; margin-bottom: 10px;">
        99.8%
      </div>
      <h3 class="card-heading" style="justify-content: center; font-size: 1.15rem; color: #f8fafc;">
        Độ Chính Xác Dữ Liệu
      </h3>
      <p class="card-desc" style="margin-top: 6px;">
        Triệt tiêu nguy cơ nhầm lẫn số liệu và công thức tính toán thủ công trên bảng tính.
      </p>
    </div>
  </div>
</div>
```

---

## 5. Component 5: Bảng Ma Trận So Sánh (Table với Badge Pills)

- **Mục đích sử dụng:** Trình bày bảng dữ liệu phân tích chi tiết, ma trận phân bổ ngân sách, so sánh tính năng hoặc trạng thái các hạng mục công việc.
- **Vị trí phù hợp:** Slide 05 hoặc 06.

```html
<!-- COMPONENT 5: BẢNG MA TRẬN SO SÁNH -->
<div class="slide" data-slide="05" data-notes="Tại bảng ma trận này, chúng tôi đã liệt kê chi tiết 4 hạng mục đầu tư cùng hiện trạng và phương án đề xuất. Mức ngân sách tổng thể là 45 triệu đồng, trong đó 60% dành cho chi phí thiết lập kỹ thuật một lần duy nhất, còn lại là chi phí hạ tầng và tài liệu hướng dẫn. Toàn bộ các hạng mục đều đã được thẩm định tính an toàn và khả thi cao.">
  <span class="slide-eyebrow eyebrow-amber">📋 MA TRẬN ĐÁNH GIÁ</span>
  <h2 class="slide-title">Ma Trận Đánh Giá Hạng Mục Triển Khai</h2>
  <p class="slide-subtitle">
    Chi tiết phân bổ ngân sách, thời lượng thực hiện và mức độ ưu tiên của từng cấu phần
  </p>

  <div class="box-card" style="padding: 10px; overflow-x: auto;">
    <table class="compare-table">
      <thead>
        <tr>
          <th style="width: 25%;">Hạng Mục Công Việc</th>
          <th style="width: 30%;">Nội Dung Trọng Tâm</th>
          <th style="width: 15%;">Thời Gian</th>
          <th style="width: 15%;">Ngân Sách</th>
          <th style="width: 15%;">Trạng Thái</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color: #f8fafc;">1. Cổng Kết Nối API</strong></td>
          <td>Tích hợp cơ sở dữ liệu bán hàng và kế toán</td>
          <td>10 ngày</td>
          <td>15.000.000 đ</td>
          <td><span class="badge-pill pill-green">SẴN SÀNG</span></td>
        </tr>
        <tr>
          <td><strong style="color: #f8fafc;">2. Động Cơ Xử Lý AI</strong></td>
          <td>Cấu hình prompt, tự động lọc và gom nhóm số liệu</td>
          <td>12 ngày</td>
          <td>18.000.000 đ</td>
          <td><span class="badge-pill pill-blue">ĐANG TRIỂN KHAI</span></td>
        </tr>
        <tr>
          <td><strong style="color: #f8fafc;">3. Giao Diện Báo Cáo</strong></td>
          <td>Xây dựng dashboard trực quan tương tác cao</td>
          <td>07 ngày</td>
          <td>8.000.000 đ</td>
          <td><span class="badge-pill pill-amber">CHỜ PHÊ DUYỆT</span></td>
        </tr>
        <tr>
          <td><strong style="color: #f8fafc;">4. Đào Tạo Chuyển Giao</strong></td>
          <td>Biên soạn tài liệu và tổ chức 2 workshop thực hành</td>
          <td>05 ngày</td>
          <td>4.000.000 đ</td>
          <td><span class="badge-pill pill-green">HOÀN TẤT GIÁO TRÌNH</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
```

---

## 6. Component 6: Summary & Q&A Slide (3 Đúc Kết Cốt Lõi & Hộp Kêu Gọi Hành Động)

- **Mục đích sử dụng:** Slide bế mạc và tổng kết bài thuyết trình. Nhắc lại 3 thông điệp quan trọng nhất, mở khung thảo luận / Q&A và cung cấp thông tin liên hệ hành động tiếp theo.
- **Vị trí phù hợp:** Slide cuối cùng (Slide 06, 07 hoặc 08).

```html
<!-- COMPONENT 6: SUMMARY & Q&A SLIDE -->
<div class="slide" data-slide="06" data-notes="Để khép lại bài thuyết trình hôm nay, tôi xin gửi gắm 3 đúc kết then chốt: Thứ nhất, công nghệ đã sẵn sàng và rất dễ tiếp cận. Thứ hai, chúng ta không thay thế con người mà giải phóng sức lao động để làm việc thông minh hơn. Và thứ ba, bắt đầu ngay hôm nay để tạo lợi thế dẫn đầu. Ngay bây giờ, rất mong nhận được câu hỏi và đóng góp ý kiến từ quý anh chị. Xin chân thành cảm ơn!">
  <span class="slide-eyebrow eyebrow-indigo">🎯 TỔNG KẾT & BÀN GIAO</span>
  <h2 class="slide-title">Đúc Kết Cốt Lõi & Kêu Gọi Hành Động</h2>
  <p class="slide-subtitle">
    Những thông điệp then chốt cần ghi nhớ và bước đi tiếp theo để đưa dự án vào thực tiễn
  </p>

  <div class="grid-2">
    <!-- Cột 3 đúc kết cốt lõi -->
    <div class="box-card">
      <span class="card-header-icon">💡</span>
      <h3 class="card-heading">3 Thông Điệp Then Chốt</h3>
      <p class="card-desc">
        <strong>1. Đơn giản & Thực chiến:</strong> Ứng dụng giải pháp 0-Setup, nhân viên không cần biết viết code vẫn dễ dàng vận hành.<br><br>
        <strong>2. Hiệu quả chứng minh ngay:</strong> Cắt giảm thời gian lãng phí và triệt tiêu sai số ngay từ tuần đầu tiên áp dụng.<br><br>
        <strong>3. Lợi thế cạnh tranh:</strong> Xây dựng văn hóa làm việc định hướng dữ liệu và làm chủ công nghệ trí tuệ nhân tạo.
      </p>
    </div>

    <!-- Cột Kêu gọi hành động & Q&A -->
    <div class="box-card box-card-highlight" style="display: flex; flex-direction: column; justify-content: space-between;">
      <div>
        <span class="card-header-icon">🤝</span>
        <h3 class="card-heading" style="color: #38bdf8;">Thảo Luận & Hỏi Đáp (Q&A)</h3>
        <p class="card-desc">
          Chúng tôi rất mong nhận được phản hồi và câu hỏi từ ban lãnh đạo cùng các anh chị đồng nghiệp để hoàn thiện kế hoạch chi tiết.
        </p>
      </div>

      <div style="background: rgba(255, 255, 255, 0.04); border-radius: 10px; padding: 14px 16px; border: 1px solid rgba(255, 255, 255, 0.08); margin-top: 16px;">
        <div style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 4px;">Liên hệ đầu mối dự án:</div>
        <div style="font-size: 0.95rem; font-weight: 700; color: #f8fafc;">Ban Quản Trị Đổi Mới Sáng Tạo & AI</div>
        <div style="font-size: 0.82rem; color: #818cf8; font-family: var(--font-mono); margin-top: 4px;">support@training-ai.internal | Hotline: 0988.xxx.xxx</div>
      </div>
    </div>
  </div>
</div>
```

---

## 🛠️ HƯỚNG DẪN KỸ THUẬT KHI LẮP RÁP (ASSEMBLY GUIDELINES)

Khi AI hoặc học viên lắp ráp các khối component vào `templates/engine.html`, hãy tuân thủ nghiêm ngặt các nguyên tắc sau:

1. **Thay thế Token `{{SLIDES_CONTENT}}`:**
   - Đặt tuần tự các slide bên trong khối `<main id="deck-stage"> ... </main>`.
   - Đảm bảo không để sót token `{{SLIDES_CONTENT}}` trong file HTML cuối cùng.

2. **Quy tắc Eyebrow Tags màu sắc có sẵn trong `engine.html`:**
   - `.eyebrow-indigo`: Màu chàm tím (`#818cf8`) — thích hợp cho Slide Mở đầu / Khởi động.
   - `.eyebrow-cyan`: Màu xanh lục lam (`#22d3ee`) — thích hợp cho Lộ trình / Quy trình.
   - `.eyebrow-emerald`: Màu xanh ngọc lục bảo (`#34d399`) — thích hợp cho KPI / Kết quả tích cực.
   - `.eyebrow-amber`: Màu vàng hổ phách (`#fbbf24`) — thích hợp cho Ma trận / Cảnh báo / Kế hoạch.
   - `.eyebrow-rose`: Màu hồng đỏ (`#fb7185`) — thích hợp cho So sánh rủi ro / Vấn đề nan giải.

3. **Quy tắc Badge Pills trạng thái:**
   - `.pill-green`: Màu xanh lá (Thành công / Hoàn thành / Khả thi cao).
   - `.pill-red`: Màu đỏ (Rủi ro / Phương pháp cũ / Cần tránh).
   - `.pill-blue`: Màu xanh dương (Đang triển khai / Trọng tâm).
   - `.pill-amber`: Màu vàng (Chờ duyệt / Lưu ý đặc biệt).
