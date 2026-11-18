"""
Department 06: Hanh chinh - Quan ly du an - Van phong chung (7 Exercises: 44 -> 50)
Updated with Security Hooks, Corporate Styling Rules, Reference Output, and 6-part PROMPT_DEMO.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generator_core import WorkspaceBuilder

DEPT = "06-hanh-chinh"

def generate():
    print(f"--> Generating {DEPT} with enhanced controls...")

    # =========================================================================
    # EXERCISE 44: Chuyen bien ban hop thanh bang Action Items
    # =========================================================================
    b44 = WorkspaceBuilder(DEPT, "44-bien-ban-hop-action-tracker")
    b44.write_agents_md(
        role_title="Thư ký Dự án & Quản lý Tiến độ (Project Secretary)",
        department_name="Văn phòng Quản lý Dự án (PMO)",
        constitution_items=[
            "Bóc tách Action Items chuẩn mực: Mỗi đầu việc phải có rõ Người chịu trách nhiệm chính (PIC), Deadline cụ thể, Mức độ ưu tiên.",
            "Cảnh báo việc ưu tiên cao: Đánh dấu các đầu việc Priority High để lập lịch nhắc nhở."
        ]
    )
    b44.write_rule(
        rule_file_name="quy_chuan_action_tracker.md",
        description="Quy chuẩn trích xuất đầu việc từ biên bản họp sang bảng tính Action Tracker",
        globs="*.txt, *.docx, *.xlsx",
        rule_title="Quy Chuẩn Bảng Theo Dõi Action Items",
        guidelines=[
            "Trích xuất đủ 7 cột: STT, Hạng mục công việc, Bộ phận, PIC, Deadline, Mức độ ưu tiên, Trạng thái.",
            "Cập nhật trực tiếp vào file `Project_Action_Tracker.xlsx`."
        ]
    )
    b44.write_corporate_styling_rule()
    b44.write_security_hooks(["bien_ban_hop.txt", "action_tracker.xlsx"])
    b44.write_skill(
        skill_name="trich-xuat-action-items",
        description="Use this skill to parse meeting minutes and unstructured notes into structured action item trackers.",
        skill_title="Quy trình bóc tách đầu việc từ biên bản họp",
        steps=[
            {"name": "Đọc biên bản họp", "desc": "Nạp file `bien_ban_hop.txt`."},
            {"name": "Trích xuất công việc", "desc": "Rút trích các quyết định và đầu việc được phân công."},
            {"name": "Cập nhật bảng tiến độ", "desc": "Lưu file `Project_Action_Tracker.xlsx`."}
        ]
    )
    b44.write_prompt_demo(
        problem_pain="Sau cuộc họp 2 tiếng có biên bản họp dài 5 trang chữ. Thư ký phải ngồi nhặt từng đầu việc ai làm, hạn nào để gõ vào Excel rất lâu.",
        interactive_hook="Nếu trong biên bản họp ghi 'Anh Tuấn phụ trách kết nối API cổng thanh toán VNPay trước 18/11/2026', làm sao để trích xuất chuẩn xác vào một bảng tính theo dõi công việc?",
        prompt_cmd="Đọc file bien_ban_hop.txt. Trích xuất toàn bộ các đầu việc cần làm (Action Items) và cập nhật vào file Project_Action_Tracker.xlsx theo các cột: STT, Hạng mục, Phòng ban, PIC, Deadline, Mức độ ưu tiên (High/Medium/Low), Trạng thái. Tô màu đỏ cho việc ưu tiên High.",
        prompt_pitfalls="Nếu cuộc họp có câu thảo luận chung chung không chốt người làm (No PIC Assigned), AI cần gắn nhãn cảnh báo 'Chưa phân công' thay vì bỏ sót đầu việc.",
        expected_output="File `Project_Action_Tracker.xlsx` được điền đầy đủ các đầu việc chuẩn xác phân theo từng cá nhân phụ trách.",
        wow_moment="Từ văn bản họp dài dòng biến ngay thành bảng theo dõi tiến độ công việc chuẩn chỉnh trên Excel."
    )
    b44.write_text_file("bien_ban_hop.txt", """
BIÊN BẢN HỌP GIAO BAN DỰ ÁN TRIỂN KHAI PHẦN MỀM ERP
Thời gian: 09:00 - 11:30 ngày 10/11/2026
Chủ trì: Anh Hoàng Nam (Giám đốc Dự án) | Thư ký: Thùy Trang

CÁC KẾT LUẬN & PHÂN CÔNG CÔNG VIỆC:
1. Anh Tuấn (Phòng Kỹ thuật): Hoàn thiện việc kết nối API cổng thanh toán VNPay và kiểm thử bảo mật. Deadline: 18/11/2026. Mức độ ưu tiên: High (Rất khẩn cấp).
2. Chị Lan (Phòng Kế toán): Chuẩn hóa danh mục tài khoản theo Thông tư 200 và chốt số dư đầu kỳ để import vào hệ thống mới. Deadline: 22/11/2026. Mức độ ưu tiên: High.
3. Anh Minh (Phòng Kho vận): Hoàn thành kiểm kê kho thực tế tại kho Hà Nội và bàn giao số liệu cho đội dự án. Deadline: 25/11/2026. Mức độ ưu tiên: Medium.
4. Chị Hà (Phòng Nhân sự): Lập danh sách phân quyền tài khoản cho 50 nhân viên tham gia đợt đào tạo nội bộ. Deadline: 15/11/2026. Mức độ ưu tiên: Medium.
    """)
    b44.create_excel("action_tracker.xlsx", {
        "Tracker": {
            "headers": ["STT", "Hạng Mục Công Việc", "Phòng Ban", "PIC", "Deadline", "Mức Độ Ưu Tiên", "Trạng Thái"],
            "rows": []
        }
    })
    # Reference output
    b44.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Project_Action_Tracker": {
            "headers": ["STT", "Hạng Mục Công Việc", "Phòng Ban", "PIC Phụ Trách", "Deadline", "Mức Độ Ưu Tiên", "Trạng Thái Tiến Độ"],
            "rows": [
                [1, "Kết nối API cổng thanh toán VNPay & kiểm thử bảo mật", "Phòng Kỹ thuật", "Anh Tuấn", "2026-11-18", "High (Rất khẩn cấp)", "Đang thực hiện"],
                [2, "Chuẩn hóa danh mục TK TT200 & chốt số dư đầu kỳ", "Phòng Kế toán", "Chị Lan", "2026-11-22", "High (Khẩn cấp)", "Chưa bắt đầu"],
                [3, "Kiểm kê kho thực tế Hà Nội & bàn giao số liệu", "Phòng Kho vận", "Anh Minh", "2026-11-25", "Medium", "Đang thực hiện"],
                [4, "Lập danh sách phân quyền tài khoản cho 50 nhân sự", "Phòng Nhân sự", "Chị Hà", "2026-11-15", "Medium", "Đang thực hiện"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 45: Xay dung bieu do tien do du an Gantt Chart tren Excel
    # =========================================================================
    b45 = WorkspaceBuilder(DEPT, "45-ve-gantt-chart-excel")
    b45.write_agents_md(
        role_title="Quản lý Kế hoạch & Điều độ Dự án (Project Planner)",
        department_name="Văn phòng Quản lý Dự án (PMO)",
        constitution_items=[
            "Lịch làm việc thực tế: Bắt buộc sử dụng hàm WORKDAY loại trừ Thứ Bảy, Chủ Nhật và ngày lễ.",
            "Tô màu Gantt Chart: Sử dụng Conditional Formatting để tự động tô màu thanh tiến độ theo các mốc ngày."
        ]
    )
    b45.write_rule(
        rule_file_name="quy_chuan_gantt_chart.md",
        description="Quy chuẩn lập lịch tiến độ dự án và vẽ biểu đồ Gantt Chart bằng lưới ô Excel",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Bảng Tiến Độ Gantt Chart",
        guidelines=[
            "Tính Ngày kết thúc = WORKDAY(Ngày bắt đầu, Số ngày thực hiện - 1).",
            "Thiết lập Conditional Formatting trên các cột ngày (từ 01/11 đến 30/11) để ô tự đổi màu xanh khi nằm giữa Ngày bắt đầu và Ngày kết thúc.",
            "Xuất ra file `Gantt_Chart_Du_An_T11.xlsx`."
        ]
    )
    b45.write_corporate_styling_rule()
    b45.write_security_hooks(["hang_muc_du_an.xlsx"])
    b45.write_skill(
        skill_name="ve-gantt-chart-excel",
        description="Use this skill to compute working-day project schedules and render interactive Excel Gantt charts using conditional formatting.",
        skill_title="Quy trình vẽ biểu đồ tiến độ Gantt Chart",
        steps=[
            {"name": "Đọc danh sách hạng mục", "desc": "Nạp file `hang_muc_du_an.xlsx`."},
            {"name": "Tính toán tiến độ ngày làm việc", "desc": "Áp dụng hàm tính ngày trừ cuối tuần."},
            {"name": "Kẻ lưới biểu đồ Gantt", "desc": "Tạo lưới ngày và lưu file `Gantt_Chart_Du_An_T11.xlsx`."}
        ]
    )
    b45.write_prompt_demo(
        problem_pain="Sếp yêu cầu vẽ biểu đồ Gantt Chart trên Excel có tô màu theo ngày và tự trừ cuối tuần. Ngồi kẻ ô tô màu bằng tay mất nửa ngày.",
        interactive_hook="Nếu một công việc bắt đầu vào Thứ Sáu và kéo dài 5 ngày làm việc, ngày hoàn thành chính xác sẽ là Thứ Ba tuần kế tiếp hay Thứ Năm nếu không làm Thứ Bảy & Chủ Nhật?",
        prompt_cmd="Từ file hang_muc_du_an.xlsx, hãy tính Ngày bắt đầu và Ngày kết thúc cho từng hạng mục (loại trừ Thứ 7 và CN), sau đó tạo biểu đồ Gantt trực quan ngay trên lưới ô Excel bằng Conditional Formatting cho tháng 11/2026. Xuất ra file Gantt_Chart_Du_An_T11.xlsx.",
        prompt_pitfalls="Nếu dùng phép cộng ngày thông thường (Ngày BĐ + Thời lượng) thay vì hàm tính ngày làm việc (Workday logic), dự án sẽ bị trễ tiến độ vì tính cả ngày nghỉ.",
        expected_output="File `Gantt_Chart_Du_An_T11.xlsx` với các thanh tiến độ Gantt Chart tự động đổi màu mượt mà theo ngày tháng.",
        wow_moment="Tạo ra một biểu đồ Gantt Chart động cực đẹp trên Excel mà không cần tốn hàng giờ kẻ ô thủ công."
    )
    b45.create_excel("hang_muc_du_an.xlsx", {
        "HangMuc": {
            "headers": ["Mã Task", "Tên Hạng Mục Công Việc", "Ngày Bắt Đầu Dự Kiến", "Thời Lượng (Ngày Làm Việc)", "Phụ Trách"],
            "rows": [
                ["T01", "Khảo sát yêu cầu người dùng", "2026-11-02", 5, "Team BA"],
                ["T02", "Thiết kế giao diện UI/UX", "2026-11-09", 7, "Team Designer"],
                ["T03", "Lập trình chức năng Backend", "2026-11-18", 10, "Team Dev"],
                ["T04", "Kiểm thử hệ thống UAT", "2026-11-26", 4, "Team QA"]
            ]
        }
    })
    # Reference output
    b45.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Gantt_Chart_T11": {
            "headers": ["Mã Task", "Tên Hạng Mục", "Ngày Bắt Đầu", "Thời Lượng", "Ngày Kết Thúc (Trừ T7,CN)", "Phụ Trách", "02/11", "03/11", "04/11", "05/11", "06/11", "09/11", "10/11"],
            "rows": [
                ["T01", "Khảo sát yêu cầu người dùng", "2026-11-02", 5, "2026-11-06", "Team BA", "■", "■", "■", "■", "■", "", ""],
                ["T02", "Thiết kế giao diện UI/UX", "2026-11-09", 7, "2026-11-17", "Team Designer", "", "", "", "", "", "■", "■"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 46: Quan ly va phan bo chi phi Taxi, Van phong pham
    # =========================================================================
    b46 = WorkspaceBuilder(DEPT, "46-phan-bo-chi-phi-taxi-vpp")
    b46.write_agents_md(
        role_title="Chuyên viên Quản trị Chi phí Hành chính (Admin Officer)",
        department_name="Phòng Hành chính - Quản trị",
        constitution_items=[
            "Phân bổ trung tâm chi phí (Cost Center): Ánh xạ tên nhân viên đi taxi về đúng phòng ban chịu chi phí.",
            "Phát hiện chuyến xe bất thường: Báo động các chuyến xe phát sinh sau 22h đêm hoặc ngày Chủ Nhật không gắn mã dự án."
        ]
    )
    b46.write_rule(
        rule_file_name="quy_chuan_chi_phi_admin.md",
        description="Quy chuẩn phân bổ chi phí Grab doanh nghiệp và lọc chuyến ngoài giờ",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Quản Lý Chi Phí Di Chuyển Taxi",
        guidelines=[
            "Khớp nối nhân viên với phòng ban từ danh sách nhân sự.",
            "Tạo cột cảnh báo: 'Chuyến xe ngoài giờ / Chủ Nhật'.",
            "Xuất ra file `Phan_bo_chi_phi_Grab_T10.xlsx`."
        ]
    )
    b46.write_corporate_styling_rule()
    b46.write_security_hooks(["bang_ke_taxi.xlsx", "nhan_su.xlsx"])
    b46.write_skill(
        skill_name="phan-bo-chi-phi-taxi",
        description="Use this skill to map corporate ride-hailing/utility invoices to department cost centers and flag policy exceptions.",
        skill_title="Quy trình phân bổ chi phí taxi và kiểm soát ngoài giờ",
        steps=[
            {"name": "Đọc bảng kê Grab và nhân sự", "desc": "Nạp file `bang_ke_taxi.xlsx` và `nhan_su.xlsx`."},
            {"name": "Gán phòng ban & Lọc giờ", "desc": "Ánh xạ Cost Center và lọc chuyến đi sau 22h hoặc ngày nghỉ."},
            {"name": "Xuất báo cáo chi phí", "desc": "Lưu file `Phan_bo_chi_phi_Grab_T10.xlsx`."}
        ]
    )
    b46.write_prompt_demo(
        problem_pain="Nhận bảng kê Grab for Business hàng trăm cuốc xe, Admin phải ngồi tra từng người thuộc phòng ban nào để phân bổ chi phí và tìm xem ai đi việc riêng ngoài giờ.",
        interactive_hook="Một cuốc xe Grab lúc 23h15 đêm Chủ Nhật từ quán bar về nhà riêng nhưng ghi chú 'Gặp đối tác', bạn sẽ duyệt thanh toán hay yêu cầu giải trình bổ sung mã dự án?",
        prompt_cmd="Kết hợp bảng kê Grab trong bang_ke_taxi.xlsx và danh sách nhan_su.xlsx. Hãy ánh xạ từng chuyến xe về đúng Phòng ban, tổng hợp chi phí theo từng bộ phận, và lọc riêng các chuyến xe sau 22h đêm hoặc ngày Chủ Nhật ra sheet Canh_Bao_Ngoai_Gio trong file Phan_bo_chi_phi_Grab_T10.xlsx.",
        prompt_pitfalls="Nếu không xử lý trùng tên nhân viên bằng Mã nhân viên hoặc chức danh, các chuyến xe của nhân viên trùng tên sẽ bị gán sai phòng ban chịu phí.",
        expected_output="File `Phan_bo_chi_phi_Grab_T10.xlsx` phân bổ chi phí chuẩn xác về từng phòng ban và khoanh vùng các cuốc xe nghi vấn đi việc riêng.",
        wow_moment="Tự động gán Cost Center và lọc ngay các cuốc xe ngoài giờ trong 5 giây."
    )
    b46.create_excel("bang_ke_taxi.xlsx", {
        "GrabBusiness": {
            "headers": ["Mã Chuyến", "Thời Gian Đặt Xe", "Tên Nhân Viên", "Điểm Đi", "Điểm Đến", "Cước Phí (VNĐ)", "Mã Dự Án"],
            "rows": [
                ["GR01", "2026-10-05 14:30", "Nguyễn Văn Tuấn", "Văn phòng công ty", "Khách hàng An Phát", 125000, "PRJ_ERP"],
                ["GR02", "2026-10-11 23:15", "Trần Thu Hà", "Quán Bar 1900 Tạ Hiện", "Chung cư Royal City", 210000, ""], # Đi đêm 23h15 Chủ nhật không mã dự án!
                ["GR03", "2026-10-18 10:00", "Lê Văn Hùng", "Văn phòng công ty", "Cục Thuế Hà Nội", 95000, "ADMIN_TAX"]
            ]
        }
    })
    b46.create_excel("nhan_su.xlsx", {
        "NhanVien": {
            "headers": ["Tên Nhân Viên", "Phòng Ban", "Chức Vụ"],
            "rows": [
                ["Nguyễn Văn Tuấn", "Phòng Kinh doanh", "Senior Sales"],
                ["Trần Thu Hà", "Phòng Marketing", "Content Creator"],
                ["Lê Văn Hùng", "Phòng Kế toán", "Kế toán viên"]
            ]
        }
    })
    # Reference output
    b46.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Phan_Bo_Phong_Ban": {
            "headers": ["Phòng Ban", "Số Lượng Chuyến", "Tổng Chi Phí (VNĐ)", "Tỷ Trọng (%)"],
            "rows": [
                ["Phòng Kinh doanh", 1, 125000, "29.1%"],
                ["Phòng Marketing", 1, 210000, "48.8%"],
                ["Phòng Kế toán", 1, 95000, "22.1%"]
            ]
        },
        "Canh_Bao_Ngoai_Gio": {
            "headers": ["Mã Chuyến", "Nhân Viên", "Thời Gian", "Điểm Đi", "Điểm Đến", "Số Tiền", "Dấu Hiệu Rủi Ro", "Kiến Nghị"],
            "rows": [
                ["GR02", "Trần Thu Hà", "2026-10-11 23:15", "Quán Bar 1900 Tạ Hiện", "Chung cư Royal City", 210000, "Đi lúc 23h15 đêm Chủ Nhật, không có mã dự án", "Yêu cầu giải trình công tác hoặc trừ lương chi phí cá nhân"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 47: Tu dong tao thu muc va phan quyen Google Drive hang loat
    # =========================================================================
    b47 = WorkspaceBuilder(DEPT, "47-tao-folder-phan-quyen-drive")
    b47.write_agents_md(
        role_title="Quản trị Hệ thống Tài liệu & Google Workspace",
        department_name="Phòng Hành chính & CNTT",
        constitution_items=[
            "Cấu trúc thư mục 3 cấp chuẩn hóa: 01_Hop_dong, 02_Tai_lieu_ky_thuat, 03_Nghiem_thu.",
            "Phân quyền chính xác: Quản lý dự án nhận quyền Editor, Khách hàng nhận quyền Viewer."
        ]
    )
    b47.write_rule(
        rule_file_name="quy_chuan_drive_folder.md",
        description="Quy chuẩn tạo cây thư mục dự án và phân quyền Google Drive",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Tổ Chức Thư Mục Google Drive",
        guidelines=[
            "Tạo cây thư mục chuẩn cho từng dự án.",
            "Ghi lại link thư mục trực tiếp vào cột `Link Google Drive`.",
            "Xuất ra file `Danh_sach_du_an_share_updated.xlsx`."
        ]
    )
    b47.write_corporate_styling_rule()
    b47.write_security_hooks(["danh_sach_du_an_share.xlsx"])
    b47.write_skill(
        skill_name="tao-folder-phan-quyen",
        description="Use this skill to batch create multi-tier Google Drive folder hierarchies and configure role-based permissions.",
        skill_title="Quy trình tạo thư mục và phân quyền Google Drive",
        steps=[
            {"name": "Đọc danh sách dự án", "desc": "Nạp file `danh_sach_du_an_share.xlsx`."},
            {"name": "Tạo cây thư mục chuẩn", "desc": "Thiết lập cấu trúc 3 thư mục con cho từng dự án."},
            {"name": "Cập nhật đường dẫn", "desc": "Lưu file `Danh_sach_du_an_share_updated.xlsx`."}
        ]
    )
    b47.write_prompt_demo(
        problem_pain="Khởi động 20 dự án mới, Admin phải vào Drive tạo tay 60 thư mục con rồi bấm Share quyền cho từng email trong Excel rất mỏi tay.",
        interactive_hook="Nếu một dự án cần cấp quyền cho khách hàng ngoài doanh nghiệp, bạn nên chia sẻ quyền Editor hay quyền Viewer để tránh bị xóa nhầm tài liệu nghiệm thu?",
        prompt_cmd="Đọc file danh_sach_du_an_share.xlsx. Với mỗi dự án, hãy tạo thư mục gồm 3 thư mục con (01_Hop_dong, 02_Tai_lieu_ky_thuat, 03_Nghiem_thu), phân quyền Editor cho Quản lý dự án và Viewer cho Khách hàng, ghi lại link thư mục vào file Danh_sach_du_an_share_updated.xlsx.",
        prompt_pitfalls="Nếu chia sẻ nhầm email cá nhân đuôi @gmail.com thay vì email tổ chức, quyền bảo mật tài liệu doanh nghiệp sẽ bị vi phạm quy chế an ninh thông tin.",
        expected_output="File `Danh_sach_du_an_share_updated.xlsx` cập nhật đường link thư mục hoàn chỉnh cho từng dự án.",
        wow_moment="Tiết kiệm hàng trăm cú click chuột tạo folder và phân quyền thủ công trên Google Drive."
    )
    b47.create_excel("danh_sach_du_an_share.xlsx", {
        "DuAn": {
            "headers": ["Mã Dự Án", "Tên Dự Án", "Email Quản Lý (Editor)", "Email Khách Hàng (Viewer)", "Link Google Drive"],
            "rows": [
                ["PRJ_01", "Dự án Chuyển Đổi Số Alpha", "pm.alpha@company.com", "director@alphacorp.vn", ""],
                ["PRJ_02", "Dự án Nâng Cấp Hạ Tầng Beta", "pm.beta@company.com", "cio@betagroup.com", ""]
            ]
        }
    })
    # Reference output
    b47.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Du_An_Da_Cap_Quyen": {
            "headers": ["Mã Dự Án", "Tên Dự Án", "Cấu Trúc Thư Mục Con", "Quyền Editor", "Quyền Viewer", "Link Thư Mục Gốc Google Drive"],
            "rows": [
                ["PRJ_01", "Dự án Chuyển Đổi Số Alpha", "01_Hop_dong; 02_Tai_lieu_ky_thuat; 03_Nghiem_thu", "pm.alpha@company.com", "director@alphacorp.vn", "https://drive.google.com/drive/folders/1AlphaProjectRoot"],
                ["PRJ_02", "Dự án Nâng Cấp Hạ Tầng Beta", "01_Hop_dong; 02_Tai_lieu_ky_thuat; 03_Nghiem_thu", "pm.beta@company.com", "cio@betagroup.com", "https://drive.google.com/drive/folders/1BetaProjectRoot"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 48: Chuyen bang bieu tu anh chup scan sang Excel va kiem tra cong
    # =========================================================================
    b48 = WorkspaceBuilder(DEPT, "48-ocr-bang-bieu-anh-pdf")
    b48.write_agents_md(
        role_title="Chuyên viên Xử lý Văn bản & Số hóa Dữ liệu (OCR Specialist)",
        department_name="Phòng Hành chính - Văn phòng",
        constitution_items=[
            "Chuyển đổi số liệu nguyên vẹn: Giữ đúng cấu trúc bảng và các ô gộp tiêu đề.",
            "Tự kiểm tra số học: Tự động dùng hàm SUM cộng lại để kiểm tra xem bản scan trên giấy có cộng sai số nào không."
        ]
    )
    b48.write_rule(
        rule_file_name="quy_chuan_ocr_bang_bieu.md",
        description="Quy chuẩn số hóa bảng biểu scan sang Excel và đối chiếu tổng cộng",
        globs="*.txt, *.pdf, *.png",
        rule_title="Quy Chuẩn Số Hóa Bảng Biểu Scan",
        guidelines=[
            "Chuyển toàn bộ các con số dạng chuỗi về định dạng Number.",
            "Tạo cột kiểm tra đối chiếu dòng Tổng cộng.",
            "Xuất ra file `Bang_so_lieu_chuyen_doi_OCR.xlsx`."
        ]
    )
    b48.write_corporate_styling_rule()
    b48.write_security_hooks(["bang_scan_du_lieu.txt"])
    b48.write_skill(
        skill_name="chuyen-bang-bieu-sang-excel",
        description="Use this skill to convert scanned table text into structured Excel tables and audit row totals.",
        skill_title="Quy trình số hóa bảng biểu scan sang Excel",
        steps=[
            {"name": "Đọc bảng scan thô", "desc": "Nạp file `bang_scan_du_lieu.txt`."},
            {"name": "Trích xuất ma trận dữ liệu", "desc": "Định dạng các cột và chuyển đổi số nguyên/thực."},
            {"name": "Kiểm toán tổng cộng", "desc": "Kiểm tra dòng Tổng cộng và lưu file `Bang_so_lieu_chuyen_doi_OCR.xlsx`."}
        ]
    )
    b48.write_prompt_demo(
        problem_pain="Đối tác gửi báo cáo dạng ảnh scan hoặc PDF không copy được chữ, phải gõ tay lại vào Excel mất hàng giờ và dễ nhầm số.",
        interactive_hook="Bao nhiêu bạn từng gặp trường hợp tài liệu giấy in có dấu đỏ của sếp nhưng dòng 'Tổng cộng' bên dưới bị cộng sai 200.000đ do người lập gõ tay máy tính cầm tay?",
        prompt_cmd="Đọc bảng số liệu trong bang_scan_du_lieu.txt. Chuyển toàn bộ sang file Excel Bang_so_lieu_chuyen_doi_OCR.xlsx, chuyển các con số về đúng định dạng Number và tự động dùng hàm SUM kiểm tra lại dòng Tổng cộng xem bản gốc có cộng sai không.",
        prompt_pitfalls="Nếu các con số bị lưu dưới dạng Text (có dấu phẩy ngăn cách hàng nghìn dạng chuỗi), hàm SUM sẽ trả về 0 nếu không được chuyển kiểu dữ liệu.",
        expected_output="File `Bang_so_lieu_chuyen_doi_OCR.xlsx` có bảng số liệu chuẩn chỉ và ghi chú phát hiện bản gốc giấy bị cộng lệch số.",
        wow_moment="Không chỉ chuyển ảnh thành bảng Excel mà còn tự kiểm tra xem tài liệu gốc trên giấy có cộng sai số không."
    )
    b48.write_text_file("bang_scan_du_lieu.txt", """
BẢNG THỐNG KÊ CHI PHÍ HOẠT ĐỘNG QUÝ 3/2026 (BẢN SCAN)
-------------------------------------------------------------------------
Khoản Mục Chi Phí        | Tháng 7 (VNĐ) | Tháng 8 (VNĐ) | Tháng 9 (VNĐ)
-------------------------------------------------------------------------
1. Tiền thuê mặt bằng     | 50,000,000    | 50,000,000    | 50,000,000
2. Điện, nước, internet  | 8,500,000     | 9,200,000     | 8,800,000
3. Văn phòng phẩm        | 3,200,000     | 4,100,000     | 2,900,000
4. Chi phí tiếp khách    | 12,000,000    | 15,000,000    | 14,000,000
-------------------------------------------------------------------------
TỔNG CỘNG TRÊN GIẤY:     | 73,700,000    | 78,300,000    | 75,500,000 
(Lưu ý: Tháng 8 cộng thực tế là 50 + 9.2 + 4.1 + 15 = 78,300,000; Tháng 9 cộng thực tế là 75,700,000 -> Bản giấy ghi nhầm 75,500,000!)
    """)
    # Reference output
    b48.create_excel("_ket_qua_mau_chuan.xlsx", {
        "So_Lieu_OCR_Kiem_Toan": {
            "headers": ["Khoản Mục Chi Phí", "Tháng 7 (VNĐ)", "Tháng 8 (VNĐ)", "Tháng 9 (VNĐ)", "Tổng Chi Quý 3"],
            "rows": [
                ["1. Tiền thuê mặt bằng", 50000000, 50000000, 50000000, 150000000],
                ["2. Điện, nước, internet", 8500000, 9200000, 8800000, 26500000],
                ["3. Văn phòng phẩm", 3200000, 4100000, 2900000, 10200000],
                ["4. Chi phí tiếp khách", 12000000, 15000000, 14000000, 41000000],
                ["TỔNG CỘNG TÍNH LẠI (SUM)", 73700000, 78300000, 75700000, 227700000],
                ["TỔNG CỘNG TRÊN GIẤY", 73700000, 78300000, 75500000, 227500000],
                ["ĐỐI SOÁT KIỂM TOÁN", "Khớp 100%", "Khớp 100%", "LỆCH 200.000đ (Bản giấy in thiếu 200k)", "Lệch tổng 200.000đ"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 49: Xep so do ban tiec su kien va tao ma Check-in duy nhat
    # =========================================================================
    b49 = WorkspaceBuilder(DEPT, "49-xep-so-do-ban-tiec-checkin")
    b49.write_agents_md(
        role_title="Quản lý Sự kiện & Lễ tân Khách mời (Event Coordinator)",
        department_name="Phòng Hành chính & Sự kiện",
        constitution_items=[
            "Quy tắc xếp bàn tiệc: Bàn 1 dành cho khách VIP. Các bàn còn lại 10 người/bàn gom theo ngành nghề tương đồng.",
            "Tạo mã Check-in duy nhất: Sinh mã định danh ngẫu nhiên không trùng lặp cho từng khách mời."
        ]
    )
    b49.write_rule(
        rule_file_name="quy_chuan_ban_tiec_checkin.md",
        description="Quy chuẩn xếp sơ đồ bàn tiệc và tạo mã check-in khách mời",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Sơ Đồ Bàn Tiệc & Check-in",
        guidelines=[
            "Tạo Mã Check-in dạng TIECTET-XXXX.",
            "Thống kê số lượng suất ăn chay/mặn theo từng bàn.",
            "Xuất ra file `So_do_ban_tiec_va_checkin.xlsx`."
        ]
    )
    b49.write_corporate_styling_rule()
    b49.write_security_hooks(["khach_moi_su_kien.xlsx"])
    b49.write_skill(
        skill_name="xep-ban-tiec-checkin",
        description="Use this skill to optimize event seating charts by affinity and generate unique check-in codes with dietary counts.",
        skill_title="Quy trình xếp sơ đồ bàn tiệc và tạo mã check-in",
        steps=[
            {"name": "Đọc danh sách khách mời", "desc": "Nạp file `khach_moi_su_kien.xlsx`."},
            {"name": "Tạo mã & Xếp bàn", "desc": "Tạo mã check-in và gom nhóm khách vào các bàn 10 người."},
            {"name": "Xuất sơ đồ bàn tiệc", "desc": "Lưu file `So_do_ban_tiec_va_checkin.xlsx` kèm số suất ăn chay."}
        ]
    )
    b49.write_prompt_demo(
        problem_pain="Tổ chức hội nghị hàng trăm khách mời, Admin phải xếp bàn tiệc sao cho người cùng ngành ngồi với nhau và thống kê suất ăn chay/mặn cho nhà hàng rất dễ nhầm.",
        interactive_hook="Nếu một bàn tiệc 10 người có 2 khách ăn chay, bạn sẽ đặt menu với nhà hàng như thế nào để phục vụ chuẩn xác đến đúng ghế ngồi?",
        prompt_cmd="Dựa vào khach_moi_su_kien.xlsx, hãy tạo Mã Check-in duy nhất cho từng khách, xếp khách vào các bàn tiệc (Bàn 1 cho VIP, các bàn còn lại gom theo ngành nghề). Thống kê số suất ăn chay/mặn từng bàn để báo nhà hàng và xuất file So_do_ban_tiec_va_checkin.xlsx.",
        prompt_pitfalls="Nếu xếp lẫn lộn khách VIP ngồi chung với khách tiêu chuẩn mà không theo dõi phân nhóm, sự kiện sẽ mất tính trang trọng và vi phạm quy chuẩn lễ tân.",
        expected_output="File `So_do_ban_tiec_va_checkin.xlsx` có sơ đồ phân bàn tiệc hợp lý và số lượng suất ăn chay/mặn chuẩn xác.",
        wow_moment="Giải quyết trọn gói bài toán hậu cần sự kiện rắc rối của dân Hành chính - Sự kiện."
    )
    b49.create_excel("khach_moi_su_kien.xlsx", {
        "KhachMoi": {
            "headers": ["Họ và Tên", "Chức Vụ", "Công Ty", "Hạng Khách", "Ngành Nghề", "Chế Độ Ăn"],
            "rows": [
                ["Ông Nguyễn Hoàng Nam", "Tổng Giám Đốc", "Tập đoàn Vingroup", "VIP", "Bất động sản", "Ăn mặn"],
                ["Bà Trần Thùy Linh", "Phó Chủ Tịch", "Sun Group", "VIP", "Bất động sản", "Ăn chay"],
                ["Ông Lê Văn Đức", "Giám Đốc CNTT", "Công ty FPT", "Standard", "Công nghệ", "Ăn mặn"],
                ["Bà Phạm Bảo Ngọc", "Trưởng Phòng AI", "Viettel AI", "Standard", "Công nghệ", "Ăn chay"],
                ["Ông Đỗ Minh Trí", "Giám Đốc Kỹ Thuật", "VNG Corporation", "Standard", "Công nghệ", "Ăn mặn"]
            ]
        }
    })
    # Reference output
    b49.create_excel("_ket_qua_mau_chuan.xlsx", {
        "So_Do_Ban_Tiec": {
            "headers": ["Mã Check-in", "Họ và Tên", "Công Ty", "Số Bàn Tiệc", "Vị Trí Ngồi", "Chế Độ Ăn", "Trạng Thái Check-in"],
            "rows": [
                ["TIECTET-8801", "Nguyễn Hoàng Nam", "Tập đoàn Vingroup", "Bàn 1 (VIP)", "Ghế Chủ tọa 1", "Ăn mặn", "Chưa check-in"],
                ["TIECTET-8802", "Trần Thùy Linh", "Sun Group", "Bàn 1 (VIP)", "Ghế Chủ tọa 2", "Ăn chay (01)", "Chưa check-in"],
                ["TIECTET-8803", "Lê Văn Đức", "Công ty FPT", "Bàn 2 (Công nghệ)", "Ghế 1", "Ăn mặn", "Chưa check-in"],
                ["TIECTET-8804", "Phạm Bảo Ngọc", "Viettel AI", "Bàn 2 (Công nghệ)", "Ghế 2", "Ăn chay (01)", "Chưa check-in"],
                ["TIECTET-8805", "Đỗ Minh Trí", "VNG Corporation", "Bàn 2 (Công nghệ)", "Ghế 3", "Ăn mặn", "Chưa check-in"]
            ]
        },
        "Dat_Tiec_Nha_Hang": {
            "headers": ["Bàn Tiệc", "Chủ Đề Nhóm", "Tổng Số Khách", "Suất Ăn Mặn", "Suất Ăn Chay"],
            "rows": [
                ["Bàn 1", "Khách Mời VIP Bất Động Sản", 2, 1, 1],
                ["Bàn 2", "Khách Mời Doanh Nghiệp Công Nghệ", 3, 2, 1]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 50: Tu dong tom tat Executive Summary Dashboard 1 trang
    # =========================================================================
    b50 = WorkspaceBuilder(DEPT, "50-executive-summary-one-page")
    b50.write_agents_md(
        role_title="Cố vấn Quản trị & Trợ lý Ban Điều Hành (Executive Assistant)",
        department_name="Văn phòng Ban Tổng Giám Đốc",
        constitution_items=[
            "Tóm tắt quản trị 1 trang (One-Page Executive Summary): Tổng hợp các chỉ số cốt lõi từ các sheet Doanh thu, Chi phí, Nhân sự, Tồn kho.",
            "Bản tóm tắt hành động: 4 gạch đầu dòng rõ ràng: Điểm sáng, Điểm nghẽn, Cảnh báo rủi ro, Đề xuất hành động."
        ]
    )
    b50.write_rule(
        rule_file_name="quy_chuan_executive_summary.md",
        description="Quy chuẩn lập báo cáo điều hành tóm tắt 1 trang cho Ban Giám đốc",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Báo Cáo Điều Hành One-Page Dashboard",
        guidelines=[
            "Tạo sheet đầu tiên tên là `00_Executive_Summary`.",
            "Trình bày các chỉ số KPI lớn nổi bật (Doanh thu, Lợi nhuận, Tồn kho, Nhân sự) so với tháng trước.",
            "Xuất ra file `Bao_cao_tong_hop_thang_Executive.xlsx`."
        ]
    )
    b50.write_corporate_styling_rule()
    b50.write_security_hooks(["bao_cao_tong_hop_thang.xlsx"])
    b50.write_skill(
        skill_name="tao-executive-summary",
        description="Use this skill to synthesize multi-sheet operational workbooks into a concise one-page executive dashboard.",
        skill_title="Quy trình lập báo cáo điều hành tóm tắt 1 trang",
        steps=[
            {"name": "Đọc tất cả các sheet", "desc": "Nạp file `bao_cao_tong_hop_thang.xlsx`."},
            {"name": "Rút trích chỉ số điều hành", "desc": "Tổng hợp các số liệu KPI quan trọng nhất."},
            {"name": "Thiết kế Dashboard 1 trang", "desc": "Tạo sheet `00_Executive_Summary` và lưu file `Bao_cao_tong_hop_thang_Executive.xlsx`."}
        ]
    )
    b50.write_prompt_demo(
        problem_pain="File Excel cuối tháng nặng 10 sheets đầy số liệu chi tiết, sếp bận chỉ muốn đọc 1 trang tóm tắt những con số quan trọng nhất và các điểm nghẽn cần duyệt.",
        interactive_hook="Nếu sếp chỉ có đúng 60 giây trước khi bước vào cuộc họp Hội đồng Quản trị, 4 con số tài chính và vận hành nào bạn bắt buộc phải đưa lên đầu trang?",
        prompt_cmd="Đọc toàn bộ các sheet trong file bao_cao_tong_hop_thang.xlsx. Hãy tạo thêm sheet đầu tiên '00_Executive_Summary' thiết kế gọn gàng trong 1 trang nhìn gồm các KPI cốt lõi. Viết bản tóm tắt quản trị ngắn gọn (Điểm sáng, Điểm nghẽn, Rủi ro, Đề xuất) vào file Bao_cao_tong_hop_thang_Executive.xlsx.",
        prompt_pitfalls="Nếu nhồi nhét quá nhiều bảng chi tiết khiến Dashboard dài hơn 1 trang màn hình (Scroll-down required), bản tóm tắt sẽ mất đi giá trị điều hành cấp cao.",
        expected_output="File `Bao_cao_tong_hop_thang_Executive.xlsx` có sheet Dashboard 1 trang sang trọng, súc tích dành cho Ban Giám đốc.",
        wow_moment="Cái kết hoàn hảo cho buổi học: biến người làm Excel từ một thợ nhập liệu thành một chuyên gia phân tích tham mưu cho lãnh đạo."
    )
    b50.create_excel("bao_cao_tong_hop_thang.xlsx", {
        "DoanhThu": {
            "headers": ["Kênh Bán Hàng", "Kế Hoạch (VNĐ)", "Thực Hiện (VNĐ)", "Tỷ Lệ Đạt (%)"],
            "rows": [
                ["Kênh Đại lý B2B", 2000000000, 2200000000, 110],
                ["Kênh Bán lẻ Showroom", 1500000000, 1350000000, 90],
                ["Kênh Sàn TMĐT Shopee/TikTok", 800000000, 950000000, 118]
            ]
        },
        "ChiPhi": {
            "headers": ["Khoản Mục", "Ngân Sách Được Duyệt (VNĐ)", "Thực Chi (VNĐ)", "Chênh Lệch"],
            "rows": [
                ["Chi phí lương & BHXH", 850000000, 840000000, -10000000],
                ["Chi phí quảng cáo Marketing", 300000000, 320000000, 20000000],
                ["Chi phí vận hành kho bãi", 150000000, 145000000, -5000000]
            ]
        },
        "NhanSu": {
            "headers": ["Chỉ Số", "Tháng Trước", "Tháng Này"],
            "rows": [
                ["Tổng số nhân sự", 120, 124],
                ["Tỷ lệ nghỉ việc (Turnover Rate)", "4.5%", "2.1%"]
            ]
        }
    })
    # Reference output
    b50.create_excel("_ket_qua_mau_chuan.xlsx", {
        "00_Executive_Summary": {
            "headers": ["Chỉ Số Điều Hành Cốt Lõi", "Kế Hoạch", "Thực Tế Đạt", "% Hoàn Thành", "Đánh Giá Ban Điều Hành"],
            "rows": [
                ["Tổng Doanh Thu Hợp Nhất", 4300000000, 4500000000, "104.7%", "Vượt mục tiêu 4.7% (Đại lý & TMĐT tăng trưởng mạnh)"],
                ["Tổng Chi Phí Hoạt Động (OPEX)", 1300000000, 1305000000, "100.4%", "Kiểm soát ngân sách tốt (+0.4% do tăng ngân sách Ads)"],
                ["Lợi Nhuận Hoạt Động Ước Tính", 3000000000, 3195000000, "106.5%", "Điểm sáng tài chính tháng 10"],
                ["Tỷ Lệ Nghỉ Việc Nhân Sự (Turnover)", "< 3.0%", "2.1%", "Đạt mục tiêu", "Giảm mạnh từ 4.5% tháng trước, nhân sự ổn định"]
            ]
        }
    })

    print(f"--> Successfully generated {DEPT} (7 exercises).")

if __name__ == "__main__":
    generate()
