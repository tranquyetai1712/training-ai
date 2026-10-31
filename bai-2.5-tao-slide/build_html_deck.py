import os

engine_path = r"C:\Users\SingPC\.gemini\config\skills\q-tao-slide-bai-giang\templates\engine.html"
with open(engine_path, "r", encoding="utf-8") as f:
    template = f.read()

slides_html = """
    <!-- SLIDE 1: COVER -->
    <div class="slide active" data-slide="1" data-notes="Chào anh em! Chắc hẳn ai trong chúng ta khi dùng Antigravity chạy những task lớn như refactor cả module hay sinh hàng chục test cases đều từng gặp cảnh: vừa đi uống cốc cà phê quay lại thì máy tính đã ngủ gật, AI bị ngắt quãng giữa chừng, hoặc phải ngồi dán mắt vào màn hình chỉ để chờ bấm Approve. Chúng ta đang dùng AI để giải phóng sức lao động nhưng lại vô tình bị xích vào bàn làm việc vì những thiết lập mặc định chưa tối ưu. Trong đúng 7 phút hôm nay, mình sẽ chia sẻ với anh em 2 vũ khí cực mạnh: tính năng Remote Control điều khiển từ xa, bộ 3 thiết lập App Settings sống còn, và phần bonus đặc biệt: cách chạy Claude Code với Model bên thứ 3 hoàn toàn miễn phí, bảo mật qua Ollama. Nắm vững những tính năng này, anh em sẽ biến công cụ AI thành một trợ lý tự hành đúng nghĩa, làm việc xuyên suốt mọi lúc mọi nơi.">
      <span class="slide-eyebrow eyebrow-indigo">⚡ CHUYÊN ĐỀ CÔNG NGHỆ NỘI BỘ • 7 PHÚT</span>
      <h1 class="slide-title">
        Tối Ưu Hóa Trải Nghiệm Phát Triển Với AI<br>
        <span style="background: linear-gradient(90deg, #818cf8, #38bdf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Làm Chủ Remote Control, App Settings & Tích Hợp Claude Code</span>
      </h1>
      <p class="slide-subtitle">Giải phóng kỹ sư khỏi bàn làm việc, bảo vệ dữ liệu tuyệt đối và làm chủ luồng thực thi tự hành.</p>

      <div class="grid-2">
        <div class="box-card" style="border-left: 4px solid var(--accent-danger);">
          <span class="card-header-icon">⚠️</span>
          <h3 class="card-heading">Thực Trạng & Rào Cản Thường Gặp</h3>
          <ul class="card-desc" style="list-style-type: none; display: flex; flex-direction: column; gap: 12px; padding-left: 0;">
            <li>❌ <strong>Máy ngủ gật (Sleep Mode):</strong> AI đang chạy task dài, máy tự tắt làm đứt kết nối.</li>
            <li>❌ <strong>Bị xích vào bàn làm việc:</strong> Phải ngồi canh máy chỉ để bấm Approve prompt.</li>
            <li>❌ <strong>Tắt nhầm cửa sổ:</strong> Đóng app làm mất context phiên làm việc.</li>
            <li>❌ <strong>Chi phí & Rò rỉ code:</strong> Dùng cloud agent lo ngại lộ source code nhạy cảm và ngốn token API.</li>
          </ul>
        </div>

        <div class="box-card box-card-highlight" style="border-left: 4px solid var(--accent-success);">
          <span class="card-header-icon">🚀</span>
          <h3 class="card-heading">Mục Tiêu & Chuẩn Thực Chiến 2026</h3>
          <ul class="card-desc" style="list-style-type: none; display: flex; flex-direction: column; gap: 12px; padding-left: 0;">
            <li>✅ <strong>Remote Control linh hoạt:</strong> Quản lý Agent trên PC từ smartphone/laptop khác mọi lúc.</li>
            <li>✅ <strong>Prevent Sleep:</strong> Giữ máy luôn thức trong lúc Agent viết code ngầm xuyên đêm.</li>
            <li>✅ <strong>Keep In Menu Bar:</strong> Thường trực trên thanh hệ thống, mở ra ngay lập tức.</li>
            <li>✅ <strong>Local LLMs via Ollama:</strong> Tích hợp model nội bộ vào Claude Code 0% phí token & bảo mật 100%.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SLIDE 2: REMOTE CONTROL OVERVIEW -->
    <div class="slide" data-slide="2" data-notes="Anh em có bao giờ ước: máy công ty cấu hình khủng cứ việc build code, còn mình thì ra quán trà sữa hay đi họp vẫn check được AI đang viết tới đâu chưa? Remote Control sinh ra chính là để giải quyết bài toán đó. Nó không phải là một công cụ remote desktop nặng nề như TeamViewer hay AnyDesk, mà là cầu nối giao diện web trực tiếp vào chính session Antigravity đang chạy trên workstation của anh em. Toàn bộ mã nguồn, git branch, terminal và công cụ build vẫn chạy 100% tại máy trạm, nhưng giao diện điều khiển, danh sách artifacts và khung chat lại hiển thị mượt mà trên trình duyệt điện thoại hoặc laptop cá nhân. Anh em có thể review diff, ấn duyệt lệnh bash hay prompt bổ sung chỉ bằng một chạm trên điện thoại. Remote Control biến cỗ máy bàn của bạn thành server AI cá nhân mà bạn nắm trọn trong lòng bàn tay.">
      <span class="slide-eyebrow eyebrow-cyan">🌐 TÍNH NĂNG ĐỘT PHÁ • CROSS-DEVICE AGENT</span>
      <h2 class="slide-title">Antigravity Remote Control Là Gì?</h2>
      <p class="slide-subtitle">Giải pháp lái, giám sát và tương tác với AI Agent từ xa trên mọi thiết bị qua nền tảng web bảo mật.</p>

      <div class="grid-2">
        <div class="box-card" style="border-left: 4px solid #f59e0b;">
          <span class="card-header-icon">🏢</span>
          <h3 class="card-heading">Cách Làm Cũ (Workstation Bound)</h3>
          <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 8px;">
            <div>
              <span class="badge-pill pill-amber">Gò bó vị trí</span>
              <p class="card-desc" style="margin-top: 4px;">Phải ngồi trực tiếp trước màn hình máy tính công ty để xem Agent sinh code.</p>
            </div>
            <div>
              <span class="badge-pill pill-amber">Gián đoạn khi di chuyển</span>
              <p class="card-desc" style="margin-top: 4px;">Rời bàn làm việc đi họp, đi ăn trưa là hoàn toàn mù thông tin về tiến độ của agent.</p>
            </div>
            <div>
              <span class="badge-pill pill-amber">Phê duyệt chậm trễ</span>
              <p class="card-desc" style="margin-top: 4px;">Agent dừng lại chờ bấm Approve prompt/lệnh bash, cả luồng công việc bị nghẽn.</p>
            </div>
          </div>
        </div>

        <div class="box-card box-card-highlight" style="border-left: 4px solid #06b6d4;">
          <span class="card-header-icon">⚡</span>
          <h3 class="card-heading">Chuẩn Remote Control (Bất Kỳ Đâu)</h3>
          <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 8px;">
            <div>
              <span class="badge-pill pill-cyan">Mobile First Web UI</span>
              <p class="card-desc" style="margin-top: 4px;">Giao diện web siêu nhẹ trên smartphone, tối ưu hóa cho thao tác cảm ứng.</p>
            </div>
            <div>
              <span class="badge-pill pill-cyan">Theo dõi Realtime</span>
              <p class="card-desc" style="margin-top: 4px;">Xem file diff, artifacts, subagent logs trực tiếp trong khi di chuyển.</p>
            </div>
            <div>
              <span class="badge-pill pill-green">Phê duyệt 1 chạm</span>
              <p class="card-desc" style="margin-top: 4px;">Nhấn 'Approve' hoặc bổ sung prompt cho Agent ngay từ màn hình điện thoại.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 3: CONNECT & SECURITY -->
    <div class="slide" data-slide="3" data-notes="Nhiều anh em sẽ hỏi: 'Remote như vậy có lộ mã nguồn công ty ra ngoài không, thiết lập có phức tạp cần mở port modem không?'. Câu trả lời là hoàn toàn không. Google thiết kế cơ chế ghép nối này theo triết lý Zero Trust cực kỳ nghiêm ngặt. Bước 1: Anh em mở Settings bằng phím Ctrl + ,, vào mục Application và gạt nút 'Enable Remote Control'. Bước 2: Antigravity sẽ sinh ngay một mã QR Code bảo mật. Anh em chỉ cần giơ camera điện thoại lên quét, hoặc truy cập antigravity.google đăng nhập đúng tài khoản Google là kết nối thành công. Toàn bộ phiên làm việc xác thực bằng Token handshake dùng một lần, dữ liệu truyền tải mã hóa end-to-end và không hề mở bất kỳ open port nào trên router nội bộ. Tiện lợi tối đa nhưng bảo mật chuẩn doanh nghiệp – anh em hoàn toàn yên tâm dùng trong mạng công ty.">
      <span class="slide-eyebrow eyebrow-indigo">🔐 CƠ CHẾ VẬN HÀNH • BẢO MẬT ZERO TRUST</span>
      <h2 class="slide-title">Cơ Chế Ghép Nối & Kiến Trúc Bảo Mật</h2>
      <p class="slide-subtitle">Bật tính năng trong 10 giây và kiến trúc bảo vệ dữ liệu doanh nghiệp đa lớp.</p>

      <div class="grid-3">
        <div class="box-card">
          <span class="badge-pill pill-cyan">BƯỚC 1</span>
          <h3 class="card-heading" style="margin-top: 10px;">⚙️ Bật Trong Settings</h3>
          <p class="card-desc">Mở Settings qua phím tắt <code>Ctrl + ,</code> (Windows/Linux) hoặc <code>Cmd + ,</code> (macOS).</p>
          <p class="card-desc" style="margin-top: 8px;">Vào mục <strong>Application</strong> ➔ gạt toggle <strong>Enable Remote Control</strong> sang ON.</p>
          <p class="card-desc" style="margin-top: 8px; color: var(--accent-secondary);">Hoặc gõ <code>agy --remote-control</code> từ terminal.</p>
        </div>

        <div class="box-card box-card-highlight">
          <span class="badge-pill pill-indigo">BƯỚC 2</span>
          <h3 class="card-heading" style="margin-top: 10px;">📱 Ghép Nối 1 Chạm</h3>
          <p class="card-desc">Antigravity sinh ngay một mã <strong>QR Code bảo mật</strong> động trên màn hình.</p>
          <p class="card-desc" style="margin-top: 8px;">Dùng camera điện thoại quét mã QR để mở session trên trình duyệt trong 2 giây.</p>
          <p class="card-desc" style="margin-top: 8px;">Hoặc truy cập trực tiếp <code>antigravity.google</code> để chọn host active.</p>
        </div>

        <div class="box-card">
          <span class="badge-pill pill-green">BẢO MẬT</span>
          <h3 class="card-heading" style="margin-top: 10px;">🛡️ Chuẩn Doanh Nghiệp</h3>
          <p class="card-desc"><strong>Token Handshake:</strong> Mã xác thực dùng 1 lần, chống dò quét IP trái phép.</p>
          <p class="card-desc" style="margin-top: 8px;"><strong>Không mở Open Port:</strong> Hoạt động an toàn sau tường lửa và VPN công ty.</p>
          <p class="card-desc" style="margin-top: 8px;"><strong>Host Boundary:</strong> Toàn bộ source code & secrets lưu tại workstation.</p>
        </div>
      </div>
    </div>

    <!-- SLIDE 4: APP SETTINGS - PREVENT SLEEP -->
    <div class="slide" data-slide="4" data-notes="Đã bao giờ anh em giao cho Agent một task lớn trước khi đi ăn trưa, quay lại thấy màn hình đen ngòm và task bị failed vì máy rơi vào Sleep Mode chưa? Mặc định, Windows và macOS đều có chính sách tiết kiệm điện tự động ngủ sau một khoảng thời gian người dùng không gõ phím hay rê chuột. Nhưng với AI Coding Agent, lúc chúng ta không chạm vào máy lại chính là lúc nó đang làm việc vất vả nhất. Tính năng 'Prevent Sleep' trong App Settings ra đời để giải quyết tận gốc vấn đề này. Khi được bật, Antigravity sẽ gửi tín hiệu giữ màn hình và hệ thống luôn thức (Awake) trong suốt thời gian Agent đang sinh mã hoặc chạy test. Khi Agent hoàn thành xong toàn bộ công việc, hệ thống mới quay trở lại cơ chế sleep bình thường. Hãy bật 'Prevent Sleep' ngay hôm nay để yên tâm giao việc lớn xuyên đêm mà không lo đứt gánh giữa đường.">
      <span class="slide-eyebrow eyebrow-amber">☕ CÀI ĐẶT HỆ THỐNG • LIÊN TỤC KHÔNG GIÁN ĐOẠN</span>
      <h2 class="slide-title">App Settings: Prevent Sleep</h2>
      <p class="slide-subtitle">Ngăn hệ thống tự động tắt màn hình và đưa PC vào chế độ ngủ khi AI đang sinh mã.</p>

      <div class="grid-2">
        <div class="box-card" style="border-left: 4px solid var(--accent-warning);">
          <span class="card-header-icon">⚡</span>
          <h3 class="card-heading">Bản Chất Cơ Chế Prevent Sleep</h3>
          <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 12px;">
            <div>
              <span class="badge-pill pill-red">Nỗi đau đứt gãy</span>
              <p class="card-desc" style="margin-top: 4px;">Hệ điều hành tự Sleep sau 5-15 phút không thao tác ➔ Tiến trình Agent bị ngắt giữa chừng, mất session.</p>
            </div>
            <div>
              <span class="badge-pill pill-green">Cơ chế giữ thức thông minh</span>
              <p class="card-desc" style="margin-top: 4px;">Antigravity tự động kích hoạt API ngăn chặn sleep ở cấp OS kernel trong suốt thời gian AI viết code.</p>
            </div>
            <div>
              <span class="badge-pill pill-cyan">Tự giải phóng</span>
              <p class="card-desc" style="margin-top: 4px;">Ngay khi Agent hoàn thành công việc, máy tính tự động trở lại cơ chế tiết kiệm điện bình thường.</p>
            </div>
          </div>
        </div>

        <div class="terminal-box">
          <div class="terminal-header">
            <div class="terminal-dots">
              <span class="dot-red"></span>
              <span class="dot-yellow"></span>
              <span class="dot-green"></span>
            </div>
            <span class="terminal-title">Antigravity > Settings > Application</span>
          </div>
          <div class="terminal-body">
            <span class="code-comment"># System-level Settings Configuration</span><br>
            <span class="code-keyword">[X]</span> <span class="code-output" style="color: #34d399; font-weight: bold;">Prevent Sleep</span><br>
            <span class="code-comment">&nbsp;&nbsp;&nbsp;&nbsp;Prevent the PC from turning off the screen & sleeping while AI writes code.</span><br><br>
            <span class="code-keyword">Status:</span> <span class="code-output" style="color: #fbbf24;">RUNNING AGENT (Awake Lock Acquired)</span><br><br>
            <span class="code-keyword">[X]</span> <span class="code-output" style="color: #38bdf8; font-weight: bold;">Keep In Menu Bar / Taskbar Tray</span><br>
            <span class="code-comment">&nbsp;&nbsp;&nbsp;&nbsp;Close button minimizes app to system tray.</span><br><br>
            <span class="code-keyword">[i]</span> <span class="code-output" style="color: #818cf8;">Notification Settings</span><br>
            <span class="code-comment">&nbsp;&nbsp;&nbsp;&nbsp;Managed directly within OS System Settings.</span>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 5: MENU BAR & NOTIFICATIONS -->
    <div class="slide" data-slide="5" data-notes="Có hai điều nhỏ nhưng ảnh hưởng cực lớn đến trải nghiệm hàng ngày của anh em: tắt nhầm cửa sổ và lỡ mất thông báo quan trọng. Thứ nhất, thói quen bấm nút 'X' để đóng cửa sổ thường vô tình tắt luôn cả ứng dụng đang chạy. Thứ hai, nhiều người tìm mãi trong app không thấy chỗ bật âm báo. Về tính năng 'Keep In Menu Bar': Khi bật lên, Antigravity sẽ neo thường trực trên khay hệ thống (Windows Taskbar Tray) hoặc Mac Menu Bar. Bấm nút 'X' chỉ là ẩn cửa sổ, app vẫn sống ngầm và sẵn sàng bật lên tức thì bằng phím tắt mà không cần khởi động lại. Về 'Notification Settings': Anh em cần lưu ý, Antigravity không tự quản lý toggle thông báo bên trong app mà đẩy toàn quyền về Settings của Windows/macOS. Anh em chỉ cần cấp quyền thông báo cho Antigravity trong OS Settings là mỗi khi AI xong task hoặc cần duyệt, máy tính và điện thoại đều sẽ ting ting báo ngay. Setup đúng 2 mục này giúp anh em luôn phản hồi kịp thời mà không tốn công chờ đợi.">
      <span class="slide-eyebrow eyebrow-indigo">📌 CÀI ĐẶT HỆ THỐNG • THƯỜNG TRỰC & THÔNG BÁO</span>
      <h2 class="slide-title">Keep In Menu Bar & Notifications</h2>
      <p class="slide-subtitle">Đảm bảo ứng dụng luôn thường trực tức thì và không bỏ sót các tín hiệu hoàn thành của AI.</p>

      <div class="grid-2">
        <div class="box-card box-card-highlight" style="border-left: 4px solid var(--accent-primary);">
          <span class="card-header-icon">📌</span>
          <h3 class="card-heading">Keep In Menu Bar / Taskbar Tray</h3>
          <ul class="card-desc" style="list-style-type: none; display: flex; flex-direction: column; gap: 12px; padding-left: 0; margin-top: 12px;">
            <li>✔ <strong>Chống tắt nhầm:</strong> Bấm dấu 'X' chỉ đóng giao diện, tiến trình Agent vẫn âm thầm tiếp tục.</li>
            <li>✔ <strong>Thường trực trên Tray:</strong> Neo tại Mac Menu Bar hoặc Windows Taskbar Tray góc dưới màn hình.</li>
            <li>✔ <strong>Triệu hồi tức thì (Summon):</strong> Bấm phím tắt hoặc click khay hệ thống là app bung ra ngay, không phải nạp lại từ đầu.</li>
            <li>✔ <strong>Bảo toàn ngữ cảnh:</strong> Giữ nguyên lịch sử terminal, context diff và các tab công việc.</li>
          </ul>
        </div>

        <div class="box-card" style="border-left: 4px solid var(--accent-secondary);">
          <span class="card-header-icon">🔔</span>
          <h3 class="card-heading">Notification Settings (OS-Level)</h3>
          <ul class="card-desc" style="list-style-type: none; display: flex; flex-direction: column; gap: 12px; padding-left: 0; margin-top: 12px;">
            <li>✔ <strong>Nguyên lý quản lý tập trung:</strong> Việc bật/tắt thông báo của Antigravity được điều khiển từ <strong>Cài đặt Hệ điều hành</strong> (Windows / macOS Settings), không nằm trong app.</li>
            <li>✔ <strong>Thiết lập trên Windows:</strong> <code>Start > Settings > System > Notifications</code> ➔ Bật On cho Antigravity.</li>
            <li>✔ <strong>Thiết lập trên macOS:</strong> <code>System Settings > Notifications > Antigravity</code> ➔ Cho phép Banners/Alerts.</li>
            <li>✔ <strong>Phản hồi thần tốc:</strong> Nhận âm báo & popup ngay khi Agent viết xong code hoặc yêu cầu approve.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SLIDE 6: WHY 3RD-PARTY LLM IN CLAUDE CODE -->
    <div class="slide" data-slide="6" data-notes="Sau khi đã làm chủ Antigravity, mình muốn chia sẻ thêm một kỹ thuật cực hot trong giới lập trình: Sử dụng Claude Code nhưng chạy bằng Model bên thứ 3 hoặc Model Local qua Ollama. Tại sao chúng ta lại cần điều này? Claude Code của Anthropic là một CLI agent xuất sắc nhất hiện nay về khả năng sửa code và chạy terminal, nhưng nó có 2 rào cản lớn: chi phí token API đắt đỏ và chính sách bảo mật dữ liệu công ty không cho phép gửi code lên cloud. Bằng cách đưa model bên thứ 3 thông qua Ollama, anh em giải quyết được cả 2 bài toán: Thứ nhất, code chạy hoàn toàn local hoặc qua server riêng của công ty, bảo mật 100%. Thứ hai, chi phí token bằng 0 khi dùng các mô hình mã nguồn mở hàng đầu như Qwen 2.5 Coder hay DeepSeek. Chúng ta vừa có 'bộ não' miễn phí/bảo mật, vừa có 'đôi tay' agentic cực kỳ linh hoạt của Claude Code. Tận dụng vỏ Claude Code nhưng thay ruột bằng Ollama là cách thông minh nhất để dev thỏa sức dùng AI mà sếp không lo lộ code hay tốn ngân sách.">
      <span class="slide-eyebrow eyebrow-purple">💡 MỞ RỘNG ĐỘT PHÁ • CLAUDE CODE & LOCAL LLM</span>
      <h2 class="slide-title">Tại Sao Cần Đưa Model Bên Thứ 3 Vào Claude Code?</h2>
      <p class="slide-subtitle">Kết hợp trí tuệ mã nguồn mở với framework CLI Agentic số 1 hiện nay.</p>

      <div class="grid-3">
        <div class="box-card" style="border-top: 3px solid var(--accent-danger);">
          <span class="badge-pill pill-red">TRỤ CỘT 1</span>
          <h3 class="card-heading" style="margin-top: 10px;">🔒 Bảo Mật & Air-Gapped</h3>
          <p class="card-desc"><strong>Mã nguồn nhạy cảm:</strong> NDA và dữ liệu khách hàng cấm tuyệt đối gửi code lên cloud công cộng.</p>
          <p class="card-desc" style="margin-top: 8px;"><strong>Chạy 100% Offline:</strong> Suy luận mã nguồn trực tiếp trên GPU máy trạm.</p>
          <p class="card-desc" style="margin-top: 8px;"><strong>Zero Data Retention:</strong> Không rủi ro bị dùng để train lại model.</p>
        </div>

        <div class="box-card box-card-highlight" style="border-top: 3px solid var(--accent-success);">
          <span class="badge-pill pill-green">TRỤ CỘT 2</span>
          <h3 class="card-heading" style="margin-top: 10px;">💰 Tiết Kiệm 100% Phí API</h3>
          <p class="card-desc"><strong>Token API đắt đỏ:</strong> Claude 3.5 Sonnet ngốn chi phí khi agent chạy vòng lặp debug nhiều lần.</p>
          <p class="card-desc" style="margin-top: 8px;"><strong>Zero Cost với Ollama:</strong> Tận dụng Qwen 2.5 Coder, DeepSeek-R1, Llama 3 hoàn toàn miễn phí.</p>
          <p class="card-desc" style="margin-top: 8px;"><strong>Không lo Rate Limits:</strong> Tự do gõ lệnh không giới hạn quota.</p>
        </div>

        <div class="box-card" style="border-top: 3px solid var(--accent-secondary);">
          <span class="badge-pill pill-cyan">TRỤ CỘT 3</span>
          <h3 class="card-heading" style="margin-top: 10px;">⚡ Giữ Trọn Workflow Agent</h3>
          <p class="card-desc"><strong>Vỏ Agent Claude Code:</strong> Tận dụng trọn bộ khả năng đọc file, sửa code, chạy lệnh bash cực mượt.</p>
          <p class="card-desc" style="margin-top: 8px;"><strong>Tự do đổi Model:</strong> Dễ dàng switch model theo từng bài toán kỹ thuật.</p>
          <p class="card-desc" style="margin-top: 8px;"><strong>Tự chủ công nghệ:</strong> Không phụ thuộc vào sự cố nghẽn mạng từ Cloud.</p>
        </div>
      </div>
    </div>

    <!-- SLIDE 7: INTEGRATION CLAUDE CODE + OLLAMA -->
    <div class="slide" data-slide="7" data-notes="Nghe thì có vẻ phức tạp nhưng thực tế tích hợp chỉ mất đúng 5 giây với 1 dòng lệnh duy nhất. Nhờ Ollama mới đây đã hỗ trợ native giao thức Anthropic Messages API, việc cầu nối giữa Claude Code và Ollama diễn ra hoàn toàn trong suốt. Cách đơn giản nhất: Anh em chỉ cần gõ 'ollama launch claude --model qwen2.5-coder'. Ollama sẽ tự động bridge và mở giao diện Claude Code kết nối trực tiếp vào model máy bạn. Hoặc nếu muốn cấu hình thủ công trong profile bash/zsh, anh em chỉ cần set 2 biến môi trường: gán ANTHROPIC_BASE_URL trỏ về localhost:11434 và ANTHROPIC_AUTH_TOKEN bằng ollama. Sau đó cứ gõ lệnh 'claude' bình thường! Agent vẫn tự động đọc file, tạo commit, chạy bash script và tìm kiếm code như khi dùng Claude 3.5 Sonnet xịn. Chỉ với một dòng lệnh, anh em đã sở hữu một AI Coding Agent độc lập, bảo mật và hoàn toàn miễn phí trên chính máy của mình.">
      <span class="slide-eyebrow eyebrow-cyan">🛠️ THỰC CHIẾN TÍCH HỢP • NATIVE ANTHROPIC API BRIDGE</span>
      <h2 class="slide-title">Cách Tích Hợp Model Vào Claude Code</h2>
      <p class="slide-subtitle">Cấu hình ghép nối Ollama với Claude Code qua 2 phương pháp tiện lợi.</p>

      <div class="grid-2">
        <div class="terminal-box">
          <div class="terminal-header">
            <div class="terminal-dots">
              <span class="dot-red"></span>
              <span class="dot-yellow"></span>
              <span class="dot-green"></span>
            </div>
            <span class="terminal-title">Cách 1: Ollama CLI Launch (Khuyên dùng)</span>
          </div>
          <div class="terminal-body">
            <span class="code-comment"># Khởi chạy Claude Code với model mặc định</span><br>
            <span class="code-prompt">$</span> <span class="code-command">ollama launch claude</span><br><br>
            <span class="code-comment"># Chỉ định model coding chuyên sâu (Qwen 2.5 Coder)</span><br>
            <span class="code-prompt">$</span> <span class="code-command">ollama launch claude --model qwen2.5-coder</span><br><br>
            <span class="code-comment"># Tự động đồng ý & dùng cho CI/CD Script</span><br>
            <span class="code-prompt">$</span> <span class="code-command">ollama launch claude --model qwen2.5-coder --yes</span><br><br>
            <span class="code-output" style="color: #34d399;">✔ Connected to local Ollama server (port 11434)</span>
          </div>
        </div>

        <div class="terminal-box">
          <div class="terminal-header">
            <div class="terminal-dots">
              <span class="dot-red"></span>
              <span class="dot-yellow"></span>
              <span class="dot-green"></span>
            </div>
            <span class="terminal-title">Cách 2: Biến Môi Trường (Environment Variables)</span>
          </div>
          <div class="terminal-body">
            <span class="code-comment"># Cấu hình trên Linux / macOS (~/.zshrc)</span><br>
            <span class="code-command">export ANTHROPIC_AUTH_TOKEN=ollama</span><br>
            <span class="code-command">export ANTHROPIC_BASE_URL=http://localhost:11434</span><br><br>
            <span class="code-comment"># Khởi chạy Claude Code bình thường</span><br>
            <span class="code-prompt">$</span> <span class="code-command">claude --model qwen2.5-coder</span><br><br>
            <span class="code-comment"># Cấu hình trên Windows PowerShell</span><br>
            <span class="code-command">$env:ANTHROPIC_AUTH_TOKEN="ollama"</span><br>
            <span class="code-command">$env:ANTHROPIC_BASE_URL="http://localhost:11434"</span>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 8: SUMMARY & Q&A -->
    <div class="slide" data-slide="8" data-notes="Để khép lại bài chia sẻ hôm nay, mình muốn nhắn nhủ một điều: Công nghệ AI sinh ra là để phục vụ chúng ta, giúp chúng ta làm việc thông minh hơn chứ không phải ngồi gò lưng canh chừng máy tính nhiều hơn. Cả Antigravity Remote Control, App Settings và Claude Code tích hợp Ollama đều cùng hướng tới một mục tiêu duy nhất: Tự động hóa triệt để và an tâm tuyệt đối. Ngay sau buổi này, anh em chỉ cần dành 30 giây làm 3 việc: Một là gạt bật Remote Control trên Antigravity để sẵn sàng lái agent từ điện thoại. Hai là bật Prevent Sleep và Menu Bar resident. Và ba là thử gõ 'ollama launch claude' để trải nghiệm coding agent offline cực kỳ mạnh mẽ. Cảm ơn tất cả anh em đã theo dõi! Bây giờ mình xin mở phần Q&A, anh em có câu hỏi hay muốn cùng quét QR thử nghiệm trực tiếp thì chúng ta cùng thảo luận nhé!">
      <span class="slide-eyebrow eyebrow-indigo">🏁 TỔNG KẾT & HÀNH ĐỘNG • Q&A</span>
      <h2 class="slide-title">Bộ Hành Trang Kỹ Sư Tương Lai</h2>
      <p class="slide-subtitle">Checklist tối ưu quy trình làm việc với AI Agent – Setup 1 lần, thảnh thơi cả ngày.</p>

      <div class="grid-3">
        <div class="box-card" style="border-left: 4px solid var(--accent-secondary);">
          <span class="card-header-icon">📱</span>
          <h3 class="card-heading">1. Remote Control</h3>
          <p class="card-desc">Bật sẵn sàng trên máy tính công ty để tự do di chuyển, giám sát tiến độ và duyệt code trên điện thoại.</p>
        </div>

        <div class="box-card box-card-highlight" style="border-left: 4px solid var(--accent-success);">
          <span class="card-header-icon">☕</span>
          <h3 class="card-heading">2. Prevent Sleep</h3>
          <p class="card-desc">Chống ngủ máy, kết hợp neo khay Menu Bar để ứng dụng thường trực và nhận thông báo OS tức thời.</p>
        </div>

        <div class="box-card" style="border-left: 4px solid var(--accent-primary);">
          <span class="card-header-icon">🚀</span>
          <h3 class="card-heading">3. Claude Code + Ollama</h3>
          <p class="card-desc">Bảo vệ 100% dữ liệu nhạy cảm, chạy model mã nguồn mở miễn phí token nhưng giữ nguyên sức mạnh agentic.</p>
        </div>
      </div>

      <div class="box-card box-card-highlight" style="margin-top: 16px; text-align: center; border: 1px dashed var(--accent-secondary);">
        <h3 class="card-heading" style="color: var(--accent-secondary); font-size: 1.15rem;">💬 CẢM ƠN ANH EM ĐÃ LẮNG NGHE! CHÚNG TA CÙNG THẢO LUẬN & DEMO TRỰC TIẾP NHÉ!</h3>
      </div>
    </div>
"""

full_html = template
full_html = full_html.replace("{{PRESENTATION_TITLE}}", "Antigravity Remote Control, App Settings & Claude Code Integration")
full_html = full_html.replace("{{THEME_CLASS}}", "theme-cyber-dark")
full_html = full_html.replace("{{TOPIC_TAG}}", "DEVELOPER MASTERCLASS")
full_html = full_html.replace("{{SERIES_TITLE}}", "AI Agentic Development Series")
full_html = full_html.replace("{{TOTAL_SLIDES}}", "08")
full_html = full_html.replace("{{COPYRIGHT_TEXT}}", "Bản quyền Đào Tạo Kỹ Thuật Nội Bộ • 2026")
full_html = full_html.replace("{{SLIDES_CONTENT}}", slides_html)

output_html = r"d:\Project\training-ai\bai-2.5-tao-slide\slide_antigravity_claude_code.html"
with open(output_html, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"HTML presentation created at: {output_html}")
