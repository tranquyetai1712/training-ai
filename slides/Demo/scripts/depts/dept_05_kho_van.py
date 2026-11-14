"""
Department 05: Mua hang - Kho van - Chuoi cung ung (8 Exercises: 36 -> 43)
Updated with Security Hooks, Corporate Styling Rules, Reference Output, and 6-part PROMPT_DEMO.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generator_core import WorkspaceBuilder

DEPT = "05-kho-van"

def generate():
    print(f"--> Generating {DEPT} with enhanced controls...")

    # =========================================================================
    # EXERCISE 36: So sanh bao gia tu nhieu Nha cung cap (Bid Comparison)
    # =========================================================================
    b36 = WorkspaceBuilder(DEPT, "36-so-sanh-bao-gia-ncc")
    b36.write_agents_md(
        role_title="Chuyên viên Mua hàng & Đấu thầu (Purchasing Specialist)",
        department_name="Phòng Mua hàng & Cung ứng",
        constitution_items=[
            "Chuẩn hóa về cùng mặt bằng giá: Đơn giá thực tế = Đơn giá gốc - Chiết khấu + Chi phí vận chuyển phân bổ (chưa VAT).",
            "Đề xuất 2 phương án: (1) Mua tối ưu giá từng món hàng, (2) Mua trọn gói tại 1 NCC có tổng chi phí thấp nhất."
        ]
    )
    b36.write_rule(
        rule_file_name="quy_chuan_so_sanh_ncc.md",
        description="Quy chuẩn lập bảng ma trận so sánh giá đấu thầu mua sắm",
        globs="*.xlsx",
        rule_title="Quy Chuẩn So Sánh Báo Giá Nhà Cung Cấp",
        guidelines=[
            "Tô màu Xanh lá cho NCC có đơn giá thấp nhất ở từng mặt hàng.",
            "Tính tổng ngân sách theo từng phương án mua sắm.",
            "Xuất ra file `Ma_tran_so_sanh_bao_gia_NCC.xlsx`."
        ]
    )
    b36.write_corporate_styling_rule()
    b36.write_security_hooks(["NCC_Quotes/ncc_an_phat.xlsx", "NCC_Quotes/ncc_viet_nhat.xlsx", "NCC_Quotes/ncc_tien_phong.xlsx"])
    b36.write_skill(
        skill_name="so-sanh-bao-gia-ncc",
        description="Use this skill to compare vendor bids, normalize discounts and logistics freight, and recommend lowest cost combinations.",
        skill_title="Quy trình so sánh báo giá nhà cung cấp",
        steps=[
            {"name": "Đọc file báo giá", "desc": "Quét toàn bộ báo giá trong thư mục `NCC_Quotes/`."},
            {"name": "Chuẩn hóa đơn giá", "desc": "Tính đơn giá thực tế sau chiết khấu và cước vận chuyển."},
            {"name": "Lập ma trận so sánh", "desc": "Tạo bảng ma trận so sánh và lưu file `Ma_tran_so_sanh_bao_gia_NCC.xlsx`."}
        ]
    )
    b36.write_prompt_demo(
        problem_pain="Cần mua 20 mặt hàng vật tư, 3 NCC gửi về 3 file báo giá: chỗ đã gồm VAT, chỗ chưa VAT, chiết khấu khác nhau, rất khó so sánh.",
        interactive_hook="Nếu một NCC báo giá gốc cao hơn 5% nhưng chiết khấu 8%, trong khi NCC khác giá gốc rẻ hơn nhưng không chiết khấu, bên nào thực sự rẻ hơn?",
        prompt_cmd="Đọc 3 file báo giá trong thư mục NCC_Quotes. Quy đổi đơn giá các mặt hàng về cùng mặt bằng chưa VAT sau chiết khấu. Tạo bảng Ma trận so sánh giá giữa 3 NCC, tô màu xanh lá cho NCC có giá thấp nhất ở từng món, và đề xuất 2 phương án: mua tối ưu từng món và mua trọn gói 1 NCC rẻ nhất. Xuất ra Ma_tran_so_sanh_bao_gia_NCC.xlsx.",
        prompt_pitfalls="Nếu không quy đổi các báo giá về cùng trạng thái thuế (đều chưa VAT hoặc đều đã VAT), việc so sánh trực tiếp số tiền sẽ làm sai lệch quyết định đấu thầu.",
        expected_output="File `Ma_tran_so_sanh_bao_gia_NCC.xlsx` có bảng so sánh trực quan và đề xuất phương án mua sắm tối ưu.",
        wow_moment="Tự động chuẩn hóa đơn giá về cùng hệ quy chiếu và lập bảng so sánh báo giá (Bid Tabulation) chuẩn quy trình đấu thầu."
    )
    b36.create_excel("NCC_Quotes/ncc_an_phat.xlsx", {
        "BaoGia": {
            "headers": ["Mã Hàng", "Tên Mặt Hàng", "Đơn Vị", "Đơn Giá Gốc (VNĐ)", "Chiết Khấu (%)", "Bao Gồm VAT"],
            "rows": [
                ["VT01", "Thùng carton 3 lớp 40x30x20", "Chiếc", 12000, 5, "Chưa VAT"],
                ["VT02", "Băng dính trong 5cm 100 yard", "Cuộn", 18000, 0, "Chưa VAT"],
                ["VT03", "Màng xốp nổ bọc hàng 1.4m x 100m", "Cuộn", 320000, 8, "Chưa VAT"]
            ]
        }
    })
    b36.create_excel("NCC_Quotes/ncc_viet_nhat.xlsx", {
        "BaoGia": {
            "headers": ["Mã Hàng", "Tên Mặt Hàng", "Đơn Vị", "Đơn Giá Gốc (VNĐ)", "Chiết Khấu (%)", "Bao Gồm VAT"],
            "rows": [
                ["VT01", "Thùng carton 3 lớp 40x30x20", "Chiếc", 11000, 0, "Chưa VAT"], # Rẻ hơn An Phát
                ["VT02", "Băng dính trong 5cm 100 yard", "Cuộn", 19000, 5, "Chưa VAT"],
                ["VT03", "Màng xốp nổ bọc hàng 1.4m x 100m", "Cuộn", 310000, 2, "Chưa VAT"]
            ]
        }
    })
    b36.create_excel("NCC_Quotes/ncc_tien_phong.xlsx", {
        "BaoGia": {
            "headers": ["Mã Hàng", "Tên Mặt Hàng", "Đơn Vị", "Đơn Giá Gốc (VNĐ)", "Chiết Khấu (%)", "Bao Gồm VAT"],
            "rows": [
                ["VT01", "Thùng carton 3 lớp 40x30x20", "Chiếc", 12500, 8, "Chưa VAT"],
                ["VT02", "Băng dính trong 5cm 100 yard", "Cuộn", 17000, 0, "Chưa VAT"], # Rẻ nhất
                ["VT03", "Màng xốp nổ bọc hàng 1.4m x 100m", "Cuộn", 330000, 10, "Chưa VAT"]
            ]
        }
    })
    # Reference output
    b36.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Ma_Tran_So_Sanh_Gia": {
            "headers": ["Mã Hàng", "Tên Mặt Hàng", "NCC An Phát (Sau CK)", "NCC Việt Nhật (Sau CK)", "NCC Tiền Phong (Sau CK)", "Đơn Vị Rẻ Nhất", "Chênh Lệch Tiết Kiệm"],
            "rows": [
                ["VT01", "Thùng carton 3 lớp 40x30x20", 11400, 11000, 11500, "Việt Nhật (11.000đ)", "Tiết kiệm 500đ/c"],
                ["VT02", "Băng dính trong 5cm", 18000, 18050, 17000, "Tiền Phong (17.000đ)", "Tiết kiệm 1.050đ/cuộn"],
                ["VT03", "Màng xốp nổ 1.4m x 100m", 294400, 303800, 297000, "An Phát (294.400đ)", "Tiết kiệm 9.400đ/cuộn"]
            ]
        },
        "De_Xuat_Mua_Sam": {
            "headers": ["Phương Án Mua", "Chi Tiết Đơn Hàng", "Tổng Ngân Sách Dự Kiến", "Ưu Điểm & Khuyến Nghị"],
            "rows": [
                ["PA 1: Tối ưu từng món", "VT01 (Việt Nhật) + VT02 (Tiền Phong) + VT03 (An Phát)", 322400, "Tiết kiệm chi phí tối đa (Rẻ nhất)"],
                ["PA 2: Trọn gói 1 NCC", "Mua toàn bộ tại NCC An Phát", 323800, "Tiện hóa đơn, giảm chi phí vận chuyển 3 nơi"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 37: Canh bao hang ton kho sap het va tinh diem dat hang lai (ROP)
    # =========================================================================
    b37 = WorkspaceBuilder(DEPT, "37-canh-bao-reorder-point")
    b37.write_agents_md(
        role_title="Quản lý Hoạch định Nhu cầu & Tồn kho (Inventory Planner)",
        department_name="Phòng Quản lý Kho",
        constitution_items=[
            "Công thức Điểm đặt hàng lại (ROP): Tốc độ bán/ngày * Thời gian giao hàng (Lead time) + Tồn an toàn (Safety Stock).",
            "Làm tròn theo MOQ: Số lượng đặt mua bắt buộc phải làm tròn lên theo số lượng đặt tối thiểu của nhà cung cấp."
        ]
    )
    b37.write_rule(
        rule_file_name="quy_chuan_reorder_point.md",
        description="Quy chuẩn tính toán điểm đặt hàng lại và lượng hàng cần bổ sung",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Hoạch Định Đặt Hàng Reorder Point",
        guidelines=[
            "Tồn hiệu dụng = Tồn kho hiện tại + Hàng đang về.",
            "Cảnh báo Đặt hàng: Nếu Tồn hiệu dụng <= ROP.",
            "Xuất ra file `Ke_hoach_dat_hang_ROP.xlsx`."
        ]
    )
    b37.write_corporate_styling_rule()
    b37.write_security_hooks(["ton_kho_toc_do_ban.xlsx"])
    b37.write_skill(
        skill_name="canh-bao-reorder-point",
        description="Use this skill to monitor inventory safety stock levels, calculate reorder points (ROP), and generate purchase recommendations.",
        skill_title="Quy trình cảnh báo điểm đặt hàng lại",
        steps=[
            {"name": "Đọc dữ liệu tồn và tốc độ bán", "desc": "Nạp file `ton_kho_toc_do_ban.xlsx`."},
            {"name": "Tính toán ROP và tồn an toàn", "desc": "Xác định các mã hàng rơi xuống dưới điểm đặt hàng lại."},
            {"name": "Tính số lượng cần mua", "desc": "Làm tròn theo MOQ và lưu file `Ke_hoach_dat_hang_ROP.xlsx`."}
        ]
    )
    b37.write_prompt_demo(
        problem_pain="Nhân viên mua hàng đặt hàng theo cảm tính: mã bán chạy thì đứt kho mất doanh số, mã bán chậm thì đọng vốn.",
        interactive_hook="Nếu một mã hàng mỗi ngày bán 10 cái, nhà cung cấp mất 10 ngày để giao hàng và cần giữ tồn an toàn 7 ngày bán, điểm đặt hàng lại (ROP) là bao nhiêu cái?",
        prompt_cmd="Từ file ton_kho_toc_do_ban.xlsx, hãy tính tốc độ tiêu thụ/ngày, mức tồn kho an toàn (7 ngày bán), và Điểm đặt hàng lại (ROP). Lọc các mã hàng cần đặt ngay hôm nay và tính số lượng cần đặt để đủ bán trong 45 ngày (làm tròn theo MOQ). Xuất file Ke_hoach_dat_hang_ROP.xlsx.",
        prompt_pitfalls="Nếu không cộng lượng 'Hàng đang về trên đường' (In-transit Stock) vào lượng tồn hiệu dụng, bạn sẽ đặt hàng trùng lặp và gây dư thừa tồn kho gấp đôi.",
        expected_output="File `Ke_hoach_dat_hang_ROP.xlsx` chỉ rõ mã nào cần đặt ngay và số lượng đặt chuẩn xác theo quy cách MOQ.",
        wow_moment="Biến bảng tính tồn kho tĩnh thành hệ thống hoạch định nhu cầu mua hàng thông minh (MRP thu nhỏ)."
    )
    b37.create_excel("ton_kho_toc_do_ban.xlsx", {
        "TonKho": {
            "headers": ["Mã Hàng", "Tên Hàng", "Tồn Hiện Tại", "Hàng Đang Về", "Bán 90 Ngày Qua", "Lead Time (Ngày)", "MOQ (Chiếc)"],
            "rows": [
                ["SKU-01", "Áo Polo Nam Classic", 120, 0, 900, 10, 100], # Bán 10c/ngày. ROP = 10*10 + 70 = 170. Tồn = 120 < 170 -> CẦN ĐẶT!
                ["SKU-02", "Quần Jean Slimfit", 350, 50, 450, 15, 50],   # Bán 5c/ngày. ROP = 5*15 + 35 = 110. Tồn = 400 > 110 -> ĐỦ
                ["SKU-03", "Áo Khoác Gió Nam", 40, 20, 630, 12, 100]    # Bán 7c/ngày. ROP = 7*12 + 49 = 133. Tồn = 60 < 133 -> CẦN ĐẶT!
            ]
        }
    })
    # Reference output
    b37.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Ke_Hoach_Dat_Hang": {
            "headers": ["Mã Hàng", "Tên Hàng", "Tốc Độ Bán (Cái/Ngày)", "Tồn An Toàn (7 Ngày)", "Điểm ROP", "Tồn Hiệu Dụng", "Trạng Thái", "Nhu Cầu 45 Ngày", "Số Lượng Đặt (Tròn MOQ)"],
            "rows": [
                ["SKU-01", "Áo Polo Nam Classic", 10.0, 70, 170, 120, "CẦN ĐẶT NGAY!", 450, 400],
                ["SKU-02", "Quần Jean Slimfit", 5.0, 35, 110, 400, "Đủ hàng tồn kho", 225, 0],
                ["SKU-03", "Áo Khoác Gió Nam", 7.0, 49, 133, 60, "CẦN ĐẶT NGAY!", 315, 300]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 38: Phan tich ton kho ABC - XYZ va canh bao hang can date / hang chet
    # =========================================================================
    b38 = WorkspaceBuilder(DEPT, "38-phan-tich-ton-kho-abc-xyz")
    b38.write_agents_md(
        role_title="Quản lý Kho & Giám sát Vòng quay Tồn kho",
        department_name="Phòng Quản lý Kho",
        constitution_items=[
            "Phân nhóm ABC Pareto: Nhóm A chiếm 80% tổng giá trị vốn đọng, Nhóm B chiếm 15%, Nhóm C chiếm 5%.",
            "Cảnh báo hạn sử dụng: Lọc các lô hàng có số ngày còn hạn sử dụng < 90 ngày.",
            "Cảnh báo hàng chết (Dead Stock): Mặt hàng tồn kho > 180 ngày không có giao dịch xuất bán."
        ]
    )
    b38.write_rule(
        rule_file_name="quy_chuan_ton_kho_abc.md",
        description="Quy chuẩn phân loại tồn kho ABC và cảnh báo hàng cận date",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Phân Loại Tồn Kho ABC & Hạn Sử Dụng",
        guidelines=[
            "Tính giá trị tồn kho = Số lượng tồn * Giá vốn.",
            "Phân loại ABC theo tỷ lệ phần trăm tích lũy giá trị vốn.",
            "Xuất ra file `Bao_cao_ton_kho_ABC_Canh_bao.xlsx` gồm 3 sheet: 'Phan_Nhom_ABC', 'Hang_Can_Date', 'Hang_Chet_Dead_Stock'."
        ]
    )
    b38.write_corporate_styling_rule()
    b38.write_security_hooks(["ton_kho_theo_lo.xlsx"])
    b38.write_skill(
        skill_name="phan-tich-ton-kho-abc",
        description="Use this skill to conduct ABC inventory valuation analysis and detect near-expiration and dead stock.",
        skill_title="Quy trình phân tích tồn kho ABC và cận date",
        steps=[
            {"name": "Đọc tồn kho chi tiết", "desc": "Nạp file `ton_kho_theo_lo.xlsx`."},
            {"name": "Phân loại ABC & Hạn sử dụng", "desc": "Phân nhóm giá trị vốn và lọc hàng cận hạn <90 ngày, hàng nằm im >180 ngày."},
            {"name": "Xuất báo cáo 3 sheets", "desc": "Lưu file `Bao_cao_ton_kho_ABC_Canh_bao.xlsx`."}
        ]
    )
    b38.write_prompt_demo(
        problem_pain="Kho có hàng nghìn mã hàng, thủ kho không rà soát kịp lô hàng nào sắp hết hạn hoặc mã nào đã nằm im 6 tháng không bán được.",
        interactive_hook="Theo nguyên lý Pareto 80/20 trong quản trị kho, việc kiểm soát chặt chẽ 20% mặt hàng Nhóm A sẽ giúp kiểm soát bao nhiêu % tổng dòng vốn của công ty?",
        prompt_cmd="Phân tích file ton_kho_theo_lo.xlsx: (1) Phân nhóm ABC theo giá trị tồn (A: 80%, B: 15%, C: 5%); (2) Lọc các lô hàng còn hạn sử dụng dưới 90 ngày; (3) Lọc danh sách hàng chết nằm im trên 180 ngày không xuất bán. Xuất ra file Bao_cao_ton_kho_ABC_Canh_bao.xlsx gồm 3 sheet.",
        prompt_pitfalls="Nếu sắp xếp dữ liệu tăng dần thay vì giảm dần theo Giá trị tồn kho trước khi tính % tích lũy, các mặt hàng giá trị nhỏ nhất sẽ bị gán nhầm thành Nhóm A.",
        expected_output="File `Bao_cao_ton_kho_ABC_Canh_bao.xlsx` phân nhóm vốn rõ ràng và khoanh vùng hàng cận date, hàng tồn chết.",
        wow_moment="Giúp lãnh đạo nhìn thấy ngay hàng trăm triệu đồng đang nằm chết trong kho hoặc sắp hết hạn sử dụng."
    )
    b38.create_excel("ton_kho_theo_lo.xlsx", {
        "TonTheoLo": {
            "headers": ["Mã SKU", "Số Lô", "Tên Hàng", "Số Lượng Tồn", "Đơn Giá Vốn", "Hạn Sử Dụng", "Ngày Xuất Gần Nhất"],
            "rows": [
                ["TP01", "L2601", "Sữa tươi tiệt trùng 1L", 2000, 25000, "2026-12-10", "2026-11-01"], # Còn ~27 ngày -> CẬN DATE!
                ["TP02", "L2602", "Dầu ăn thực vật 2L", 500, 85000, "2027-08-20", "2026-11-05"],
                ["MP01", "L2588", "Kem dưỡng da ban đêm", 120, 450000, "2027-10-15", "2026-03-10"] # 8 tháng không bán -> DEAD STOCK!
            ]
        }
    })
    # Reference output
    b38.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Phan_Nhom_ABC": {
            "headers": ["Mã SKU", "Tên Hàng", "Số Lượng Tồn", "Tổng Giá Trị Vốn (VNĐ)", "Tỷ Trọng (%)", "Lũy Kế (%)", "Phân Nhóm ABC"],
            "rows": [
                ["MP01", "Kem dưỡng da ban đêm", 120, 54000000, "36.9%", "36.9%", "Nhóm A"],
                ["TP01", "Sữa tươi tiệt trùng 1L", 2000, 50000000, "34.1%", "71.0%", "Nhóm A"],
                ["TP02", "Dầu ăn thực vật 2L", 500, 42500000, "29.0%", "100.0%", "Nhóm B"]
            ]
        },
        "Hang_Can_Date": {
            "headers": ["Mã SKU", "Số Lô", "Tên Hàng", "Số Lượng", "Hạn Sử Dụng", "Số Ngày Còn Lại", "Cảnh Báo"],
            "rows": [
                ["TP01", "L2601", "Sữa tươi tiệt trùng 1L", 2000, "2026-12-10", 27, "CẬN DATE (<90 ngày) - Khuyến mãi xả kho gấp!"]
            ]
        },
        "Hang_Chet_Dead_Stock": {
            "headers": ["Mã SKU", "Tên Hàng", "Tổng Vốn Đọng", "Ngày Xuất Cuối", "Số Ngày Nằm Im", "Hành Động Khắc Phục"],
            "rows": [
                ["MP01", "Kem dưỡng da ban đêm", 54000000, "2026-03-10", 248, "DEAD STOCK (>180 ngày) - Thanh lý thu hồi vốn"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 39: Tinh toan nhu cau nguyen vat lieu (BOM Explosion)
    # =========================================================================
    b39 = WorkspaceBuilder(DEPT, "39-tinh-nhu-cau-nguyen-lieu-bom")
    b39.write_agents_md(
        role_title="Kỹ sư Định mức & Điều độ Sản xuất (Production Planner)",
        department_name="Phòng Kế hoạch Sản xuất",
        constitution_items=[
            "Nổ định mức nguyên vật liệu (BOM): Nhân số lượng thành phẩm cần sản xuất với định mức từng linh kiện.",
            "Tỷ lệ hao hụt định mức: Cộng thêm % hao hụt tiêu chuẩn trong quá trình gia công."
        ]
    )
    b39.write_rule(
        rule_file_name="quy_chuan_bom_explosion.md",
        description="Quy chuẩn tính toán nhu cầu nguyên vật liệu từ kế hoạch sản xuất",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Bóc Tách Định Mức BOM",
        guidelines=[
            "Tổng nhu cầu NVL = Số lượng thành phẩm * Định mức * (1 + % Hao hụt).",
            "Nhu cầu mua thêm = Max(0, Tổng nhu cầu NVL - Tồn kho hiện có).",
            "Xuất ra file `Nhu_cau_nguyen_vat_lieu_BOM.xlsx`."
        ]
    )
    b39.write_corporate_styling_rule()
    b39.write_security_hooks(["ke_hoach_sx.xlsx", "dinh_muc_bom.xlsx"])
    b39.write_skill(
        skill_name="tinh-nhu-cau-bom",
        description="Use this skill to explode bill of materials (BOM), account for scrap factors, and calculate material shortages.",
        skill_title="Quy trình bóc tách định mức nguyên vật liệu",
        steps=[
            {"name": "Đọc kế hoạch & định mức", "desc": "Nạp file `ke_hoach_sx.xlsx` và `dinh_muc_bom.xlsx`."},
            {"name": "Nổ định mức BOM", "desc": "Nhân hệ số linh kiện kèm tỷ lệ hao hụt và đối chiếu tồn kho."},
            {"name": "Xuất bảng mua hàng", "desc": "Lưu file `Nhu_cau_nguyen_vat_lieu_BOM.xlsx`."}
        ]
    )
    b39.write_prompt_demo(
        problem_pain="Khách đặt nhiều loại thành phẩm, mỗi món lại cấu thành từ hàng chục linh kiện có tỷ lệ hao hụt khác nhau, tính tay rất dễ đặt thiếu linh kiện.",
        interactive_hook="Nếu định mức may 1 áo là 1.4m vải với tỷ lệ hao hụt cắt vải 3%, thì để may 1.000 áo bạn cần chuẩn bị chính xác bao nhiêu mét vải?",
        prompt_cmd="Kết hợp file ke_hoach_sx.xlsx và dinh_muc_bom.xlsx. Hãy tính tổng nhu cầu từng loại nguyên vật liệu cần dùng (gồm cả hao hụt), đối chiếu với tồn kho để tính số lượng cần mua thêm, và cho biết tối đa sản xuất được bao nhiêu thành phẩm nếu không mua thêm. Xuất file Nhu_cau_nguyen_vat_lieu_BOM.xlsx.",
        prompt_pitfalls="Nếu không tính tỷ lệ hao hụt vào công thức, phân xưởng may khi vào chuyền sẽ bị hụt vải và không hoàn thành đủ số lượng áo theo đơn hàng.",
        expected_output="File `Nhu_cau_nguyen_vat_lieu_BOM.xlsx` liệt kê chi tiết từng linh kiện thiếu hụt và năng lực sản xuất tối đa.",
        wow_moment="Xử lý bài toán nổ định mức BOM (BOM Explosion) và nút thắt cổ chai sản xuất cực nhanh."
    )
    b39.create_excel("ke_hoach_sx.xlsx", {
        "KeHoach": {
            "headers": ["Mã Thành Phẩm", "Tên Thành Phẩm", "Số Lượng Cần SX"],
            "rows": [
                ["TP_POLO", "Áo Polo Nam Phối Bo", 1000],
                ["TP_TSHIRT", "Áo Thun Cổ Tròn", 2000]
            ]
        }
    })
    b39.create_excel("dinh_muc_bom.xlsx", {
        "DinhMuc": {
            "headers": ["Mã Thành Phẩm", "Mã Nguyên Liệu", "Tên Nguyên Liệu", "Định Mức / 1 SP", "Hao Hụt (%)", "Tồn Kho Hiện Có"],
            "rows": [
                ["TP_POLO", "NL_VAI_COTTON", "Vải Cotton Cá Sấu (Mét)", 1.4, 3, 1200],  # Cần 1000 * 1.4 * 1.03 = 1442m -> Thiếu 242m
                ["TP_POLO", "NL_CUC_AO", "Cúc Áo Nhựa (Chiếc)", 3.0, 1, 5000],          # Cần 3030c -> Đủ
                ["TP_TSHIRT", "NL_VAI_THUN", "Vải Thun Cotton 4 Chiều (Mét)", 1.2, 2, 2000] # Cần 2448m -> Thiếu 448m
            ]
        }
    })
    # Reference output
    b39.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Bang_Nhu_Cau_BOM": {
            "headers": ["Mã NVL", "Tên Nguyên Vật Liệu", "Thành Phẩm", "Tổng Nhu Cầu Gồm Hao Hụt", "Tồn Kho Hiện Có", "Lượng Thiếu Hụt", "Đề Xuất Mua Thêm"],
            "rows": [
                ["NL_VAI_COTTON", "Vải Cotton Cá Sấu (Mét)", "Áo Polo Nam", 1442, 1200, 242, "Mua thêm 250m"],
                ["NL_CUC_AO", "Cúc Áo Nhựa (Chiếc)", "Áo Polo Nam", 3030, 5000, 0, "Đủ tồn kho sản xuất"],
                ["NL_VAI_THUN", "Vải Thun Cotton 4 Chiều (Mét)", "Áo Thun Cổ Tròn", 2448, 2000, 448, "Mua thêm 450m"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 40: Doi soat bang ke cuoc phi van chuyen va tien COD
    # =========================================================================
    b40 = WorkspaceBuilder(DEPT, "40-doi-soat-cuoc-phi-cod")
    b40.write_agents_md(
        role_title="Kế toán Vận chuyển & Điều phối Giao nhận (Logistics Auditor)",
        department_name="Phòng Kho vận & Giao nhận",
        constitution_items=[
            "Chống lạm thu cước: Kiểm tra các đơn bị hãng vận chuyển cân vọt trọng lượng so với trọng lượng chuẩn của hàng.",
            "Kiểm soát tiền thu hộ (COD): Đối soát đơn đã giao thành công nhưng chưa nhận được tiền hoàn trả COD."
        ]
    )
    b40.write_rule(
        rule_file_name="quy_chuan_doi_soat_cod.md",
        description="Quy chuẩn đối soát cước vận chuyển và tiền thu hộ COD",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Đối Soát Bảng Kê Vận Chuyển & COD",
        guidelines=[
            "Phát hiện đơn chênh lệch trọng lượng > 200g so với trọng lượng chuẩn.",
            "Lọc các đơn hàng trạng thái 'Đã giao' nhưng cột 'Tiền COD đã trả' = 0.",
            "Xuất ra file `Bien_ban_doi_soat_cuoc_van_chuyen.xlsx`."
        ]
    )
    b40.write_corporate_styling_rule()
    b40.write_security_hooks(["bang_ke_van_chuyen.xlsx"])
    b40.write_skill(
        skill_name="doi-soat-cuoc-phi-cod",
        description="Use this skill to audit 3PL carrier freight bills, weight discrepancies, and pending COD remissions.",
        skill_title="Quy trình đối soát cước vận chuyển và COD",
        steps=[
            {"name": "Đọc bảng kê hãng vận chuyển", "desc": "Nạp file `bang_ke_van_chuyen.xlsx`."},
            {"name": "So sánh trọng lượng & cước phí", "desc": "Kiểm tra chênh lệch cân nặng và trạng thái trả tiền COD."},
            {"name": "Lập biên bản chênh lệch", "desc": "Lưu file `Bien_ban_doi_soat_cuoc_van_chuyen.xlsx`."}
        ]
    )
    b40.write_prompt_demo(
        problem_pain="Hàng tháng nhận bảng kê 5.000 vận đơn từ ViettelPost/GiaoHangNhanh, shop hay bị tính sai cân nặng hoặc sót tiền COD thu hộ.",
        interactive_hook="Một chiếc áo sơ mi đóng hộp nặng 300g nhưng bưu cục cân vọt lên 950g và nhảy bậc cước, shop của bạn mất bao nhiêu tiền cước oan uổng?",
        prompt_cmd="Đối soát bảng kê bang_ke_van_chuyen.xlsx: Hãy kiểm tra đơn nào bị hãng cân vọt trọng lượng so với trọng lượng chuẩn nội bộ, và đơn nào trạng thái 'Đã giao' nhưng chưa nhận được tiền COD. Xuất danh sách chênh lệch ra file Bien_ban_doi_soat_cuoc_van_chuyen.xlsx để làm việc với bưu cục.",
        prompt_pitfalls="Nếu không quy định ngưỡng sai số cho phép của bao bì (Tolerance threshold, ví dụ 50g cho túi niêm phong), AI sẽ bắt bớ cả những đơn chỉ lệch vài gram bình thường.",
        expected_output="File `Bien_ban_doi_soat_cuoc_van_chuyen.xlsx` chỉ rõ từng mã vận đơn bị tính lố cước và sót tiền COD.",
        wow_moment="Giúp doanh nghiệp thu hồi lại ngay tiền cước bị tính lố và tiền COD bị sót mỗi tháng."
    )
    b40.create_excel("bang_ke_van_chuyen.xlsx", {
        "VanDon": {
            "headers": ["Mã Vận Đơn", "Khách Hàng", "Trọng Lượng Chuẩn (Gram)", "Hãng Vận Chuyển Cân (Gram)", "Cước Phí Thu (VNĐ)", "Trạng Thái Giao", "Tiền COD Đã Trả (VNĐ)"],
            "rows": [
                ["VTP001", "Nguyễn Văn Hùng", 500, 500, 30000, "Đã giao thành công", 450000],
                ["VTP002", "Trần Mai Anh", 300, 950, 48000, "Đã giao thành công", 320000], # Cân vọt 300g lên 950g!
                ["VTP003", "Lê Văn Thắng", 400, 420, 30000, "Đã giao thành công", 0]        # Đã giao nhưng chưa trả tiền COD!
            ]
        }
    })
    # Reference output
    b40.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Bien_Ban_Loi_Cuoc": {
            "headers": ["Mã Vận Đơn", "Khách Hàng", "Cân Nặng Chuẩn", "Bưu Cục Cân", "Chênh Lệch", "Cước Đã Trừ", "Cước Chuẩn Phải Thu", "Tiền Cước Đòi Lại", "Trạng Thái COD"],
            "rows": [
                ["VTP002", "Trần Mai Anh", 300, 950, "+650g", 48000, 26000, 22000, "Đã trả đủ tiền COD"],
                ["VTP003", "Lê Văn Thắng", 400, 420, "+20g (Chuẩn)", 30000, 30000, 0, "THIẾU TIỀN COD (Chưa chuyển hoàn 0đ)"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 41: Doi chieu Bo chung tu Xuat nhap khau (Invoice - Packing List - B/L)
    # =========================================================================
    b41 = WorkspaceBuilder(DEPT, "41-doi-chieu-chung-tu-xnk")
    b41.write_agents_md(
        role_title="Chuyên viên Xuất Nhập Khẩu & Chứng từ Hải quan",
        department_name="Phòng Xuất Nhập Khẩu",
        constitution_items=[
            "Chính xác tuyệt đối giữa các chứng từ: Số lượng kiện (Packages), Trọng lượng tịnh (Net Weight), Trọng lượng cả bì (Gross Weight), Thể tích (CBM).",
            "Cảnh báo sai lệch (Discrepancy): Bất kỳ sự không đồng nhất nào giữa Invoice, Packing List và Vận đơn (B/L) đều phải được báo cáo ngay."
        ]
    )
    b41.write_rule(
        rule_file_name="quy_chuan_chung_tu_xnk.md",
        description="Quy chuẩn đối chiếu chéo bộ chứng từ hải quan xuất nhập khẩu",
        globs="*.xlsx, *.txt, *.pdf",
        rule_title="Quy Chuẩn Kiểm Tra Chéo Chứng Từ XNK",
        guidelines=[
            "Khớp mã HS Code, Tên hàng tiếng Anh, Số lượng kiện giữa Invoice và Packing List.",
            "Khớp Gross Weight và CBM giữa Packing List và Bill of Lading.",
            "Xuất ra file `Bien_ban_doi_chieu_chung_tu_XNK.xlsx`."
        ]
    )
    b41.write_corporate_styling_rule()
    b41.write_security_hooks(["Invoice.xlsx", "PackingList.xlsx", "BillOfLading.txt"])
    b41.write_skill(
        skill_name="doi-chieu-chung-tu-xnk",
        description="Use this skill to cross-examine Commercial Invoices, Packing Lists, and Bills of Lading for customs compliance.",
        skill_title="Quy trình đối chiếu bộ chứng từ xuất nhập khẩu",
        steps=[
            {"name": "Đọc 3 tài liệu chứng từ", "desc": "Nạp file `Invoice.xlsx`, `PackingList.xlsx` và `BillOfLading.txt`."},
            {"name": "Kiểm tra chéo các chỉ tiêu", "desc": "Đối chiếu trọng lượng, số khối, số kiện và tên người nhận hàng."},
            {"name": "Lập biên bản soát xét", "desc": "Lưu file `Bien_ban_doi_chieu_chung_tu_XNK.xlsx`."}
        ]
    )
    b41.write_prompt_demo(
        problem_pain="Trước khi truyền tờ khai hải quan phải dò từng con số Gross Weight, Net Weight, CBM giữa Invoice, Packing List và B/L. Lệch 1 số là kẹt hàng ở cảng.",
        interactive_hook="Nếu Gross Weight trên Packing List ghi 1.400 KGS nhưng trên Vận đơn (Bill of Lading) lại in 1.450 KGS, hậu quả pháp lý gì có thể xảy ra khi thông quan hải quan?",
        prompt_cmd="Đọc và đối chiếu chéo 3 chứng từ: Invoice.xlsx, PackingList.xlsx và BillOfLading.txt. Kiểm tra xem Tên hàng, Số lượng kiện, Trọng lượng Gross Weight, Net Weight, Số khối CBM có khớp nhau 100% không. Liệt kê bất kỳ điểm sai lệch nào tìm thấy vào file Bien_ban_doi_chieu_chung_tu_XNK.xlsx.",
        prompt_pitfalls="Nếu bỏ qua việc kiểm tra đơn vị tính trọng lượng (ví dụ LBS sang KGS), việc sai lệch hệ đo lường sẽ dẫn đến mức phạt hành chính rất nặng từ cơ quan Hải quan.",
        expected_output="File `Bien_ban_doi_chieu_chung_tu_XNK.xlsx` chỉ ra các điểm khớp và cảnh báo sai lệch số liệu giữa các chứng từ.",
        wow_moment="Đối chiếu chéo giữa Excel và PDF/Text chuẩn xác từng con số thập phân, cứu dân XNK khỏi những lỗi sai chứng từ đắt giá."
    )
    b41.create_excel("Invoice.xlsx", {
        "Invoice": {
            "headers": ["Item No", "Description", "HS Code", "Quantity (PCS)", "Unit Price (USD)", "Total Amount (USD)"],
            "rows": [
                [1, "Men Knitted Polo Shirts 100% Cotton", "6105.10.00", 5000, 6.50, 32500.00]
            ]
        }
    })
    b41.create_excel("PackingList.xlsx", {
        "PackingList": {
            "headers": ["Item No", "Description", "Packages (CTNS)", "Net Weight (KGS)", "Gross Weight (KGS)", "Measurement (CBM)"],
            "rows": [
                [1, "Men Knitted Polo Shirts 100% Cotton", 100, 1250.00, 1400.00, 24.50]
            ]
        }
    })
    b41.write_text_file("BillOfLading.txt", """
OCEAN BILL OF LADING (DRAFT)
B/L No: ONEYHAN268899
Shipper: VIETNAM TEXTILE APPAREL CORP
Consignee: PACIFIC TRADING LLC, CALIFORNIA, USA
Port of Loading: HAIPHONG, VIETNAM | Port of Discharge: LOS ANGELES, USA
Description of Goods: 100 CARTONS OF MEN KNITTED POLO SHIRTS
Gross Weight: 1,450.00 KGS  <-- Lệch 50kg so với Packing List (1400 KGS)!
Measurement: 24.50 CBM
    """)
    # Reference output
    b41.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Doi_Chieu_Chung_Tu": {
            "headers": ["Chỉ Tiêu Soát Xét", "Commercial Invoice", "Packing List", "Bill of Lading (B/L)", "Trạng Thái Khớp", "Mức Độ Rủi Ro & Đề Xuất"],
            "rows": [
                ["Mô tả hàng hóa", "Men Knitted Polo Shirts", "Men Knitted Polo Shirts", "100 CTNS OF MEN KNITTED POLO SHIRTS", "Khớp 100%", "Hợp lệ"],
                ["Số lượng kiện", "5,000 PCS", "100 CTNS", "100 CARTONS", "Khớp 100%", "Hợp lệ"],
                ["Trọng lượng Gross Weight", "N/A", "1,400.00 KGS", "1,450.00 KGS", "LỆCH 50 KGS!", "RẤT CAO: Yêu cầu hãng tàu đính chính B/L trước khi truyền hải quan"],
                ["Thể tích hàng (CBM)", "N/A", "24.50 CBM", "24.50 CBM", "Khớp 100%", "Hợp lệ"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 42: Kiem ke kho thuc te so voi so sach va phat hien lech cheo
    # =========================================================================
    b42 = WorkspaceBuilder(DEPT, "42-kiem-ke-kho-lech-thuc-te")
    b42.write_agents_md(
        role_title="Trưởng nhóm Kiểm kê & Kế toán Kho",
        department_name="Phòng Quản lý Kho",
        constitution_items=[
            "Tổng hợp phiếu đếm tay: Cộng dồn số lượng thực đếm của cùng một mặt hàng nằm ở nhiều vị trí kệ khác nhau.",
            "Phát hiện lỗi xuất nhầm chéo mã: Nhận diện trường hợp một mặt hàng thừa X cái và mặt hàng tương đồng bị thiếu đúng X cái."
        ]
    )
    b42.write_rule(
        rule_file_name="quy_chuan_kiem_ke_kho.md",
        description="Quy chuẩn xử lý chênh lệch kiểm kê kho thực tế và sổ sách",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Biên Bản Xử Lý Chênh Lệch Kiểm Kê",
        guidelines=[
            "Chênh lệch = Thực đếm - Tồn sổ sách ERP.",
            "Phát hiện nghi vấn nhầm chéo: Mã hàng thừa và mã hàng thiếu cùng số lượng và cùng nhóm hàng.",
            "Xuất ra file `Bien_ban_kiem_ke_xu_ly_chenh_lech.xlsx`."
        ]
    )
    b42.write_corporate_styling_rule()
    b42.write_security_hooks(["kiem_ke_ke_1.xlsx", "ton_erp.xlsx"])
    b42.write_skill(
        skill_name="kiem-ke-lech-thuc-te",
        description="Use this skill to reconcile physical inventory counts against ERP balances and detect cross-SKU mispicks.",
        skill_title="Quy trình xử lý chênh lệch kiểm kê kho",
        steps=[
            {"name": "Đọc kết quả đếm & sổ sách", "desc": "Nạp file `kiem_ke_ke_1.xlsx` và `ton_erp.xlsx`."},
            {"name": "Cộng dồn & Đối chiếu", "desc": "Tính số lượng thừa thiếu từng mã hàng."},
            {"name": "Phát hiện nhầm chéo", "desc": "Phân tích giả thiết nhầm lẫn mã hàng và lưu file `Bien_ban_kiem_ke_xu_ly_chenh_lech.xlsx`."}
        ]
    )
    b42.write_prompt_demo(
        problem_pain="Kiểm kê xong có nhiều phiếu đếm tay rời rạc, cộng gộp lại so với phần mềm ERP rất dễ rối, không tìm ra nguyên nhân lệch.",
        interactive_hook="Nếu kiểm kê thấy Áo Polo size M thừa 5 cái còn Áo Polo size L thiếu đúng 5 cái, nguyên nhân phổ biến nhất trong vận hành kho là gì?",
        prompt_cmd="Đối chiếu kết quả đếm kho kiem_ke_ke_1.xlsx với tồn sổ sách ton_erp.xlsx. Tính số lượng Thừa/Thiếu cho từng mã hàng, phân tích nguyên nhân nghi ngờ (đặc biệt là lỗi xuất nhầm chéo size/mã giữa 2 sản phẩm tương đồng). Xuất file Bien_ban_kiem_ke_xu_ly_chenh_lech.xlsx.",
        prompt_pitfalls="Nếu gom nhóm kiểm kê mà không gộp chung các dòng cùng mã hàng nhưng nằm ở các vị trí kệ kho khác nhau (Multi-bin storage), số lượng thực đếm sẽ bị thiếu hụt giả tạo.",
        expected_output="File `Bien_ban_kiem_ke_xu_ly_chenh_lech.xlsx` chỉ rõ số lượng chênh lệch và phát hiện chính xác ca xuất nhầm chéo size.",
        wow_moment="Điểm thông minh vượt trội: AI phát hiện được lỗi xuất nhầm chéo mã (Áo size M thừa 5 cái, Áo size L thiếu đúng 5 cái)."
    )
    b42.create_excel("kiem_ke_ke_1.xlsx", {
        "ThucDem": {
            "headers": ["Vị Trí Kệ", "Mã Hàng", "Tên Hàng", "Số Lượng Thực Đếm"],
            "rows": [
                ["Kệ A1", "AO_POLO_DEN_M", "Áo Polo Đen Size M", 45], # Thực tế thừa 5
                ["Kệ A2", "AO_POLO_DEN_L", "Áo Polo Đen Size L", 25], # Thực tế thiếu 5 -> Nhầm chéo size!
                ["Kệ B1", "QUAN_JEAN_30", "Quần Jean Size 30", 60]
            ]
        }
    })
    b42.create_excel("ton_erp.xlsx", {
        "SoSachERP": {
            "headers": ["Mã Hàng", "Tên Hàng", "Tồn Sổ Sách ERP"],
            "rows": [
                ["AO_POLO_DEN_M", "Áo Polo Đen Size M", 40],
                ["AO_POLO_DEN_L", "Áo Polo Đen Size L", 30],
                ["QUAN_JEAN_30", "Quần Jean Size 30", 60]
            ]
        }
    })
    # Reference output
    b42.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Xu_Ly_Chenh_Lech": {
            "headers": ["Mã Hàng", "Tên Mặt Hàng", "Tồn Sổ Sách ERP", "Thực Tế Đếm", "Chênh Lệch", "Phân Tích Nguyên Nhân", "Đề Xuất Xử Lý"],
            "rows": [
                ["AO_POLO_DEN_M", "Áo Polo Đen Size M", 40, 45, "+5 (Thừa)", "Xuất nhầm chéo mã với size L trong đơn bán hàng", "Lập phiếu điều chỉnh bù trừ nội bộ"],
                ["AO_POLO_DEN_L", "Áo Polo Đen Size L", 30, 25, "-5 (Thiếu)", "Bị dán nhầm tem nhãn size M lúc đóng gói xuất kho", "Bù trừ cân bằng kho"],
                ["QUAN_JEAN_30", "Quần Jean Size 30", 60, 60, "0 (Khớp 100%)", "Số liệu hoàn hảo", "Không cần xử lý"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 43: Toi uu hoa dong hang vao thung / Xe tai giao hang
    # =========================================================================
    b43 = WorkspaceBuilder(DEPT, "43-chia-tai-trong-xe-container")
    b43.write_agents_md(
        role_title="Điều phối Giao nhận & Tải trọng Vận chuyển (Fleet Dispatcher)",
        department_name="Phòng Điều vận & Kho bãi",
        constitution_items=[
            "Ràng buộc kép tải trọng: Mỗi chuyến xe tải 2.5 tấn chỉ chở tối đa 2.000 kg và tối đa 12 CBM.",
            "Tối ưu gom tuyến: Gom các đơn hàng thuộc cùng một Quận/Huyện vào cùng một chuyến xe."
        ]
    )
    b43.write_rule(
        rule_file_name="quy_chuan_tai_trong_xe.md",
        description="Quy chuẩn gom tuyến và phân bổ tải trọng xe giao hàng",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Phân Bổ Tải Trọng Đơn Giao Hàng",
        guidelines=[
            "Không vượt quá 2.000 kg hoặc 12 CBM trên mỗi xe.",
            "Lập danh sách đơn hàng cho từng chuyến xe (Delivery Manifest).",
            "Xuất ra file `Ke_hoach_dieu_xe_giao_hang.xlsx`."
        ]
    )
    b43.write_corporate_styling_rule()
    b43.write_security_hooks(["danh_sach_don_giao.xlsx"])
    b43.write_skill(
        skill_name="chia-tai-trong-xe",
        description="Use this skill to optimize multi-order delivery vehicle load assignments under cubic volume and weight constraints.",
        skill_title="Quy trình phân bổ tải trọng và gom tuyến giao hàng",
        steps=[
            {"name": "Đọc danh sách đơn giao", "desc": "Nạp file `danh_sach_don_giao.xlsx`."},
            {"name": "Thuật toán gom tuyến & tải trọng", "desc": "Gom cụm quận/huyện và kiểm tra ngưỡng tải trọng, thể tích."},
            {"name": "Xuất bảng điều xe", "desc": "Lưu file `Ke_hoach_dieu_xe_giao_hang.xlsx`."}
        ]
    )
    b43.write_prompt_demo(
        problem_pain="Có hàng chục đơn hàng giao trong ngày, điều vận phải tính nhẩm thể tích và cân nặng để biết cần thuê bao nhiêu xe tải và xếp đơn nào đi với nhau.",
        interactive_hook="Nếu một đơn hàng thể tích chỉ 3 CBM nhưng nặng tới 1.800 kg, đơn hàng này đang chiếm dụng tải trọng theo Khối lượng (Weight) hay Thể tích (Volume)?",
        prompt_cmd="Dựa vào danh_sach_don_giao.xlsx, hãy gom các đơn hàng theo cụm Quận gần nhau để chia vào các chuyến xe tải (mỗi xe tối đa 2.000 kg và 12 CBM). Tối ưu sao cho số chuyến xe ít nhất và lập bảng danh sách giao hàng cho từng xe vào file Ke_hoach_dieu_xe_giao_hang.xlsx.",
        prompt_pitfalls="Nếu chỉ tối ưu về mặt cân nặng mà quên kiểm tra thể tích CBM, hàng hóa cồng kềnh sẽ bị tràn thùng xe dù cân nặng vẫn chưa chạm ngưỡng tải trọng.",
        expected_output="File `Ke_hoach_dieu_xe_giao_hang.xlsx` có lịch phân chuyến cho từng xe tải đảm bảo không xe nào bị quá tải hay quá khổ.",
        wow_moment="Tự động gom tuyến và giải bài toán tải trọng vận chuyển xe tải chỉ trong tích tắc."
    )
    b43.create_excel("danh_sach_don_giao.xlsx", {
        "DonGiao": {
            "headers": ["Mã Đơn", "Quận Giao Hàng", "Số Thùng", "Thể Tích (CBM)", "Trọng Lượng (KG)"],
            "rows": [
                ["DG01", "Cầu Giấy", 20, 2.5, 450],
                ["DG02", "Cầu Giấy", 35, 4.0, 750],
                ["DG03", "Nam Từ Liêm", 40, 4.5, 800], # Tuyến 1: Cầu Giấy + Nam Từ Liêm = 11 CBM, 2000 KG -> ĐỦ 1 XE!
                ["DG04", "Hoàn Kiếm", 30, 3.2, 600],
                ["DG05", "Hai Bà Trưng", 50, 5.5, 1100] # Tuyến 2: Hoàn Kiếm + Hai Bà Trưng = 8.7 CBM, 1700 KG -> ĐỦ 1 XE!
            ]
        }
    })
    # Reference output
    b43.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Dieu_Xe_Giao_Hang": {
            "headers": ["Chuyến Xe", "Biển Số Dự Kiến", "Tuyến Đường Phục Vụ", "Các Mã Đơn Được Xếp", "Tổng Thể Tích (CBM)", "Tổng Cân Nặng (KG)", "Tỷ Lệ Lấp Đầy Xe"],
            "rows": [
                ["Chuyến 01", "29C-881.23", "Cầu Giấy -> Nam Từ Liêm", "DG01, DG02, DG03", "11.0 / 12.0 CBM", "2,000 / 2,000 KG", "100% Cân nặng (Tối ưu tuyệt đối)"],
                ["Chuyến 02", "29C-992.45", "Hoàn Kiếm -> Hai Bà Trưng", "DG04, DG05", "8.7 / 12.0 CBM", "1,700 / 2,000 KG", "85% Cân nặng (An toàn)"]
            ]
        }
    })

    print(f"--> Successfully generated {DEPT} (8 exercises).")

if __name__ == "__main__":
    generate()
