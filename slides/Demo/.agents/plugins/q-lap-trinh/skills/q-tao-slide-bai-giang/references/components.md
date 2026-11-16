# THƯ VIỆN COMPONENT TRÌNH CHIẾU CHUẨN HÓA (SLIDE COMPONENT LIBRARY)

Tài liệu này chứa toàn bộ mẫu mã nguồn HTML (HTML Snippets) cho các dạng slide thông dụng. Mỗi slide phải được bọc trong thẻ:
```html
<div class="slide" data-slide="X" data-notes="[Nội dung kịch bản lời thoại diễn giả tại đây]">
  <!-- Nội dung bên trong -->
</div>
```
*(Lưu ý: Slide đầu tiên luôn có thêm class `active`: `<div class="slide active" data-slide="1" ...>`)*

---

## 1. COMPONENT: COVER / HERO SLIDE (SLIDE MỞ ĐẦU)
Dùng cho slide số 1 giới thiệu chủ đề, tầm quan trọng và tạo ấn tượng mạnh mẽ ban đầu.

```html
<div class="slide active" data-slide="1" data-notes="Chào các bạn, hôm nay chúng ta sẽ cùng nhau khám phá một chuyên đề rất quan trọng...">
  <span class="slide-eyebrow eyebrow-indigo">⚡ CHUYÊN ĐỀ: [TÊN CHUYÊN ĐỀ HOẶC MÃ BÀI HỌC]</span>
  <h1 class="slide-title">
    [Tiêu Đề Dòng 1]<br>
    <span style="background: linear-gradient(90deg, #818cf8, #38bdf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">[Tiêu Đề Dòng 2 Nổi Bật]</span>
  </h1>
  <p class="slide-subtitle">[Mô tả ngắn gọn về giá trị thực tế và mục tiêu đầu ra của bài học này trong 1-2 câu].</p>

  <div class="grid-2">
    <div class="box-card" style="border-left: 4px solid var(--accent-danger);">
      <span class="card-header-icon">⚠️</span>
      <h3 class="card-heading">Thực Trạng / Sai Lầm Thường Gặp</h3>
      <ul class="card-desc" style="list-style-type: none; display: flex; flex-direction: column; gap: 12px; padding-left: 0;">
        <li>❌ <strong>[Sai lầm 1]:</strong> [Mô tả ngắn gọn hệ quả].</li>
        <li>❌ <strong>[Sai lầm 2]:</strong> [Mô tả ngắn gọn hệ quả].</li>
        <li>❌ <strong>[Sai lầm 3]:</strong> [Mô tả ngắn gọn hệ quả].</li>
      </ul>
    </div>

    <div class="box-card box-card-highlight" style="border-left: 4px solid var(--accent-success);">
      <span class="card-header-icon">🚀</span>
      <h3 class="card-heading">Mục Tiêu & Chuẩn Thực Chiến</h3>
      <ul class="card-desc" style="list-style-type: none; display: flex; flex-direction: column; gap: 12px; padding-left: 0;">
        <li>✅ <strong>[Chuẩn 1]:</strong> [Mô tả lợi ích vượt trội].</li>
        <li>✅ <strong>[Chuẩn 2]:</strong> [Mô tả lợi ích vượt trội].</li>
        <li>✅ <strong>[Chuẩn 3]:</strong> [Mô tả lợi ích vượt trội].</li>
      </ul>
    </div>
  </div>
</div>
```

---

## 2. COMPONENT: SO SÁNH TRỰC DIỆN 2 CỘT (SPLIT COMPARISON)
Dùng khi so sánh Sinh viên vs Kỹ sư, Cũ vs Mới, Bad Practice vs Best Practice, Ưu điểm vs Nhược điểm.

```html
<div class="slide" data-slide="2" data-notes="Hãy nhìn vào sự đối lập giữa hai tư duy này...">
  <span class="slide-eyebrow eyebrow-cyan">⚖️ SO SÁNH ĐỐI CHIẾU</span>
  <h2 class="slide-title">[Tiêu Đề So Sánh: Đối Tượng A vs Đối Tượng B]</h2>
  <p class="slide-subtitle">[Tóm tắt điểm mấu chốt tạo nên sự khác biệt cốt lõi].</p>

  <div class="grid-2">
    <div class="box-card" style="border-left: 4px solid #f43f5e;">
      <span class="card-header-icon">❌</span>
      <h3 class="card-heading">[Cách Làm Sai / Chưa Chuẩn]</h3>
      <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 8px;">
        <div>
          <span class="badge-pill pill-red">[Đặc điểm 1]</span>
          <p class="card-desc" style="margin-top: 4px;">[Giải thích cụ thể và rủi ro tiềm ẩn].</p>
        </div>
        <div>
          <span class="badge-pill pill-red">[Đặc điểm 2]</span>
          <p class="card-desc" style="margin-top: 4px;">[Giải thích cụ thể và rủi ro tiềm ẩn].</p>
        </div>
      </div>
    </div>

    <div class="box-card box-card-highlight" style="border-left: 4px solid #10b981;">
      <span class="card-header-icon">✅</span>
      <h3 class="card-heading">[Chuẩn Chuyên Nghiệp / Khuyên Dùng]</h3>
      <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 8px;">
        <div>
          <span class="badge-pill pill-green">[Giải pháp 1]</span>
          <p class="card-desc" style="margin-top: 4px;">[Lợi ích về khả năng mở rộng, bảo trì].</p>
        </div>
        <div>
          <span class="badge-pill pill-green">[Giải pháp 2]</span>
          <p class="card-desc" style="margin-top: 4px;">[Lợi ích về hiệu năng hoặc trải nghiệm].</p>
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## 3. COMPONENT: LƯỚI 3 CỘT (GRID-3) - QUY TRÌNH 3 BƯỚC HOẶC 3 TRỤ CỘT
Dùng cho chu trình làm việc, 3 giai đoạn hoặc 3 nguyên tắc nền tảng.

```html
<div class="slide" data-slide="3" data-notes="Quy trình này gồm 3 giai đoạn then chốt mà bạn cần nắm vững...">
  <span class="slide-eyebrow eyebrow-emerald">🔄 QUY TRÌNH THỰC HIỆN</span>
  <h2 class="slide-title">[Quy Trình 3 Bước Tinh Gọn]</h2>
  <p class="slide-subtitle">[Mô tả nhịp độ và cách phối hợp giữa các bước trong thực tế].</p>

  <div class="grid-3">
    <div class="box-card">
      <div style="font-family: var(--font-mono); color: #818cf8; font-weight: 700; font-size: 0.8rem; margin-bottom: 6px;">01. BƯỚC MỞ ĐẦU</div>
      <h4 class="card-heading">[Tên Giai Đoạn 1]</h4>
      <p class="card-desc">[Nội dung hành động cụ thể cần hoàn thành trong bước này].</p>
    </div>

    <div class="box-card box-card-highlight">
      <div style="font-family: var(--font-mono); color: #38bdf8; font-weight: 700; font-size: 0.8rem; margin-bottom: 6px;">02. BƯỚC TRỌNG TÂM</div>
      <h4 class="card-heading">[Tên Giai Đoạn 2]</h4>
      <p class="card-desc">[Hành động kỹ thuật hoặc nghiệp vụ cốt lõi tạo ra sản phẩm].</p>
    </div>

    <div class="box-card">
      <div style="font-family: var(--font-mono); color: #34d399; font-weight: 700; font-size: 0.8rem; margin-bottom: 6px;">03. BÀN GIAO</div>
      <h4 class="card-heading">[Tên Giai Đoạn 3]</h4>
      <p class="card-desc">[Kiểm thử, nghiệm thu và chuyển giao sản phẩm hoàn thiện].</p>
    </div>
  </div>
</div>
```

---

## 4. COMPONENT: LƯỚI 4 CỘT (GRID-4) - 4 TIÊU CHÍ HOẶC 4 MODULE CỐT LÕI
Dùng khi chia nhỏ thành 4 phần bằng nhau (ví dụ: 4 trụ cột OOP, 4 nguyên lý SOLID, 4 chỉ số tài chính).

```html
<div class="slide" data-slide="4" data-notes="Chúng ta có 4 trụ cột chính để đánh giá chất lượng...">
  <span class="slide-eyebrow eyebrow-amber">🧱 KIẾN TRÚC NỀN TẢNG</span>
  <h2 class="slide-title">[4 Trụ Cột / 4 Tiêu Chí Quan Trọng]</h2>
  <p class="slide-subtitle">[Bức tranh tổng thể giúp kiểm soát toàn diện vấn đề].</p>

  <div class="grid-4">
    <div class="box-card">
      <span class="card-header-icon">🎯</span>
      <h4 class="card-heading">[Tiêu Chí 1]</h4>
      <p class="card-desc">[Mô tả tiêu chuẩn và cách áp dụng].</p>
    </div>
    <div class="box-card">
      <span class="card-header-icon">⚡</span>
      <h4 class="card-heading">[Tiêu Chí 2]</h4>
      <p class="card-desc">[Mô tả tiêu chuẩn và cách áp dụng].</p>
    </div>
    <div class="box-card">
      <span class="card-header-icon">🔒</span>
      <h4 class="card-heading">[Tiêu Chí 3]</h4>
      <p class="card-desc">[Mô tả tiêu chuẩn và cách áp dụng].</p>
    </div>
    <div class="box-card">
      <span class="card-header-icon">📈</span>
      <h4 class="card-heading">[Tiêu Chí 4]</h4>
      <p class="card-desc">[Mô tả tiêu chuẩn và cách áp dụng].</p>
    </div>
  </div>
</div>
```

---

## 5. COMPONENT: CỬA SỔ TERMINAL / MÃ NGUỒN (CODE WINDOW MOCKUP)
Dùng cho các bài giảng Kỹ thuật, CLI, Code mẫu hoặc log hệ thống.

```html
<div class="slide" data-slide="5" data-notes="Để thực thi việc này, các bạn mở terminal và làm theo các bước sau...">
  <span class="slide-eyebrow eyebrow-indigo">💻 THỰC HÀNH DÒNG LỆNH</span>
  <h2 class="slide-title">[Thao Tác Terminal / Code Mẫu]</h2>
  <p class="slide-subtitle">[Giải thích ngữ cảnh thực thi câu lệnh hoặc đoạn mã].</p>

  <div class="terminal-box">
    <div class="terminal-topbar">
      <span class="term-dot term-dot-r"></span>
      <span class="term-dot term-dot-y"></span>
      <span class="term-dot term-dot-g"></span>
      <span class="term-title">bash — 80x24</span>
    </div>
    <div class="terminal-body">
      <p><span class="term-comment"># Bước 1: Khởi tạo dự án</span></p>
      <p><span class="term-cmd">git</span> checkout -b feature/awesome-feature</p>
      <br>
      <p><span class="term-comment"># Bước 2: Chạy kiểm thử tự động</span></p>
      <p><span class="term-cmd">npm</span> run test <span class="term-flag">--coverage</span></p>
      <p><span class="term-success">✔ Tests passing: 42/42 suites (100%)</span></p>
      <br>
      <p><span class="term-comment"># Bước 3: Đóng gói bản phát hành</span></p>
      <p><span class="term-cmd">npm</span> run build</p>
      <p><span class="term-warn">⚡ Build complete in 1.42s (Production Ready)</span></p>
    </div>
  </div>
</div>
```

---

## 6. COMPONENT: BẢNG SO SÁNH MA TRẬN (COMPARISON TABLE)
Dùng để đối chiếu nhiều phương án, công nghệ hoặc chỉ số.

```html
<div class="slide" data-slide="6" data-notes="Bảng ma trận này giúp các bạn có cái nhìn tổng quan khi đưa ra quyết định lựa chọn công nghệ...">
  <span class="slide-eyebrow eyebrow-cyan">📊 BẢNG ĐỐI CHIẾU</span>
  <h2 class="slide-title">[Ma Trận Lựa Chọn Công Nghệ / Giải Pháp]</h2>
  <p class="slide-subtitle">[So sánh các tiêu chí then chốt để quyết định đúng đắn].</p>

  <table class="compare-table">
    <thead>
      <tr>
        <th>Tiêu Chí Đánh Giá</th>
        <th>Phương Án A (Cổ Điển)</th>
        <th>Phương Án B (Hiện Đại)</th>
        <th>Khuyến Nghị</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Tốc độ thực thi</strong></td>
        <td>Chậm khi tải dữ liệu lớn</td>
        <td>Tối ưu với Virtual DOM / SSR</td>
        <td><span class="badge-pill pill-green">Ưu tiên B</span></td>
      </tr>
      <tr>
        <td><strong>Độ phức tạp bảo trì</strong></td>
        <td>Khó mở rộng theo thời gian</td>
        <td>Module hóa rõ ràng, dễ test</td>
        <td><span class="badge-pill pill-blue">B vượt trội</span></td>
      </tr>
      <tr>
        <td><strong>Chi phí triển khai</strong></td>
        <td>Thấp ở giai đoạn đầu</td>
        <td>Cần đầu tư kiến trúc chuẩn</td>
        <td><span class="badge-pill pill-amber">Cân nhắc quy mô</span></td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## 7. COMPONENT: TIẾN TRÌNH DÒNG CHẢY (LIFECYCLE / PIPELINE FLOW)
Dùng cho quy trình duyệt PR, Pipeline CI/CD, Phễu chuyển đổi khách hàng.

```html
<div class="slide" data-slide="7" data-notes="Mọi công việc đều phải đi qua các chặng kiểm soát nghiêm ngặt...">
  <span class="slide-eyebrow eyebrow-emerald">🧭 QUY TRÌNH VẬN HÀNH</span>
  <h2 class="slide-title">[Vòng Đời Hoàn Chỉnh Của Một Nhiệm Vụ]</h2>
  <p class="slide-subtitle">[Các trạm kiểm soát chất lượng từ lúc bắt đầu đến khi hoàn thành].</p>

  <div class="box-card" style="background: rgba(15, 23, 42, 0.6); margin-top: 20px;">
    <div style="font-size: 0.85rem; font-weight: 700; color: #cbd5e1; margin-bottom: 14px;">CÁC CHẶNG CHUYỂN DỊCH TRẠNG THÁI:</div>
    <div style="display: flex; align-items: center; justify-content: space-between; gap: 8px; flex-wrap: wrap;">
      <span class="badge-pill pill-blue">1. Tiếp Nhận (To Do)</span> ➔
      <span class="badge-pill pill-amber">2. Đang Xử Lý (In Progress)</span> ➔
      <span class="badge-pill pill-blue">3. Tự Kiểm Thử (Self-Test)</span> ➔
      <span class="badge-pill pill-blue">4. Review Đánh Giá (Peer Review)</span> ➔
      <span class="badge-pill pill-amber">5. Kiểm Thử Độc Lập (QA)</span> ➔
      <span class="badge-pill pill-green">6. Đạt Chuẩn (Done)</span>
    </div>
  </div>
</div>
```

---

## 8. COMPONENT: SỐ LIỆU ĐỘT PHÁ (KPI STATS & CALLOUT)
Dùng cho bài giảng Quản trị, Kinh doanh hoặc Đánh giá hiệu năng kỹ thuật.

```html
<div class="slide" data-slide="8" data-notes="Những con số sau đây chứng minh sức mạnh của phương pháp mới...">
  <span class="slide-eyebrow eyebrow-amber">📈 KẾT QUẢ ĐỘT PHÁ</span>
  <h2 class="slide-title">[Hiệu Suất Đo Lường Sau Khi Tối Ưu]</h2>
  <p class="slide-subtitle">[Bằng chứng số liệu cụ thể phản ánh tác động thực tế].</p>

  <div class="grid-3">
    <div class="box-card box-card-highlight" style="text-align: center; padding: 32px 20px;">
      <div style="font-size: 3rem; font-weight: 800; color: #38bdf8; font-family: var(--font-mono);">-65%</div>
      <h4 class="card-heading" style="justify-content: center; margin-top: 8px;">Thời Gian Phản Hồi</h4>
      <p class="card-desc">Tối ưu từ 450ms xuống còn 150ms sau khi áp dụng caching.</p>
    </div>

    <div class="box-card box-card-highlight" style="text-align: center; padding: 32px 20px;">
      <div style="font-size: 3rem; font-weight: 800; color: #34d399; font-family: var(--font-mono);">99.9%</div>
      <h4 class="card-heading" style="justify-content: center; margin-top: 8px;">Độ Sẵn Sàng (Uptime)</h4>
      <p class="card-desc">Hệ thống duy trì vận hành ổn định không phát sinh downtime.</p>
    </div>

    <div class="box-card box-card-highlight" style="text-align: center; padding: 32px 20px;">
      <div style="font-size: 3rem; font-weight: 800; color: #fbbf24; font-family: var(--font-mono);">3.5x</div>
      <h4 class="card-heading" style="justify-content: center; margin-top: 8px;">Năng Suất Bàn Giao</h4>
      <p class="card-desc">Tăng tốc độ release tính năng mới lên gấp hơn 3 lần.</p>
    </div>
  </div>
</div>
```

---

## 9. COMPONENT: TỔNG KẾT & HỎI ĐÁP (SUMMARY & Q&A SLIDE)
Dùng cho slide kết thúc bài giảng để đọng lại giá trị và mở phần thảo luận.

```html
<div class="slide" data-slide="9" data-notes="Cảm ơn các bạn đã lắng nghe bài giảng. Bây giờ là thời gian dành cho phần hỏi đáp thảo luận...">
  <span class="slide-eyebrow eyebrow-rose">🎯 TỔNG KẾT BÀI HỌC</span>
  <h2 class="slide-title">[Những Điểm Cốt Lõi Cần Khắc Ghi]</h2>
  <p class="slide-subtitle">[Hành trang thực chiến giúp bạn áp dụng thành công vào công việc ngay hôm nay].</p>

  <div class="grid-3" style="margin-bottom: 20px;">
    <div class="box-card">
      <span class="card-header-icon">💡</span>
      <h4 class="card-heading">Nguyên Tắc 1</h4>
      <p class="card-desc">[Tóm tắt điểm cốt lõi nhất].</p>
    </div>
    <div class="box-card">
      <span class="card-header-icon">🛠️</span>
      <h4 class="card-heading">Hành Động 2</h4>
      <p class="card-desc">[Hành động cụ thể cần làm ngay].</p>
    </div>
    <div class="box-card">
      <span class="card-header-icon">🚀</span>
      <h4 class="card-heading">Tư Duy 3</h4>
      <p class="card-desc">[Tư duy lâu dài giúp tiến xa].</p>
    </div>
  </div>

  <div class="box-card box-card-highlight" style="text-align: center; padding: 22px;">
    <h3 style="color: #ffffff; margin-bottom: 6px;">💬 PHẦN HỎI & ĐÁP (Q&A)</h3>
    <p style="color: var(--text-muted); font-size: 0.95rem;">Hãy đặt bất kỳ câu hỏi nào về những điểm bạn còn băn khoăn. Chúc bạn gặt hái nhiều thành công!</p>
  </div>
</div>
```
