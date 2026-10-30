import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Color Palette - Cyber Dark Luxury
BG_DARK = RGBColor(9, 13, 22)        # #090D16
CARD_BG = RGBColor(19, 27, 46)       # #131B2E
CARD_BG_ALT = RGBColor(15, 23, 42)   # #0F172A
CARD_BORDER = RGBColor(51, 65, 85)   # #334155
BORDER_GLOW = RGBColor(99, 102, 241) # #6366F1
TEXT_WHITE = RGBColor(248, 250, 252) # #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184) # #94A3B8
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
    bg.line.fill.background()

def add_top_decorations(slide, slide_num, total_slides=10, tag="⚡ CHUYÊN ĐỀ CÔNG NGHỆ NỘI BỘ • AI AGENT WORKFLOW"):
    top_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(10), Inches(0.35))
    tf = top_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = tag.upper()
    p.font.name = "Segoe UI"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = ACCENT_INDIGO

    num_box = slide.shapes.add_textbox(Inches(11.0), Inches(0.35), Inches(1.5), Inches(0.35))
    ntf = num_box.text_frame
    np = ntf.paragraphs[0]
    np.text = f"{slide_num:02d} / {total_slides:02d}"
    np.alignment = PP_ALIGN.RIGHT
    np.font.name = "Consolas"
    np.font.size = Pt(11)
    np.font.bold = True
    np.font.color.rgb = ACCENT_CYAN

    foot_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.7), Inches(0.3))
    ftf = foot_box.text_frame
    fp = ftf.paragraphs[0]
    fp.text = "Google Antigravity & Claude Code • Internal Tech Sharing • 2026"
    fp.font.name = "Segoe UI"
    fp.font.size = Pt(9)
    fp.font.color.rgb = TEXT_DIM

def add_header(slide, title, subtitle=None):
    header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.82), Inches(11.7), Inches(1.1))
    tf = header_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = "Segoe UI"
    p.font.size = Pt(25)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    
    if subtitle:
        p2 = tf.add_paragraph()
        p2.text = subtitle
        p2.font.name = "Segoe UI"
        p2.font.size = Pt(12.5)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(3)

def add_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = notes_text

def add_flowchart_3_nodes(slide, left, top, width, height, nodes_data):
    node_w = Inches(3.2)
    node_h = height
    arrow_w = Inches(0.7)
    gap = (width - (node_w * 3) - (arrow_w * 2)) / 2

    cur_x = left
    for i, (title, desc) in enumerate(nodes_data):
        node = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_x, top, node_w, node_h)
        node.fill.solid()
        node.fill.fore_color.rgb = CARD_BG
        node.line.color.rgb = BORDER_GLOW if i == 1 else (ACCENT_CYAN if i == 0 else ACCENT_GREEN)
        node.line.width = Pt(1.5)

        ntf = node.text_frame
        ntf.word_wrap = True
        ntf.margin_left = ntf.margin_right = Inches(0.2)
        ntf.margin_top = Inches(0.12)
        p1 = ntf.paragraphs[0]
        p1.text = title
        p1.font.name = "Segoe UI"
        p1.font.size = Pt(12.5)
        p1.font.bold = True
        p1.font.color.rgb = TEXT_WHITE

        p2 = ntf.add_paragraph()
        p2.text = desc
        p2.font.name = "Segoe UI"
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_MUTED
        p2.space_before = Pt(4)

        cur_x += node_w
        if i < 2:
            arrow_x = cur_x + Inches(0.05)
            arrow_y = top + (height / 2) - Inches(0.18)
            arrow = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, arrow_x, arrow_y, arrow_w - Inches(0.1), Inches(0.36))
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = ACCENT_INDIGO
            arrow.line.fill.background()
            cur_x += arrow_w + gap

def add_terminal_mockup(slide, left, top, width, height, title, command, logs):
    win = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    win.fill.solid()
    win.fill.fore_color.rgb = CODE_BG
    win.line.color.rgb = CARD_BORDER
    win.line.width = Pt(1)

    tbar_h = Inches(0.4)
    tbar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, tbar_h)
    tbar.fill.solid()
    tbar.fill.fore_color.rgb = CARD_BG_ALT
    tbar.line.fill.background()

    # Dots
    dot_d = Inches(0.14)
    dot_y = top + Inches(0.13)
    for i, color in enumerate([ACCENT_RED, ACCENT_AMBER, ACCENT_GREEN]):
        dot = slide.shapes.add_shape(MSO_SHAPE.OVAL, left + Inches(0.2 + i * 0.22), dot_y, dot_d, dot_d)
        dot.fill.solid()
        dot.fill.fore_color.rgb = color
        dot.line.fill.background()

    tbox = slide.shapes.add_textbox(left + Inches(1.0), top + Inches(0.05), width - Inches(1.2), Inches(0.3))
    ttf = tbox.text_frame
    tp = ttf.paragraphs[0]
    tp.text = title
    tp.font.name = "Consolas"
    tp.font.size = Pt(10)
    tp.font.color.rgb = TEXT_MUTED

    cbox = slide.shapes.add_textbox(left + Inches(0.25), top + tbar_h + Inches(0.1), width - Inches(0.5), height - tbar_h - Inches(0.2))
    ctf = cbox.text_frame
    ctf.word_wrap = True
    
    cp = ctf.paragraphs[0]
    cp.text = command
    cp.font.name = "Consolas"
    cp.font.size = Pt(11.5)
    cp.font.bold = True
    cp.font.color.rgb = ACCENT_CYAN

    for log in logs:
        lp = ctf.add_paragraph()
        lp.text = log
        lp.font.name = "Consolas"
        lp.font.size = Pt(10.5)
        lp.font.color.rgb = ACCENT_GREEN if "[✓]" in log else TEXT_MUTED
        lp.space_before = Pt(4)

def build_slides_1_to_4(prs):
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 1: COVER / HERO SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)
    add_top_decorations(s1, 1, 10, "⚡ CHUYÊN ĐỀ CÔNG NGHỆ NỘI BỘ • AI AGENT WORKFLOW")

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
    p2.font.size = Pt(21)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_CYAN
    p2.space_before = Pt(6)

    p3 = tf1.add_paragraph()
    p3.text = "Giải phóng kỹ sư khỏi bàn làm việc, bảo vệ dữ liệu tuyệt đối và làm chủ luồng thực thi tự hành."
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(13)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_before = Pt(8)

    # 3 Hero Metric Cards
    hero_cards = [
        ("📱 Multi-Device Control", "Lái AI Agent tự hành từ smartphone mọi lúc mọi nơi.\nXem diff, duyệt lệnh bash và gửi prompt bổ sung tức thì khi đang di chuyển.", ACCENT_CYAN),
        ("☕ Continuous Execution", "Ngăn máy tính ngủ gật trong lúc Agent viết code ngầm xuyên đêm.\nTự động khóa và mở wake-lock cấp hệ điều hành khi hoàn thành task.", ACCENT_GREEN),
        ("🔒 100% Offline & Zero Cost", "Tích hợp mô hình cục bộ qua Ollama vào thẳng Claude Code.\nBảo vệ 100% mã nguồn dự án tuyệt mật và cắt giảm toàn bộ chi phí token API.", ACCENT_INDIGO)
    ]
    card_w = Inches(3.7)
    card_h = Inches(3.1)
    card_y = Inches(3.6)
    for i, (title, desc, border_c) in enumerate(hero_cards):
        cx = Inches(0.8 + i * 4.0)
        card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = border_c
        card.line.width = Pt(1.5)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = ctf.margin_top = Inches(0.25)
        cp1 = ctf.paragraphs[0]
        cp1.text = title
        cp1.font.name = "Segoe UI"
        cp1.font.size = Pt(15.5)
        cp1.font.bold = True
        cp1.font.color.rgb = border_c

        cp2 = ctf.add_paragraph()
        cp2.text = desc
        cp2.font.name = "Segoe UI"
        cp2.font.size = Pt(12)
        cp2.font.color.rgb = TEXT_WHITE
        cp2.space_before = Pt(12)

    add_notes(s1, """[LỜI THOẠI DIỄN GIẢ]
Chào anh em! Chắc hẳn ai trong chúng ta khi dùng Antigravity chạy những task lớn như refactor cả module hay sinh hàng chục test cases đều từng gặp cảnh: vừa đi uống cốc cà phê quay lại thì máy tính đã ngủ gật, AI bị ngắt quãng giữa chừng, hoặc phải ngồi dán mắt vào màn hình chỉ để chờ bấm Approve.
Chúng ta đang dùng AI để giải phóng sức lao động nhưng lại vô tình bị xích vào bàn làm việc vì những thiết lập mặc định chưa tối ưu.
Hôm nay, mình sẽ chia sẻ với anh em 2 vũ khí cực mạnh: tính năng Remote Control điều khiển từ xa, bộ thiết lập App Settings sống còn, và cách chạy Claude Code với Model cục bộ hoàn toàn miễn phí, bảo mật qua Ollama.
Nắm vững những tính năng này, anh em sẽ biến công cụ AI thành một trợ lý tự hành đúng nghĩa, làm việc xuyên suốt mọi lúc mọi nơi.""")

    # =========================================================================
    # SLIDE 2: 4 THỰC TRẠNG & RÀO CẢN
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_top_decorations(s2, 2, 10, "⚠️ THỰC TRẠNG & RÀO CẢN THƯỜNG GẶP")
    add_header(s2, "Bốn Rào Cản Khi Vận Hành AI Coding Agent", "AI giải phóng sức lao động nhưng các thiết lập mặc định lại trói chân kỹ sư vào bàn làm việc.")

    pains = [
        ("Máy ngủ gật (Sleep Mode):", "Windows và macOS tự động chuyển sang chế độ Sleep sau 10-15 phút không thao tác bàn phím/chuột. Khi đó kết nối mạng bị ngắt, tiến trình AI bị suspend và task lớn bị hỏng dở dang.", Inches(0.8), Inches(2.10)),
        ("Bị xích vào bàn làm việc:", "Kỹ sư phải ngồi dán mắt vào màn hình chỉ để chờ Agent sinh xong code rồi bấm nút Approve lệnh bash hoặc tool calling, làm gián đoạn mọi hoạt động khác.", Inches(6.8), Inches(2.10)),
        ("Đóng nhầm cửa sổ:", "Thói quen bấm nút 'X' để đóng cửa sổ làm tắt luôn cả tiến trình Antigravity đang chạy ngầm, làm mất sạch ngữ cảnh làm việc và các phiên terminal đang mở.", Inches(0.8), Inches(4.55)),
        ("Nguy cơ lộ mã nguồn dự án:", "Sử dụng các Cloud Agent tiềm ẩn nguy cơ rò rỉ source code nhạy cảm vi phạm cam kết bảo mật NDA của khách hàng, đồng thời làm phát sinh chi phí token API đắt đỏ.", Inches(6.8), Inches(4.55))
    ]
    for p_title, p_desc, px, py in pains:
        c = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, py, Inches(5.7), Inches(2.2))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = ACCENT_RED
        c.line.width = Pt(1.5)

        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = ctf.margin_top = Inches(0.25)

        p = ctf.paragraphs[0]
        r1 = p.add_run()
        r1.text = "❌ " + p_title + "\n"
        r1.font.name = "Segoe UI"
        r1.font.bold = True
        r1.font.size = Pt(13.5)
        r1.font.color.rgb = ACCENT_RED

        r2 = p.add_run()
        r2.text = p_desc
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(11.5)
        r2.font.color.rgb = TEXT_WHITE

    add_notes(s2, """[LỜI THOẠI DIỄN GIẢ]
Khi bắt đầu ứng dụng AI Agent vào công việc thực tế, hầu hết kỹ sư chúng ta đều va phải 4 rào cản rất khó chịu này.
Thứ nhất là máy ngủ gật: vừa rời máy đi họp quay lại thấy màn hình đen ngòm và task bị lỗi đứt kết nối mạng.
Thứ hai là bị xích vào bàn: AI sinh code thì nhanh nhưng cứ chốc chốc lại dừng chờ mình bấm Approve một lệnh terminal, thế là mình không dám đi đâu.
Thứ ba là thói quen tiện tay bấm dấu X đóng cửa sổ: tắt luôn cả app, mất sạch context và các terminal tab.
Và cuối cùng là nỗi lo bảo mật: nhiều dự án có cam kết NDA khách hàng cấm tuyệt đối gửi code lên cloud, cộng với chi phí token đắt đỏ khi phải debug lặp đi lặp lại.""")

    # =========================================================================
    # SLIDE 3: BỨC TRANH MỚI (PARADIGM SHIFT)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_top_decorations(s3, 3, 10, "🌐 BỨC TRANH MỚI • TỰ DO HÓA KỸ SƯ")
    add_header(s3, "Chuyển Dịch Từ Gò Bó Sang Tự Do Hóa Quy Trình", "Đối chiếu sự khác biệt giữa mô hình làm việc truyền thống và kỷ nguyên Cross-Device Agentic.")

    # Col 1: Old way
    col1 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.10), Inches(5.7), Inches(4.65))
    col1.fill.solid()
    col1.fill.fore_color.rgb = CARD_BG
    col1.line.color.rgb = ACCENT_AMBER
    col1.line.width = Pt(1.5)

    tf_c1 = col1.text_frame
    tf_c1.word_wrap = True
    tf_c1.margin_left = tf_c1.margin_right = tf_c1.margin_top = Inches(0.3)
    p = tf_c1.paragraphs[0]
    p.text = "🏢 Cách Làm Cũ (Workstation Bound)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER

    items_c1 = [
        ("Gò bó vị trí địa lý:", " Bắt buộc phải ngồi trực tiếp trước màn hình máy tính công ty để theo dõi Agent sinh mã nguồn."),
        ("Mù thông tin khi di chuyển:", " Rời bàn làm việc đi họp hay ăn trưa là hoàn toàn mất kiểm soát về tiến độ thực thi của AI."),
        ("Phê duyệt thủ công chậm trễ:", " Agent dừng lại chờ câu trả lời xác nhận (Bash tool / Prompt approval), cả quy trình bị tắc nghẽn hàng giờ."),
        ("Remote Desktop nặng nề:", " Dùng TeamViewer hay AnyDesk ngốn băng thông lớn, thao tác chậm chạp và giật lag trên smartphone.")
    ]
    for it_title, it_desc in items_c1:
        p = tf_c1.add_paragraph()
        p.space_before = Pt(8)
        r1 = p.add_run()
        r1.text = "• " + it_title + "\n"
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = it_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_MUTED

    # Col 2: New way
    col2 = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.10), Inches(5.7), Inches(4.65))
    col2.fill.solid()
    col2.fill.fore_color.rgb = CARD_BG
    col2.line.color.rgb = ACCENT_CYAN
    col2.line.width = Pt(1.5)

    tf_c2 = col2.text_frame
    tf_c2.word_wrap = True
    tf_c2.margin_left = tf_c2.margin_right = tf_c2.margin_top = Inches(0.3)
    p = tf_c2.paragraphs[0]
    p.text = "⚡ Chuẩn Mới (Cross-Device Agentic)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    items_c2 = [
        ("Tự do di chuyển tuyệt đối:", " Theo dõi diff code, tiến độ subagent và logs thời gian thực trên điện thoại khi đang di chuyển."),
        ("Phê duyệt một chạm tức thì:", " Nhấn 'Approve' hoặc nhập prompt bổ sung trực tiếp từ trình duyệt smartphone chỉ với một lần chạm."),
        ("Giữ nguyên môi trường máy trạm:", " Workstation chịu trách nhiệm build, test và commit; điện thoại đóng vai trò bảng điều khiển siêu nhẹ."),
        ("Độc lập mạng nội bộ:", " Bạn có thể ngồi ở quán cà phê dùng 4G điều khiển máy trạm công ty an toàn mà không cần cài đặt VPN phức tạp.")
    ]
    for it_title, it_desc in items_c2:
        p = tf_c2.add_paragraph()
        p.space_before = Pt(8)
        r1 = p.add_run()
        r1.text = "✔ " + it_title + "\n"
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = ACCENT_GREEN
        r2 = p.add_run()
        r2.text = it_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_WHITE

    add_notes(s3, """[LỜI THOẠI DIỄN GIẢ]
Để vượt qua 4 rào cản đó, chúng ta cần một sự chuyển dịch tư duy từ cách làm cũ sang chuẩn làm việc mới.
Cách làm cũ là mô hình phụ thuộc hoàn toàn vào máy trạm: bạn phải ngồi dính chặt vào ghế, đi đâu là mù thông tin, và muốn remote thì phải bật TeamViewer nặng nề, giật lag.
Còn với chuẩn Cross-Device Agentic mới: máy tính công ty cấu hình mạnh cứ việc cày code và chạy test, còn bạn thì cầm chiếc điện thoại đi lại tự do. Mọi thông báo hoàn thành, mọi yêu cầu phê duyệt lệnh đều đẩy về smartphone để bạn duyệt chỉ bằng một chạm tay.""")

    # =========================================================================
    # SLIDE 4: ANTIGRAVITY REMOTE CONTROL LÀ GÌ?
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_top_decorations(s4, 4, 10, "🌐 TÍNH NĂNG ĐỘT PHÁ • CROSS-DEVICE AGENT")
    add_header(s4, "Antigravity Remote Control Là Gì?", "Giải pháp điều khiển, giám sát và tương tác với AI Agent từ xa qua nền tảng web bảo mật.")

    # Left: Architecture Boundary
    left_c4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.10), Inches(4.8), Inches(4.65))
    left_c4.fill.solid()
    left_c4.fill.fore_color.rgb = CODE_BG
    left_c4.line.color.rgb = CARD_BORDER
    left_c4.line.width = Pt(1)

    tl4 = left_c4.text_frame
    tl4.word_wrap = True
    tl4.margin_left = tl4.margin_right = tl4.margin_top = Inches(0.3)
    p = tl4.paragraphs[0]
    p.text = "PHÂN ĐỊNH RANH GIỚI HỆ THỐNG"
    p.font.name = "Consolas"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    blocks = [
        ("🖥️ WORKSTATION (MÁY TRẠM)", "Chịu 100% trách nhiệm tính toán nặng:\n• Source Code, Git branches & Worktrees\n• Trình chạy Test, Compiler & Linter\n• Toàn bộ API Secrets & Token nằm tại máy", ACCENT_INDIGO),
        ("📱 SMARTPHONE (CLIENT TỪ XA)", "Giao diện Web UI siêu nhẹ:\n• Xem logs tiến độ thời gian thực\n• Nút Approve 1 chạm duyệt bash/tool\n• Nhập prompt bổ sung ngay lập tức", ACCENT_GREEN)
    ]
    for b_title, b_desc, b_color in blocks:
        p = tl4.add_paragraph()
        p.space_before = Pt(12)
        r1 = p.add_run()
        r1.text = b_title + "\n"
        r1.font.name = "Segoe UI"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = b_color
        r2 = p.add_run()
        r2.text = b_desc
        r2.font.name = "Segoe UI"
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = TEXT_MUTED

    # Right: Detailed Explanations
    right_c4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.9), Inches(2.10), Inches(6.6), Inches(4.65))
    right_c4.fill.solid()
    right_c4.fill.fore_color.rgb = CARD_BG
    right_c4.line.color.rgb = BORDER_GLOW
    right_c4.line.width = Pt(1.5)

    tr4 = right_c4.text_frame
    tr4.word_wrap = True
    tr4.margin_left = tr4.margin_right = tr4.margin_top = Inches(0.3)
    p = tr4.paragraphs[0]
    p.text = "⚡ ĐẶC ĐIỂM CỐT LÕI CỦA REMOTE CONTROL"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    rc_details = [
        ("Không phải Remote Desktop:", "Remote Control không truyền tải hình ảnh màn hình nặng nề ngốn băng thông, mà truyền trực tiếp dữ liệu trạng thái qua web socket nhẹ nhàng."),
        ("Máy trạm giữ quyền điều phối:", "Toàn bộ mã nguồn dự án, git branches, terminal build và các công cụ thực thi nằm nguyên vẹn tại máy trạm công ty."),
        ("Trải nghiệm mượt mà trên di động:", "Giao diện web được tối ưu riêng cho màn hình cảm ứng, hiển thị danh sách artifacts và diff code cực kỳ sắc nét."),
        ("Độc lập mạng nội bộ:", "Bạn có thể ngồi ở quán cà phê dùng 4G điều khiển máy trạm công ty an toàn mà không cần cài đặt VPN phức tạp.")
    ]
    for dt, dd in rc_details:
        p = tr4.add_paragraph()
        p.space_before = Pt(8)
        r1 = p.add_run()
        r1.text = "• " + dt + " "
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = dd
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_MUTED

    add_notes(s4, """[LỜI THOẠI DIỄN GIẢ]
Vậy bản chất Antigravity Remote Control là gì?
Anh em cần lưu ý: Nó hoàn toàn không phải là một công cụ remote desktop như TeamViewer.
Nó là một cầu nối giao diện web trực tiếp vào session Antigravity đang chạy trên workstation của anh em.
Toàn bộ mã nguồn, git branch, terminal và công cụ build vẫn chạy 100% tại máy trạm. Điện thoại chỉ đóng vai trò là một bảng điều khiển từ xa hiển thị danh sách file diff và khung chat.
Nhờ đó, anh em có thể review code và ấn duyệt lệnh chỉ bằng một chạm trên điện thoại mà không tốn băng thông hay lo giật lag.""")

def build_slides_5_to_7(prs):
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 5: SƠ ĐỒ GHÉP NỐI & ZERO TRUST
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_top_decorations(s5, 5, 10, "🔐 CƠ CHẾ VẬN HÀNH • BẢO MẬT ZERO TRUST")
    add_header(s5, "Sơ Đồ Luồng Ghép Nối & Kiến Trúc Bảo Mật", "Cách kết nối thiết bị trong 10 giây và kiến trúc bảo vệ dữ liệu chuẩn Zero Trust.")

    # Flowchart 3 Nodes
    nodes = [
        ("🖥️ MÁY TRẠM (HOST)", "Workstation Antigravity\nGiữ mã nguồn, test & git"),
        ("🔐 CỔNG GHÉP NỐI (PROXY)", "Mã QR & Token Handshake\nKhông mở port Firewall / NAT"),
        ("📱 CLIENT TỪ XA (WEB)", "Trình duyệt Smartphone\nKết nối mã hóa E2E hai chiều")
    ]
    add_flowchart_3_nodes(s5, Inches(0.8), Inches(2.10), Inches(11.7), Inches(1.45), nodes)

    # 3 Explanation Cards
    steps_data = [
        ("BƯỚC 1: KÍCH HOẠT", "⚙️ Bật Trong Settings", [
            ("Mở Settings nhanh chóng:", " Phím tắt Ctrl + , (hoặc Cmd + , trên Mac), vào mục Application và gạt nút 'Enable Remote Control' sang ON trong 10 giây."),
            ("Khởi động qua CLI:", " Hoặc gõ lệnh 'agy --remote-control' hay slash command '/remote-control' ngay trong terminal.")
        ], ACCENT_CYAN),
        ("BƯỚC 2: GHÉP NỐI", "📱 Quét Mã QR & Token", [
            ("Mã QR bảo mật dùng 1 lần:", " Máy tính sinh ngay một QR Handshake động trên màn hình, dùng camera điện thoại quét để truy cập ngay."),
            ("Đăng nhập qua Web SSO:", " Hoặc vào trang antigravity.google đăng nhập tài khoản Google để quản lý các máy trạm.")
        ], BORDER_GLOW),
        ("TIÊU CHUẨN AN TOÀN", "🛡️ Bảo Mật Doanh Nghiệp", [
            ("Chuẩn bảo mật Zero Trust:", " Hoạt động hoàn toàn phía sau tường lửa (Firewall) và VPN công ty, không mở bất kỳ cổng Open Port nào."),
            ("Boundary bất khả xâm phạm:", " Toàn bộ mã nguồn, token Git và secrets nằm nguyên vẹn tại máy trạm, không bị gửi ra ngoài.")
        ], ACCENT_GREEN)
    ]
    cw5 = Inches(3.7)
    ch5 = Inches(2.85)
    cy5 = Inches(3.80)
    for i, (tag, title, items, border_c) in enumerate(steps_data):
        cx = Inches(0.8 + i * 4.0)
        c = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy5, cw5, ch5)
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = border_c
        c.line.width = Pt(1.5)

        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = Inches(0.2)
        ctf.margin_top = Inches(0.18)

        p = ctf.paragraphs[0]
        p.text = tag
        p.font.name = "Segoe UI"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = border_c

        p2 = ctf.add_paragraph()
        p2.text = title
        p2.font.name = "Segoe UI"
        p2.font.size = Pt(14)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_before = Pt(3)

        for it, idesc in items:
            p3 = ctf.add_paragraph()
            p3.space_before = Pt(6)
            r1 = p3.add_run()
            r1.text = "• " + it
            r1.font.bold = True
            r1.font.size = Pt(11)
            r1.font.color.rgb = TEXT_WHITE
            r2 = p3.add_run()
            r2.text = idesc
            r2.font.size = Pt(10.5)
            r2.font.color.rgb = TEXT_MUTED

    add_notes(s5, """[LỜI THOẠI DIỄN GIẢ]
Nhiều anh em sẽ thắc mắc: 'Điều khiển từ xa như vậy có lộ mã nguồn công ty ra ngoài không, thiết lập có phức tạp cần mở port modem không?'.
Câu trả lời là hoàn toàn không. Google thiết kế cơ chế ghép nối này theo triết lý Zero Trust cực kỳ nghiêm ngặt.
Bước 1: Anh em mở Settings bằng phím Ctrl + ,, vào mục Application và gạt nút 'Enable Remote Control'.
Bước 2: Antigravity sẽ sinh ngay một mã QR Code bảo mật. Anh em chỉ cần giơ camera điện thoại lên quét, hoặc truy cập antigravity.google đăng nhập đúng tài khoản Google là kết nối thành công trong 2 giây.
Toàn bộ phiên làm việc xác thực bằng Token handshake dùng một lần, dữ liệu truyền tải mã hóa end-to-end và không hề mở bất kỳ open port nào trên router nội bộ công ty.""")

    # =========================================================================
    # SLIDE 6: APP SETTINGS - PREVENT SLEEP
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_top_decorations(s6, 6, 10, "☕ CÀI ĐẶT HỆ THỐNG • LIÊN TỤC KHÔNG GIÁN ĐOẠN")
    add_header(s6, "App Settings: Cơ Chế Prevent Sleep", "Ngăn hệ thống tự động tắt màn hình và đưa PC vào chế độ ngủ khi AI đang làm việc.")

    # Left Card: Thực Trạng & Rủi Ro
    left_c6 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.10), Inches(5.7), Inches(4.65))
    left_c6.fill.solid()
    left_c6.fill.fore_color.rgb = CARD_BG
    left_c6.line.color.rgb = ACCENT_AMBER
    left_c6.line.width = Pt(1.5)

    tl6 = left_c6.text_frame
    tl6.word_wrap = True
    tl6.margin_left = tl6.margin_right = tl6.margin_top = Inches(0.3)

    p = tl6.paragraphs[0]
    p.text = "⚠️ THỰC TRẠNG & NGUY CƠ SLEEP MODE"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER

    points_left_6 = [
        ("Mặc định hệ điều hành ngắt kết nối:", " Windows và macOS tự động đưa máy vào chế độ Sleep sau 10-15 phút không có thao tác phím chuột để tiết kiệm điện năng."),
        ("AI Agent bị suspend giữa chừng:", " Khi máy ngủ gật, toàn bộ kết nối mạng và socket bị ngắt, tiến trình AI đang viết code, sinh test hoặc chạy benchmark ngầm bị dừng đột ngột."),
        ("Lãng phí thời gian & Token:", " Kỹ sư quay lại sau giờ ăn trưa mới phát hiện task bị hỏng dở dang, buộc phải khởi động lại từ đầu và tốn thêm chi phí token không đáng có.")
    ]
    for pt, pd in points_left_6:
        p = tl6.add_paragraph()
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

    # Right Card: Giải Pháp & Cơ Chế Prevent Sleep
    right_c6 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.10), Inches(5.7), Inches(4.65))
    right_c6.fill.solid()
    right_c6.fill.fore_color.rgb = CARD_BG
    right_c6.line.color.rgb = ACCENT_GREEN
    right_c6.line.width = Pt(1.5)

    tr6 = right_c6.text_frame
    tr6.word_wrap = True
    tr6.margin_left = tr6.margin_right = tr6.margin_top = Inches(0.3)

    p = tr6.paragraphs[0]
    p.text = "⚡ CƠ CHẾ PREVENT SLEEP THÔNG MINH"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    points_right_6 = [
        ("Kích hoạt Wake-Lock cấp Kernel:", " Khi Agent bắt đầu thực thi chuỗi task dài, Antigravity tự động kích hoạt API kernel hệ điều hành để giữ hệ thống luôn thức (Awake) ổn định."),
        ("Tự do hóa kỹ sư hoàn toàn:", " Bạn có thể an tâm rời khỏi bàn làm việc, đi họp, ăn trưa hoặc ra ngoài mà công việc lập trình của AI vẫn diễn ra liên tục không đứt đoạn."),
        ("Tự động hoàn trả quyền Sleep (Auto-Release):", " Ngay khi Agent hoàn thành 100% nhiệm vụ, hệ thống tự động giải phóng wake-lock để máy tính quay về chế độ tiết kiệm điện bình thường.")
    ]
    for pt, pd in points_right_6:
        p = tr6.add_paragraph()
        p.space_before = Pt(12)
        r1 = p.add_run()
        r1.text = "✔ " + pt + "\n"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = ACCENT_GREEN
        r2 = p.add_run()
        r2.text = pd
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_WHITE

    add_notes(s6, """[LỜI THOẠI DIỄN GIẢ]
Đã bao giờ anh em giao cho Agent một task lớn trước khi đi ăn trưa, quay lại thấy màn hình đen ngòm và task bị failed vì máy rơi vào Sleep Mode chưa?
Mặc định, Windows và macOS đều có chính sách tiết kiệm điện tự động ngủ sau một khoảng thời gian người dùng không gõ phím. Nhưng với AI Coding Agent, lúc chúng ta không chạm vào máy lại chính là lúc nó đang làm việc vất vả nhất.
Tính năng 'Prevent Sleep' trong App Settings sinh ra để giải quyết triệt để vấn đề này. Khi được bật, Antigravity sẽ gửi tín hiệu giữ màn hình và hệ thống luôn thức (Awake) trong suốt thời gian Agent đang sinh mã hoặc chạy test.
Và điều tuyệt vời là khi Agent hoàn thành xong toàn bộ công việc, hệ thống sẽ tự động nhả lock để máy tính quay về cơ chế sleep bình thường nhằm tiết kiệm điện.""")

    # =========================================================================
    # SLIDE 7: APP SETTINGS - MENU BAR & NOTIFICATIONS
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_top_decorations(s7, 7, 10, "📌 CÀI ĐẶT HỆ THỐNG • THƯỜNG TRỰC & THÔNG BÁO")
    add_header(s7, "Keep In Menu Bar & Cấu Hình Thông Báo", "Đảm bảo ứng dụng luôn thường trực tức thì và không bỏ lỡ tín hiệu quan trọng từ Agent.")

    col7_1 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.10), Inches(5.7), Inches(4.65))
    col7_1.fill.solid()
    col7_1.fill.fore_color.rgb = CARD_BG
    col7_1.line.color.rgb = BORDER_GLOW
    col7_1.line.width = Pt(1.5)
    
    t7_1 = col7_1.text_frame
    t7_1.word_wrap = True
    t7_1.margin_left = t7_1.margin_right = t7_1.margin_top = Inches(0.3)
    p = t7_1.paragraphs[0]
    p.text = "📌 Keep In Menu Bar (Taskbar Tray)"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_INDIGO

    f7_1 = [
        ("Tránh đóng nhầm cửa sổ tai hại:", " Bấm nút 'X' chỉ là ẩn cửa sổ xuống khay hệ thống (Taskbar Tray / macOS Menu Bar) chứ tuyệt đối không tắt hẳn ứng dụng."),
        ("Thường trực & Triệu hồi tức thì:", " Antigravity luôn chạy ngầm ổn định, kỹ sư có thể gọi lên tức thì bằng phím tắt hoặc 1 click chuột mà không mất thời gian nạp lại project."),
        ("Bảo toàn 100% ngữ cảnh (Context):", " Mọi lịch sử thảo luận, các tab terminal đang chạy và trạng thái subagent được giữ nguyên vẹn không bị reset.")
    ]
    for ft, fd in f7_1:
        p = t7_1.add_paragraph()
        p.space_before = Pt(12)
        r1 = p.add_run()
        r1.text = "• " + ft + "\n"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = fd
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_MUTED

    col7_2 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.10), Inches(5.7), Inches(4.65))
    col7_2.fill.solid()
    col7_2.fill.fore_color.rgb = CARD_BG
    col7_2.line.color.rgb = ACCENT_CYAN
    col7_2.line.width = Pt(1.5)
    
    t7_2 = col7_2.text_frame
    t7_2.word_wrap = True
    t7_2.margin_left = t7_2.margin_right = t7_2.margin_top = Inches(0.3)
    p = t7_2.paragraphs[0]
    p.text = "🔔 Quản Lý Thông Báo Cấp Hệ Điều Hành"
    p.font.name = "Segoe UI"
    p.font.size = Pt(15.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    f7_2 = [
        ("Quản lý tập trung ở Hệ điều hành:", " Antigravity đẩy toàn bộ quyền điều khiển về trung tâm Notifications của Windows/macOS thay vì cấu hình riêng rẽ."),
        ("Cấu hình nhanh trên máy tính:", " Vào OS Settings > Notifications và cấp quyền để nhận biểu ngữ cùng âm thanh ping mỗi khi Agent có tiến triển mới."),
        ("Phản hồi kịp thời & Đồng bộ di động:", " Nhận thông báo ping ngay lập tức khi Agent hoàn thành task lớn hoặc cần duyệt lệnh bash, đồng bộ trực tiếp sang smartphone qua Remote Control.")
    ]
    for ft, fd in f7_2:
        p = t7_2.add_paragraph()
        p.space_before = Pt(12)
        r1 = p.add_run()
        r1.text = "• " + ft + "\n"
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = TEXT_WHITE
        r2 = p.add_run()
        r2.text = fd
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_MUTED

    add_notes(s7, """[LỜI THOẠI DIỄN GIẢ]
Có hai thiết lập nhỏ nhưng ảnh hưởng cực lớn đến trải nghiệm hàng ngày: tắt nhầm cửa sổ và lỡ mất thông báo.
Về 'Keep In Menu Bar': Khi bật lên, Antigravity sẽ neo thường trực trên khay hệ thống. Bấm nút X chỉ là ẩn cửa sổ, app vẫn sống ngầm và sẵn sàng bật lên tức thì bằng phím tắt mà không mất ngữ cảnh.
Về 'Notification Settings': Anh em lưu ý Antigravity đẩy toàn bộ việc quản lý thông báo về Settings của Windows/macOS. Anh em chỉ cần cấp quyền thông báo trong OS Settings là mỗi khi AI hoàn thành task hoặc cần phê duyệt, máy tính và điện thoại đều sẽ ting ting báo ngay.""")

def build_slides_8_to_10(prs):
    blank_layout = prs.slide_layouts[6]

    # =========================================================================
    # SLIDE 8: TẠI SAO CẦN LOCAL LLM TRONG CLAUDE CODE
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_top_decorations(s8, 8, 10, "💡 MỞ RỘNG ĐỘT PHÁ • CLAUDE CODE & LOCAL LLM")
    add_header(s8, "Tại Sao Cần Đưa Model Bên Thứ 3 Vào Claude Code?", "Kết hợp bộ não mã nguồn mở mạnh mẽ với framework CLI Agentic số 1 hiện nay.")

    pillars = [
        ("TRỤ CỘT 1", "🔒 Bảo Mật & Air-Gapped", [
            ("Tuân thủ nghiêm ngặt NDA:", " Cam kết bảo mật của khách hàng cấm tuyệt đối việc đẩy source code dự án lên các server đám mây công cộng."),
            ("Xử lý hoàn toàn Offline:", " Toàn bộ quá trình đọc hiểu mã nguồn và sinh giải pháp được thực thi trên GPU nội bộ của máy trạm."),
            ("Không lưu vết huấn luyện:", " Dữ liệu nội bộ không bao giờ bị sử dụng để huấn luyện lại các mô hình AI của bên thứ ba.")
        ], ACCENT_RED),
        ("TRỤ CỘT 2", "💰 Tiết Kiệm 100% Phí API", [
            ("Cắt giảm chi phí token:", " Các tác vụ lặp đi lặp lại như debug hay sinh test cases ngốn hàng trăm USD nếu dùng API Claude 3.5 Sonnet."),
            ("Sử dụng Ollama 0 đồng:", " Tận dụng tối đa sức mạnh của các model mã nguồn mở hàng đầu như Qwen 2.5 Coder, DeepSeek-R1."),
            ("Không lo giới hạn Rate Limit:", " Không bị chặn tần suất yêu cầu trên phút (RPM/TPM) khi chạy benchmark quy mô lớn.")
        ], ACCENT_GREEN),
        ("TRỤ CỘT 3", "⚡ Giữ Trọn Workflow Agent", [
            ("Tận dụng vỏ Claude Code:", " Giữ nguyên khả năng đọc ghi file chuẩn xác, tự động chạy lệnh terminal và tạo commit tự động."),
            ("Linh hoạt đổi model coding:", " Dễ dàng chuyển đổi giữa các model coding chuyên biệt chỉ với một tham số dòng lệnh duy nhất."),
            ("Tự chủ công nghệ lâu dài:", " Hoạt động độc lập và không phụ thuộc vào tình trạng quá tải hoặc sự cố gián đoạn của nhà cung cấp Cloud.")
        ], ACCENT_CYAN)
    ]
    cw8 = Inches(3.7)
    ch8 = Inches(4.65)
    cy8 = Inches(2.10)
    for i, (tag, title, items, border_c) in enumerate(pillars):
        cx = Inches(0.8 + i * 4.0)
        c = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy8, cw8, ch8)
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = border_c
        c.line.width = Pt(1.5)

        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = ctf.margin_top = Inches(0.25)

        p = ctf.paragraphs[0]
        p.text = tag
        p.font.name = "Segoe UI"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = border_c

        p2 = ctf.add_paragraph()
        p2.text = title
        p2.font.name = "Segoe UI"
        p2.font.size = Pt(15.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_before = Pt(4)

        for it, idesc in items:
            p3 = ctf.add_paragraph()
            p3.space_before = Pt(8)
            r1 = p3.add_run()
            r1.text = "• " + it + "\n"
            r1.font.bold = True
            r1.font.size = Pt(11.5)
            r1.font.color.rgb = TEXT_WHITE
            r2 = p3.add_run()
            r2.text = idesc
            r2.font.size = Pt(11)
            r2.font.color.rgb = TEXT_MUTED

    add_notes(s8, """[LỜI THOẠI DIỄN GIẢ]
Sau khi đã làm chủ Antigravity, mình muốn chia sẻ thêm một kỹ thuật cực hot: Sử dụng Claude Code nhưng chạy bằng Model bên thứ 3 hoặc Model Local qua Ollama. Tại sao chúng ta lại cần điều này?
Claude Code của Anthropic là một CLI agent xuất sắc nhất hiện nay về khả năng sửa code và chạy terminal, nhưng nó có 2 rào cản lớn: chi phí token API đắt đỏ và chính sách bảo mật dữ liệu công ty không cho phép gửi code lên cloud.
Bằng cách đưa model bên thứ 3 thông qua Ollama, anh em giải quyết được cả 2 bài toán:
Thứ nhất, code chạy hoàn toàn local trên GPU máy trạm, bảo mật 100%.
Thứ hai, chi phí token bằng 0 khi dùng các mô hình mã nguồn mở hàng đầu như Qwen 2.5 Coder hay DeepSeek.
Chúng ta vừa có 'bộ não' miễn phí/bảo mật, vừa có 'đôi tay' agentic cực kỳ linh hoạt của Claude Code.""")

    # =========================================================================
    # SLIDE 9: THỰC CHIẾN TÍCH HỢP OLLAMA
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_top_decorations(s9, 9, 10, "🛠️ THỰC CHIẾN TÍCH HỢP • NATIVE ANTHROPIC API BRIDGE")
    add_header(s9, "Cách Tích Hợp Model Vào Claude Code", "Cấu hình ghép nối Ollama với Claude Code qua 2 phương pháp đơn giản.")

    # Terminal Mockup
    add_terminal_mockup(s9, Inches(0.8), Inches(2.10), Inches(11.7), Inches(1.85), "bash — claude-code-bridge", "$ ollama launch claude --model qwen2.5-coder", [
        "[✓] Connected to local Ollama (http://localhost:11434)",
        "[✓] Anthropic Messages API Bridge: READY",
        "[✓] Initializing Agent tools: ReadFile, EditFile, Bash... Done."
    ])

    # 2 Method Cards
    m_left = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.15), Inches(5.7), Inches(2.60))
    m_left.fill.solid()
    m_left.fill.fore_color.rgb = CODE_BG
    m_left.line.color.rgb = ACCENT_GREEN
    m_left.line.width = Pt(1.5)

    tl9 = m_left.text_frame
    tl9.word_wrap = True
    tl9.margin_left = tl9.margin_right = tl9.margin_top = Inches(0.25)
    p = tl9.paragraphs[0]
    p.text = "CÁCH 1: OLLAMA LAUNCH (1 DÒNG DUY NHẤT)"
    p.font.name = "Consolas"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    p2 = tl9.add_paragraph()
    p2.text = "$ ollama launch claude --model qwen2.5-coder"
    p2.font.name = "Consolas"
    p2.font.size = Pt(10.5)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_CYAN
    p2.space_before = Pt(5)

    p3 = tl9.add_paragraph()
    p3.text = "• Ollama phiên bản mới tự động thiết lập cầu nối Anthropic API.\n• Tự động tải model nếu chưa có sẵn trong máy trạm.\n• Sẵn sàng làm việc chỉ sau vài giây."
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(10.5)
    p3.font.color.rgb = TEXT_WHITE
    p3.space_before = Pt(5)

    m_right = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.15), Inches(5.7), Inches(2.60))
    m_right.fill.solid()
    m_right.fill.fore_color.rgb = CODE_BG
    m_right.line.color.rgb = CARD_BORDER
    m_right.line.width = Pt(1)

    tr9 = m_right.text_frame
    tr9.word_wrap = True
    tr9.margin_left = tr9.margin_right = tr9.margin_top = Inches(0.25)
    p = tr9.paragraphs[0]
    p.text = "CÁCH 2: CẤU HÌNH BIẾN MÔI TRƯỜNG (ENV VARS)"
    p.font.name = "Consolas"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_INDIGO

    p2 = tr9.add_paragraph()
    p2.text = "export ANTHROPIC_BASE_URL=http://localhost:11434\nexport ANTHROPIC_AUTH_TOKEN=ollama"
    p2.font.name = "Consolas"
    p2.font.size = Pt(10)
    p2.font.color.rgb = ACCENT_INDIGO
    p2.space_before = Pt(5)

    p3 = tr9.add_paragraph()
    p3.text = "• Khởi chạy lệnh 'claude --model qwen2.5-coder' như bình thường.\n• Hỗ trợ toàn diện Tool calling: Chạy lệnh shell, đọc & sửa file.\n• Tự do cấu hình trong profile ~/.bashrc hoặc ~/.zshrc."
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(10.5)
    p3.font.color.rgb = TEXT_WHITE
    p3.space_before = Pt(5)

    add_notes(s9, """[LỜI THOẠI DIỄN GIẢ]
Nghe thì có vẻ phức tạp nhưng thực tế tích hợp chỉ mất đúng 5 giây với 1 dòng lệnh duy nhất.
Nhờ Ollama mới đây đã hỗ trợ native giao thức Anthropic Messages API, việc cầu nối giữa Claude Code và Ollama diễn ra hoàn toàn trong suốt.
Cách 1 đơn giản nhất: Anh em chỉ cần gõ 'ollama launch claude --model qwen2.5-coder'. Ollama sẽ tự động bridge và mở giao diện Claude Code kết nối trực tiếp vào model máy bạn.
Cách 2 nếu muốn cấu hình cố định trong profile shell: Anh em set 2 biến môi trường ANTHROPIC_BASE_URL trỏ về localhost:11434 và ANTHROPIC_AUTH_TOKEN bằng ollama. Sau đó cứ gõ lệnh 'claude' bình thường!
Agent vẫn tự động đọc file, tạo commit, chạy bash script và tìm kiếm code như khi dùng Claude 3.5 Sonnet xịn.""")

    # =========================================================================
    # SLIDE 10: TỔNG KẾT & Q&A
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_top_decorations(s10, 10, 10, "🏁 TỔNG KẾT & HÀNH ĐỘNG • Q&A")
    add_header(s10, "Bộ Hành Trang Kỹ Sư Tương Lai", "Checklist 3 bước tối ưu quy trình làm việc với AI Agent – Setup 1 lần, thảnh thơi cả ngày.")

    actions = [
        ("1. BẬT REMOTE CONTROL", "Gạt nút toggle trong Settings để sẵn sàng duyệt code và bấm Approve từ điện thoại khi đi họp hoặc đi ăn trưa.\nGiải phóng bản thân khỏi việc phải ngồi canh máy tính liên tục.", ACCENT_CYAN),
        ("2. BẬT PREVENT SLEEP & TRAY", "Giữ máy tính luôn thức trong lúc Agent cày task nặng xuyên đêm và tránh nguy cơ đóng nhầm cửa sổ bằng nút 'X'.\nỨng dụng luôn thường trực trên khay Taskbar Tray.", ACCENT_GREEN),
        ("3. THỬ NGHIỆM OLLAMA LAUNCH", "Chạy thử lệnh 'ollama launch claude' để trải nghiệm cảm giác sở hữu một trợ lý AI Coding offline miễn phí 100%.\nBảo vệ tuyệt đối mã nguồn nhạy cảm của dự án.", ACCENT_INDIGO)
    ]
    for i, (a_title, a_desc, a_border) in enumerate(actions):
        cx = Inches(0.8 + i * 4.0)
        c = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(2.10), Inches(3.7), Inches(3.35))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = a_border
        c.line.width = Pt(1.5)

        ctf = c.text_frame
        ctf.word_wrap = True
        ctf.margin_left = ctf.margin_right = ctf.margin_top = Inches(0.25)

        p = ctf.paragraphs[0]
        p.text = a_title
        p.font.name = "Segoe UI"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = a_border

        p2 = ctf.add_paragraph()
        p2.text = a_desc
        p2.font.name = "Segoe UI"
        p2.font.size = Pt(11.5)
        p2.font.color.rgb = TEXT_WHITE
        p2.space_before = Pt(8)

    qa_box = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(5.65), Inches(11.7), Inches(1.10))
    qa_box.fill.solid()
    qa_box.fill.fore_color.rgb = CARD_BG_ALT
    qa_box.line.color.rgb = ACCENT_CYAN
    qa_box.line.width = Pt(1.5)

    tqa = qa_box.text_frame
    tqa.word_wrap = True
    tqa.margin_left = Inches(0.3)
    p = tqa.paragraphs[0]
    p.text = "💬 CẢM ƠN ANH EM ĐÃ LẮNG NGHE! CHÚNG TA CÙNG THẢO LUẬN & DEMO TRỰC TIẾP NHÉ!"
    p.font.name = "Segoe UI"
    p.font.size = Pt(13.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    p2 = tqa.add_paragraph()
    p2.text = "Hãy quét mã QR hoặc mở Settings trên máy của bạn để cùng thực hành và trải nghiệm ngay bây giờ!"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MUTED
    p2.space_before = Pt(3)

    add_notes(s10, """[LỜI THOẠI DIỄN GIẢ]
Để khép lại bài chia sẻ hôm nay, mình muốn nhắn nhủ một điều: Công nghệ AI sinh ra là để phục vụ chúng ta, giúp chúng ta làm việc thông minh hơn chứ không phải ngồi gò lưng canh chừng máy tính nhiều hơn.
Cả Antigravity Remote Control, App Settings và Claude Code tích hợp Ollama đều cùng hướng tới một mục tiêu duy nhất: Tự động hóa triệt để và an tâm tuyệt đối.
Ngay sau buổi này, anh em chỉ cần dành 30 giây làm 3 việc:
Một là gạt bật Remote Control trên Antigravity để sẵn sàng lái agent từ điện thoại.
Hai là bật Prevent Sleep và Menu Bar resident.
Và ba là thử gõ 'ollama launch claude' để trải nghiệm coding agent offline cực kỳ mạnh mẽ.
Cảm ơn tất cả anh em đã theo dõi! Bây giờ mình xin mở phần Q&A, anh em có câu hỏi hay muốn cùng quét QR thử nghiệm trực tiếp thì chúng ta cùng thảo luận nhé!""")

def create_deck(output_path=None):
    if output_path is None:
        output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Antigravity_RemoteControl_ClaudeCode_Slides.pptx")

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    build_slides_1_to_4(prs)
    build_slides_5_to_7(prs)
    build_slides_8_to_10(prs)

    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")
    return output_path

if __name__ == "__main__":
    create_deck()
