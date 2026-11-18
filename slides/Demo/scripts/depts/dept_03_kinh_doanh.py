"""
Department 03: Kinh doanh - CRM - CSKH (9 Exercises: 19 -> 27)
Updated with Security Hooks, Corporate Styling Rules, Reference Output, and 6-part PROMPT_DEMO.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generator_core import WorkspaceBuilder

DEPT = "03-kinh-doanh"

def generate():
    print(f"--> Generating {DEPT} with enhanced controls...")

    # =========================================================================
    # EXERCISE 19: Lam sach va loc trung du lieu khach hang CRM
    # =========================================================================
    b19 = WorkspaceBuilder(DEPT, "19-lam-sach-chuan-hoa-crm")
    b19.write_agents_md(
        role_title="Quản trị Cơ sở Dữ liệu Khách hàng & CRM",
        department_name="Phòng Kinh doanh & Tiếp thị",
        constitution_items=[
            "Chống trùng lặp dữ liệu: Phát hiện các khách hàng trùng SĐT hoặc tên công ty tương đồng trên 85%.",
            "Bảo toàn lịch sử chăm sóc: Khi gộp 2 dòng trùng nhau, bắt buộc nối toàn bộ nội dung ghi chú cũ vào chung 1 ô."
        ]
    )
    b19.write_rule(
        rule_file_name="quy_chuan_chuan_hoa_crm.md",
        description="Quy chuẩn làm sạch số điện thoại và lọc trùng dữ liệu CRM",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Chuẩn Hóa Dữ Liệu Khách Hàng CRM",
        guidelines=[
            "SĐT: Loại bỏ dấu chấm, dấu cách, đổi mã quốc gia +84 thành số 0 ở đầu.",
            "Tên công ty: Đồng bộ 'Cty', 'CT TNHH' về chuẩn 'Công ty TNHH'.",
            "Xuất ra file `Data_CRM_Chuan_Hoa.xlsx`."
        ]
    )
    b19.write_corporate_styling_rule()
    b19.write_security_hooks(["data_khach_hang_raw.xlsx"])
    b19.write_skill(
        skill_name="lam-sach-chuan-hoa-crm",
        description="Use this skill to clean CRM contact records, unify company name acronyms, and deduplicate leads.",
        skill_title="Quy trình làm sạch dữ liệu CRM",
        steps=[
            {"name": "Đọc bảng khách hàng thô", "desc": "Nạp file `data_khach_hang_raw.xlsx`."},
            {"name": "Chuẩn hóa chuỗi", "desc": "Làm sạch SĐT và quy chuẩn hóa tên công ty."},
            {"name": "Lọc trùng & Gộp ghi chú", "desc": "Gộp dòng trùng lặp, bảo toàn lịch sử tương tác."},
            {"name": "Lưu file", "desc": "Xuất file `Data_CRM_Chuan_Hoa.xlsx`."}
        ]
    )
    b19.write_prompt_demo(
        problem_pain="Nhiều nhân viên sales cùng nhập khách hàng: SĐT người có dấu chấm, người có +84, tên công ty viết tắt lung tung làm 1 khách bị nhiều sales gọi trùng.",
        interactive_hook="Nếu gộp 2 dòng khách hàng trùng nhau, bạn sẽ xóa bỏ dòng cũ hay làm sao để không làm mất nhật ký cuộc gọi của sales trước đó?",
        prompt_cmd="Làm sạch file data_khach_hang_raw.xlsx: Chuẩn hóa toàn bộ SĐT về dạng 10 số bắt đầu bằng 0 (xóa dấu chấm, đổi +84 thành 0). Chuẩn hóa tên công ty (đưa 'Cty', 'CT TNHH' về 'Công ty TNHH'). Phát hiện các khách hàng trùng SĐT hoặc tên tương đồng, giữ lại dòng mới nhất và gộp lịch sử ghi chú vào chung 1 ô. Xuất ra Data_CRM_Chuan_Hoa.xlsx.",
        prompt_pitfalls="Nếu không hướng dẫn AI nối chuỗi ghi chú (String Concatenation), AI sẽ ghi đè ghi chú mới và xóa sạch toàn bộ lịch sử chăm sóc trước đây.",
        expected_output="File `Data_CRM_Chuan_Hoa.xlsx` sạch sẽ, không còn dòng trùng lặp, tên công ty đồng nhất và ghi chú được bảo toàn.",
        wow_moment="Xử lý trùng lặp thông minh và không làm mất lịch sử ghi chú chăm sóc khách hàng khi gộp dòng."
    )
    b19.create_excel("data_khach_hang_raw.xlsx", {
        "CRM_Raw": {
            "headers": ["Mã KH", "Tên Công Ty", "Người Liên Hệ", "Số Điện Thoại", "Ghi Chú Chăm Sóc"],
            "rows": [
                ["KH101", "Cty TNHH An Phát", "Nguyễn Văn Hùng", "+84912345678", "Đã gọi ngày 10/10: Khách quan tâm gói Basic"],
                ["KH102", "Công ty TNHH An Phát", "Nguyễn V. Hùng", "0912.345.678", "Đã gửi báo giá ngày 15/10: Hẹn gặp lại sau"], # Trùng KH101!
                ["KH103", "CT Cổ Phần Sao Vàng", "Trần Mai Anh", "0988-776-655", "Chưa liên hệ được"],
                ["KH104", "Công ty CP Sao Vàng", "Trần M. Anh", "0988776655", "Gọi lại ngày 20/10: Khách từ chối"] # Trùng KH103!
            ]
        }
    })
    # Reference output
    b19.create_excel("_ket_qua_mau_chuan.xlsx", {
        "CRM_Cleaned": {
            "headers": ["Mã KH Chuẩn", "Tên Doanh Nghiệp Chuẩn", "Người Liên Hệ", "Số Điện Thoại Chuẩn", "Lịch Sử Chăm Sóc Gộp", "Trạng Thái"],
            "rows": [
                ["KH101", "Công ty TNHH An Phát", "Nguyễn Văn Hùng", "0912345678", "[10/10] Khách quan tâm gói Basic | [15/10] Đã gửi báo giá, hẹn gặp lại", "Đã gộp 2 bản ghi trùng"],
                ["KH103", "Công ty Cổ phần Sao Vàng", "Trần Mai Anh", "0988776655", "[18/10] Chưa liên hệ được | [20/10] Gọi lại: Khách từ chối", "Đã gộp 2 bản ghi trùng"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 20: Tinh hoa hong sales luy tien nhieu bac
    # =========================================================================
    b20 = WorkspaceBuilder(DEPT, "20-tinh-hoa-hong-luy-tien")
    b20.write_agents_md(
        role_title="Quản lý Vận hành Kinh doanh & Thưởng Doanh số",
        department_name="Phòng Kinh doanh",
        constitution_items=[
            "Minh bạch hoa hồng: Tính toán tách bạch hoa hồng bậc thang theo tỷ lệ hoàn thành KPI.",
            "Điều kiện ghi nhận: Chỉ tính hoa hồng trên các đơn hàng có trạng thái 'Đã thu đủ tiền'."
        ]
    )
    b20.write_rule(
        rule_file_name="quy_chuan_hoa_hong_sales.md",
        description="Quy chuẩn tính thưởng hoa hồng lũy tiến cho Sales và Team Leader",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Bảng Tính Hoa Hồng Lũy Tiến",
        guidelines=[
            "Tỷ lệ hoàn thành KPI = Doanh số thực thu / Chỉ tiêu KPI * 100%.",
            "Mức thưởng: <80% KPI: 0%; 80-100%: 3%; Phần vượt 100-120%: 5%; Phần vượt >120%: 8%.",
            "Thưởng Team Leader: 1.5% trên tổng doanh số thực thu của cả nhóm.",
            "Xuất ra file `Bang_tinh_hoa_hong_T11.xlsx`."
        ]
    )
    b20.write_corporate_styling_rule()
    b20.write_security_hooks(["doanh_so_sales_t11.xlsx"])
    b20.write_skill(
        skill_name="tinh-hoa-hong-sales",
        description="Use this skill to compute multi-tier tiered sales commission bonuses for representatives and team leads.",
        skill_title="Quy trình tính hoa hồng doanh số lũy tiến",
        steps=[
            {"name": "Đọc dữ liệu doanh số", "desc": "Nạp file `doanh_so_sales_t11.xlsx`."},
            {"name": "Lọc đơn hợp lệ", "desc": "Chỉ lấy các đơn hàng đã thu đủ tiền."},
            {"name": "Tính hoa hồng bậc thang", "desc": "Áp dụng biểu tỷ lệ lũy tiến cho từng nhân viên và trưởng nhóm."},
            {"name": "Xuất bảng tính", "desc": "Lưu file `Bang_tinh_hoa_hong_T11.xlsx`."}
        ]
    )
    b20.write_prompt_demo(
        problem_pain="Chính sách hoa hồng bậc thang nhiều tầng rất phức tạp, tháng nào tính thưởng kế toán và sales cũng tranh cãi nhau.",
        interactive_hook="Nếu một sales đạt 115% KPI thì số doanh số vượt 15% sẽ được nhân hoa hồng 5% hay toàn bộ 115% đều được hưởng mức 5%?",
        prompt_cmd="Từ file doanh_so_sales_t11.xlsx, hãy tính bảng thưởng hoa hồng tháng 11 cho từng Sales và Team Leader theo chính sách bậc thang: <80% KPI: 0%, 80-100%: 3%, 100-120%: 5%, >120%: 8%; cộng 1.5% cho Team Leader. Chỉ tính trên đơn 'Đã thu tiền'. Xuất ra Bang_tinh_hoa_hong_T11.xlsx.",
        prompt_pitfalls="Nếu không hướng dẫn lọc bỏ đơn 'Chưa thanh toán', nhân viên bán được nhiều đơn ảo chưa thu tiền vẫn được tính thưởng sai quy định.",
        expected_output="File `Bang_tinh_hoa_hong_T11.xlsx` minh bạch rõ ràng số tiền thưởng của từng bậc và thưởng nhóm.",
        wow_moment="Minh bạch hóa toàn bộ công thức tính thưởng bậc thang, xóa bỏ hoàn toàn tranh cãi giữa Sales và Kế toán."
    )
    b20.create_excel("doanh_so_sales_t11.xlsx", {
        "DonHang": {
            "headers": ["Mã Đơn", "Nhân Viên", "Nhóm", "Chỉ Tiêu KPI", "Doanh Thu Đơn", "Trạng Thái Thu Tiền"],
            "rows": [
                ["DH01", "Nguyễn Văn Tuấn", "Nhóm 1", 100000000, 70000000, "Đã thu đủ tiền"],
                ["DH02", "Nguyễn Văn Tuấn", "Nhóm 1", 100000000, 45000000, "Đã thu đủ tiền"], # Tổng = 115tr (115% KPI)
                ["DH03", "Trần Thu Hà", "Nhóm 1", 80000000, 50000000, "Chưa thanh toán"],
                ["DH04", "Trần Thu Hà", "Nhóm 1", 80000000, 60000000, "Đã thu đủ tiền"],     # Tổng thực thu = 60tr (75% KPI - không đạt)
                ["DH05", "Lê Văn Hùng (Leader)", "Nhóm 1", 150000000, 160000000, "Đã thu đủ tiền"]
            ]
        }
    })
    # Reference output
    b20.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Bang_Hoa_Hong_Sales": {
            "headers": ["Nhân Viên", "Vị Trí", "Chỉ Tiêu KPI", "Doanh Thu Thực Thu", "% Đạt KPI", "Thưởng Bậc 1 (80-100%)", "Thưởng Bậc 2 (100-120%)", "Thưởng Leader (1.5%)", "Tổng Hoa Hồng Nhận"],
            "rows": [
                ["Nguyễn Văn Tuấn", "Sales Executive", 100000000, 115000000, "115.0%", 600000, 750000, 0, 1350000],
                ["Trần Thu Hà", "Sales Executive", 80000000, 60000000, "75.0%", 0, 0, 0, 0],
                ["Lê Văn Hùng", "Team Leader", 150000000, 160000000, "106.7%", 900000, 500000, 5025000, 6425000]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 21: Phan nhom khach hang VIP / Ngu dong theo mo hinh RFM
    # =========================================================================
    b21 = WorkspaceBuilder(DEPT, "21-phan-nhom-khach-hang-rfm")
    b21.write_agents_md(
        role_title="Chuyên viên Phân tích Tăng trưởng Khách hàng (Growth Analyst)",
        department_name="Phòng Kinh doanh",
        constitution_items=[
            "Mô hình RFM chuẩn quốc tế: R (Recency - Ngày mua gần nhất), F (Frequency - Tần suất mua), M (Monetary - Tổng tiền chi).",
            "Phân khúc hành vi: VIP Champions, Loyal, At-risk (Nguy cơ rời bỏ), Dormant (Ngủ đông)."
        ]
    )
    b21.write_rule(
        rule_file_name="quy_chuan_rfm_segment.md",
        description="Quy chuẩn phân nhóm khách hàng bằng mô hình RFM",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Phân Nhóm Khách Hàng RFM",
        guidelines=[
            "Chấm điểm R, F, M từ 1 đến 5.",
            "Khách VIP (Champions): R >= 4, F >= 4, M >= 4.",
            "Khách Nguy cơ rời bỏ (At-risk): R <= 2, F >= 3, M >= 4.",
            "Xuất ra file `Phan_khuc_khach_hang_RFM.xlsx` kèm gợi ý kịch bản chăm sóc."
        ]
    )
    b21.write_corporate_styling_rule()
    b21.write_security_hooks(["lich_su_don_hang.xlsx"])
    b21.write_skill(
        skill_name="phan-nhom-khach-hang-rfm",
        description="Use this skill to score customer transactions with RFM segmentation methodology.",
        skill_title="Quy trình phân nhóm khách hàng RFM",
        steps=[
            {"name": "Đọc lịch sử đơn hàng", "desc": "Nạp file `lich_su_don_hang.xlsx`."},
            {"name": "Tính chỉ số R, F, M", "desc": "Tính số ngày từ lần mua cuối, tổng số đơn và tổng giá trị đơn."},
            {"name": "Phân loại phân khúc", "desc": "Gán nhãn nhóm khách hàng và xuất file `Phan_khuc_khach_hang_RFM.xlsx`."}
        ]
    )
    b21.write_prompt_demo(
        problem_pain="Có hàng nghìn đơn hàng trong 2 năm qua nhưng không biết ai là khách VIP sắp bỏ đi, ai là khách ngủ đông để kích hoạt lại.",
        interactive_hook="Một khách hàng chi 200 triệu năm ngoái nhưng 9 tháng nay không phát sinh đơn hàng nào, bạn xếp họ vào nhóm khách VIP hay nhóm có Nguy cơ rời bỏ?",
        prompt_cmd="Áp dụng mô hình RFM lên file lich_su_don_hang.xlsx: Tính Recency, Frequency, Monetary của từng khách hàng. Chấm điểm và phân nhóm: VIP, Khách trung thành, Có nguy cơ rời bỏ, Khách ngủ đông. Xuất danh sách từng nhóm ra các sheet riêng trong file Phan_khuc_khach_hang_RFM.xlsx.",
        prompt_pitfalls="Nếu không xác định mốc thời gian cố định làm điểm neo tính Recency (Ví dụ ngày 15/11/2026), điểm R sẽ bị thay đổi mỗi lần chạy.",
        expected_output="File `Phan_khuc_khach_hang_RFM.xlsx` có các sheet phân khúc khách hàng kèm điểm số và hành động đề xuất.",
        wow_moment="Đưa một kỹ thuật phân tích dữ liệu cao cấp (RFM Data Analytics) thành 1 câu lệnh đơn giản cho dân văn phòng."
    )
    b21.create_excel("lich_su_don_hang.xlsx", {
        "DonHang": {
            "headers": ["Mã Đơn", "Mã KH", "Tên Khách Hàng", "Ngày Mua", "Giá Trị Đơn (VNĐ)"],
            "rows": [
                ["DH01", "KH01", "Công ty An Phát", "2026-11-05", 50000000],
                ["DH02", "KH01", "Công ty An Phát", "2026-10-12", 45000000],
                ["DH03", "KH01", "Công ty An Phát", "2026-08-15", 60000000], # R gần, F cao, M cao -> VIP
                ["DH04", "KH02", "Công ty Sao Mai", "2025-12-10", 80000000],
                ["DH05", "KH02", "Công ty Sao Mai", "2026-01-20", 90000000], # R rất xa (>9 tháng), F cao, M cao -> At-risk!
                ["DH06", "KH03", "Nguyễn Tuấn Tú", "2026-10-30", 1500000],
                ["DH07", "KH04", "Trần Mai Anh", "2025-05-10", 2000000]   # Dormant
            ]
        }
    })
    # Reference output
    b21.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Tong_Hop_RFM": {
            "headers": ["Mã KH", "Tên Khách Hàng", "Ngày Mua Cuối", "Số Đơn (F)", "Tổng Chi (M)", "Điểm R", "Điểm F", "Điểm M", "Phân Khúc Khách Hàng", "Kịch Bản Đề Xuất"],
            "rows": [
                ["KH01", "Công ty An Phát", "2026-11-05", 3, 155000000, 5, 5, 5, "Champions (VIP)", "Tặng quà tri ân cấp lãnh đạo"],
                ["KH02", "Công ty Sao Mai", "2026-01-20", 2, 170000000, 1, 4, 5, "At-Risk (Nguy cơ mất)", "Giám đốc kinh doanh gọi điện trực tiếp thăm hỏi"],
                ["KH03", "Nguyễn Tuấn Tú", "2026-10-30", 1, 1500000, 4, 1, 1, "New Customer (Mới)", "Gửi email hướng dẫn sử dụng sản phẩm"],
                ["KH04", "Trần Mai Anh", "2025-05-10", 1, 2000000, 1, 1, 1, "Lost / Dormant (Ngủ đông)", "Gửi voucher ưu đãi tái kích hoạt"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 22: Tu dong tao hang loat bao gia Excel tu yeu cau
    # =========================================================================
    b22 = WorkspaceBuilder(DEPT, "22-tao-hang-loat-bao-gia")
    b22.write_agents_md(
        role_title="Sales Admin & Điều phối Hợp đồng",
        department_name="Phòng Kinh doanh",
        constitution_items=[
            "Tra cứu chính xác bảng giá: Ánh xạ mã sản phẩm để lấy đúng đơn giá chuẩn.",
            "Chiết khấu thương mại: Tự động áp dụng chiết khấu 5% cho đơn hàng có giá trị trước thuế trên 50 triệu đồng."
        ]
    )
    b22.write_rule(
        rule_file_name="quy_chuan_tao_bao_gia.md",
        description="Quy chuẩn lập báo giá bán hàng tự động",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Báo Giá Sản Phẩm & Chiết Khấu",
        guidelines=[
            "Lấy thông tin khách hàng từ file yêu cầu báo giá.",
            "Tra cứu đơn giá từ file bảng giá chuẩn.",
            "Xuất ra từng file báo giá riêng trong thư mục `Bao_Gia_Xuat/` theo cú pháp: `Bao_Gia_[MaKH]_[Ngay].xlsx`."
        ]
    )
    b22.write_corporate_styling_rule()
    b22.write_security_hooks(["yeu_cau_bao_gia.xlsx", "bang_gia.xlsx"])
    b22.write_skill(
        skill_name="tao-hang-loat-bao-gia",
        description="Use this skill to generate client quotations by looking up item prices and applying volume discounts.",
        skill_title="Quy trình lập báo giá tự động",
        steps=[
            {"name": "Đọc yêu cầu và bảng giá", "desc": "Nạp file `yeu_cau_bao_gia.xlsx` và `bang_gia.xlsx`."},
            {"name": "Tính giá & Chiết khấu", "desc": "Nhân số lượng với đơn giá và áp dụng mức giảm giá hợp lệ."},
            {"name": "Sinh file báo giá", "desc": "Tạo các file báo giá riêng biệt cho từng khách hàng."}
        ]
    )
    b22.write_prompt_demo(
        problem_pain="Sales Admin mỗi ngày phải làm 15-20 báo giá: tra mã sản phẩm, gõ thông tin khách hàng, tính chiết khấu rất mất thì giờ.",
        interactive_hook="Nếu một khách hàng mua 3 mặt hàng khác nhau trong 1 yêu cầu báo giá, làm sao để tính chiết khấu 5% trên tổng giá trị đơn thay vì chiết khấu từng dòng lẻ?",
        prompt_cmd="Dựa vào yêu cầu trong yeu_cau_bao_gia.xlsx, hãy tra cứu đơn giá từ bang_gia.xlsx, áp dụng chiết khấu 5% cho khách mua trên 50 triệu, và tạo từng file báo giá riêng trong thư mục Bao_Gia_Xuat theo tên Bao_Gia_[MaKH].xlsx.",
        prompt_pitfalls="Nếu không hướng dẫn tính thuế GTGT (10%) sau khi trừ tiền chiết khấu, giá trị tổng thanh toán sẽ bị chênh lệch so với chuẩn kế toán.",
        expected_output="Các file báo giá chuẩn chỉnh được tạo tự động trong thư mục `Bao_Gia_Xuat/`.",
        wow_moment="Tạo hàng loạt báo giá đúng chuẩn nhận diện thương hiệu chỉ trong vài giây."
    )
    b22.create_excel("yeu_cau_bao_gia.xlsx", {
        "YeuCau": {
            "headers": ["Mã KH", "Tên Khách Hàng", "Mã Sản Phẩm", "Số Lượng"],
            "rows": [
                ["KH_ALPHA", "Công ty TNHH Alpha Tech", "SP01", 10],
                ["KH_ALPHA", "Công ty TNHH Alpha Tech", "SP03", 5],
                ["KH_BETA", "Công ty CP Beta Group", "SP02", 2]
            ]
        }
    })
    b22.create_excel("bang_gia.xlsx", {
        "BangGia": {
            "headers": ["Mã Sản Phẩm", "Tên Sản Phẩm", "Đơn Vị Tính", "Đơn Giá (VNĐ)"],
            "rows": [
                ["SP01", "Máy trạm Dell Precision 3660", "Bộ", 28000000],
                ["SP02", "Màn hình Dell UltraSharp 27 inch", "Chiếc", 9500000],
                ["SP03", "Bàn phím cơ Logitech MX Mechanical", "Chiếc", 3200000]
            ]
        }
    })
    # Reference output
    b22.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Mau_Bao_Gia_Chuan": {
            "headers": ["Mã KH", "Tên Khách Hàng", "Mặt Hàng", "Số Lượng", "Đơn Giá", "Thành Tiền", "Chiết Khấu (5%)", "VAT (10%)", "Tổng Thanh Toán"],
            "rows": [
                ["KH_ALPHA", "Công ty TNHH Alpha Tech", "Máy trạm Dell Precision 3660", 10, 28000000, 280000000, 14000000, 26600000, 292600000],
                ["KH_ALPHA", "Công ty TNHH Alpha Tech", "Bàn phím cơ Logitech MX", 5, 3200000, 16000000, 800000, 1520000, 16720000],
                ["KH_BETA", "Công ty CP Beta Group", "Màn hình Dell UltraSharp 27 inch", 2, 9500000, 19000000, 0, 1900000, 20900000]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 23: Phan tich ly do mat khach (Lost Deals) tu text ghi chu
    # =========================================================================
    b23 = WorkspaceBuilder(DEPT, "23-phan-tich-ly-do-mat-khach")
    b23.write_agents_md(
        role_title="Chuyên viên Phân tích Cơ hội Kinh doanh & Win/Loss",
        department_name="Phòng Kinh doanh",
        constitution_items=[
            "Chuyển đổi văn bản phi cấu trúc: Đọc các câu văn tự do của Sales để phân loại nguyên nhân mất đơn hàng.",
            "Nhóm nguyên nhân chuẩn hóa: Giá cao, Thiếu tính năng, Đối thủ cạnh tranh, Chưa có ngân sách, Không liên lạc được, Khác."
        ]
    )
    b23.write_rule(
        rule_file_name="quy_chuan_win_loss.md",
        description="Quy chuẩn phân loại lý do mất khách từ nhật ký ghi chú",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Phân Tích Lost Deals",
        guidelines=[
            "Gán nhãn chuẩn hóa vào cột mới `Nhóm Lý Do Thất Bại`.",
            "Tạo bảng thống kê tỷ trọng % từng lý do theo dòng sản phẩm.",
            "Xuất ra file `Phan_tich_Lost_Deals_CRM.xlsx`."
        ]
    )
    b23.write_corporate_styling_rule()
    b23.write_security_hooks(["crm_lost_deals.xlsx"])
    b23.write_skill(
        skill_name="phan-tich-lost-deals",
        description="Use this skill to categorize unstructured sales notes into standardized win/loss deal outcome categories.",
        skill_title="Quy trình phân tích nguyên nhân mất khách",
        steps=[
            {"name": "Đọc ghi chú CRM", "desc": "Nạp file `crm_lost_deals.xlsx`."},
            {"name": "Phân tích ngữ nghĩa AI", "desc": "Đọc hiểu nội dung từng câu ghi chú và gán nhóm nguyên nhân."},
            {"name": "Lập bảng Pivot thống kê", "desc": "Xuất file `Phan_tich_Lost_Deals_CRM.xlsx` kèm tỷ lệ % từng lý do."}
        ]
    )
    b23.write_prompt_demo(
        problem_pain="Cột ghi chú lý do mất khách trên CRM chứa hàng nghìn câu văn tự do lộn xộn, quản lý không thể dùng PivotTable thống kê được.",
        interactive_hook="Nếu một nhân viên ghi chú 'Khách bảo bên Fast bán rẻ hơn 15%', nguyên nhân chính là 'Giá cao' hay 'Đối thủ cạnh tranh'?",
        prompt_cmd="Đọc cột Ghi chú của Sales trong file crm_lost_deals.xlsx. Hãy phân tích và gán nhãn chuẩn hóa vào cột mới 'Nhóm lý do thất bại' gồm: Giá cao, Thiếu tính năng, Đối thủ cạnh tranh, Chưa có ngân sách, Không liên lạc được. Lập bảng thống kê tỷ lệ % từng nhóm lý do vào file Phan_tich_Lost_Deals_CRM.xlsx.",
        prompt_pitfalls="Nếu không quy định danh mục nhãn cố định (Closed Taxonomy), AI sẽ tự nghĩ ra hàng chục nhãn khác nhau làm loãng dữ liệu thống kê.",
        expected_output="File `Phan_tich_Lost_Deals_CRM.xlsx` với các nhãn nguyên nhân chuẩn hóa và bảng PivotTable thống kê chi tiết.",
        wow_moment="Sức mạnh tuyệt đối của AI: biến văn bản tự do lộn xộn (Unstructured Text) thành danh mục định lượng để làm PivotTable."
    )
    b23.create_excel("crm_lost_deals.xlsx", {
        "LostDeals": {
            "headers": ["Mã Deal", "Khách Hàng", "Sản Phẩm", "Giá Trị Deal", "Ghi Chú Của Sales"],
            "rows": [
                ["D01", "Cty Minh Đức", "Phần mềm HRM", 40000000, "Khách chê đắt hơn bên Fast 15%, không thương lượng được."],
                ["D02", "Cty Đại Nam", "Phần mềm HRM", 60000000, "Gọi điện 3 lần không bắt máy, nhắn Zalo không xem."],
                ["D03", "Cty Hoàng Hà", "Phần mềm CRM", 30000000, "Khách cần tích hợp tổng đài ảo VoIP mà bản hiện tại của mình chưa hỗ trợ."],
                ["D04", "Cty Tân Á", "Phần mềm CRM", 50000000, "Sếp khách hàng cắt ngân sách quý này, hẹn sang năm sau tính tiếp."]
            ]
        }
    })
    # Reference output
    b23.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Lost_Deals_Categorized": {
            "headers": ["Mã Deal", "Khách Hàng", "Sản Phẩm", "Giá Trị Deal", "Ghi Chú Gốc", "Nhóm Lý Do Thất Bại Chuẩn", "Đề Xuất Cải Tiến"],
            "rows": [
                ["D01", "Cty Minh Đức", "Phần mềm HRM", 40000000, "Khách chê đắt hơn bên Fast 15%", "Đối thủ cạnh tranh / Giá", "Xem xét chính sách giá linh hoạt"],
                ["D02", "Cty Đại Nam", "Phần mềm HRM", 60000000, "Gọi 3 lần không bắt máy", "Không liên lạc được", "Chuyển sang kênh Zalo ZNS tự động"],
                ["D03", "Cty Hoàng Hà", "Phần mềm CRM", 30000000, "Cần tích hợp tổng đài ảo VoIP", "Thiếu tính năng", "Đưa vào Product Roadmap Q1/2027"],
                ["D04", "Cty Tân Á", "Phần mềm CRM", 50000000, "Sếp cắt ngân sách quý này", "Chưa có ngân sách", "Duy trì chăm sóc định kỳ"]
            ]
        },
        "Thong_Ke_Ty_Le": {
            "headers": ["Nhóm Lý Do", "Số Lượng Deal", "Tổng Giá Trị (VNĐ)", "Tỷ Trọng (%)"],
            "rows": [
                ["Đối thủ cạnh tranh / Giá", 1, 40000000, "22.2%"],
                ["Không liên lạc được", 1, 60000000, "33.3%"],
                ["Thiếu tính năng", 1, 30000000, "16.7%"],
                ["Chưa có ngân sách", 1, 50000000, "27.8%"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 24: Chia gio Data khach hang (Lead Routing) tu dong
    # =========================================================================
    b24 = WorkspaceBuilder(DEPT, "24-chia-gio-lead-routing")
    b24.write_agents_md(
        role_title="Quản lý Phân bổ Cơ hội Bán hàng (Lead Operations)",
        department_name="Phòng Kinh doanh",
        constitution_items=[
            "Phân chia công bằng & địa lý: Chia đều theo hình thức xoay vòng (Round-robin) theo khu vực địa lý Miền Bắc / Miền Nam.",
            "Ưu tiên năng lực: Các lead doanh nghiệp quy mô > 100 nhân sự được ưu tiên chia cho Senior Sales."
        ]
    )
    b24.write_rule(
        rule_file_name="quy_chuan_lead_routing.md",
        description="Quy chuẩn chia giỏ cơ hội bán hàng tự động cho đội ngũ sales",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Lead Routing",
        guidelines=[
            "Phân bổ lead Hà Nội cho Sales miền Bắc, TP.HCM cho Sales miền Nam.",
            "Tạo các sheet riêng cho từng nhân viên Sales trong file kết quả `Lead_Da_Phan_Bo_Tuan_45.xlsx`."
        ]
    )
    b24.write_corporate_styling_rule()
    b24.write_security_hooks(["lead_moi_tuan_45.xlsx"])
    b24.write_skill(
        skill_name="chia-gio-lead-routing",
        description="Use this skill to distribute inbound sales leads across team members by region and deal size.",
        skill_title="Quy trình chia giỏ Lead tự động",
        steps=[
            {"name": "Đọc lead mới", "desc": "Nạp file `lead_moi_tuan_45.xlsx`."},
            {"name": "Áp dụng luật định tuyến", "desc": "Phân chia theo khu vực và quy mô khách hàng."},
            {"name": "Xuất giỏ riêng từng sales", "desc": "Lưu file `Lead_Da_Phan_Bo_Tuan_45.xlsx`."}
        ]
    )
    b24.write_prompt_demo(
        problem_pain="Marketing đổ về hàng trăm leads mỗi tuần, trưởng phòng sales phải ngồi chia tay và copy vào file riêng của từng bạn rất mất thời gian.",
        interactive_hook="Nếu một lead đến từ Đà Nẵng mà đội ngũ chỉ có team Hà Nội và team Sài Gòn, quy tắc định tuyến của bạn sẽ ưu tiên theo khoảng cách hay theo tải công việc hiện tại của nhân viên?",
        prompt_cmd="Đọc file lead_moi_tuan_45.xlsx. Hãy chia đều các leads khu vực Hà Nội cho 2 Sales miền Bắc (Tuấn, Hà) và TP.HCM cho 2 Sales miền Nam (Hùng, My) theo xoay vòng, ưu tiên lead >100 nhân sự cho Senior Sales (Tuấn, Hùng). Xuất ra file Lead_Da_Phan_Bo_Tuan_45.xlsx gồm các sheet riêng cho từng Sales.",
        prompt_pitfalls="Nếu không hướng dẫn thứ tự ưu tiên: Ưu tiên điều kiện Senior trước, sau đó mới chia vòng tròn các lead còn lại, các lead lớn có thể bị chia nhầm cho nhân viên thử việc.",
        expected_output="File `Lead_Da_Phan_Bo_Tuan_45.xlsx` với các sheet riêng cho từng nhân viên sales, dữ liệu chia công bằng và bảo mật.",
        wow_moment="Tự động hóa hoàn toàn quy trình Lead Routing phức tạp chỉ trong 10 giây."
    )
    b24.create_excel("lead_moi_tuan_45.xlsx", {
        "Leads": {
            "headers": ["Mã Lead", "Tên Công Ty", "Khu Vực", "Số Nhân Sự", "Số Điện Thoại"],
            "rows": [
                ["L01", "Công ty Alpha Hà Nội", "Hà Nội", 150, "0912111222"], # Lead lớn -> Senior Tuấn
                ["L02", "Công ty Beta Sài Gòn", "TP.HCM", 250, "0988333444"],  # Lead lớn -> Senior Hùng
                ["L03", "Cửa hàng Hoa Mai", "Hà Nội", 15, "0905555666"],      # Lead nhỏ -> Hà
                ["L04", "Doanh nghiệp Tân Bình", "TP.HCM", 30, "0934777888"]  # Lead nhỏ -> My
            ]
        }
    })
    # Reference output
    b24.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Phan_Bo_Tong_Hop": {
            "headers": ["Mã Lead", "Tên Doanh Nghiệp", "Khu Vực", "Số Nhân Sự", "Nhân Viên Được Phân Bổ", "Lý Do Phân Bổ"],
            "rows": [
                ["L01", "Công ty Alpha Hà Nội", "Hà Nội", 150, "Nguyễn Văn Tuấn", "Khu vực Hà Nội & Quy mô >100 (Senior)"],
                ["L03", "Cửa hàng Hoa Mai", "Hà Nội", 15, "Trần Thu Hà", "Khu vực Hà Nội (Round-robin)"],
                ["L02", "Công ty Beta Sài Gòn", "TP.HCM", 250, "Lê Văn Hùng", "Khu vực TP.HCM & Quy mô >100 (Senior)"],
                ["L04", "Doanh nghiệp Tân Bình", "TP.HCM", 30, "Vũ Hoàng My", "Khu vực TP.HCM (Round-robin)"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 25: Theo doi tien do muc tieu doanh so (Pacing & Run-rate)
    # =========================================================================
    b25 = WorkspaceBuilder(DEPT, "25-theo-doi-pacing-runrate-sales")
    b25.write_agents_md(
        role_title="Giám đốc Kinh doanh & Quản trị Hiệu suất (Sales Director)",
        department_name="Phòng Kinh doanh",
        constitution_items=[
            "Công thức Run-rate: (Doanh số lũy kế / Số ngày làm việc đã qua) * Tổng số ngày làm việc trong tháng.",
            "Mục tiêu ngày còn lại: (Chỉ tiêu KPI - Doanh số lũy kế) / Số ngày làm việc còn lại."
        ]
    )
    b25.write_rule(
        rule_file_name="quy_chuan_pacing_sales.md",
        description="Quy chuẩn tính toán Pacing, Run-rate và tô màu đèn giao thông",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Báo Cáo Pacing & Run-Rate Doanh Số",
        guidelines=[
            "Định dạng Conditional Formatting màu Xanh (Đạt >=100% KPI), Vàng (80-99%), Đỏ (<80%).",
            "Xuất ra file `Bao_cao_pacing_sales_T11.xlsx`."
        ]
    )
    b25.write_corporate_styling_rule()
    b25.write_security_hooks(["doanh_so_luy_ke.xlsx"])
    b25.write_skill(
        skill_name="theo-doi-pacing-sales",
        description="Use this skill to track sales pacing, project month-end run rates, and daily required run rates.",
        skill_title="Quy trình theo dõi tiến độ doanh số",
        steps=[
            {"name": "Đọc số liệu lũy kế", "desc": "Nạp file `doanh_so_luy_ke.xlsx` tính đến ngày 18 của tháng."},
            {"name": "Tính toán Run-rate", "desc": "Dự phóng doanh số cuối tháng theo nhịp độ bán hàng hiện tại."},
            {"name": "Xuất Dashboard", "desc": "Tạo file `Bao_cao_pacing_sales_T11.xlsx` có định dạng màu trực quan."}
        ]
    )
    b25.write_prompt_demo(
        problem_pain="Đang ở giữa tháng, giám đốc kinh doanh muốn biết cuối tháng ai dự kiến đạt KPI, ai cần tăng tốc bao nhiêu tiền mỗi ngày còn lại.",
        interactive_hook="Hôm nay là ngày 18 của tháng có 26 ngày làm việc, một sales mới đạt 42% chỉ tiêu thì mỗi ngày còn lại bạn ấy phải bán gấp mấy lần tốc độ hiện tại?",
        prompt_cmd="Kết hợp file doanh_so_luy_ke.xlsx (tính đến ngày 18/11, tháng có 26 ngày làm việc). Hãy tính: % Hoàn thành hiện tại, Dự phóng cuối tháng (Run-rate), và Số tiền cần đạt mỗi ngày trong 8 ngày làm việc còn lại để cán đích 100% KPI. Định dạng màu sắc cảnh báo vào file Bao_cao_pacing_sales_T11.xlsx.",
        prompt_pitfalls="Nếu chia đều theo tổng số ngày trong tháng (30 ngày) thay vì số ngày làm việc thực tế (26 ngày, trừ Chủ nhật), mục tiêu ngày sẽ bị tính thấp hơn thực tế.",
        expected_output="File `Bao_cao_pacing_sales_T11.xlsx` chỉ rõ từng nhân viên đang chạy trước hay chậm hơn tiến độ kèm chỉ tiêu ngày.",
        wow_moment="Tạo báo cáo quản trị điều hành sắc bén kèm icon đèn giao thông chỉ trong 1 câu lệnh."
    )
    b25.create_excel("doanh_so_luy_ke.xlsx", {
        "Pacing": {
            "headers": ["Nhân Viên", "Chỉ Tiêu KPI (VNĐ)", "Doanh Số Lũy Kế (VNĐ)", "Số Ngày Đã Bán"],
            "rows": [
                ["Nguyễn Văn Tuấn", 120000000, 95000000, 18],  # Đang chạy rất tốt
                ["Trần Thu Hà", 100000000, 42000000, 18],       # Đang bị chậm tiến độ
                ["Lê Văn Hùng", 150000000, 110000000, 18]
            ]
        }
    })
    # Reference output
    b25.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Pacing_Dashboard": {
            "headers": ["Nhân Viên", "Chỉ Tiêu (VNĐ)", "Lũy Kế (VNĐ)", "% Đã Đạt", "Dự Phóng Cuối Tháng", "% Dự Phóng", "Chỉ Tiêu Cần Đạt/Ngày Còn Lại", "Trạng Thái"],
            "rows": [
                ["Nguyễn Văn Tuấn", 120000000, 95000000, "79.2%", 137222222, "114.4%", 3125000, "Xanh (Vượt tiến độ)"],
                ["Trần Thu Hà", 100000000, 42000000, "42.0%", 60666667, "60.7%", 7250000, "Đỏ (Báo động chậm)"],
                ["Lê Văn Hùng", 150000000, 110000000, "73.3%", 158888889, "105.9%", 5000000, "Xanh (Kịp tiến độ)"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 26: Tong hop khao sat muc do hai long khach hang (NPS / CSAT)
    # =========================================================================
    b26 = WorkspaceBuilder(DEPT, "26-tong-hop-khao-sat-nps-csat")
    b26.write_agents_md(
        role_title="Quản lý Trải nghiệm Khách hàng (CX Manager)",
        department_name="Phòng Chăm sóc Khách hàng",
        constitution_items=[
            "Chỉ số Net Promoter Score (NPS): % Promoters (Điểm 9-10) - % Detractors (Điểm 0-6).",
            "Trích xuất Voice of Customer: Đọc các câu nhận xét mở để gom nhóm các chủ đề khách hàng phàn nàn nhiều nhất."
        ]
    )
    b26.write_rule(
        rule_file_name="quy_chuan_nps_csat.md",
        description="Quy chuẩn tính toán NPS và phân loại phản hồi khảo sát",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Báo Cáo Khảo Sát NPS & CSAT",
        guidelines=[
            "Phân loại điểm: 9-10 (Promoters), 7-8 (Passives), 0-6 (Detractors).",
            "Tính điểm NPS tổng và NPS theo từng chi nhánh/sản phẩm.",
            "Xuất ra file `Bao_cao_khao_sat_NPS.xlsx`."
        ]
    )
    b26.write_corporate_styling_rule()
    b26.write_security_hooks(["khao_sat_khach_hang.xlsx"])
    b26.write_skill(
        skill_name="tong-hop-khao-sat-nps",
        description="Use this skill to analyze CSAT/NPS survey results and extract key customer satisfaction insights.",
        skill_title="Quy trình phân tích kết quả khảo sát khách hàng",
        steps=[
            {"name": "Đọc kết quả khảo sát", "desc": "Nạp file `khao_sat_khach_hang.xlsx`."},
            {"name": "Tính toán chỉ số NPS", "desc": "Phân nhóm điểm và tính công thức NPS chuẩn."},
            {"name": "Phân tích nhận xét mở", "desc": "Gom nhóm các vấn đề phản ánh và xuất file `Bao_cao_khao_sat_NPS.xlsx`."}
        ]
    )
    b26.write_prompt_demo(
        problem_pain="Xuất file khảo sát Google Forms gồm điểm số 1-10 và câu góp ý dài dòng, rất khó tính nhanh NPS và tìm ra khách đang phàn nàn gì nhất.",
        interactive_hook="Nếu khách hàng chấm 7 hoặc 8 điểm thì điểm số này có được tính vào công thức Net Promoter Score (NPS) không?",
        prompt_cmd="Phân tích file khao_sat_khach_hang.xlsx: Phân loại điểm 9-10 (Promoters), 7-8 (Passives), 0-6 (Detractors) để tính chỉ số NPS chung. Đọc cột Ý kiến đóng góp để tìm Top 3 vấn đề khách hàng chưa hài lòng nhất kèm câu trích dẫn tiêu biểu. Xuất file Bao_cao_khao_sat_NPS.xlsx.",
        prompt_pitfalls="Nếu nhầm công thức NPS thành điểm trung bình cộng (Mean Average), báo cáo sẽ không phản ánh đúng tỷ lệ người ủng hộ ròng theo chuẩn quản trị quốc tế.",
        expected_output="File `Bao_cao_khao_sat_NPS.xlsx` có bảng điểm NPS và danh sách các nhóm phản hồi của khách hàng.",
        wow_moment="Vừa tính toán định lượng chỉ số NPS vừa đọc hiểu tiếng Việt để rút trích insight khách hàng trong cùng 1 báo cáo."
    )
    b26.create_excel("khao_sat_khach_hang.xlsx", {
        "KhaoSat": {
            "headers": ["Mã KH", "Chi Nhánh", "Điểm Đánh Giá (0-10)", "Ý Kiến Đóng Góp"],
            "rows": [
                ["KH01", "Hà Nội", 10, "Dịch vụ rất tuyệt vời, nhân viên tư vấn nhiệt tình!"],
                ["KH02", "Hà Nội", 5, "Thời gian giao hàng quá lâu, chờ mất 4 ngày."],
                ["KH03", "TP.HCM", 8, "Sản phẩm tốt nhưng giá hơi cao so với thị trường."],
                ["KH04", "TP.HCM", 4, "Giao sai mẫu sản phẩm, gọi hotline mãi không nghe máy."],
                ["KH05", "Đà Nẵng", 9, "Rất hài lòng, sẽ tiếp tục ủng hộ công ty."]
            ]
        }
    })
    # Reference output
    b26.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Chi_So_NPS": {
            "headers": ["Chỉ Số", "Số Lượng Khách", "Tỷ Lệ (%)", "Điểm NPS Chung"],
            "rows": [
                ["Promoters (9-10)", 2, "40.0%", "+0 (Trung tính)"],
                ["Passives (7-8)", 1, "20.0%", "Công thức: %Promoters - %Detractors"],
                ["Detractors (0-6)", 2, "40.0%", "40% - 40% = 0 NPS"]
            ]
        },
        "Phan_Tich_Phan_Hoi": {
            "headers": ["Vấn Đề Phản Ánh", "Mức Độ Nghiêm Trọng", "Chi Nhánh", "Trích Dẫn Tiêu Biểu Của Khách", "Hành Động Khắc Phục"],
            "rows": [
                ["Giao hàng chậm trễ", "Cao", "Hà Nội", "Chờ mất 4 ngày", "Đổi đơn vị vận chuyển express"],
                ["Giao sai mẫu & Hotline bận", "Rất cao", "TP.HCM", "Gọi hotline mãi không nghe máy", "Kiểm tra khâu đóng gói & thêm trực hotline"],
                ["Giá cao", "Trung bình", "TP.HCM", "Giá hơi cao so với thị trường", "Xem xét chính sách combo"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 27: Quet danh thiep (Namecard) va soan email ket noi
    # =========================================================================
    b27 = WorkspaceBuilder(DEPT, "27-quet-namecard-soan-mail")
    b27.write_agents_md(
        role_title="Chuyên viên Phát triển Đối tác & Kinh doanh",
        department_name="Phòng Kinh doanh",
        constitution_items=[
            "Trích xuất danh bạ đầy đủ: Họ tên, Chức vụ, Tên công ty, SĐT, Email, Địa chỉ website.",
            "Cá nhân hóa thư kết nối: Soạn thư chào hỏi kết nối sau sự kiện dựa trên đúng tên và vị trí công tác của đối tác."
        ]
    )
    b27.write_rule(
        rule_file_name="quy_chuan_namecard.md",
        description="Quy chuẩn bóc tách danh thiếp và lập danh bạ đối tác",
        globs="*.txt, *.jpg, *.png",
        rule_title="Quy Chuẩn Bóc Tách Danh Thiếp & Email Kết Nối",
        guidelines=[
            "Chuẩn hóa số điện thoại và email.",
            "Tạo file Excel `Danh_ba_doi_tac_hoi_thao.xlsx`.",
            "Tạo sẵn nội dung email nháp kết nối chuyên nghiệp."
        ]
    )
    b27.write_corporate_styling_rule()
    b27.write_security_hooks(["Namecards/namecard_01.txt", "Namecards/namecard_02.txt"])
    b27.write_skill(
        skill_name="quet-namecard-soan-mail",
        description="Use this skill to extract contact info from business cards into an Excel directory and draft outreach emails.",
        skill_title="Quy trình bóc tách danh thiếp và soạn email kết nối",
        steps=[
            {"name": "Đọc nội dung danh thiếp", "desc": "Quét tài liệu trong thư mục `Namecards/`."},
            {"name": "Bóc tách thông tin liên hệ", "desc": "Rút trích tên, chức vụ, công ty, email, số điện thoại."},
            {"name": "Xuất Excel & Soạn thư", "desc": "Lưu `Danh_ba_doi_tac_hoi_thao.xlsx` và tạo nội dung thư chào kết nối."}
        ]
    )
    b27.write_prompt_demo(
        problem_pain="Đi hội thảo về cầm 30 tấm danh thiếp, ngồi gõ từng thông tin vào Excel rồi gửi thư chào hỏi mất cả buổi sáng.",
        interactive_hook="Sau khi dự hội thảo kết nối đối tác, trong vòng bao lâu bạn nên gửi email chào hỏi để đối phương còn nhớ đến bạn?",
        prompt_cmd="Đọc toàn bộ file danh thiếp trong thư mục Namecards. Trích xuất thông tin từng người ra file Danh_ba_doi_tac_hoi_thao.xlsx gồm: Họ tên, Chức vụ, Công ty, SĐT, Email. Đồng thời tạo mẫu thư chào hỏi kết nối sau sự kiện được cá nhân hóa theo Tên và Chức vụ của từng người.",
        prompt_pitfalls="Nếu không hướng dẫn bóc tách riêng Họ và Tên đệm với Tên gọi (First Name), email chào hỏi sẽ dùng cả họ lẫn tên một cách gượng gạo (Ví dụ 'Kính gửi Anh Nguyễn Tiến Đạt').",
        expected_output="File `Danh_ba_doi_tac_hoi_thao.xlsx` và các bản thư kết nối đối tác được chuẩn bị sẵn sàng.",
        wow_moment="Biến ảnh/chữ trên danh thiếp thành bảng dữ liệu khách hàng và thư chào hàng cá nhân hóa chỉ trong chớp mắt."
    )
    b27.write_text_file("Namecards/namecard_01.txt", """
VIET COMBANK SECURITIES (VCBS)
NGUYỄN TIẾN ĐẠT - Giám Đốc Phân Tích Khách Hàng Doanh Nghiệp
Mobile: 0915.888.999 | Email: dat.nt@vcbs.com.vn
Địa chỉ: Tòa nhà Vietcombank, 198 Trần Quang Khải, Hoàn Kiếm, Hà Nội
Website: www.vcbs.com.vn
    """)
    b27.write_text_file("Namecards/namecard_02.txt", """
GREEN LOGISTICS SOLUTIONS
TRẦN THỊ HỒNG NHUNG - Head of Supply Chain Partnerships
Hotline: 0904.333.222 | Email: nhung.tran@greenlog.vn
Add: Tầng 8, Vincom Center, 72 Lê Thánh Tôn, Bến Nghé, Quận 1, TP.HCM
    """)
    # Reference output
    b27.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Danh_Ba_Doi_Tac": {
            "headers": ["Họ và Tên", "Chức Vụ", "Tên Doanh Nghiệp", "Số Điện Thoại", "Email", "Địa Chỉ", "Tiêu Đề Email Chào Hỏi", "Nội Dung Thư Kết Nối Cá Nhân Hóa"],
            "rows": [
                ["Nguyễn Tiến Đạt", "Giám Đốc Phân Tích KHDN", "Vietcombank Securities (VCBS)", "0915888999", "dat.nt@vcbs.com.vn", "198 Trần Quang Khải, Hoàn Kiếm, Hà Nội", "Rất vui được kết nối cùng Anh Đạt - Hội thảo Tài chính Doanh nghiệp", "Kính gửi Anh Đạt, Em rất vui khi có cơ hội trao đổi ngắn cùng anh tại sự kiện..."],
                ["Trần Thị Hồng Nhung", "Head of Supply Chain Partnerships", "Green Logistics Solutions", "0904333222", "nhung.tran@greenlog.vn", "72 Lê Thánh Tôn, Bến Nghé, Q.1, TP.HCM", "Kết nối hợp tác chuỗi cung ứng cùng Chị Nhung - Green Logistics", "Kính gửi Chị Nhung, Cảm ơn chị đã dành thời gian chia sẻ về định hướng logistics xanh..."]
            ]
        }
    })

    print(f"--> Successfully generated {DEPT} (9 exercises).")

if __name__ == "__main__":
    generate()
