"""
Department 01: Nhan su - Tuyen dung - C&B (9 Exercises)
Updated with Security Hooks, Corporate Styling Rules, Reference Output, and 6-part PROMPT_DEMO.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generator_core import WorkspaceBuilder

DEPT = "01-nhan-su"

def generate():
    print(f"--> Generating {DEPT} with enhanced controls...")

    # =========================================================================
    # EXERCISE 01: Chuan hoa cham cong tu may quet the
    # =========================================================================
    b1 = WorkspaceBuilder(DEPT, "01-chuan-hoa-cham-cong")
    b1.write_agents_md(
        role_title="Chuyên viên C&B & Chấm công",
        department_name="Phòng Nhân sự",
        constitution_items=[
            "Độ chính xác thời gian: Luôn đảm bảo lấy đúng mốc giờ quẹt thẻ sớm nhất trong ngày làm Giờ Vào và muộn nhất làm Giờ Ra.",
            "Quy tắc ca hành chính: Ca chuẩn 08:30 - 17:30 (nghỉ trưa 12:00 - 13:00). Vào sau 08:30 là đi muộn, ra trước 17:30 là về sớm.",
            "Tô màu trực quan: Tự động highlight màu đỏ cho các trường hợp đi muộn trên 30 phút hoặc quên quẹt thẻ."
        ]
    )
    b1.write_rule(
        rule_file_name="quy_chuan_cham_cong.md",
        description="Quy chuẩn xử lý dữ liệu chấm công thô từ máy vân tay / FaceID",
        globs="*.xlsx, *.csv",
        rule_title="Quy Chuẩn Tính Giờ Vào Ra & Số Phút Đi Muộn",
        guidelines=[
            "Chuyển đổi cột Ngày giờ về đúng định dạng datetime chuẩn ISO.",
            "Gom nhóm (Group by) theo Mã NV và Ngày để tính MIN(Giờ quẹt) = Giờ Vào, MAX(Giờ quẹt) = Giờ Ra.",
            "Nếu chỉ có 1 lần quẹt trong ngày: ghi chú 'Quên quẹt Vào/Ra' và tính 0.5 công.",
            "Xuất ra file kết quả `bang_cong_chuan_hoa.xlsx` gồm 2 sheet: 'Chi_Tiet_Hang_Ngay' và 'Tong_Hop_Thang'."
        ]
    )
    b1.write_corporate_styling_rule()
    b1.write_security_hooks(["cham_cong_thang_10_raw.xlsx"])
    b1.write_skill(
        skill_name="xu-ly-cham-cong",
        description="Use this skill when processing raw biometric attendance logs into monthly timesheet reports.",
        skill_title="Quy trình xử lý bảng chấm công vân tay",
        steps=[
            {"name": "Đọc dữ liệu thô", "desc": "Kiểm tra cấu trúc file `cham_cong_thang_10_raw.xlsx`, xác định các cột Mã NV, Tên NV, Thời gian quẹt."},
            {"name": "Làm sạch & Gom nhóm", "desc": "Tách Ngày và Giờ, gom theo từng nhân viên trong từng ngày để tìm mốc quẹt đầu tiên và cuối cùng."},
            {"name": "Tính toán công & Phút vi phạm", "desc": "So sánh với mốc 08:30 và 17:30 để tính số phút đi muộn, về sớm và quy đổi công chuẩn."},
            {"name": "Xuất bảng tính chuẩn", "desc": "Tạo file `bang_cong_chuan_hoa.xlsx`, kẻ khung viền, tô màu các ô vi phạm và tính dòng tổng cộng."}
        ]
    )
    b1.write_prompt_demo(
        problem_pain="Máy chấm công xuất file log thô 20.000 dòng, mỗi lần quẹt thẻ là 1 dòng. HR mất 4-5 tiếng dùng hàm mảng phức tạp để tìm giờ vào/ra và tính số phút đi muộn.",
        interactive_hook="Theo các bạn, nếu một nhân viên quẹt thẻ 5 lần trong ngày thì làm sao Excel biết lần nào là Giờ Vào và lần nào là Giờ Ra nếu không viết code VBA?",
        prompt_cmd="Đọc file cham_cong_thang_10_raw.xlsx. Hãy gom nhóm theo từng Nhân viên và từng Ngày: lấy giờ quẹt sớm nhất làm Giờ vào, muộn nhất làm Giờ ra. Tính số phút đi muộn (nếu vào sau 08:30), số phút về sớm (nếu ra trước 17:30), và tổng số công trong ngày. Xuất ra file bang_cong_chuan_hoa.xlsx gồm 2 sheet: Chi tiết từng ngày và Bảng tổng hợp tháng của từng nhân viên, tô màu đỏ các dòng đi muộn quá 30 phút.",
        prompt_pitfalls="Nếu không dặn AI mốc giờ nghỉ trưa (12:00 - 13:00) hoặc không dặn quy tắc 'quẹt 1 lần trong ngày tính quên quẹt', AI có thể lấy nhầm giờ ăn trưa làm giờ ra về.",
        expected_output="File `bang_cong_chuan_hoa.xlsx` được tạo tự động với 2 sheets, các cột giờ vào/ra chuẩn chỉ, tính đúng số phút đi muộn và tô màu cảnh báo vi phạm.",
        wow_moment="Xử lý 20.000 dòng log thô trong 15 giây mà không cần viết bất kỳ công thức mảng hay VBA phức tạp nào."
    )
    rows_att = [
        ["NV001", "Nguyễn Văn An", "2026-10-01 08:15:20"],
        ["NV001", "Nguyễn Văn An", "2026-10-01 12:05:10"],
        ["NV001", "Nguyễn Văn An", "2026-10-01 12:50:33"],
        ["NV001", "Nguyễn Văn An", "2026-10-01 17:40:12"],
        ["NV002", "Trần Thị Mai", "2026-10-01 09:12:00"],
        ["NV002", "Trần Thị Mai", "2026-10-01 17:35:00"],
        ["NV003", "Lê Hoàng Long", "2026-10-01 08:25:00"],
        ["NV003", "Lê Hoàng Long", "2026-10-01 16:50:00"],
        ["NV004", "Phạm Quỳnh Chi", "2026-10-01 08:20:00"],
        ["NV005", "Vũ Minh Đức", "2026-10-01 08:28:00"],
        ["NV005", "Vũ Minh Đức", "2026-10-01 17:32:00"],
        ["NV001", "Nguyễn Văn An", "2026-10-02 08:22:15"],
        ["NV001", "Nguyễn Văn An", "2026-10-02 17:33:00"],
        ["NV002", "Trần Thị Mai", "2026-10-02 08:29:00"],
        ["NV002", "Trần Thị Mai", "2026-10-02 17:31:00"],
        ["NV003", "Lê Hoàng Long", "2026-10-02 09:35:00"],
        ["NV003", "Lê Hoàng Long", "2026-10-02 18:00:00"],
    ]
    b1.create_excel("cham_cong_thang_10_raw.xlsx", {
        "Raw_Attendance_Logs": {
            "headers": ["Mã Nhân Viên", "Họ và Tên", "Thời Gian Quẹt Thẻ"],
            "rows": rows_att
        }
    })
    # Reference output
    b1.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Chi_Tiet_Hang_Ngay": {
            "headers": ["Ngày", "Mã NV", "Họ và Tên", "Giờ Vào", "Giờ Ra", "Phút Đi Muộn", "Phút Về Sớm", "Số Công", "Ghi Chú"],
            "rows": [
                ["2026-10-01", "NV001", "Nguyễn Văn An", "08:15", "17:40", 0, 0, 1.0, "Đúng giờ"],
                ["2026-10-01", "NV002", "Trần Thị Mai", "09:12", "17:35", 42, 0, 1.0, "Đi muộn >30p"],
                ["2026-10-01", "NV003", "Lê Hoàng Long", "08:25", "16:50", 0, 40, 1.0, "Về sớm"],
                ["2026-10-01", "NV004", "Phạm Quỳnh Chi", "08:20", "--:--", 0, 0, 0.5, "Quên quẹt Ra"]
            ]
        },
        "Tong_Hop_Thang": {
            "headers": ["Mã NV", "Họ và Tên", "Tổng Công Chuẩn", "Tổng Phút Đi Muộn", "Số Lần Quên Quẹt"],
            "rows": [
                ["NV001", "Nguyễn Văn An", 2.0, 0, 0],
                ["NV002", "Trần Thị Mai", 2.0, 42, 0],
                ["NV003", "Lê Hoàng Long", 2.0, 65, 0],
                ["NV004", "Phạm Quỳnh Chi", 0.5, 0, 1]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 02: Gop 12 bang danh gia KPI thang
    # =========================================================================
    b2 = WorkspaceBuilder(DEPT, "02-gop-danh-gia-kpi")
    b2.write_agents_md(
        role_title="Quản lý Hiệu suất & Đánh giá KPI",
        department_name="Phòng Nhân sự",
        constitution_items=[
            "Chuẩn hóa cấu trúc cột: Tự động ánh xạ tên cột bị lệch giữa các phòng ban (ví dụ: 'ID' -> 'Mã NV', 'Tổng điểm' -> 'Điểm KPI').",
            "Công thức xếp loại: A (>=90), B (75-89), C (60-74), D (<60).",
            "Xuất kết quả duy nhất vào file `Tong_hop_KPI_Nam_2026.xlsx`."
        ]
    )
    b2.write_rule(
        rule_file_name="quy_chuan_gop_kpi.md",
        description="Quy chuẩn tổng hợp và xếp loại KPI đa phòng ban",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Ánh Xạ Cột & Thang Điểm Xếp Loại KPI",
        guidelines=[
            "Tự động nhận diện cột Mã nhân viên qua các từ khóa: ID, MaNV, Mã NV, Employee_ID.",
            "Giữ nguyên tên phòng ban xuất xứ của từng nhân viên.",
            "Tính điểm trung bình năm và cột Xếp loại bằng công thức Excel có thể kiểm tra được."
        ]
    )
    b2.write_corporate_styling_rule()
    b2.write_security_hooks(["KPI_2026/kpi_ky_thuat.xlsx", "KPI_2026/kpi_kinh_doanh.xlsx", "KPI_2026/kpi_marketing.xlsx"])
    b2.write_skill(
        skill_name="gop-kpi-phong-ban",
        description="Use this skill to consolidate heterogeneous departmental KPI spreadsheets into an annual performance report.",
        skill_title="Quy trình gộp báo cáo KPI các phòng ban",
        steps=[
            {"name": "Quét thư mục", "desc": "Tìm tất cả file Excel trong thư mục `KPI_2026`."},
            {"name": "Ánh xạ ngữ nghĩa", "desc": "Chuẩn hóa tiêu đề cột của từng file về định dạng chuẩn chung."},
            {"name": "Gộp dữ liệu", "desc": "Ghép nối các dòng dữ liệu, tránh trùng lặp và bổ sung cột Phòng ban."},
            {"name": "Tính điểm & Xếp loại", "desc": "Tính điểm trung bình, xếp loại A/B/C/D và lưu vào file tổng hợp."}
        ]
    )
    b2.write_prompt_demo(
        problem_pain="Mỗi phòng ban gửi 1 file KPI cấu trúc cột hơi lệch nhau. HR phải mở từng file copy-paste thủ công và dễ nhầm thứ tự cột.",
        interactive_hook="Nếu cột ở file Kỹ thuật ghi là 'ID', còn file Kinh doanh ghi là 'Mã NV', khi dùng Power Query hoặc copy paste thông thường chuyện gì sẽ xảy ra?",
        prompt_cmd="Quét toàn bộ các file Excel trong thư mục KPI_2026. Dù tên cột giữa các file có hơi khác nhau (ví dụ: 'Mã NV'/'ID', 'Điểm KPI'/'Tổng điểm'), hãy tự động nhận diện và ánh xạ về chuẩn chung gồm: Mã NV, Họ tên, Phòng ban, Điểm Q1, Điểm Q2, Điểm Q3, Điểm Q4, Điểm trung bình năm. Gộp tất cả vào file Tong_hop_KPI_Nam_2026.xlsx và tự động xếp loại A/B/C/D theo thang điểm.",
        prompt_pitfalls="Nếu không yêu cầu rõ 'bảo toàn tên phòng ban xuất xứ', AI có thể gộp dữ liệu nhưng bỏ quên cột nhận diện phòng ban của nhân viên.",
        expected_output="File `Tong_hop_KPI_Nam_2026.xlsx` chứa đầy đủ nhân sự từ tất cả các phòng ban, chuẩn hóa cột thống nhất và có cột xếp loại tự động.",
        wow_moment="AI tự hiểu ngữ nghĩa của các cột khác tên nhau để gộp chính xác mà không báo lỗi như Power Query hay VBA."
    )
    b2.create_excel("KPI_2026/kpi_ky_thuat.xlsx", {
        "KPI": {
            "headers": ["ID", "Họ và Tên", "Phòng Ban", "Q1", "Q2", "Q3", "Q4"],
            "rows": [
                ["KT01", "Đặng Quốc Huy", "Kỹ thuật", 92, 88, 95, 90],
                ["KT02", "Bùi Hoàng Nam", "Kỹ thuật", 78, 82, 80, 85],
                ["KT03", "Trịnh Thùy Trang", "Kỹ thuật", 65, 70, 68, 72]
            ]
        }
    })
    b2.create_excel("KPI_2026/kpi_kinh_doanh.xlsx", {
        "Sheet1": {
            "headers": ["Mã NV", "Họ tên", "Bộ phận", "Điểm_Q1", "Điểm_Q2", "Điểm_Q3", "Điểm_Q4"],
            "rows": [
                ["KD01", "Nguyễn Tuấn Anh", "Kinh doanh", 95, 98, 92, 96],
                ["KD02", "Lê Thu Hằng", "Kinh doanh", 85, 80, 88, 84]
            ]
        }
    })
    b2.create_excel("KPI_2026/kpi_marketing.xlsx", {
        "DanhSach": {
            "headers": ["Mã Nhân Viên", "Tên Nhân Sự", "Phòng", "Q1", "Q2", "Q3", "Q4"],
            "rows": [
                ["MKT01", "Trần Đình Khôi", "Marketing", 88, 90, 85, 92],
                ["MKT02", "Phạm Bảo Ngọc", "Marketing", 55, 60, 58, 62]
            ]
        }
    })
    # Reference output
    b2.create_excel("_ket_qua_mau_chuan.xlsx", {
        "TongHopKPI": {
            "headers": ["Mã NV", "Họ và Tên", "Phòng Ban", "Q1", "Q2", "Q3", "Q4", "Điểm TB Năm", "Xếp Loại"],
            "rows": [
                ["KT01", "Đặng Quốc Huy", "Kỹ thuật", 92, 88, 95, 90, 91.25, "A"],
                ["KT02", "Bùi Hoàng Nam", "Kỹ thuật", 78, 82, 80, 85, 81.25, "B"],
                ["KT03", "Trịnh Thùy Trang", "Kỹ thuật", 65, 70, 68, 72, 68.75, "C"],
                ["KD01", "Nguyễn Tuấn Anh", "Kinh doanh", 95, 98, 92, 96, 95.25, "A"],
                ["KD02", "Lê Thu Hằng", "Kinh doanh", 85, 80, 88, 84, 84.25, "B"],
                ["MKT01", "Trần Đình Khôi", "Marketing", 88, 90, 85, 92, 88.75, "B"],
                ["MKT02", "Phạm Bảo Ngọc", "Marketing", 55, 60, 58, 62, 58.75, "D"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 03: Tinh luong Gross - Net, BHXH va Thue TNCN luy tien
    # =========================================================================
    b3 = WorkspaceBuilder(DEPT, "03-tinh-luong-gross-net-thue")
    b3.write_agents_md(
        role_title="Chuyên viên C&B & Thuế thu nhập cá nhân",
        department_name="Phòng Nhân sự",
        constitution_items=[
            "Chính xác theo luật lao động & thuế hiện hành: BHXH (8%), BHYT (1.5%), BHTN (1%) = tổng 10.5%.",
            "Mức giảm trừ gia cảnh: Bản thân 11.000.000đ/tháng, Người phụ thuộc 4.400.000đ/người/tháng.",
            "Miễn thuế: Phụ cấp ăn trưa tối đa 730.000đ/tháng và phần chênh lệch lương làm thêm giờ (OT).",
            "Biểu thuế TNCN 7 bậc lũy tiến từng phần chuẩn xác."
        ]
    )
    b3.write_rule(
        rule_file_name="quy_chuan_tinh_luong.md",
        description="Quy chuẩn tính toán lương Gross, Net, bảo hiểm và thuế TNCN lũy tiến",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Bảng Tính Lương & Thuế Thu Nhập Cá Nhân",
        guidelines=[
            "Chèn công thức Excel trực tiếp vào các cột tính toán để kế toán có thể audit kiểm tra.",
            "Thu nhập chịu thuế = Tổng thu nhập - Các khoản phụ cấp miễn thuế.",
            "Thu nhập tính thuế = Thu nhập chịu thuế - Các khoản giảm trừ (Bảo hiểm + Bản thân + Người phụ thuộc).",
            "Xuất ra file `Bang_luong_chi_tiet_T10.xlsx`."
        ]
    )
    b3.write_corporate_styling_rule()
    b3.write_security_hooks(["du_lieu_luong_thang.xlsx"])
    b3.write_skill(
        skill_name="tinh-luong-gross-net",
        description="Use this skill to calculate payroll, insurance deductions, and 7-tier progressive personal income tax.",
        skill_title="Quy trình lập bảng tính lương & thuế TNCN",
        steps=[
            {"name": "Đọc bảng công & mức lương", "desc": "Nạp file `du_lieu_luong_thang.xlsx` chứa lương cơ bản, phụ cấp, OT và số người phụ thuộc."},
            {"name": "Tính bảo hiểm bắt buộc", "desc": "Tính trích BHXH/BHYT/BHTN 10.5% trên mức lương đóng bảo hiểm."},
            {"name": "Tính thuế TNCN lũy tiến", "desc": "Áp dụng biểu thuế 7 bậc lũy tiến tính số thuế phải nộp."},
            {"name": "Tính lương Net thực nhận", "desc": "Lương Net = Tổng thu nhập - Bảo hiểm - Thuế TNCN."}
        ]
    )
    b3.write_prompt_demo(
        problem_pain="Công thức tính thuế TNCN 7 bậc lũy tiến trên Excel cực kỳ dài và dễ sai khi nhân viên có thay đổi người phụ thuộc và lương OT.",
        interactive_hook="Ai ở đây từng viết công thức tính thuế TNCN 7 bậc bằng 7 hàm IF lồng nhau và bị sót dấu ngoặc đóng chưa?",
        prompt_cmd="Dựa vào file du_lieu_luong_thang.xlsx, hãy tính bảng lương hoàn chỉnh: trừ BHXH/BHYT/BHTN (10.5%), trừ giảm trừ gia cảnh bản thân (11 triệu) và người phụ thuộc (4.4 triệu/người), miễn thuế ăn trưa tối đa 730k và phần chênh lệch OT. Tính thuế TNCN 7 bậc và lương Net thực nhận. Chèn công thức Excel vào các cột và lưu vào Bang_luong_chi_tiet_T10.xlsx.",
        prompt_pitfalls="Nếu không nhắc AI về ngưỡng miễn thuế tiền ăn trưa (tối đa 730k) hoặc không dặn chèn Live Formulas, AI có thể chỉ dán số chết (hardcoded static values) làm mất khả năng audit của kế toán.",
        expected_output="File `Bang_luong_chi_tiet_T10.xlsx` có đầy đủ công thức Excel hoạt động tại từng ô, tính đúng từng bậc thuế và lương Net.",
        wow_moment="Không chỉ điền kết quả tĩnh mà ghi trực tiếp công thức Excel chuẩn vào từng ô để kế toán kiểm tra được."
    )
    b3.create_excel("du_lieu_luong_thang.xlsx", {
        "Luong_Thang_10": {
            "headers": ["Mã NV", "Họ và Tên", "Lương Thỏa Thuận", "Phụ Cấp Ăn Trưa", "Phụ Cấp Điện Thoại", "Giờ OT Ngày Thường", "Số Người Phụ Thuộc"],
            "rows": [
                ["NV01", "Nguyễn Văn Tuấn", 25000000, 1000000, 500000, 10, 1],
                ["NV02", "Trần Thị Hà", 15000000, 800000, 300000, 0, 0],
                ["NV03", "Lê Văn Hùng", 45000000, 1000000, 1000000, 5, 2],
                ["NV04", "Vũ Hoàng My", 9000000, 730000, 200000, 0, 0]
            ]
        }
    })
    b3.create_excel("_ket_qua_mau_chuan.xlsx", {
        "BangLuongChiTiet": {
            "headers": ["Mã NV", "Họ và Tên", "Tổng Thu Nhập", "BHXH (10.5%)", "Giảm Trừ Bản Thân", "Giảm Trừ NPT", "Thu Nhập Tính Thuế", "Thuế TNCN", "Lương Net Thực Nhận"],
            "rows": [
                ["NV01", "Nguyễn Văn Tuấn", 26500000, 2625000, 11000000, 4400000, 8205000, 520500, 23354500],
                ["NV02", "Trần Thị Hà", 16100000, 1575000, 11000000, 0, 3455000, 172750, 14352250],
                ["NV03", "Lê Văn Hùng", 47000000, 4725000, 11000000, 8800000, 22205000, 2690750, 39584250],
                ["NV04", "Vũ Hoàng My", 9930000, 945000, 11000000, 0, 0, 0, 8985000]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 04: Tach phieu luong va tao ban nhap Gmail (Cross-app MCP)
    # =========================================================================
    b4 = WorkspaceBuilder(DEPT, "04-tach-phieu-luong-gui-email")
    b4.write_agents_md(
        role_title="Chuyên viên Truyền thông Nội bộ & Lương",
        department_name="Phòng Nhân sự",
        constitution_items=[
            "Tuyệt đối bảo mật: Phiếu lương của nhân viên nào chỉ gửi đến đúng email của nhân viên đó.",
            "Tạo bản nháp an toàn: Chỉ tạo thư nháp (Draft) trên Gmail, không tự ý bấm gửi trực tiếp để C&B duyệt lại lần cuối."
        ]
    )
    b4.write_rule(
        rule_file_name="quy_chuan_phieu_luong.md",
        description="Quy chuẩn tách phiếu lương cá nhân và định dạng email HTML",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Định Dạng Phiếu Lương & Tiêu Đề Email",
        guidelines=[
            "Tiêu đề email theo cú pháp: [Phiếu Lương Tháng 10/2026] - [Họ và Tên] - [Mã NV].",
            "Nội dung email là bảng HTML gọn gàng, liệt kê rõ: Lương cơ bản, Thưởng, Khấu trừ BHXH/Thuế, và Thực lĩnh.",
            "Lưu danh sách phiếu lương đã tách ra thư mục `Phieu_Luong_Ca_Nhan/`."
        ]
    )
    b4.write_corporate_styling_rule()
    b4.write_security_hooks(["bang_luong_chot.xlsx"])
    b4.write_mcp_config("gmail")
    b4.write_skill(
        skill_name="tach-phieu-luong-email",
        description="Use this skill to split a master payroll spreadsheet into individual payslips and prepare personalized Gmail drafts.",
        skill_title="Quy trình tách phiếu lương và tạo email nháp",
        steps=[
            {"name": "Đọc bảng lương tổng", "desc": "Nạp file `bang_luong_chot.xlsx` chứa danh sách nhân viên và địa chỉ email."},
            {"name": "Trích xuất từng cá nhân", "desc": "Lặp qua từng dòng, tạo file Excel hoặc bảng biểu chi tiết cho từng nhân viên."},
            {"name": "Tạo bản nháp Gmail", "desc": "Sử dụng công cụ Gmail tạo các bản nháp email chứa bảng lương HTML cá nhân hóa."}
        ]
    )
    b4.write_prompt_demo(
        problem_pain="Sau khi chốt bảng lương tổng, C&B phải tách dòng của từng người để gửi email cá nhân. Làm tay mất 2-3 tiếng và cực kỳ nguy hiểm nếu gửi nhầm.",
        interactive_hook="Nếu gửi nhầm phiếu lương của người có thu nhập 50 triệu cho một bạn nhân viên mới vào lương 8 triệu thì hậu quả nhân sự sẽ thế nào?",
        prompt_cmd="Đọc file bang_luong_chot.xlsx. Với mỗi nhân viên, hãy tạo một bảng chi tiết phiếu lương đẹp mắt và tạo bản nháp (Draft) trên Gmail gửi tới địa chỉ email của nhân viên đó với tiêu đề '[Phiếu lương Tháng 10] - [Họ tên]'. Tuyệt đối chỉ gửi thông tin của đúng cá nhân đó.",
        prompt_pitfalls="Quên ghi rõ 'Chỉ tạo bản nháp Draft' có thể khiến AI gửi thư đi ngay lập tức khi chưa qua bước kiểm duyệt của HR.",
        expected_output="Hàng loạt bản nháp Gmail được tạo tự động với nội dung bảng HTML phiếu lương chỉn chu, đúng người đúng địa chỉ email.",
        wow_moment="Kết hợp Antigravity với Gmail tạo xong hàng chục bản nháp email cá nhân hóa trong 1 phút, an toàn 100% vì vẫn cho người dùng duyệt lại."
    )
    b4.create_excel("bang_luong_chot.xlsx", {
        "LuongChot": {
            "headers": ["Mã NV", "Họ và Tên", "Email", "Phòng Ban", "Lương Thỏa Thuận", "Trừ BHXH", "Thuế TNCN", "Thực Lĩnh"],
            "rows": [
                ["NV01", "Nguyễn Văn An", "an.nguyen@company.com", "Kỹ thuật", 25000000, 2625000, 1150000, 21225000],
                ["NV02", "Trần Thị Mai", "mai.tran@company.com", "Kinh doanh", 18000000, 1890000, 520000, 15590000],
                ["NV03", "Lê Văn Đức", "duc.le@company.com", "Marketing", 16000000, 1680000, 310000, 14010000]
            ]
        }
    })
    b4.create_excel("_ket_qua_mau_chuan.xlsx", {
        "PhieuLuong_Mau_NV01": {
            "headers": ["Khoản Mục", "Số Tiền (VNĐ)", "Ghi Chú"],
            "rows": [
                ["Lương thỏa thuận", 25000000, "Theo hợp đồng lao động"],
                ["Trừ BHXH/BHYT/BHTN (10.5%)", -2625000, "Trừ theo quy định pháp luật"],
                ["Thuế thu nhập cá nhân tạm khấu trừ", -1150000, "Biểu thuế 7 bậc lũy tiến"],
                ["LƯƠNG THỰC LĨNH CHUYỂN KHOẢN", 21225000, "Đã chuyển vào STK ngân hàng"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 05: Trich xuat hang loat CV ung vien vao Excel
    # =========================================================================
    b5 = WorkspaceBuilder(DEPT, "05-trich-xuat-cv-ung-vien")
    b5.write_agents_md(
        role_title="Chuyên viên Tuyển dụng & Đánh giá Ứng viên",
        department_name="Phòng Nhân sự",
        constitution_items=[
            "Trích xuất dữ liệu không thiên vị: Đọc trung thực thông tin kinh nghiệm, kỹ năng và học vấn từ hồ sơ.",
            "Chuẩn hóa số điện thoại: Luôn chuẩn hóa số điện thoại về dạng 10 chữ số bắt đầu bằng số 0.",
            "Chấm điểm độ phù hợp: Cho điểm thang 100 dựa trên mô tả công việc (JD) vị trí Senior Marketing."
        ]
    )
    b5.write_rule(
        rule_file_name="quy_chuan_trich_xuat_cv.md",
        description="Quy chuẩn bóc tách thông tin hồ sơ ứng viên từ tài liệu văn bản sang Excel",
        globs="*.txt, *.docx, *.pdf",
        rule_title="Quy Chuẩn Bóc Tách Hồ Sơ Tuyển Dụng",
        guidelines=[
            "Trích xuất đủ các trường: Họ tên, Số điện thoại, Email, Số năm kinh nghiệm, Công ty gần nhất, Kỹ năng cốt lõi, Điểm đánh giá.",
            "Sắp xếp bảng theo thứ tự Điểm đánh giá từ cao xuống thấp.",
            "Lưu kết quả vào file `Tracking_Ung_Vien.xlsx`."
        ]
    )
    b5.write_corporate_styling_rule()
    b5.write_security_hooks(["CV_Ung_Vien/CV_Nguyen_Van_A.txt", "CV_Ung_Vien/CV_Tran_Thi_B.txt", "CV_Ung_Vien/CV_Le_Van_C.txt"])
    b5.write_skill(
        skill_name="trich-xuat-cv-ung-vien",
        description="Use this skill to scan candidate resume files and compile them into a standardized applicant tracking Excel sheet.",
        skill_title="Quy trình bóc tách CV và lập bảng theo dõi ứng viên",
        steps=[
            {"name": "Đọc thư mục CV", "desc": "Quét toàn bộ hồ sơ trong thư mục `CV_Ung_Vien/`."},
            {"name": "Phân tích nội dung", "desc": "Rút trích các thông tin định danh và đánh giá năng lực theo yêu cầu công việc."},
            {"name": "Xuất file bảng tính", "desc": "Tạo file `Tracking_Ung_Vien.xlsx` với định dạng chuyên nghiệp."}
        ]
    )
    b5.write_prompt_demo(
        problem_pain="Tuyển dụng nhận về hàng chục CV mỗi ngày. Ngồi mở từng CV gõ họ tên, SĐT, kinh nghiệm vào file Excel mất 2-3 tiếng.",
        interactive_hook="Mỗi đợt tuyển dụng các bạn nhận được bao nhiêu CV? Có bao giờ bị hoa mắt gõ nhầm số điện thoại của ứng viên tiềm năng chưa?",
        prompt_cmd="Đọc toàn bộ các file CV trong thư mục CV_Ung_Vien. Trích xuất thông tin từng ứng viên gồm: Họ tên, SĐT (chuẩn hóa về dạng 09xx), Email, Vị trí ứng tuyển, Số năm kinh nghiệm, Công ty gần nhất, Học vấn, Kỹ năng chính, và chấm điểm độ phù hợp (thang 100) so với yêu cầu Senior Marketing. Xuất ra file Tracking_Ung_Vien.xlsx sắp xếp từ điểm cao xuống thấp.",
        prompt_pitfalls="Nếu không quy định thang điểm cụ thể và tiêu chí chấm điểm (ví dụ: Senior Marketing cần kinh nghiệm Performance, Teamwork), AI sẽ chấm điểm rất cảm tính.",
        expected_output="File `Tracking_Ung_Vien.xlsx` tổng hợp đầy đủ thông tin các ứng viên kèm điểm số và nhận xét tóm tắt.",
        wow_moment="Biến đống file hồ sơ rời rạc thành bảng Excel quản lý tuyển dụng sạch đẹp chỉ sau 1 câu lệnh."
    )
    b5.write_text_file("CV_Ung_Vien/CV_Nguyen_Van_A.txt", """
HỌ VÀ TÊN: Nguyễn Văn An
SĐT: 0912-345-678 | Email: an.nguyen.mkt@gmail.com
VỊ TRÍ ỨNG TUYỂN: Senior Marketing Specialist
KINH NGHIỆM: 5 năm kinh nghiệm quản lý chiến dịch Performance Marketing tại Vingroup và Shopee.
KỸ NĂNG: Facebook Ads, Google Ads, SEO, Data Analysis, SQL, Teamwork.
HỌC VẤN: Cử nhân Marketing - Đại học Kinh tế Quốc dân (GPA: 3.4/4.0).
    """)
    b5.write_text_file("CV_Ung_Vien/CV_Tran_Thi_B.txt", """
Họ tên: Trần Thị Bích
Số điện thoại: +84 988 776 655
Email: bichtran98@yahoo.com
Ứng tuyển: Chuyên viên Marketing
Kinh nghiệm làm việc: 2 năm làm Content Creator tại công ty truyền thông nhỏ. Viết bài Fanpage, làm video TikTok ngắn.
Kỹ năng: Viết lách, Photoshop cơ bản, Capcut.
Học vấn: Đại học Văn hóa Hà Nội.
    """)
    b5.write_text_file("CV_Ung_Vien/CV_Le_Van_C.txt", """
Ứng viên: Lê Văn Cường
Điện thoại: 0905.123.456
Email: cuong.levan@outlook.com
Vị trí: Senior Marketing Lead
Kinh nghiệm: 6 năm trong ngành F&B, từng dẫn dắt team 8 người chạy chiến dịch ra mắt 15 chuỗi cửa hàng.
Kỹ năng: Brand Strategy, Budget Allocation, Media Planning, KOL Management.
Học vấn: Thạc sĩ QTKD - Đại học Ngoại Thương.
    """)
    b5.create_excel("_ket_qua_mau_chuan.xlsx", {
        "TrackingUngVien": {
            "headers": ["Họ và Tên", "Số Điện Thoại", "Email", "Vị Trí", "Kinh Nghiệm", "Kỹ Năng Chính", "Điểm Phù Hợp", "Đánh Giá"],
            "rows": [
                ["Lê Văn Cường", "0905123456", "cuong.levan@outlook.com", "Senior Marketing", "6 năm", "Brand Strategy, Media Planning", 92, "Xuất sắc, có kinh nghiệm lead"],
                ["Nguyễn Văn An", "0912345678", "an.nguyen.mkt@gmail.com", "Senior Marketing", "5 năm", "Performance, Google/FB Ads, SQL", 88, "Rất tốt, mạnh về kỹ thuật số"],
                ["Trần Thị Bích", "0988776655", "bichtran98@yahoo.com", "Marketing", "2 năm", "Content, Capcut", 65, "Chưa đủ kinh nghiệm cho cấp Senior"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 06: Canh bao hop dong lao dong sap het han (Cross-app MCP)
    # =========================================================================
    b6 = WorkspaceBuilder(DEPT, "06-canh-bao-het-han-hop-dong")
    b6.write_agents_md(
        role_title="Quản lý Quan hệ Lao động & Hợp đồng",
        department_name="Phòng Nhân sự",
        constitution_items=[
            "Chủ động cảnh báo: Lọc các hợp đồng thử việc hoặc hợp đồng xác định thời hạn sắp hết hạn trong vòng 30 ngày.",
            "Tạo lịch nhắc nhở: Tự động ghi nhận thông tin nhắc việc trước 7 ngày để kịp thời chuẩn bị thủ tục gia hạn hoặc chấm dứt."
        ]
    )
    b6.write_rule(
        rule_file_name="quy_chuan_canh_bao_hd.md",
        description="Quy chuẩn phát hiện và cảnh báo hợp đồng lao động sắp hết hạn",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Quản Lý Thời Hạn Hợp Đồng Lao Động",
        guidelines=[
            "Tính số ngày còn lại tính từ Ngày hiện tại đến Ngày kết thúc HĐ.",
            "Phân loại cảnh báo: 'Sắp hết hạn trong 15 ngày' (Màu Đỏ), 'Hết hạn trong 16-30 ngày' (Màu Vàng).",
            "Xuất ra sheet mới mang tên `Canh_Bao_Gia_Han`."
        ]
    )
    b6.write_corporate_styling_rule()
    b6.write_security_hooks(["danh_sach_nhan_su.xlsx"])
    b6.write_mcp_config("google_workspace")
    b6.write_skill(
        skill_name="canh-bao-hop-dong",
        description="Use this skill to scan employee contracts and flag records expiring within 30 days.",
        skill_title="Quy trình rà soát và cảnh báo hạn hợp đồng",
        steps=[
            {"name": "Đọc danh sách nhân sự", "desc": "Nạp file `danh_sach_nhan_su.xlsx`."},
            {"name": "Tính toán hạn hợp đồng", "desc": "Tính số ngày còn lại của từng hợp đồng so với mốc hiện tại."},
            {"name": "Tạo sheet cảnh báo", "desc": "Lọc và định dạng màu sắc cho danh sách nhân sự cần gia hạn hợp đồng."}
        ]
    )
    b6.write_prompt_demo(
        problem_pain="HR thường quên ngày hết hạn thử việc hoặc hợp đồng 1 năm của nhân viên, dẫn đến bị động khi cần gia hạn hoặc làm thủ tục chấm dứt.",
        interactive_hook="Nếu một nhân viên thử việc 2 tháng kết thúc vào hôm nay mà HR quên không gửi thông báo tiếp nhận hay chấm dứt, thì theo luật lao động nhân viên đó sẽ mặc nhiên trở thành gì?",
        prompt_cmd="Đọc file danh_sach_nhan_su.xlsx. Lọc ra tất cả nhân sự có Hợp đồng thử việc hoặc Hợp đồng chính thức sẽ hết hạn trong vòng 30 ngày tới. Tạo một sheet mới tên Canh_Bao_Gia_Han trong file đó, tô màu đỏ các trường hợp dưới 15 ngày và vàng cho các trường hợp 16-30 ngày.",
        prompt_pitfalls="Nếu không quy định mốc ngày hiện tại (Reference Date), AI có thể dùng ngày ngẫu nhiên trong quá khứ dẫn đến lọc sai số ngày còn lại.",
        expected_output="Sheet mới `Canh_Bao_Gia_Han` được tạo với danh sách nhân sự sắp đến hạn, phân loại ngày và định dạng màu sắc nổi bật.",
        wow_moment="Không bao giờ sợ bị sót hạn hợp đồng lao động nhờ khả năng lọc ngày tháng và tự động hóa báo cáo trong vài giây."
    )
    b6.create_excel("danh_sach_nhan_su.xlsx", {
        "DanhSachNhanSu": {
            "headers": ["Mã NV", "Họ và Tên", "Phòng Ban", "Loại HĐ", "Ngày Bắt Đầu", "Ngày Kết Thúc HĐ"],
            "rows": [
                ["NV01", "Phạm Quốc Toản", "Kỹ thuật", "Thử việc 2 tháng", "2026-09-20", "2026-11-20"],
                ["NV02", "Đặng Thị Lan", "Kế toán", "Xác định thời hạn 1 năm", "2025-12-01", "2026-11-30"],
                ["NV03", "Bùi Minh Khang", "Kinh doanh", "Không xác định thời hạn", "2023-01-15", "Vô thời hạn"],
                ["NV04", "Vũ Thị Nguyệt", "Marketing", "Thử việc 2 tháng", "2026-10-01", "2026-12-01"],
                ["NV05", "Nguyễn Tiến Đạt", "Kho vận", "Xác định thời hạn 1 năm", "2026-03-01", "2027-02-28"]
            ]
        }
    })
    b6.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Canh_Bao_Gia_Han": {
            "headers": ["Mã NV", "Họ và Tên", "Phòng Ban", "Loại HĐ", "Ngày Hết Hạn", "Số Ngày Còn Lại", "Mức Độ Cảnh Báo", "Hành Động Cần Làm"],
            "rows": [
                ["NV01", "Phạm Quốc Toản", "Kỹ thuật", "Thử việc 2 tháng", "2026-11-20", 7, "KHẨN CẤP (Dưới 15 ngày)", "Gửi phiếu đánh giá hết thử việc cho Trưởng phòng"],
                ["NV02", "Đặng Thị Lan", "Kế toán", "HĐ 1 năm", "2026-11-30", 17, "CHÚ Ý (16-30 ngày)", "Soạn phụ lục gia hạn HĐLĐ"],
                ["NV04", "Vũ Thị Nguyệt", "Marketing", "Thử việc 2 tháng", "2026-12-01", 18, "CHÚ Ý (16-30 ngày)", "Lên lịch phỏng vấn kết thúc thử việc"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 07: Lam sach du lieu kham suc khoe (Data Cleaning)
    # =========================================================================
    b7 = WorkspaceBuilder(DEPT, "07-lam-sach-du-lieu-kham-suc-khoe")
    b7.write_agents_md(
        role_title="Chuyên viên Quản trị Dữ liệu Nhân sự",
        department_name="Phòng Nhân sự",
        constitution_items=[
            "Chuẩn hóa dữ liệu triệt để: Xóa khoảng trắng thừa, viết hoa chữ cái đầu danh từ riêng (Proper Case).",
            "Đồng bộ ngày tháng: Đưa 100% định dạng ngày tháng về dạng chuẩn duy nhất DD/MM/YYYY.",
            "Bảo toàn số điện thoại & CCCD: Bắt buộc định dạng dưới dạng Text và giữ nguyên số 0 ở đầu."
        ]
    )
    b7.write_rule(
        rule_file_name="quy_chuan_lam_sach_hr.md",
        description="Quy chuẩn làm sạch và chuẩn hóa dữ liệu nhân sự văn phòng",
        globs="*.xlsx, *.csv",
        rule_title="Quy Chuẩn Làm Sạch Dữ Liệu Họ Tên, CCCD, SĐT",
        guidelines=[
            "Họ tên: Bỏ khoảng trắng thừa ở đầu/cuối và giữa các từ; viết hoa chữ cái đầu mỗi từ.",
            "Ngày sinh: Chuyển các định dạng (YYYY-MM-DD, DD.MM.YYYY, DD/MM/YY) về chuẩn DD/MM/YYYY.",
            "Số điện thoại: Đủ 10 số bắt đầu bằng số 0.",
            "Số CCCD: Đủ 12 số bắt đầu bằng số 0 (nếu bị mất phải bù lại).",
            "Xuất ra file `danh_sach_chuan_gui_benh_vien.xlsx`."
        ]
    )
    b7.write_corporate_styling_rule()
    b7.write_security_hooks(["dang_ky_kham_suc_khoe_raw.xlsx"])
    b7.write_skill(
        skill_name="lam-sach-du-lieu-hr",
        description="Use this skill to clean up messy user-submitted forms, fixing capitalization, phone numbers, and dates.",
        skill_title="Quy trình làm sạch dữ liệu đăng ký nhân sự",
        steps=[
            {"name": "Đọc file form thô", "desc": "Nạp file `dang_ky_kham_suc_khoe_raw.xlsx`."},
            {"name": "Xử lý chuỗi & Format", "desc": "Sử dụng các quy tắc regex và xử lý chuỗi để chuẩn hóa tên, SĐT, CCCD và ngày sinh."},
            {"name": "Phát hiện trùng lặp", "desc": "Đánh dấu các dòng trùng lặp số CCCD nếu có."},
            {"name": "Lưu file chuẩn", "desc": "Lưu thành `danh_sach_chuan_gui_benh_vien.xlsx`."}
        ]
    )
    b7.write_prompt_demo(
        problem_pain="Nhân viên tự điền form: tên người viết hoa hết, người viết thường, ngày sinh lộn xộn, CCCD bị mất số 0 đầu.",
        interactive_hook="Bao nhiêu bạn ở đây từng mở file Excel lên và thấy cột Số điện thoại bị mất sạch số 0 ở đầu hoặc biến thành dạng 9.123E+08?",
        prompt_cmd="Làm sạch file dang_ky_kham_suc_khoe_raw.xlsx: chuẩn hóa Họ tên viết hoa chữ cái đầu mỗi từ và bỏ khoảng trắng thừa; chuẩn hóa Ngày sinh về đúng định dạng DD/MM/YYYY; thêm lại số 0 ở đầu cho cột SĐT (đủ 10 số) và CCCD (đủ 12 số) dưới dạng Text; phát hiện và đánh dấu các dòng bị trùng lặp CCCD. Lưu thành file danh_sach_chuan_gui_benh_vien.xlsx.",
        prompt_pitfalls="Nếu không dặn AI lưu cột CCCD/SĐT dưới định dạng Text (chuỗi ký tự), Excel sẽ tự động ép kiểu thành số (Number) và làm biến mất số 0 đầu lần nữa.",
        expected_output="File `danh_sach_chuan_gui_benh_vien.xlsx` sạch bóng lỗi: họ tên chuẩn đẹp, số điện thoại và CCCD đủ số 0 đầu, ngày sinh đồng bộ.",
        wow_moment="Giải quyết các lỗi kinh điển nhất của Excel (mất số 0 đầu, sai ngày tháng, thừa dấu cách) chỉ bằng 1 câu lệnh đơn giản."
    )
    b7.create_excel("dang_ky_kham_suc_khoe_raw.xlsx", {
        "DangKyRaw": {
            "headers": ["STT", "Họ Và Tên", "Ngày Sinh", "Số CCCD", "Số Điện Thoại", "Bệnh Viện Chọn"],
            "rows": [
                [1, "  nguyen   van an  ", "12/05/1995", 10195001234, 912345678, "Bệnh viện Hồng Ngọc"],
                [2, "TRẦN THỊ MAI", "1998-11-25", 38098005678, "0988776655", "Bệnh viện Thu Cúc"],
                [3, "lê hoàng long", "15.8.1992", 10192009999, 905112233, "Bệnh viện Bạch Mai"],
                [4, "Vũ   Minh  Đức ", "04/02/1997", 10195001234, "0912.345.678", "Bệnh viện Hồng Ngọc"]
            ]
        }
    })
    b7.create_excel("_ket_qua_mau_chuan.xlsx", {
        "DanhSachChuan": {
            "headers": ["STT", "Họ và Tên", "Ngày Sinh (DD/MM/YYYY)", "Số CCCD (12 Số)", "Số Điện Thoại", "Bệnh Viện Chọn", "Ghi Chú Trùng Lặp"],
            "rows": [
                [1, "Nguyễn Văn An", "12/05/1995", "010195001234", "0912345678", "Bệnh viện Hồng Ngọc", ""],
                [2, "Trần Thị Mai", "25/11/1998", "038098005678", "0988776655", "Bệnh viện Thu Cúc", ""],
                [3, "Lê Hoàng Long", "15/08/1992", "010192009999", "0905112233", "Bệnh viện Bạch Mai", ""],
                [4, "Vũ Minh Đức", "04/02/1997", "010195001234", "0912345678", "Bệnh viện Hồng Ngọc", "Trùng số CCCD với dòng 1"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 08: Phan tich bien dong nhan su (Turnover Dashboard)
    # =========================================================================
    b8 = WorkspaceBuilder(DEPT, "08-phan-tich-turnover-dashboard")
    b8.write_agents_md(
        role_title="Chuyên viên Phân tích Dữ liệu Nhân sự (HR Analytics)",
        department_name="Phòng Nhân sự",
        constitution_items=[
            "Công thức tính Turnover Rate: Số nhân viên nghỉ việc / ((Số NV đầu kỳ + Số NV cuối kỳ) / 2) * 100%.",
            "Phân tích đa chiều: Tỷ lệ nghỉ việc theo tháng, theo phòng ban và theo nhóm lý do nghỉ."
        ]
    )
    b8.write_rule(
        rule_file_name="quy_chuan_turnover.md",
        description="Quy chuẩn tính toán tỷ lệ nghỉ việc và tạo bảng tổng hợp Dashboard",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Thống Kê Biến Động Nhân Sự",
        guidelines=[
            "Tính tỷ lệ biến động nhân sự từng tháng trong năm.",
            "Tạo bảng Pivot/Summary thể hiện rõ Top 3 lý do nhân viên nghỉ việc nhiều nhất.",
            "Xuất ra file `HR_Turnover_Report.xlsx` kèm bảng biểu trực quan."
        ]
    )
    b8.write_corporate_styling_rule()
    b8.write_security_hooks(["nhan_su_bien_dong_2026.xlsx"])
    b8.write_skill(
        skill_name="phan-tich-turnover",
        description="Use this skill to calculate employee turnover rate and build human resource retention dashboard reports.",
        skill_title="Quy trình phân tích biến động nhân sự",
        steps=[
            {"name": "Đọc dữ liệu nhân sự", "desc": "Nạp file `nhan_su_bien_dong_2026.xlsx`."},
            {"name": "Tính toán chỉ số", "desc": "Tính tỷ lệ nghỉ việc và tốc độ tăng trưởng nhân sự ròng theo từng tháng."},
            {"name": "Lập báo cáo tổng hợp", "desc": "Xuất file `HR_Turnover_Report.xlsx` trình Ban Giám đốc."}
        ]
    )
    b8.write_prompt_demo(
        problem_pain="Sếp yêu cầu báo cáo tỷ lệ nghỉ việc theo phòng ban và lý do nghỉ việc, nhưng HR chỉ có danh sách nhân viên nghỉ việc rời rạc.",
        interactive_hook="Nếu sếp hỏi phòng ban nào đang có tỷ lệ nghỉ việc cao nhất quý vừa qua và lý do hàng đầu là gì, bạn sẽ mất bao lâu để làm bảng biểu này?",
        prompt_cmd="Phân tích file nhan_su_bien_dong_2026.xlsx để lập báo cáo biến động nhân sự: tính tỷ lệ nghỉ việc (Turnover Rate) theo từng tháng, theo từng phòng ban, và thống kê tỷ trọng lý do nghỉ việc. Xuất ra file HR_Turnover_Report.xlsx có sẵn bảng tổng hợp trực quan.",
        prompt_pitfalls="Tính sai mẫu số của Turnover Rate (phải là số nhân sự bình quân trong kỳ = (Đầu kỳ + Cuối kỳ) / 2, không phải chỉ lấy số đầu kỳ).",
        expected_output="File `HR_Turnover_Report.xlsx` chứa bảng chỉ số Turnover Rate chi tiết từng tháng và ma trận phân tích lý do nghỉ việc.",
        wow_moment="Biến dữ liệu biến động nhân sự thô sơ thành một bản báo cáo phân tích quản trị nhân lực sắc bén."
    )
    b8.create_excel("nhan_su_bien_dong_2026.xlsx", {
        "BienDong2026": {
            "headers": ["Tháng", "Phòng Ban", "Đầu Kỳ", "Tuyển Mới", "Nghỉ Việc", "Lý Do Chính"],
            "rows": [
                ["Tháng 1", "Kinh doanh", 40, 5, 4, "Tìm được cơ hội thu nhập cao hơn"],
                ["Tháng 1", "Kỹ thuật", 30, 2, 1, "Chuyển nơi ở"],
                ["Tháng 2", "Kinh doanh", 41, 4, 6, "Áp lực KPI"],
                ["Tháng 2", "Kỹ thuật", 31, 3, 0, "Không có"],
                ["Tháng 3", "Kinh doanh", 39, 6, 5, "Áp lực KPI"],
                ["Tháng 3", "Marketing", 15, 2, 3, "Thay đổi định hướng nghề nghiệp"]
            ]
        }
    })
    b8.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Turnover_Dashboard": {
            "headers": ["Tháng", "Phòng Ban", "Nhân Sự Đầu Kỳ", "Tuyển Mới", "Nghỉ Việc", "Cuối Kỳ", "Bình Quân", "Turnover Rate (%)"],
            "rows": [
                ["Tháng 1", "Kinh doanh", 40, 5, 4, 41, 40.5, "9.9%"],
                ["Tháng 1", "Kỹ thuật", 30, 2, 1, 31, 30.5, "3.3%"],
                ["Tháng 2", "Kinh doanh", 41, 4, 6, 39, 40.0, "15.0%"],
                ["Tháng 2", "Kỹ thuật", 31, 3, 0, 34, 32.5, "0.0%"],
                ["Tháng 3", "Kinh doanh", 39, 6, 5, 40, 39.5, "12.7%"],
                ["Tháng 3", "Marketing", 15, 2, 3, 14, 14.5, "20.7%"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 09: Xep lich truc ca tu dong theo rang buoc
    # =========================================================================
    b9 = WorkspaceBuilder(DEPT, "09-xep-lich-truc-ca-tu-dong")
    b9.write_agents_md(
        role_title="Điều phối Ca trực & Lịch làm việc",
        department_name="Phòng Nhân sự & Vận hành",
        constitution_items=[
            "Tôn trọng ngày nghỉ phép: Không bao giờ xếp nhân viên vào ca trực trong những ngày họ đã đăng ký nghỉ phép.",
            "Quy tắc an toàn sức khỏe: Không ai làm Ca Tối hôm trước mà phải làm Ca Sáng hôm sau.",
            "Công bằng phân bổ: Số lượng ca trực giữa các nhân sự phải được chia đều tương đương nhau."
        ]
    )
    b9.write_rule(
        rule_file_name="quy_chuan_xep_ca.md",
        description="Quy chuẩn xếp lịch trực ca theo các ràng buộc vận hành",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Xếp Lịch Phân Ca Làm Việc",
        guidelines=[
            "Ca Sáng: 08:00 - 16:00 (Ký hiệu: S).",
            "Ca Chiều: 14:00 - 22:00 (Ký hiệu: C).",
            "Ca Tối: 22:00 - 06:00 (Ký hiệu: T).",
            "Nghỉ phép: Ký hiệu: P.",
            "Xuất ra file `Lich_Phan_Ca_Thang_11.xlsx` theo ma trận Nhân Viên x Ngày."
        ]
    )
    b9.write_corporate_styling_rule()
    b9.write_security_hooks(["danh_sach_nv_va_nghi_phep.xlsx"])
    b9.write_skill(
        skill_name="xep-lich-truc-ca",
        description="Use this skill to optimize shift scheduling under employee leave requests and fatigue prevention constraints.",
        skill_title="Quy trình xếp lịch trực ca tự động",
        steps=[
            {"name": "Đọc danh sách và ngày nghỉ", "desc": "Nạp file `danh_sach_nv_va_nghi_phep.xlsx`."},
            {"name": "Áp dụng thuật toán ràng buộc", "desc": "Xếp ca đảm bảo đủ quân số mỗi ca và tuân thủ các quy tắc không làm ca sáng sau ca tối."},
            {"name": "Xuất bảng ma trận", "desc": "Lưu bảng lịch trực ca vào file `Lich_Phan_Ca_Thang_11.xlsx`."}
        ]
    )
    b9.write_prompt_demo(
        problem_pain="Xếp lịch trực 3 ca cho hàng chục nhân viên sao cho vừa đủ người mỗi ca, vừa không trùng lịch xin nghỉ phép, vừa công bằng rất dễ bị sót.",
        interactive_hook="Có ai từng xếp lịch trực ca xong thì bị nhân viên khiếu nại vì vừa trực ca tối đêm hôm trước mà sáng hôm sau 8h đã phải có mặt đi làm không?",
        prompt_cmd="Dựa trên danh sách nhân viên và ngày đăng ký nghỉ phép trong file danh_sach_nv_va_nghi_phep.xlsx, hãy xếp lịch phân ca tháng 11 (Ca Sáng: 2 người, Ca Chiều: 2 người, Ca Tối: 1 người mỗi ngày). Đảm bảo công bằng tổng số ca, không ai trực Ca Tối hôm trước mà phải trực Ca Sáng hôm sau. Xuất ra bảng phân ca theo ma trận Ngày x Nhân viên vào file Lich_Phan_Ca_Thang_11.xlsx.",
        prompt_pitfalls="Quên kiểm tra ràng buộc liên tiếp (No Back-to-Back: Tối hôm trước -> Sáng hôm sau) khiến nhân viên không đủ thời gian ngủ nghỉ phục hồi sức khỏe.",
        expected_output="File `Lich_Phan_Ca_Thang_11.xlsx` dạng ma trận lịch trực cả tháng, tuân thủ 100% các ràng buộc nghỉ phép và quy định ca.",
        wow_moment="Giải quyết bài toán tổ hợp tối ưu hóa phức tạp trong chớp mắt mà làm tay mất cả ngày tẩy xóa."
    )
    b9.create_excel("danh_sach_nv_va_nghi_phep.xlsx", {
        "NhanVienVaPhep": {
            "headers": ["Mã NV", "Họ và Tên", "Chức Vụ", "Ngày Đăng Ký Nghỉ Phép Tháng 11"],
            "rows": [
                ["NV01", "Nguyễn Văn Hùng", "Kỹ thuật viên", "05/11, 12/11"],
                ["NV02", "Trần Đình Trọng", "Kỹ thuật viên", "08/11, 20/11"],
                ["NV03", "Lê Văn Thắng", "Kỹ thuật viên", "15/11, 16/11"],
                ["NV04", "Vũ Hải Đăng", "Kỹ thuật viên", "02/11, 25/11"],
                ["NV05", "Đỗ Tuấn Minh", "Kỹ thuật viên", "10/11, 22/11"],
                ["NV06", "Hoàng Kim Ngân", "Kỹ thuật viên", "01/11, 18/11"]
            ]
        }
    })
    b9.create_excel("_ket_qua_mau_chuan.xlsx", {
        "MaTranPhanCa": {
            "headers": ["Mã NV", "Họ và Tên", "01/11", "02/11", "03/11", "04/11", "05/11", "Tổng Ca Sáng", "Tổng Ca Chiều", "Tổng Ca Tối"],
            "rows": [
                ["NV01", "Nguyễn Văn Hùng", "S", "C", "T", "OFF", "P", 1, 1, 1],
                ["NV02", "Trần Đình Trọng", "C", "S", "S", "C", "T", 2, 2, 1],
                ["NV03", "Lê Văn Thắng", "T", "OFF", "C", "S", "S", 2, 1, 1],
                ["NV04", "Vũ Hải Đăng", "S", "P", "S", "C", "C", 2, 2, 0],
                ["NV05", "Đỗ Tuấn Minh", "C", "T", "OFF", "S", "S", 2, 1, 1],
                ["NV06", "Hoàng Kim Ngân", "P", "S", "C", "T", "OFF", 1, 1, 1]
            ]
        }
    })

    print(f"--> Successfully generated {DEPT} with enhanced controls.")

if __name__ == "__main__":
    generate()
