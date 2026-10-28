import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette - Cyber Dark Luxury
    BG_DARK = RGBColor(9, 13, 22)        # #090D16
    CARD_BG = RGBColor(19, 27, 46)       # #131B2E
    CARD_BG_ALT = RGBColor(15, 23, 42)   # #0F172A
    CARD_BORDER = RGBColor(51, 65, 85)   # #334155
    BORDER_GLOW = RGBColor(99, 102, 241) # #6366F1
    TEXT_WHITE = RGBColor(248, 250, 252) # #F8FAFC
    TEXT_MUTED = RGBColor(148, 163, 184)# #94A3B8
    TEXT_DIM = RGBColor(100, 116, 139)   # #64748B
    
    ACCENT_INDIGO = RGBColor(129, 140, 248) # #818CF8
    ACCENT_CYAN = RGBColor(56, 189, 248)    # #38BDF8
    ACCENT_GREEN = RGBColor(52, 211, 153)   # #34D399
    ACCENT_RED = RGBColor(244, 63, 94)      # #F43F5E
    ACCENT_AMBER = RGBColor(245, 158, 11)   # #F59E0B
    CODE_BG = RGBColor(5, 8, 17)            # #050811

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background() # no line

    def add_top_decorations(slide, slide_num, total_slides=8, tag="DEVELOPER MASTERCLASS • 7 PHÚT"):
        # Top banner text
        top_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(10), Inches(0.4))
        tf = top_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = tag.upper()
        p.font.name = "Segoe UI"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = ACCENT_INDIGO

        # Slide indicator
        num_box = slide.shapes.add_textbox(Inches(11.0), Inches(0.4), Inches(1.5), Inches(0.4))
        ntf = num_box.text_frame
        np = ntf.paragraphs[0]
        np.text = f"{slide_num:02d} / {total_slides:02d}"
        np.alignment = PP_ALIGN.RIGHT
        np.font.name = "Consolas"
        np.font.size = Pt(11)
        np.font.bold = True
        np.font.color.rgb = ACCENT_CYAN

        # Bottom footer
        foot_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.7), Inches(0.3))
        ftf = foot_box.text_frame
        fp = ftf.paragraphs[0]
        fp.text = "Google Antigravity & Claude Code • Internal Tech Sharing • 2026"
        fp.font.name = "Segoe UI"
        fp.font.size = Pt(9)
        fp.font.color.rgb = TEXT_DIM

    def add_header(slide, title, subtitle=None):
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(1.1))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Segoe UI"
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        
        if subtitle:
            p2 = tf.add_paragraph()
            p2.text = subtitle
            p2.font.name = "Segoe UI"
            p2.font.size = Pt(13)
            p2.font.color.rgb = TEXT_MUTED
            p2.space_before = Pt(4)

    def add_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # =========================================================================
    # SLIDE 1: COVER / HERO SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)
    add_top_decorations(s1, 1, 8, "⚡ CHUYÊN ĐỀ CÔNG NGHỆ NỘI BỘ • 7 PHÚT")

    # Title Hero
    tbox = s1.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(11.7), Inches(2.2))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "Tối Ưu Hóa Trải Nghiệm Phát Triển Với AI"
    p.font.name = "Segoe UI"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Làm Chủ Antigravity Remote Control, App Settings & Tích Hợp Claude Code"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_CYAN
    p2.space_before = Pt(6)

    p3 = tf1.add_paragraph()
    p3.text = "Giải phóng kỹ sư khỏi bàn làm việc, bảo vệ dữ liệu tuyệt đối và làm chủ luồng thực thi tự hành."
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(8)

    # 2 Comparison Cards (Problem vs Solution)
    card1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.6), Inches(5.7), Inches(3.1))
    card1.fill.solid()
    card1.fill.fore_color.rgb = CARD_BG
    card1.line.color.rgb = ACCENT_RED
    card1.line.width = Pt(1.5)
    
    ctf1 = card1.text_frame
    ctf1.word_wrap = True
    ctf1.margin_left = ctf1.margin_right = ctf1.margin_top = Inches(0.3)
    cp1 = ctf1.paragraphs[0]
    cp1.text = "⚠️  Thực Trạng & Rào Cản Thường Gặp"
    cp1.font.name = "Segoe UI"
    cp1.font.size = Pt(16)
    cp1.font.bold = True
    cp1.font.color.rgb = ACCENT_RED

    bullets_c1 = [
        ("Máy ngủ gật (Sleep Mode):", " AI đang chạy task dài, máy tự tắt làm đứt kết nối."),
        ("Bị xích vào bàn làm việc:", " Phải ngồi canh máy chỉ để bấm Approve prompt."),
        ("Tắt nhầm cửa sổ:", " Đóng app làm mất context phiên làm việc."),
        ("Chi phí API & Rò rỉ code:", " Dùng cloud agent lo ngại lộ source code mật.")
    ]
    for b_title, b_desc in bullets_c1:
        bp = ctf1.add_paragraph()
        bp.space_before = Pt(8)
        run1 = bp.add_run()
        run1.text = "❌ " + b_title
        run1.font.bold = True
        run1.font.size = Pt(11.5)
        run1.font.color.rgb = TEXT_WHITE
        run2 = bp.add_run()
        run2.text = b_desc
        run2.font.size = Pt(11)
        run2.font.color.rgb = TEXT_MUTED

    # Card 2 (Target)
    card2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.6), Inches(5.7), Inches(3.1))
    card2.fill.solid()
    card2.fill.fore_color.rgb = CARD_BG
    card2.line.color.rgb = ACCENT_GREEN
    card2.line.width = Pt(1.5)

    ctf2 = card2.text_frame
    ctf2.word_wrap = True
    ctf2.margin_left = ctf2.margin_right = ctf2.margin_top = Inches(0.3)
    cp2 = ctf2.paragraphs[0]
    cp2.text = "🚀  Mục Tiêu & Chuẩn Thực Chiến 2026"
    cp2.font.name = "Segoe UI"
    cp2.font.size = Pt(16)
    cp2.font.bold = True
    cp2.font.color.rgb = ACCENT_GREEN

    bullets_c2 = [
        ("Remote Control linh hoạt:", " Quản lý Agent trên PC từ điện thoại di động mọi lúc."),
        ("Prevent Sleep:", " Giữ máy luôn thức trong lúc Agent viết code ngầm xuyên đêm."),
        ("Keep In Menu Bar:", " Thường trực trên thanh hệ thống, mở ra ngay lập tức."),
        ("Local LLMs via Ollama:", " Tích hợp model nội bộ vào Claude Code 0% phí token & bảo mật 100%.")
    ]
    for b_title, b_desc in bullets_c2:
        bp = ctf2.add_paragraph()
        bp.space_before = Pt(8)
        run1 = bp.add_run()
        run1.text = "✅ " + b_title
        run1.font.bold = True
        run1.font.size = Pt(11.5)
        run1.font.color.rgb = TEXT_WHITE
        run2 = bp.add_run()
        run2.text = b_desc
        run2.font.size = Pt(11)
        run2.font.color.rgb = TEXT_MUTED

    add_notes(s1, """[LỜI THOẠI DIỄN GIẢ - 0:00 - 0:55]
(Hook) Chào anh em! Chắc hẳn ai trong chúng ta khi dùng Antigravity chạy những task lớn như refactor cả module hay sinh hàng chục test cases đều từng gặp cảnh: vừa đi uống cốc cà phê quay lại thì máy tính đã ngủ gật, AI bị ngắt quãng giữa chừng, hoặc phải ngồi dán mắt vào màn hình chỉ để chờ bấm Approve.
(Why) Chúng ta đang dùng AI để giải phóng sức lao động nhưng lại vô tình bị xích vào bàn làm việc vì những thiết lập mặc định chưa tối ưu.
(How) Trong đúng 7 phút hôm nay, mình sẽ chia sẻ với anh em 2 vũ khí cực mạnh: tính năng Remote Control điều khiển từ xa, bộ 3 thiết lập App Settings sống còn, và phần bonus đặc biệt: cách chạy Claude Code với Model bên thứ 3 hoàn toàn miễn phí, bảo mật qua Ollama.
(Takeaway) Nắm vững những tính năng này, anh em sẽ biến công cụ AI thành một trợ lý tự hành đúng nghĩa, làm việc xuyên suốt mọi lúc mọi nơi.""")

    # =========================================================================
    # SLIDE 2: ANTIGRAVITY REMOTE CONTROL OVERVIEW
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_top_decorations(s2, 2, 8, "🌐 TÍNH NĂNG ĐỘT PHÁ • CROSS-DEVICE AGENT")
    add_header(s2, "Antigravity Remote Control Là Gì?", "Giải pháp lái, giám sát và tương tác với AI Agent từ xa trên mọi thiết bị.")

    # 2 Comparison Columns
    col1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(5.7), Inches(4.5))
    col1.fill.solid()
    col1.fill.fore_color.rgb = CARD_BG
    col1.line.color.rgb = CARD_BORDER
    col1.line.width = Pt(1)

    tf_c1 = col1.text_frame
    tf_c1.word_wrap = True
    tf_c1.margin_left = tf_c1.margin_right = tf_c1.margin_top = Inches(0.3)
    p = tf_c1.paragraphs[0]
    p.text = "🏢 Cách Làm Cũ (Workstation Bound)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER

    items_c1 = [
        ("Gò bó vị trí:", " Phải ngồi trực tiếp trước màn hình máy tính công ty để xem Agent sinh code."),
        ("Gián đoạn khi di chuyển:", " Rời bàn làm việc đi họp, đi ăn trưa là hoàn toàn mù thông tin về tiến độ."),
        ("Phê duyệt thủ công chậm trễ:", " Agent dừng lại chờ câu trả lời xác nhận (Approve prompt / Bash tool), cả quy trình bị tắc nghẽn."),
        ("Remote Desktop cồng kềnh:", " Dùng TeamViewer, AnyDesk ngốn băng thông, lag giật trên điện thoại.")
    ]
    for it_title, it_desc in items_c1:
        p = tf_c1.add_paragraph()
        p.space_before = Pt(12)
        r1 = p.add_run()
        r1.text = "• " + it_title
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = it_desc
        r2.font.size = Pt(11.5)
        r2.font.color.rgb = TEXT_MUTED

    col2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.2), Inches(5.7), Inches(4.5))
    col2.fill.solid()
    col2.fill.fore_color.rgb = CARD_BG
    col2.line.color.rgb = BORDER_GLOW
    col2.line.width = Pt(1.5)

    tf_c2 = col2.text_frame
    tf_c2.word_wrap = True
    tf_c2.margin_left = tf_c2.margin_right = tf_c2.margin_top = Inches(0.3)
    p = tf_c2.paragraphs[0]
    p.text = "⚡ Chuẩn Remote Control (Bất Kỳ Đâu)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    items_c2 = [
        ("Mobile First Web UI:", " Giao diện web siêu nhẹ trên smartphone, tối ưu hóa cho màn hình cảm ứng."),
        ("Theo dõi Artifacts Thời Gian Thực:", " Xem file diff, tiến độ subagent, command logs trực tiếp khi đang di chuyển."),
        ("Tương tác & Phê duyệt 1 chạm:", " Nhấn 'Approve' hoặc gõ hướng dẫn bổ sung cho Agent ngay từ điện thoại."),
        ("Giữ trọn môi trường Local:", " Máy trạm chịu trách nhiệm build, test, git; điện thoại đóng vai trò remote dashboard.")
    ]
    for it_title, it_desc in items_c2:
        p = tf_c2.add_paragraph()
        p.space_before = Pt(12)
        r1 = p.add_run()
        r1.text = "✔ " + it_title
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = ACCENT_GREEN
        r2 = p.add_run()
        r2.text = it_desc
        r2.font.size = Pt(11.5)
        r2.font.color.rgb = TEXT_MUTED

    add_notes(s2, """[LỜI THOẠI DIỄN GIẢ - 0:55 - 1:55]
(Hook) Anh em có bao giờ ước: máy công ty cấu hình khủng cứ việc build code, còn mình thì ra quán trà sữa hay đi họp vẫn check được AI đang viết tới đâu chưa?
(Why) Remote Control sinh ra chính là để giải quyết bài toán đó. Nó không phải là một công cụ remote desktop nặng nề như TeamViewer hay AnyDesk, mà là cầu nối giao diện web trực tiếp vào chính session Antigravity đang chạy trên workstation của anh em.
(How) Toàn bộ mã nguồn, git branch, terminal và công cụ build vẫn chạy 100% tại máy trạm, nhưng giao diện điều khiển, danh sách artifacts và khung chat lại hiển thị mượt mà trên trình duyệt điện thoại hoặc laptop cá nhân. Anh em có thể review diff, ấn duyệt lệnh bash hay prompt bổ sung chỉ bằng một chạm trên điện thoại.
(Takeaway) Remote Control biến cỗ máy bàn của bạn thành server AI cá nhân mà bạn nắm trọn trong lòng bàn tay.""")

    # =========================================================================
    # SLIDE 3: CƠ CHẾ KẾT NỐI & BẢO MẬT
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_top_decorations(s3, 3, 8, "🔐 CƠ CHẾ VẬN HÀNH • BẢO MẬT ZERO TRUST")
    add_header(s3, "Cơ Chế Ghép Nối & Kiến Trúc Bảo Mật", "Cách bật Remote Control trong 10 giây và kiến trúc bảo vệ dữ liệu doanh nghiệp.")

    # 3 Steps Cards
    card_w = Inches(3.7)
    card_h = Inches(4.5)
    card_y = Inches(2.2)

    # Step 1
    c1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), card_y, card_w, card_h)
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = CARD_BORDER
    tfc1 = c1.text_frame
    tfc1.word_wrap = True
    tfc1.margin_left = tfc1.margin_right = tfc1.margin_top = Inches(0.25)
    p = tfc1.paragraphs[0]
    p.text = "BƯỚC 1: KÍCH HOẠT"
    p.font.name = "Segoe UI"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p2 = tfc1.add_paragraph()
    p2.text = "⚙️ Bật Trong Settings"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(17)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(4)

    s1_details = [
        ("Mở Settings:", " Phím tắt Ctrl + , (Windows/Linux) hoặc Cmd + , (macOS)."),
        ("Chọn mục Application:", " Danh mục cấu hình hệ thống cấp ứng dụng."),
        ("Gạt toggle:", " Chuyển 'Enable Remote Control' sang ON."),
        ("Lệnh CLI tương đương:", " Gõ 'agy --remote-control' hoặc slash command '/remote-control'.")
    ]
    for dt, dd in s1_details:
        p = tfc1.add_paragraph()
        p.space_before = Pt(8)
        r1 = p.add_run()
        r1.text = "• " + dt
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = dd
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = TEXT_MUTED

    # Step 2
    c2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), card_y, card_w, card_h)
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = BORDER_GLOW
    c2.line.width = Pt(1.5)
    tfc2 = c2.text_frame
    tfc2.word_wrap = True
    tfc2.margin_left = tfc2.margin_right = tfc2.margin_top = Inches(0.25)
    p = tfc2.paragraphs[0]
    p.text = "BƯỚC 2: GHÉP NỐI"
    p.font.name = "Segoe UI"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_INDIGO
    p2 = tfc2.add_paragraph()
    p2.text = "📱 Quét QR Code & URL"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(17)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(4)

    s2_details = [
        ("Mã QR bảo mật:", " Máy tính sinh ngay một QR Handshake động trên màn hình."),
        ("Quét bằng Camera:", " Dùng camera điện thoại quét mã để mở ngay session trong 2 giây."),
        ("Truy cập qua Web:", " Vào antigravity.google và đăng nhập Google Account."),
        ("Quản lý Host:", " Dashboard liệt kê toàn bộ các máy trạm đang mở quyền Remote.")
    ]
    for dt, dd in s2_details:
        p = tfc2.add_paragraph()
        p.space_before = Pt(8)
        r1 = p.add_run()
        r1.text = "• " + dt
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = dd
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = TEXT_MUTED

    # Step 3
    c3 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.8), card_y, card_w, card_h)
    c3.fill.solid()
    c3.fill.fore_color.rgb = CARD_BG
    c3.line.color.rgb = CARD_BORDER
    tfc3 = c3.text_frame
    tfc3.word_wrap = True
    tfc3.margin_left = tfc3.margin_right = tfc3.margin_top = Inches(0.25)
    p = tfc3.paragraphs[0]
    p.text = "TIÊU CHUẨN AN TOÀN"
    p.font.name = "Segoe UI"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p2 = tfc3.add_paragraph()
    p2.text = "🛡️ Bảo Mật Doanh Nghiệp"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(17)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(4)

    s3_details = [
        ("Token Handshake:", " Mã xác thực dùng 1 lần, chống dò quét IP trái phép."),
        ("Không mở Open Port:", " Hoạt động an toàn sau tường lửa (Firewall) và VPN công ty."),
        ("Google Account SSO:", " Hỗ trợ Google Workspace công ty và Workload Identity Federation."),
        ("Boundary An Toàn:", " Mã nguồn, token Git, secrets nằm nguyên vẹn tại máy trạm.")
    ]
    for dt, dd in s3_details:
        p = tfc3.add_paragraph()
        p.space_before = Pt(8)
        r1 = p.add_run()
        r1.text = "• " + dt
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = dd
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = TEXT_MUTED

    add_notes(s3, """[LỜI THOẠI DIỄN GIẢ - 1:55 - 3:00]
(Hook) Nhiều anh em sẽ hỏi: 'Remote như vậy có lộ mã nguồn công ty ra ngoài không, thiết lập có phức tạp cần mở port modem không?'.
(Why) Câu trả lời là hoàn toàn không. Google thiết kế cơ chế ghép nối này theo triết lý Zero Trust cực kỳ nghiêm ngặt.
(How) Bước 1: Anh em mở Settings bằng phím Ctrl + ,, vào mục Application và gạt nút 'Enable Remote Control'. Bước 2: Antigravity sẽ sinh ngay một mã QR Code bảo mật. Anh em chỉ cần giơ camera điện thoại lên quét, hoặc truy cập antigravity.google đăng nhập đúng tài khoản Google là kết nối thành công. Toàn bộ phiên làm việc xác thực bằng Token handshake dùng một lần, dữ liệu truyền tải mã hóa end-to-end và không hề mở bất kỳ open port nào trên router nội bộ.
(Takeaway) Tiện lợi tối đa nhưng bảo mật chuẩn doanh nghiệp – anh em hoàn toàn yên tâm dùng trong mạng công ty.""")

    # =========================================================================
    # SLIDE 4: APP SETTINGS #1 - PREVENT SLEEP
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_top_decorations(s4, 4, 8, "☕ CÀI ĐẶT HỆ THỐNG • LIÊN TỤC KHÔNG GIÁN ĐOẠN")
    add_header(s4, "App Settings: Prevent Sleep", "Ngăn hệ thống tự động tắt màn hình và đưa PC vào chế độ ngủ khi AI đang làm việc.")

    # Left: The Mechanism & Risk
    left_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(6.0), Inches(4.5))
    left_card.fill.solid()
    left_card.fill.fore_color.rgb = CARD_BG
    left_card.line.color.rgb = ACCENT_AMBER
    left_card.line.width = Pt(1.5)
    
    tl = left_card.text_frame
    tl.word_wrap = True
    tl.margin_left = tl.margin_right = tl.margin_top = Inches(0.3)
    p = tl.paragraphs[0]
    p.text = "⚡ Bản Chất Cơ Chế Prevent Sleep"
    p.font.name = "Segoe UI"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER

    points_l = [
        ("Nỗi đau mất kết nối:", " Windows/macOS mặc định chuyển sang Sleep sau 5-15 phút không thao tác bàn phím/chuột. Khi đó tiến trình AI bị suspend, kết nối mạng đứt, task dở dang."),
        ("Cơ chế giữ thức thông minh:", " Khi Agent bắt đầu thực thi chuỗi prompt dài (viết test, refactor, benchmark), Antigravity tự động kích hoạt API ngăn chặn sleep ở cấp OS kernel."),
        ("Tự động trả lại trạng thái thường:", " Ngay khi Agent hoàn tất toàn bộ công việc, hệ thống tự động giải phóng lock để máy tính quay về chế độ tiết kiệm điện bình thường.")
    ]
    for pt, pd in points_l:
        p = tl.add_paragraph()
        p.space_before = Pt(12)
        r1 = p.add_run()
        r1.text = "• " + pt + "\n"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = pd
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_MUTED

    # Right: Code Mockup / Visual Setting Box
    right_card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(2.2), Inches(5.4), Inches(4.5))
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = CODE_BG
    right_card.line.color.rgb = CARD_BORDER
    
    tr = right_card.text_frame
    tr.word_wrap = True
    tr.margin_left = tr.margin_right = tr.margin_top = Inches(0.3)
    p = tr.paragraphs[0]
    p.text = "SETTINGS > APPLICATION"
    p.font.name = "Consolas"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    p2 = tr.add_paragraph()
    p2.text = "[UI Preview: System Settings Panel]"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(15)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(8)

    mockup_lines = [
        ("[X] Prevent Sleep", "Keep PC awake while AI agent generates code"),
        ("    Status: ACTIVE (Agent Working...)", "System sleep lock acquired"),
        ("[X] Keep In Menu Bar", "Remain in Windows Taskbar Tray / macOS Menu Bar"),
        ("    Close button: MINIMIZE TO TRAY", "Never kill background agent accidentally"),
        ("[i] Notification Settings", "Configured in Windows/macOS System Settings")
    ]
    for title_line, sub_line in mockup_lines:
        p = tr.add_paragraph()
        p.space_before = Pt(10)
        r1 = p.add_run()
        r1.text = title_line + "\n"
        r1.font.name = "Consolas"
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = ACCENT_GREEN if "[X]" in title_line else (ACCENT_AMBER if "ACTIVE" in title_line else ACCENT_INDIGO)
        r2 = p.add_run()
        r2.text = "   " + sub_line
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = TEXT_MUTED

    add_notes(s4, """[LỜI THOẠI DIỄN GIẢ - 3:00 - 4:05]
(Hook) Đã bao giờ anh em giao cho Agent một task lớn trước khi đi ăn trưa, quay lại thấy màn hình đen ngòm và task bị failed vì máy rơi vào Sleep Mode chưa?
(Why) Mặc định, Windows và macOS đều có chính sách tiết kiệm điện tự động ngủ sau một khoảng thời gian người dùng không gõ phím hay rê chuột. Nhưng với AI Coding Agent, lúc chúng ta không chạm vào máy lại chính là lúc nó đang làm việc vất vả nhất.
(How) Tính năng 'Prevent Sleep' trong App Settings ra đời để giải quyết tận gốc vấn đề này. Khi được bật, Antigravity sẽ gửi tín hiệu giữ màn hình và hệ thống luôn thức (Awake) trong suốt thời gian Agent đang sinh mã hoặc chạy test. Khi Agent hoàn thành xong toàn bộ công việc, hệ thống mới quay trở lại cơ chế sleep bình thường.
(Takeaway) Hãy bật 'Prevent Sleep' ngay hôm nay để yên tâm giao việc lớn xuyên đêm mà không lo đứt gánh giữa đường.""")

    # =========================================================================
    # SLIDE 5: APP SETTINGS #2 & #3 - KEEP IN MENU BAR & NOTIFICATIONS
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_top_decorations(s5, 5, 8, "📌 CÀI ĐẶT HỆ THỐNG • THƯỜNG TRỰC & THÔNG BÁO")
    add_header(s5, "Keep In Menu Bar & Notification Settings", "Đảm bảo ứng dụng luôn thường trực tức thì và không bỏ lỡ thông báo quan trọng.")

    col5_1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(5.7), Inches(4.5))
    col5_1.fill.solid()
    col5_1.fill.fore_color.rgb = CARD_BG
    col5_1.line.color.rgb = BORDER_GLOW
    col5_1.line.width = Pt(1.5)
    
    t5_1 = col5_1.text_frame
    t5_1.word_wrap = True
    t5_1.margin_left = t5_1.margin_right = t5_1.margin_top = Inches(0.3)
    p = t5_1.paragraphs[0]
    p.text = "📌 Keep In Menu Bar (Taskbar Tray)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = ACCENT_INDIGO

    f1 = [
        ("Thói quen bấm 'X' tai hại:", " Đóng cửa sổ không làm tắt ứng dụng mà chỉ ẩn xuống Tray hệ thống."),
        ("Thường trực sẵn sàng:", " Antigravity luôn chạy nền, có thể gọi lên (summon) tức thì bằng phím tắt hoặc 1 click chuột."),
        ("Không mất Context:", " Giữ nguyên trạng thái agent, lịch sử terminal và các tab công việc đang mở."),
        ("Tối ưu RAM/CPU:", " Ứng dụng đưa về trạng thái tối giản khi ẩn ở khay hệ thống.")
    ]
    for ft, fd in f1:
        p = t5_1.add_paragraph()
        p.space_before = Pt(12)
        r1 = p.add_run()
        r1.text = "✔ " + ft + "\n"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = fd
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_MUTED

    col5_2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.2), Inches(5.7), Inches(4.5))
    col5_2.fill.solid()
    col5_2.fill.fore_color.rgb = CARD_BG
    col5_2.line.color.rgb = CARD_BORDER
    col5_2.line.width = Pt(1)
    
    t5_2 = col5_2.text_frame
    t5_2.word_wrap = True
    t5_2.margin_left = t5_2.margin_right = t5_2.margin_top = Inches(0.3)
    p = t5_2.paragraphs[0]
    p.text = "🔔 Quản Lý Thông Báo (OS-Level)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    f2 = [
        ("Lưu ý kiến trúc cốt lõi:", " Antigravity không chứa công tắc bật/tắt thông báo trong app mà đẩy về quản lý tập trung ở Hệ điều hành."),
        ("Cấu hình trên Windows:", " Start > Settings > System > Notifications > Bật quyền cho Antigravity."),
        ("Cấu hình trên macOS:", " System Settings > Notifications > Antigravity > Allow Notifications."),
        ("Nhận báo cáo tức thì:", " Được ping thông báo ngay khi Agent hoàn thành task lớn hoặc khi cần người dùng bấm xác nhận.")
    ]
    for ft, fd in f2:
        p = t5_2.add_paragraph()
        p.space_before = Pt(12)
        r1 = p.add_run()
        r1.text = "✔ " + ft + "\n"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = fd
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_MUTED

    add_notes(s5, """[LỜI THOẠI DIỄN GIẢ - 4:05 - 5:10]
(Hook) Có hai điều nhỏ nhưng ảnh hưởng cực lớn đến trải nghiệm hàng ngày của anh em: tắt nhầm cửa sổ và lỡ mất thông báo quan trọng.
(Why) Thứ nhất, thói quen bấm nút 'X' để đóng cửa sổ thường vô tình tắt luôn cả ứng dụng đang chạy. Thứ hai, nhiều người tìm mãi trong app không thấy chỗ bật âm báo.
(How) Về tính năng 'Keep In Menu Bar': Khi bật lên, Antigravity sẽ neo thường trực trên khay hệ thống (Windows Taskbar Tray) hoặc Mac Menu Bar. Bấm nút 'X' chỉ là ẩn cửa sổ, app vẫn sống ngầm và sẵn sàng bật lên tức thì bằng phím tắt mà không cần khởi động lại. Về 'Notification Settings': Anh em cần lưu ý, Antigravity không tự quản lý toggle thông báo bên trong app mà đẩy toàn quyền về Settings của Windows/macOS. Anh em chỉ cần cấp quyền thông báo cho Antigravity trong OS Settings là mỗi khi AI xong task hoặc cần duyệt, máy tính và điện thoại đều sẽ ting ting báo ngay.
(Takeaway) Setup đúng 2 mục này giúp anh em luôn phản hồi kịp thời mà không tốn công chờ đợi.""")

    # =========================================================================
    # SLIDE 6: TẠI SAO CẦN MODEL BÊN THỨ 3 VÀO CLAUDE CODE?
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_top_decorations(s6, 6, 8, "💡 MỞ RỘNG ĐỘT PHÁ • CLAUDE CODE & LOCAL LLM")
    add_header(s6, "Tại Sao Cần Đưa Model Bên Thứ 3 Vào Claude Code?", "Kết hợp trí tuệ mã nguồn mở với framework CLI Agentic số 1 hiện nay.")

    # 3 Columns
    col6_1 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(3.7), Inches(4.5))
    col6_1.fill.solid()
    col6_1.fill.fore_color.rgb = CARD_BG
    col6_1.line.color.rgb = ACCENT_RED
    col6_1.line.width = Pt(1.5)
    t6_1 = col6_1.text_frame
    t6_1.word_wrap = True
    t6_1.margin_left = t6_1.margin_right = t6_1.margin_top = Inches(0.25)
    p = t6_1.paragraphs[0]
    p.text = "TRỤ CỘT 1"
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED
    p2 = t6_1.add_paragraph()
    p2.text = "🔒 Bảo Mật & Air-Gapped"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(16)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(4)
    r_items = [
        ("Mã nguồn dự án mật:", " NDA và bảo mật khách hàng cấm tuyệt đối gửi code lên cloud."),
        ("Chạy 100% Offline:", " Toàn bộ suy luận xử lý ngay trên GPU máy trạm của công ty."),
        ("Không lưu vết:", " Không có dữ liệu nào bị dùng để train lại model của bên thứ ba.")
    ]
    for it, idesc in r_items:
        p = t6_1.add_paragraph()
        p.space_before = Pt(10)
        r1 = p.add_run()
        r1.text = "• " + it + "\n"
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = idesc
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = TEXT_MUTED

    col6_2 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), Inches(2.2), Inches(3.7), Inches(4.5))
    col6_2.fill.solid()
    col6_2.fill.fore_color.rgb = CARD_BG
    col6_2.line.color.rgb = ACCENT_GREEN
    col6_2.line.width = Pt(1.5)
    t6_2 = col6_2.text_frame
    t6_2.word_wrap = True
    t6_2.margin_left = t6_2.margin_right = t6_2.margin_top = Inches(0.25)
    p = t6_2.paragraphs[0]
    p.text = "TRỤ CỘT 2"
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p2 = t6_2.add_paragraph()
    p2.text = "💰 Tiết Kiệm 100% Phí API"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(16)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(4)
    g_items = [
        ("Chi phí token đắt đỏ:", " Claude 3.5 Sonnet / Opus ngốn ngân sách khi debug lặp lại nhiều lần."),
        ("Zero Cost với Ollama:", " Tận dụng model mã nguồn mở như Qwen 2.5 Coder, DeepSeek-R1, Llama 3."),
        ("Không lo Rate Limit:", " Không bị giới hạn số lượt request mỗi phút (TPM / RPM).")
    ]
    for it, idesc in g_items:
        p = t6_2.add_paragraph()
        p.space_before = Pt(10)
        r1 = p.add_run()
        r1.text = "• " + it + "\n"
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = idesc
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = TEXT_MUTED

    col6_3 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.8), Inches(2.2), Inches(3.7), Inches(4.5))
    col6_3.fill.solid()
    col6_3.fill.fore_color.rgb = CARD_BG
    col6_3.line.color.rgb = ACCENT_CYAN
    col6_3.line.width = Pt(1.5)
    t6_3 = col6_3.text_frame
    t6_3.word_wrap = True
    t6_3.margin_left = t6_3.margin_right = t6_3.margin_top = Inches(0.25)
    p = t6_3.paragraphs[0]
    p.text = "TRỤ CỘT 3"
    p.font.name = "Segoe UI"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p2 = t6_3.add_paragraph()
    p2.text = "⚡ Giữ Trọn Workflow Agent"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(16)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(4)
    b_items = [
        ("Vỏ Claude Code Agentic:", " Tận dụng toàn bộ khả năng đọc file, ghi code, chạy bash test cực chuẩn."),
        ("Đa dạng hóa Model:", " Thích model nào thì kéo model đó về (`ollama pull qwen2.5-coder`)."),
        ("Tự chủ công nghệ:", " Không phụ thuộc vào sự cố gián đoạn dịch vụ của nhà cung cấp Cloud.")
    ]
    for it, idesc in b_items:
        p = t6_3.add_paragraph()
        p.space_before = Pt(10)
        r1 = p.add_run()
        r1.text = "• " + it + "\n"
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = idesc
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = TEXT_MUTED

    add_notes(s6, """[LỜI THOẠI DIỄN GIẢ - 5:10 - 6:05]
(Hook) Sau khi đã làm chủ Antigravity, mình muốn chia sẻ thêm một kỹ thuật cực hot trong giới lập trình: Sử dụng Claude Code nhưng chạy bằng Model bên thứ 3 hoặc Model Local qua Ollama. Tại sao chúng ta lại cần điều này?
(Why) Claude Code của Anthropic là một CLI agent xuất sắc nhất hiện nay về khả năng sửa code và chạy terminal, nhưng nó có 2 rào cản lớn: chi phí token API đắt đỏ và chính sách bảo mật dữ liệu công ty không cho phép gửi code lên cloud.
(How) Bằng cách đưa model bên thứ 3 thông qua Ollama, anh em giải quyết được cả 2 bài toán: Thứ nhất, code chạy hoàn toàn local hoặc qua server riêng của công ty, bảo mật 100%. Thứ hai, chi phí token bằng 0 khi dùng các mô hình mã nguồn mở hàng đầu như Qwen 2.5 Coder hay DeepSeek. Chúng ta vừa có 'bộ não' miễn phí/bảo mật, vừa có 'đôi tay' agentic cực kỳ linh hoạt của Claude Code.
(Takeaway) Tận dụng vỏ Claude Code nhưng thay ruột bằng Ollama là cách thông minh nhất để dev thỏa sức dùng AI mà sếp không lo lộ code hay tốn ngân sách.""")

    # =========================================================================
    # SLIDE 7: HƯỚNG DẪN TÍCH HỢP OLLAMA + CLAUDE CODE
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_top_decorations(s7, 7, 8, "🛠️ THỰC CHIẾN TÍCH HỢP • NATIVE ANTHROPIC API BRIDGE")
    add_header(s7, "Cách Tích Hợp Model Vào Claude Code", "Cấu hình ghép nối Ollama với Claude Code qua 2 phương pháp đơn giản.")

    # Left Card: Native CLI Launch
    left_c7 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(5.7), Inches(4.5))
    left_c7.fill.solid()
    left_c7.fill.fore_color.rgb = CODE_BG
    left_c7.line.color.rgb = ACCENT_GREEN
    left_c7.line.width = Pt(1.5)

    tl7 = left_c7.text_frame
    tl7.word_wrap = True
    tl7.margin_left = tl7.margin_right = tl7.margin_top = Inches(0.3)
    p = tl7.paragraphs[0]
    p.text = "CÁCH 1: OLLAMA LAUNCH (1 DÒNG DUY NHẤT)"
    p.font.name = "Consolas"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    p2 = tl7.add_paragraph()
    p2.text = "# Khởi chạy nhanh với model mặc định:\n$ ollama launch claude\n\n# Chỉ định model coding chuyên sâu:\n$ ollama launch claude --model qwen2.5-coder\n\n# Chạy tự động trong CI/CD không hỏi prompt:\n$ ollama launch claude --model qwen2.5-coder --yes"
    p2.font.name = "Consolas"
    p2.font.size = Pt(11)
    p2.font.color.rgb = ACCENT_CYAN
    p2.space_before = Pt(8)

    p3 = tl7.add_paragraph()
    p3.text = "💡 Ưu điểm vượt trội:\n• Ollama tự động thiết lập cầu nối Anthropic Messages API.\n• Tự động tải model nếu chưa có sẵn trong máy.\n• Sẵn sàng làm việc chỉ sau vài giây."
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(11)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(10)

    # Right Card: Manual Environment Variables
    right_c7 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.2), Inches(5.7), Inches(4.5))
    right_c7.fill.solid()
    right_c7.fill.fore_color.rgb = CODE_BG
    right_c7.line.color.rgb = CARD_BORDER
    right_c7.line.width = Pt(1)

    tr7 = right_c7.text_frame
    tr7.word_wrap = True
    tr7.margin_left = tr7.margin_right = tr7.margin_top = Inches(0.3)
    p = tr7.paragraphs[0]
    p.text = "CÁCH 2: CẤU HÌNH BIẾN MÔI TRƯỜNG (ENV VARS)"
    p.font.name = "Consolas"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_INDIGO

    p2 = tr7.add_paragraph()
    p2.text = "# Thiết lập trên Linux / macOS (~/.zshrc hoặc ~/.bashrc):\nexport ANTHROPIC_AUTH_TOKEN=ollama\nexport ANTHROPIC_BASE_URL=http://localhost:11434\n\n# Khởi chạy Claude Code trỏ thẳng vào Ollama:\nclaude --model qwen2.5-coder\n\n# Trên Windows PowerShell:\n$env:ANTHROPIC_AUTH_TOKEN=\"ollama\"\n$env:ANTHROPIC_BASE_URL=\"http://localhost:11434\""
    p2.font.name = "Consolas"
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = ACCENT_INDIGO
    p2.space_before = Pt(8)

    p3 = tr7.add_paragraph()
    p3.text = "💡 Tính năng hỗ trợ toàn diện:\n• Tool calling: Tự động chạy lệnh shell, đọc & sửa file.\n• Subagents: Chia việc cho các agent con chạy song song.\n• /loop schedule: Chạy tác vụ lặp định kỳ (vd: kiểm tra PR)."
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(11)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(10)

    add_notes(s7, """[LỜI THOẠI DIỄN GIẢ - 6:05 - 6:55]
(Hook) Nghe thì có vẻ phức tạp nhưng thực tế tích hợp chỉ mất đúng 5 giây với 1 dòng lệnh duy nhất.
(Why) Nhờ Ollama mới đây đã hỗ trợ native giao thức Anthropic Messages API, việc cầu nối giữa Claude Code và Ollama diễn ra hoàn toàn trong suốt.
(How) Cách đơn giản nhất: Anh em chỉ cần gõ 'ollama launch claude --model qwen2.5-coder'. Ollama sẽ tự động bridge và mở giao diện Claude Code kết nối trực tiếp vào model máy bạn. Hoặc nếu muốn cấu hình thủ công trong profile bash/zsh, anh em chỉ cần set 2 biến môi trường: gán ANTHROPIC_BASE_URL trỏ về localhost:11434 và ANTHROPIC_AUTH_TOKEN bằng ollama. Sau đó cứ gõ lệnh 'claude' bình thường! Agent vẫn tự động đọc file, tạo commit, chạy bash script và tìm kiếm code như khi dùng Claude 3.5 Sonnet xịn.
(Takeaway) Chỉ với một dòng lệnh, anh em đã sở hữu một AI Coding Agent độc lập, bảo mật và hoàn toàn miễn phí trên chính máy của mình.""")

    # =========================================================================
    # SLIDE 8: TỔNG KẾT & Q&A
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_top_decorations(s8, 8, 8, "🏁 TỔNG KẾT & HÀNH ĐỘNG • Q&A")
    add_header(s8, "Bộ Hành Trang Kỹ Sư Tương Lai", "Checklist tối ưu quy trình làm việc với AI Agent – Setup 1 lần, thảnh thơi cả ngày.")

    # 3 Summary Cards
    cw8 = Inches(3.7)
    ch8 = Inches(3.4)
    cy8 = Inches(2.2)

    # Box 1
    b1 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), cy8, cw8, ch8)
    b1.fill.solid()
    b1.fill.fore_color.rgb = CARD_BG
    b1.line.color.rgb = BORDER_GLOW
    b1.line.width = Pt(1.5)
    tb1 = b1.text_frame
    tb1.word_wrap = True
    tb1.margin_left = tb1.margin_right = tb1.margin_top = Inches(0.25)
    p = tb1.paragraphs[0]
    p.text = "1. BẬT REMOTE CONTROL"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p2 = tb1.add_paragraph()
    p2.text = "Tự do di chuyển, duyệt code trên smartphone mọi lúc mọi nơi."
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(11.5)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(6)

    # Box 2
    b2 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), cy8, cw8, ch8)
    b2.fill.solid()
    b2.fill.fore_color.rgb = CARD_BG
    b2.line.color.rgb = ACCENT_GREEN
    b2.line.width = Pt(1.5)
    tb2 = b2.text_frame
    tb2.word_wrap = True
    tb2.margin_left = tb2.margin_right = tb2.margin_top = Inches(0.25)
    p = tb2.paragraphs[0]
    p.text = "2. BẬT PREVENT SLEEP"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p2 = tb2.add_paragraph()
    p2.text = "Giữ hệ thống luôn thức, tự tin giao việc nặng chạy ngầm xuyên đêm."
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(11.5)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(6)

    # Box 3
    b3 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.8), cy8, cw8, ch8)
    b3.fill.solid()
    b3.fill.fore_color.rgb = CARD_BG
    b3.line.color.rgb = ACCENT_INDIGO
    b3.line.width = Pt(1.5)
    tb3 = b3.text_frame
    tb3.word_wrap = True
    tb3.margin_left = tb3.margin_right = tb3.margin_top = Inches(0.25)
    p = tb3.paragraphs[0]
    p.text = "3. CLAUDE CODE + OLLAMA"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_INDIGO
    p2 = tb3.add_paragraph()
    p2.text = "Bảo vệ mã nguồn nhạy cảm, tiết kiệm 100% token với model open-source."
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(11.5)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(6)

    # Bottom Callout / Q&A Banner
    qa_banner = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.8), Inches(11.7), Inches(0.95))
    qa_banner.fill.solid()
    qa_banner.fill.fore_color.rgb = CARD_BG_ALT
    qa_banner.line.color.rgb = CARD_BORDER
    tqa = qa_banner.text_frame
    tqa.word_wrap = True
    tqa.margin_left = Inches(0.3)
    p = tqa.paragraphs[0]
    p.text = "💬 CẢM ƠN ANH EM ĐÃ LẮNG NGHE! CHÚNG TA CÙNG THẢO LUẬN & DEMO TRỰC TIẾP NHÉ!"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    add_notes(s8, """[LỜI THOẠI DIỄN GIẢ - 6:55 - 7:45]
(Hook) Để khép lại bài chia sẻ hôm nay, mình muốn nhắn nhủ một điều: Công nghệ AI sinh ra là để phục vụ chúng ta, giúp chúng ta làm việc thông minh hơn chứ không phải ngồi gò lưng canh chừng máy tính nhiều hơn.
(Why) Cả Antigravity Remote Control, App Settings và Claude Code tích hợp Ollama đều cùng hướng tới một mục tiêu duy nhất: Tự động hóa triệt để và an tâm tuyệt đối.
(How) Ngay sau buổi này, anh em chỉ cần dành 30 giây làm 3 việc: Một là gạt bật Remote Control trên Antigravity để sẵn sàng lái agent từ điện thoại. Hai là bật Prevent Sleep và Menu Bar resident. Và ba là thử gõ 'ollama launch claude' để trải nghiệm coding agent offline cực kỳ mạnh mẽ.
(Takeaway) Cảm ơn tất cả anh em đã theo dõi! Bây giờ mình xin mở phần Q&A, anh em có câu hỏi hay muốn cùng quét QR thử nghiệm trực tiếp thì chúng ta cùng thảo luận nhé!""")

    output_path = r"d:\Project\training-ai\bai-2.5-tao-slide\Antigravity_RemoteControl_ClaudeCode_Slides.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_deck()
