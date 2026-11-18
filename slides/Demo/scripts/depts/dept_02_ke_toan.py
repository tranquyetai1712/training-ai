"""
Department 02: Ke toan - Tai chinh (9 Exercises: 10 -> 18)
Updated with Security Hooks, Corporate Styling Rules, Reference Output, and 6-part PROMPT_DEMO.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generator_core import WorkspaceBuilder

DEPT = "02-ke-toan"

def generate():
    print(f"--> Generating {DEPT} with enhanced controls...")

    # =========================================================================
    # EXERCISE 10: Doi soat sao ke ngan hang voi so quy noi bo
    # =========================================================================
    b10 = WorkspaceBuilder(DEPT, "10-doi-soat-sao-ke-so-quy")
    b10.write_agents_md(
        role_title="Kế toán Thanh toán & Kiểm soát Dòng tiền",
        department_name="Phòng Kế toán - Tài chính",
        constitution_items=[
            "Chính xác tuyệt đối về số tiền: Sai lệch dù chỉ 1 đồng cũng phải được phân loại vào danh sách kiểm tra riêng.",
            "Nhận diện ngữ nghĩa mờ (Fuzzy Matching): Khớp mã hóa đơn, tên khách hàng trong chuỗi nội dung chuyển khoản không dấu hoặc viết tắt.",
            "Phát hiện tổ hợp gộp tiền: Nhận diện trường hợp khách hàng chuyển khoản 1 lần để thanh toán cho 2-3 hóa đơn."
        ]
    )
    b10.write_rule(
        rule_file_name="quy_chuan_doi_soat_ngan_hang.md",
        description="Quy chuẩn đối soát giao dịch ngân hàng với sổ kế toán nội bộ",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Đối Soát Sao Kê Ngân Hàng",
        guidelines=[
            "Khớp 1-1: Cùng số tiền, ngày giao dịch chênh lệch tối đa 1 ngày làm việc, nội dung chứa Mã đơn hoặc Tên khách.",
            "Khớp Gộp: 1 giao dịch ngân hàng bằng tổng số tiền của 2-3 hóa đơn cùng khách hàng.",
            "Xuất file kết quả `Ket_qua_doi_soat_T10.xlsx` gồm 3 sheet: 'Da_Khop_1_1', 'Khop_Gop_Don', 'Chua_Khop_Can_Lam_Ro'."
        ]
    )
    b10.write_corporate_styling_rule()
    b10.write_security_hooks(["sao_ke_vcb.xlsx", "so_thu_chi.xlsx"])
    b10.write_skill(
        skill_name="doi-soat-sao-ke",
        description="Use this skill to reconcile bank statement transaction rows against internal accounting ledgers.",
        skill_title="Quy trình đối soát sao kê ngân hàng và sổ quỹ",
        steps=[
            {"name": "Đọc 2 nguồn dữ liệu", "desc": "Nạp file `sao_ke_vcb.xlsx` và `so_thu_chi.xlsx`."},
            {"name": "Đối soát khớp 1-1", "desc": "So sánh mã đơn, số tiền và ngày giao dịch."},
            {"name": "Tìm kiếm tổ hợp gộp", "desc": "Tìm các lệnh chuyển khoản bằng tổng tiền của nhiều hóa đơn chưa thanh toán."},
            {"name": "Xuất báo cáo đối soát", "desc": "Phân loại 3 nhóm kết quả vào file `Ket_qua_doi_soat_T10.xlsx`."}
        ]
    )
    b10.write_prompt_demo(
        problem_pain="Dò sao kê ngân hàng với sổ thu chi cực kỳ mất thời gian vì nội dung chuyển khoản viết tắt, dính chữ, hoặc khách trả gộp 2 hóa đơn một lúc.",
        interactive_hook="Nếu khách hàng chuyển khoản 28 triệu với nội dung vỏn vẹn 'Hoang Gia ck', làm thế nào bạn biết món tiền này trả cho hóa đơn nào nếu công ty đang có 2 hóa đơn 18tr và 10tr?",
        prompt_cmd="Đối soát 2 file sao_ke_vcb.xlsx và so_thu_chi.xlsx. Hãy khớp các giao dịch dựa trên Số tiền, Ngày giao dịch (cho phép lệch tối đa 1 ngày) và nhận diện mờ Mã hóa đơn/Tên khách trong nội dung CK. Tìm ra cả các trường hợp 1 lệnh chuyển khoản bằng tổng của 2 hóa đơn cùng khách hàng. Xuất file Ket_qua_doi_soat_T10.xlsx gồm 3 sheet: Đã khớp 1-1, Khớp gộp đơn, và Chưa khớp.",
        prompt_pitfalls="Nếu không dặn AI tìm kiếm tổ hợp gộp tiền (Subset Sum), AI sẽ báo khoản 28 triệu là 'Không tìm thấy hóa đơn tương ứng'.",
        expected_output="File `Ket_qua_doi_soat_T10.xlsx` bóc tách chuẩn xác các khoản đã khớp 1-1, chỉ ra trường hợp trả gộp đơn và khoanh vùng khoản tiền lạ.",
        wow_moment="Khả năng Fuzzy Matching kết hợp tìm tổ hợp tiền gộp đơn giải phóng kế toán khỏi hàng nghìn dòng dò mắt thủ công."
    )
    b10.create_excel("sao_ke_vcb.xlsx", {
        "VCB_Statement": {
            "headers": ["Ngày GD", "Số GD", "Số Tiền Ghi Có", "Nội Dung Chuyển Khoản"],
            "rows": [
                ["2026-10-05", "FT2627801", 15000000, "CTY AN PHAT THANH TOAN HD 1089"],
                ["2026-10-06", "FT2627802", 28000000, "CONG TY HOANG GIA CK TIEN HANG"], # Gộp HD 1090 (18tr) + HD 1091 (10tr)
                ["2026-10-07", "FT2627803", 5200000, "NGUYEN VAN TAM TRA TIEN HD1092"],
                ["2026-10-08", "FT2627804", 9900000, "TRAN THI THUY CK"] # Khoản lạ chưa rõ mã đơn
            ]
        }
    })
    b10.create_excel("so_thu_chi.xlsx", {
        "SoNoiBo": {
            "headers": ["Mã HĐ", "Khách Hàng", "Ngày Xuất HĐ", "Số Tiền Phải Thu", "Trạng Thái"],
            "rows": [
                ["HD-1089", "Công ty TNHH An Phát", "2026-10-05", 15000000, "Chờ thanh toán"],
                ["HD-1090", "Công ty CP Hoàng Gia", "2026-10-04", 18000000, "Chờ thanh toán"],
                ["HD-1091", "Công ty CP Hoàng Gia", "2026-10-05", 10000000, "Chờ thanh toán"],
                ["HD-1092", "Nguyễn Văn Tám", "2026-10-07", 5200000, "Chờ thanh toán"],
                ["HD-1093", "Công ty Dược Minh Anh", "2026-10-08", 22000000, "Chờ thanh toán"]
            ]
        }
    })
    # Reference output
    b10.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Da_Khop_1_1": {
            "headers": ["Số GD", "Mã HĐ", "Khách Hàng", "Số Tiền Khớp", "Ngày GD", "Ghi Chú"],
            "rows": [
                ["FT2627801", "HD-1089", "Công ty TNHH An Phát", 15000000, "2026-10-05", "Khớp chuẩn xác mã HĐ & số tiền"],
                ["FT2627803", "HD-1092", "Nguyễn Văn Tám", 5200000, "2026-10-07", "Khớp chuẩn xác mã HĐ & số tiền"]
            ]
        },
        "Khop_Gop_Don": {
            "headers": ["Số GD", "Khách Hàng", "Số Tiền GD", "Các Mã HĐ Được Gộp", "Tổng Tiền HĐ", "Trạng Thái"],
            "rows": [
                ["FT2627802", "Công ty CP Hoàng Gia", 28000000, "HD-1090 (18tr) + HD-1091 (10tr)", 28000000, "Khớp gộp 2 hóa đơn"]
            ]
        },
        "Chua_Khop_Can_Lam_Ro": {
            "headers": ["Loại", "Mã GD / Mã HĐ", "Đối Tượng", "Số Tiền", "Nội Dung / Diễn Giải", "Hành Động Đề Xuất"],
            "rows": [
                ["Khoản thu chưa rõ", "FT2627804", "TRAN THI THUY", 9900000, "TRAN THI THUY CK", "Liên hệ sales xác nhận khách hàng"],
                ["Hóa đơn chưa thu tiền", "HD-1093", "Công ty Dược Minh Anh", 22000000, "Chưa có giao dịch thanh toán", "Theo dõi công nợ trong hạn"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 11: Trich xuat hang loat hoa don dien tu vao bang ke
    # =========================================================================
    b11 = WorkspaceBuilder(DEPT, "11-trich-xuat-hoa-don-dien-tu")
    b11.write_agents_md(
        role_title="Kế toán Thuế & Hóa đơn",
        department_name="Phòng Kế toán - Tài chính",
        constitution_items=[
            "Kiểm tra tính hợp lệ thuế: Tiền trước thuế + Tiền thuế GTGT = Tổng thanh toán.",
            "Tách rõ ràng thuế suất: Phân loại chính xác hóa đơn thuế suất 8%, 10% hoặc không chịu thuế.",
            "Đồng bộ Mã số thuế: MST người bán và người mua phải được lưu dưới dạng Text chuẩn."
        ]
    )
    b11.write_rule(
        rule_file_name="quy_chuan_hoa_don_gtgt.md",
        description="Quy chuẩn bóc tách hóa đơn GTGT vào bảng kê mua vào",
        globs="*.txt, *.xml, *.pdf",
        rule_title="Quy Chuẩn Bảng Kê Hóa Đơn Giá Trị Gia Tăng Mua Vào",
        guidelines=[
            "Trích xuất đủ 9 trường: Ký hiệu mẫu, Số HĐ, Ngày lập, Tên NCC, MST, Mặt hàng, Tiền chưa thuế, Thuế GTGT, Tổng tiền.",
            "Kiểm tra chéo: Nếu Tiền chưa thuế + Thuế GTGT lệch Tổng tiền > 10 đồng, đánh dấu 'Cần kiểm tra lại'.",
            "Xuất ra file `Bang_ke_mua_vao_T10.xlsx`."
        ]
    )
    b11.write_corporate_styling_rule()
    b11.write_security_hooks(["Hoa_Don/HD_001.txt", "Hoa_Don/HD_002.txt"])
    b11.write_skill(
        skill_name="trich-xuat-hoa-don",
        description="Use this skill to extract VAT invoices from text/XML files into a standardized tax declaration workbook.",
        skill_title="Quy trình bóc tách hóa đơn mua vào",
        steps=[
            {"name": "Đọc thư mục hóa đơn", "desc": "Quét toàn bộ hóa đơn trong thư mục `Hoa_Don/`."},
            {"name": "Trích xuất & Kiểm toán số học", "desc": "Bóc tách MST, số tiền và kiểm tra tính đúng đắn của thuế GTGT."},
            {"name": "Xuất bảng kê", "desc": "Tạo file `Bang_ke_mua_vao_T10.xlsx` theo chuẩn kê khai thuế."}
        ]
    )
    b11.write_prompt_demo(
        problem_pain="Kế toán phải mở từng hóa đơn PDF/XML gõ lại tay Số HĐ, Ngày, MST, Tiền hàng, Tiền thuế vào bảng kê rất mất thời gian.",
        interactive_hook="Bao nhiêu bạn ở đây từng bị cơ quan thuế phạt vì kê khai sai lệch 1 chữ số trong Mã Số Thuế do gõ tay từ hóa đơn giấy/ảnh?",
        prompt_cmd="Quét tất cả hóa đơn trong thư mục Hoa_Don. Trích xuất thông tin từng hóa đơn gồm: Số HĐ, Ngày lập, Tên đơn vị bán, Mã số thuế, Mặt hàng, Tiền chưa thuế, Thuế suất GTGT, Tiền thuế, Tổng thanh toán. Kiểm tra xem Tiền chưa thuế + Tiền thuế có khớp Tổng thanh toán không. Xuất ra file Bang_ke_mua_vao_T10.xlsx.",
        prompt_pitfalls="Nếu hóa đơn áp dụng thuế suất giảm (8%) mà không hướng dẫn AI kiểm tra trường thuế suất riêng biệt, AI có thể mặc định tính thuế 10%.",
        expected_output="File `Bang_ke_mua_vao_T10.xlsx` chuẩn kê khai thuế, tự động đối chiếu cộng trừ và cảnh báo nếu hóa đơn bị lệch số học.",
        wow_moment="Tự động bóc tách hóa đơn và tích hợp luôn bước kiểm toán chéo số học (Cross-audit validation)."
    )
    b11.write_text_file("Hoa_Don/HD_001.txt", """
HÓA ĐƠN GIÁ TRỊ GIA TĂNG
Ký hiệu: 1C26TAA | Số: 0001234
Ngày lập: 15/10/2026
Đơn vị bán hàng: CÔNG TY TNHH VĂN PHÒNG PHẨM TIẾN PHÁT
Mã số thuế: 0102345678
Mặt hàng: Giấy in A4 Double A, Bút bi Thiên Long, File còng Kingjim
Cộng tiền hàng: 8.500.000 VNĐ
Thuế suất GTGT: 10% | Tiền thuế GTGT: 850.000 VNĐ
Tổng cộng tiền thanh toán: 9.350.000 VNĐ
    """)
    b11.write_text_file("Hoa_Don/HD_002.txt", """
HÓA ĐƠN ĐIỆN TỬ
Ký hiệu: 2C26TBB | Số: 0005678
Ngày lập: 20/10/2026
Đơn vị bán hàng: CÔNG TY CỔ PHẦN CÔNG NGHỆ THẾ KỶ MỚI
Mã số thuế: 0314567890
Mặt hàng: Máy in Laser đa năng HP LaserJet Pro M404dn
Cộng tiền hàng: 6.200.000 VNĐ
Thuế suất GTGT: 8% (Nghị quyết giảm thuế) | Tiền thuế GTGT: 496.000 VNĐ
Tổng cộng thanh toán: 6.696.000 VNĐ
    """)
    # Reference output
    b11.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Bang_Ke_Mua_Vao": {
            "headers": ["Ký Hiệu", "Số HĐ", "Ngày Lập", "Tên Nhà Cung Cấp", "Mã Số Thuế", "Mặt Hàng", "Tiền Chưa Thuế", "Thuế Suất", "Tiền Thuế GTGT", "Tổng Thanh Toán", "Kiểm Tra"],
            "rows": [
                ["1C26TAA", "0001234", "2026-10-15", "CÔNG TY TNHH VĂN PHÒNG PHẨM TIẾN PHÁT", "0102345678", "Giấy in A4, Bút bi, File còng", 8500000, "10%", 8500000 * 0.1, 9350000, "Khớp 100%"],
                ["2C26TBB", "0005678", "2026-10-20", "CÔNG TY CỔ PHẦN CÔNG NGHỆ THẾ KỶ MỚI", "0314567890", "Máy in Laser đa năng HP LaserJet Pro", 6200000, "8%", 496000, 6696000, "Khớp 100%"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 12: Phan loai tuoi no (AR Aging) va soan email nhac no
    # =========================================================================
    b12 = WorkspaceBuilder(DEPT, "12-phan-loai-tuoi-no-nhac-no")
    b12.write_agents_md(
        role_title="Kế toán Công nợ Phải thu (AR Specialist)",
        department_name="Phòng Kế toán - Tài chính",
        constitution_items=[
            "Phân loại tuổi nợ chuẩn kế toán: Trong hạn, 1-30 ngày, 31-60 ngày, 61-90 ngày, và Trên 90 ngày.",
            "Tông giọng nhắc nợ phù hợp: Lịch sự đối với nợ 1-30 ngày; kiên quyết và cảnh báo tạm dừng cấp hàng đối với nợ >60 ngày."
        ]
    )
    b12.write_rule(
        rule_file_name="quy_chuan_tuoi_no.md",
        description="Quy chuẩn phân bổ tuổi nợ phải thu và lập báo cáo quản trị công nợ",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Báo Cáo Tuổi Nợ Phải Thu (AR Aging Report)",
        guidelines=[
            "Tính số ngày quá hạn = Hôm nay - Ngày đến hạn thanh toán.",
            "Phân bổ số dư nợ còn lại vào đúng cột tuổi nợ tương ứng.",
            "Xuất ra file `Bao_cao_tuoi_no_va_nhac_no.xlsx` kèm bản nháp email nhắc nợ cho các khách hàng quá hạn > 15 ngày."
        ]
    )
    b12.write_corporate_styling_rule()
    b12.write_security_hooks(["cong_no_phai_thu.xlsx"])
    b12.write_skill(
        skill_name="phan-loai-tuoi-no",
        description="Use this skill to calculate accounts receivable aging buckets and prepare debt reminder emails.",
        skill_title="Quy trình phân loại tuổi nợ và gửi thư nhắc công nợ",
        steps=[
            {"name": "Đọc sổ công nợ", "desc": "Nạp file `cong_no_phai_thu.xlsx`."},
            {"name": "Tính toán khung tuổi nợ", "desc": "Phân bổ nợ vào các khung Trong hạn, 1-30, 31-60, 61-90, >90 ngày."},
            {"name": "Soạn thư nhắc nợ", "desc": "Tạo mẫu thư nhắc nợ với nội dung phù hợp cho từng mức độ quá hạn."}
        ]
    )
    b12.write_prompt_demo(
        problem_pain="Kế toán công nợ phải lọc danh sách hóa đơn quá hạn, chia từng khung tuổi nợ rồi soạn email nhắc nợ cho từng khách hàng rất mất thời gian.",
        interactive_hook="Nếu một khách hàng có 3 hóa đơn quá hạn khác nhau, bạn sẽ gửi 3 email riêng rẽ hay gộp vào 1 email bảng kê tổng hợp?",
        prompt_cmd="Đọc file cong_no_phai_thu.xlsx. Tính số ngày quá hạn tính đến hôm nay và phân bổ số dư nợ vào các cột tuổi nợ: Trong hạn, Quá hạn 1-30 ngày, 31-60 ngày, 61-90 ngày, và Trên 90 ngày. Với những khách hàng quá hạn trên 15 ngày, hãy gom tất cả hóa đơn nợ của họ và tạo bản nháp email nhắc thanh toán lịch sự. Xuất file Bao_cao_tuoi_no_va_nhac_no.xlsx.",
        prompt_pitfalls="Nếu không hướng dẫn lọc bỏ các hóa đơn có 'Còn Phải Thu = 0', AI có thể gửi nhầm email đòi nợ khách hàng đã thanh toán xong.",
        expected_output="File `Bao_cao_tuoi_no_va_nhac_no.xlsx` có bảng Aging Report chuẩn và sheet bản nháp email nhắc nợ đã gom gộp hóa đơn.",
        wow_moment="Không chỉ tính toán tuổi nợ mà còn tự động gom gộp nhiều hóa đơn của cùng 1 khách hàng vào chung 1 email nhắc nợ chỉn chu."
    )
    b12.create_excel("cong_no_phai_thu.xlsx", {
        "CongNo": {
            "headers": ["Mã KH", "Tên Khách Hàng", "Email", "Số HĐ", "Ngày Đến Hạn", "Số Tiền Phải Thu", "Đã Thu", "Còn Phải Thu"],
            "rows": [
                ["KH01", "Công ty TNHH Nam Hải", "namhai.ketoan@gmail.com", "HD-881", "2026-10-01", 50000000, 20000000, 30000000], # Quá hạn ~43 ngày
                ["KH01", "Công ty TNHH Nam Hải", "namhai.ketoan@gmail.com", "HD-895", "2026-10-25", 25000000, 0, 25000000],       # Quá hạn ~19 ngày
                ["KH02", "Công ty CP Thắng Lợi", "thangloi@corp.vn", "HD-890", "2026-11-20", 80000000, 80000000, 0],               # Đã thu hết
                ["KH03", "Doanh nghiệp Tư nhân Á Châu", "achau.kt@achau.com", "HD-720", "2026-07-15", 40000000, 0, 40000000],      # Quá hạn >90 ngày
                ["KH04", "Công ty Quốc Tế Sao Mai", "saomai@saomai.vn", "HD-910", "2026-11-25", 15000000, 0, 15000000]             # Trong hạn
            ]
        }
    })
    # Reference output
    b12.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Aging_Report": {
            "headers": ["Mã KH", "Tên Khách Hàng", "Tổng Nợ Phải Thu", "Trong Hạn", "1-30 Ngày", "31-60 Ngày", "61-90 Ngày", ">90 Ngày"],
            "rows": [
                ["KH01", "Công ty TNHH Nam Hải", 55000000, 0, 25000000, 30000000, 0, 0],
                ["KH03", "Doanh nghiệp Tư nhân Á Châu", 40000000, 0, 0, 0, 0, 40000000],
                ["KH04", "Công ty Quốc Tế Sao Mai", 15000000, 15000000, 0, 0, 0, 0]
            ]
        },
        "Draft_Emails": {
            "headers": ["Mã KH", "Tên Khách Hàng", "Email", "Tổng Tiền Nợ", "Tiêu Đề Email", "Nội Dung Thư Nhắc Nợ"],
            "rows": [
                ["KH01", "Công ty TNHH Nam Hải", "namhai.ketoan@gmail.com", 55000000, "[Nhắc Nợ] Bảng kê hóa đơn đến hạn thanh toán - Tháng 11/2026", "Kính gửi Quý công ty, chúng tôi xin gửi bảng kê 2 hóa đơn HD-881 (30tr) và HD-895 (25tr) hiện đã quá hạn thanh toán..."],
                ["KH03", "Doanh nghiệp Tư nhân Á Châu", "achau.kt@achau.com", 40000000, "[Cảnh Báo Nợ Quá Hạn >90 Ngày] Hóa đơn HD-720", "Kính gửi Quý công ty, hóa đơn HD-720 số tiền 40.000.000 VNĐ đã quá hạn trên 90 ngày. Đề nghị quý công ty thanh toán trong vòng 3 ngày làm việc..."]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 13: Phan bo chi phi tra truoc (242) va khau hao TSCD
    # =========================================================================
    b13 = WorkspaceBuilder(DEPT, "13-phan-bo-chi-phi-khau-hao")
    b13.write_agents_md(
        role_title="Kế toán Tài sản & Chi phí",
        department_name="Phòng Kế toán - Tài chính",
        constitution_items=[
            "Tính chính xác ngày lẻ: Tháng ghi tăng tài sản đầu tiên phải tính theo số ngày thực tế sử dụng trong tháng.",
            "Kiểm soát giá trị còn lại: Không bao giờ phân bổ vượt quá Nguyên giá ban đầu."
        ]
    )
    b13.write_rule(
        rule_file_name="quy_chuan_phan_bo_chi_phi.md",
        description="Quy chuẩn tính phân bổ chi phí trả trước TK 242 và trích khấu hao TSCĐ",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Bảng Phân Bổ Chi Phí Trả Trước & Khấu Hao",
        guidelines=[
            "Chi phí 1 tháng tròn = Nguyên giá / Số tháng phân bổ.",
            "Chi phí tháng đầu tiên = (Chi phí 1 tháng tròn / Số ngày trong tháng) * (Số ngày trong tháng - Ngày bắt đầu sử dụng + 1).",
            "Xuất ra file `Bang_phan_bo_chi_phi_2026.xlsx`."
        ]
    )
    b13.write_corporate_styling_rule()
    b13.write_security_hooks(["danh_muc_tscd_242.xlsx"])
    b13.write_skill(
        skill_name="phan-bo-chi-phi-tscd",
        description="Use this skill to schedule monthly amortization for prepaid expenses and fixed asset depreciation.",
        skill_title="Quy trình lập bảng phân bổ chi phí trả trước",
        steps=[
            {"name": "Đọc danh mục tài sản", "desc": "Nạp file `danh_muc_tscd_242.xlsx`."},
            {"name": "Tính toán phân bổ 12 tháng", "desc": "Lập lịch phân bổ từng tháng trong năm 2026, xử lý ngày lẻ tháng đầu."},
            {"name": "Kiểm tra giá trị còn lại", "desc": "Đảm bảo lũy kế phân bổ không vượt nguyên giá."},
            {"name": "Xuất bảng tính", "desc": "Lưu file `Bang_phan_bo_chi_phi_2026.xlsx`."}
        ]
    )
    b13.write_prompt_demo(
        problem_pain="Theo dõi hàng trăm công cụ dụng cụ mua ở các ngày khác nhau trong tháng rất dễ tính sai số ngày sử dụng thực tế của tháng đầu tiên.",
        interactive_hook="Nếu mua 10 dàn máy vi tính ngày 12/03/2026, trong tháng 3 bạn sẽ tính phân bổ trọn tháng hay tính chính xác theo 20 ngày còn lại?",
        prompt_cmd="Từ file danh_muc_tscd_242.xlsx, hãy lập bảng tính phân bổ chi phí từng tháng cho cả năm 2026: tháng đầu tiên tính phân bổ theo số ngày thực tế sử dụng trong tháng, các tháng tiếp theo phân bổ tròn tháng, đảm bảo không phân bổ vượt quá Nguyên giá. Xuất ra file Bang_phan_bo_chi_phi_2026.xlsx.",
        prompt_pitfalls="Nếu không hướng dẫn rõ quy tắc 'Ngày trong tháng - Ngày bắt đầu + 1', AI có thể tính thiếu 1 ngày sử dụng thực tế trong tháng đầu.",
        expected_output="File `Bang_phan_bo_chi_phi_2026.xlsx` với 12 cột cho 12 tháng trong năm, xử lý mượt mà ngày lẻ tháng đầu và giá trị còn lại.",
        wow_moment="Xử lý gọn gàng bài toán phân bổ chi phí ngày lẻ tháng đầu và tháng cuối vốn là nỗi ám ảnh khi viết hàm Excel."
    )
    b13.create_excel("danh_muc_tscd_242.xlsx", {
        "ChiPhi242": {
            "headers": ["Mã CCDC/TSCĐ", "Tên Tài Sản", "Ngày Ghi Tăng", "Nguyên Giá", "Thời Gian Phân Bổ (Tháng)", "Bộ Phận Sử Dụng"],
            "rows": [
                ["CCDC-01", "Dàn máy tính Dell Optiplex (10 bộ)", "2026-03-12", 150000000, 24, "Phòng Kỹ thuật"],
                ["CCDC-02", "Bản quyền phần mềm ERP SAP 1 năm", "2026-01-01", 120000000, 12, "Toàn công ty"],
                ["CCDC-03", "Bàn ghế làm việc văn phòng mới", "2026-06-20", 45000000, 36, "Hành chính"],
                ["CCDC-04", "Máy chủ lưu trữ dữ liệu NAS Synology", "2026-08-05", 60000000, 24, "CNTT"]
            ]
        }
    })
    # Reference output
    b13.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Phan_Bo_Chi_Phi_2026": {
            "headers": ["Mã CCDC", "Tên Tài Sản", "Nguyên Giá", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "Lũy Kế 2026", "Giá Trị Còn Lại"],
            "rows": [
                ["CCDC-01", "Dàn máy tính Dell", 150000000, 0, 0, 4032258, 6250000, 6250000, 6250000, 6250000, 6250000, 6250000, 6250000, 6250000, 6250000, 60282258, 89717742],
                ["CCDC-02", "Bản quyền SAP", 120000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 120000000, 0]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 14: Hop nhat bao cao ket qua kinh doanh (P&L) da chi nhanh
    # =========================================================================
    b14 = WorkspaceBuilder(DEPT, "14-hop-nhat-bao-cao-kinh-doanh")
    b14.write_agents_md(
        role_title="Kế toán Tổng hợp & Hợp nhất Báo cáo",
        department_name="Phòng Kế toán - Tài chính",
        constitution_items=[
            "Thống nhất mã mục chi phí: Ánh xạ chuẩn xác các chỉ tiêu Doanh thu, Giá vốn, Chi phí bán hàng, Chi phí quản lý giữa các chi nhánh.",
            "Tự động tính tỷ suất lợi nhuận: Tính % Gross Margin và Net Margin của từng chi nhánh để so sánh hiệu quả."
        ]
    )
    b14.write_rule(
        rule_file_name="quy_chuan_hop_nhat_pl.md",
        description="Quy chuẩn hợp nhất báo cáo kết quả hoạt động kinh doanh đa chi nhánh",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Hợp Nhất Báo Cáo P&L",
        guidelines=[
            "Tổng hợp số liệu từ các chi nhánh: Hà Nội, Đà Nẵng, TP.HCM.",
            "Lập cột Tổng cộng toàn công ty = Sum(Hà Nội + Đà Nẵng + TP.HCM).",
            "Xuất ra file `Bao_cao_PL_Hop_Nhat_T10.xlsx` kèm bảng xếp hạng chi nhánh hiệu quả nhất."
        ]
    )
    b14.write_corporate_styling_rule()
    b14.write_security_hooks(["Chi_Nhanh/pl_hanoi.xlsx", "Chi_Nhanh/pl_danang.xlsx", "Chi_Nhanh/pl_hcm.xlsx"])
    b14.write_skill(
        skill_name="hop-nhat-bao-cao-pl",
        description="Use this skill to consolidate individual branch P&L income statements into a unified corporate report.",
        skill_title="Quy trình hợp nhất báo cáo kết quả kinh doanh",
        steps=[
            {"name": "Đọc báo cáo chi nhánh", "desc": "Quét toàn bộ file trong thư mục `Chi_Nhanh/`."},
            {"name": "Khớp nối chỉ tiêu", "desc": "Ánh xạ các dòng Doanh thu, Chi phí về bảng chỉ tiêu chuẩn."},
            {"name": "Hợp nhất & Tính tỷ lệ", "desc": "Cộng dồn số liệu toàn công ty và tính biên lợi nhuận."},
            {"name": "Xuất báo cáo hợp nhất", "desc": "Lưu file `Bao_cao_PL_Hop_Nhat_T10.xlsx`."}
        ]
    )
    b14.write_prompt_demo(
        problem_pain="Công ty có nhiều chi nhánh gửi báo cáo doanh thu chi phí riêng biệt. Kế toán trưởng phải mở từng tab gom số lên báo cáo tổng rất dễ sai sót.",
        interactive_hook="Nếu một chi nhánh doanh thu cao gấp 3 chi nhánh khác nhưng tỷ suất lợi nhuận ròng chỉ đạt 5% so với 18% của chi nhánh nhỏ, chi nhánh nào đang hoạt động hiệu quả hơn?",
        prompt_cmd="Đọc toàn bộ file báo cáo của các chi nhánh trong thư mục Chi_Nhanh. Hãy tổng hợp số liệu Doanh thu, Giá vốn, Chi phí bán hàng, Chi phí quản lý và Lợi nhuận ròng của từng chi nhánh vào file Bao_cao_PL_Hop_Nhat_T10.xlsx, thêm cột Tổng công ty và cột % Biên lợi nhuận ròng, xếp hạng chi nhánh có tỷ suất sinh lời cao nhất.",
        prompt_pitfalls="Nếu các chi nhánh đặt tên dòng chi tiêu hơi lệch nhau (ví dụ 'Chi phí QLDN' vs 'Chi phí quản lý'), AI cần có bước chuẩn hóa chỉ tiêu trước khi SUM.",
        expected_output="File `Bao_cao_PL_Hop_Nhat_T10.xlsx` với cấu trúc cột đa chi nhánh, tổng cộng toàn công ty và biểu đồ so sánh lợi nhuận.",
        wow_moment="Chỉ 1 câu lệnh hợp nhất toàn bộ số liệu P&L từ nhiều chi nhánh thành báo cáo tài chính quản trị hoàn chỉnh."
    )
    b14.create_excel("Chi_Nhanh/pl_hanoi.xlsx", {
        "PL": {
            "headers": ["Chỉ Tiêu", "Số Tiền (VNĐ)"],
            "rows": [
                ["Doanh thu thuần", 1200000000],
                ["Giá vốn hàng bán", 720000000],
                ["Lợi nhuận gộp", 480000000],
                ["Chi phí bán hàng", 150000000],
                ["Chi phí quản lý", 120000000],
                ["Lợi nhuận thuần từ HĐKD", 210000000]
            ]
        }
    })
    b14.create_excel("Chi_Nhanh/pl_danang.xlsx", {
        "PL": {
            "headers": ["Chỉ Tiêu", "Số Tiền (VNĐ)"],
            "rows": [
                ["Doanh thu thuần", 500000000],
                ["Giá vốn hàng bán", 290000000],
                ["Lợi nhuận gộp", 210000000],
                ["Chi phí bán hàng", 70000000],
                ["Chi phí quản lý", 50000000],
                ["Lợi nhuận thuần từ HĐKD", 90000000]
            ]
        }
    })
    b14.create_excel("Chi_Nhanh/pl_hcm.xlsx", {
        "PL": {
            "headers": ["Chỉ Tiêu", "Số Tiền (VNĐ)"],
            "rows": [
                ["Doanh thu thuần", 1800000000],
                ["Giá vốn hàng bán", 1050000000],
                ["Lợi nhuận gộp", 750000000],
                ["Chi phí bán hàng", 220000000],
                ["Chi phí quản lý", 180000000],
                ["Lợi nhuận thuần từ HĐKD", 350000000]
            ]
        }
    })
    # Reference output
    b14.create_excel("_ket_qua_mau_chuan.xlsx", {
        "PL_Hop_Nhat": {
            "headers": ["Chỉ Tiêu", "Hà Nội", "Đà Nẵng", "TP.HCM", "Tổng Toàn Công Ty", "Tỷ Trọng (%)"],
            "rows": [
                ["Doanh thu thuần", 1200000000, 500000000, 1800000000, 3500000000, "100.0%"],
                ["Giá vốn hàng bán", 720000000, 290000000, 1050000000, 2060000000, "58.9%"],
                ["Lợi nhuận gộp", 480000000, 210000000, 750000000, 1440000000, "41.1%"],
                ["Chi phí bán hàng", 150000000, 70000000, 220000000, 440000000, "12.6%"],
                ["Chi phí quản lý", 120000000, 50000000, 180000000, 350000000, "10.0%"],
                ["Lợi nhuận thuần", 210000000, 90000000, 350000000, 650000000, "18.6%"]
            ]
        },
        "Xep_Hang_Hieu_Qua": {
            "headers": ["Chi Nhánh", "Doanh Thu", "Lợi Nhuận Thuần", "Biên Lợi Nhuận Ròng (%)", "Xếp Hạng Hiệu Quả"],
            "rows": [
                ["TP.HCM", 1800000000, 350000000, "19.4%", "Hạng 1"],
                ["Đà Nẵng", 500000000, 90000000, "18.0%", "Hạng 2"],
                ["Hà Nội", 1200000000, 210000000, "17.5%", "Hạng 3"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 15: Phat hien giao dich bat thuong va gian lan chi phi
    # =========================================================================
    b15 = WorkspaceBuilder(DEPT, "15-phat-hien-gian-lan-chi-phi")
    b15.write_agents_md(
        role_title="Kiểm toán viên Nội bộ & Soát xét Chi phí",
        department_name="Ban Kiểm toán Nội bộ",
        constitution_items=[
            "Chống gian lận hóa đơn: Phát hiện hóa đơn bị kê khai trùng 2 lần dù khác người đề nghị thanh toán.",
            "Quy định thuế GTGT: Hóa đơn từ 20 triệu đồng trở lên bắt buộc phải chuyển khoản qua ngân hàng.",
            "Phát hiện thủ thuật tách hóa đơn: Cùng 1 nhân viên thanh toán nhiều hóa đơn cùng 1 NCC trong 1 ngày có tổng vượt 20 triệu đồng."
        ]
    )
    b15.write_rule(
        rule_file_name="quy_chuan_kiem_toan_chi_phi.md",
        description="Quy chuẩn rà soát phát hiện rủi ro và gian lận trong bảng kê hoàn ứng chi phí",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Kiểm Toán Bảng Kê Thanh Toán",
        guidelines=[
            "Cảnh báo Đỏ (Gian lận): Trùng Số HĐ + MST người bán.",
            "Cảnh báo Vàng (Vi phạm quy chế): Thanh toán tiền mặt từ 20 triệu trở lên.",
            "Cảnh báo Cam (Nghi vấn lách luật): Tách hóa đơn cùng ngày cùng NCC tổng > 20tr.",
            "Xuất kết quả kiểm toán ra file `Bao_cao_kiem_toan_chi_phi_Q3.xlsx`."
        ]
    )
    b15.write_corporate_styling_rule()
    b15.write_security_hooks(["de_nghi_thanh_toan_q3.xlsx"])
    b15.write_skill(
        skill_name="phat-hien-gian-lan-chi-phi",
        description="Use this skill to audit employee expense claims for duplicates, policy violations, and suspicious splitting.",
        skill_title="Quy trình kiểm toán phát hiện gian lận chi phí",
        steps=[
            {"name": "Nạp bảng kê đề nghị thanh toán", "desc": "Đọc file `de_nghi_thanh_toan_q3.xlsx`."},
            {"name": "Chạy thuật toán kiểm tra rủi ro", "desc": "Quét trùng lặp hóa đơn, kiểm tra ngưỡng thanh toán tiền mặt 20 triệu và phát hiện tách đơn."},
            {"name": "Xuất báo cáo kiểm toán", "desc": "Tạo sheet phân loại các khoản chi rủi ro vào file `Bao_cao_kiem_toan_chi_phi_Q3.xlsx`."}
        ]
    )
    b15.write_prompt_demo(
        problem_pain="Duyệt bảng kê chi phí hàng nghìn dòng, kế toán rất khó phát hiện các hóa đơn bị thanh toán trùng, hoặc nhân viên cố tình tách nhỏ hóa đơn để lách duyệt tiền mặt.",
        interactive_hook="Nếu hai nhân viên ở hai phòng ban khác nhau nộp cùng một số hóa đơn để thanh toán hoàn ứng cách nhau 1 tuần, làm sao kế toán phát hiện kịp trước khi chuyển tiền?",
        prompt_cmd="Kiểm toán file de_nghi_thanh_toan_q3.xlsx: Tìm và đánh dấu các dòng có dấu hiệu rủi ro: (1) Trùng số hóa đơn + MST nhà cung cấp dù khác người đề nghị, (2) Hóa đơn từ 20 triệu trở lên thanh toán Tiền mặt, (3) Cùng 1 nhân viên thanh toán nhiều hóa đơn cùng 1 NCC trong 1 ngày tổng trên 20 triệu (nghi vấn tách hóa đơn). Xuất báo cáo ra file Bao_cao_kiem_toan_chi_phi_Q3.xlsx.",
        prompt_pitfalls="Nếu chỉ so khớp số hóa đơn mà không kèm MST người bán, AI có thể báo sai trùng lặp giữa 2 nhà cung cấp khác nhau nhưng tình cờ trùng số HĐ 0012.",
        expected_output="File `Bao_cao_kiem_toan_chi_phi_Q3.xlsx` chỉ đích danh các khoản thanh toán trùng lặp và các giao dịch vi phạm quy chế tài chính.",
        wow_moment="Biến AI thành Kiểm toán viên nội bộ rà soát 100% giao dịch trong vài giây thay vì chỉ chọn mẫu ngẫu nhiên."
    )
    b15.create_excel("de_nghi_thanh_toan_q3.xlsx", {
        "ThanhToan": {
            "headers": ["Mã Phiếu", "Ngày", "Người Đề Nghị", "Tên NCC", "MST NCC", "Số HĐ", "Số Tiền (VNĐ)", "Hình Thức TT"],
            "rows": [
                ["TT01", "2026-08-10", "Nguyễn Tuấn Anh", "Công ty TNHH Ánh Dương", "0109988776", "HD-0012", 8500000, "Tiền mặt"],
                ["TT02", "2026-08-15", "Trần Thu Hà", "Khách sạn Mường Thanh", "0101122334", "HD-9941", 25000000, "Tiền mặt"], # Vi phạm: >20tr tiền mặt
                ["TT03", "2026-08-20", "Lê Văn Hùng", "Công ty TNHH Ánh Dương", "0109988776", "HD-0012", 8500000, "Chuyển khoản"], # Trùng HD-0012 với TT01!
                ["TT04", "2026-08-25", "Vũ Hoàng My", "Nhà hàng Sen Tây Hồ", "0105544332", "HD-3311", 12000000, "Tiền mặt"], # Cùng ngày cùng NCC với TT05
                ["TT05", "2026-08-25", "Vũ Hoàng My", "Nhà hàng Sen Tây Hồ", "0105544332", "HD-3312", 11000000, "Tiền mặt"]  # Tách đơn tổng = 23tr > 20tr!
            ]
        }
    })
    # Reference output
    b15.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Bao_Cao_Kiem_Toan": {
            "headers": ["Mã Phiếu", "Người Đề Nghị", "Tên NCC", "Số HĐ", "Số Tiền", "Hình Thức", "Mức Độ Rủi Ro", "Nguyên Nhân Phát Hiện", "Kiến Nghị Xử Lý"],
            "rows": [
                ["TT03", "Lê Văn Hùng", "Công ty Ánh Dương", "HD-0012", 8500000, "Chuyển khoản", "ĐỎ (Gian lận)", "Trùng Số HĐ + MST với phiếu TT01 (Nguyễn Tuấn Anh)", "Thu hồi tiền, kỷ luật gian lận"],
                ["TT02", "Trần Thu Hà", "Khách sạn Mường Thanh", "HD-9941", 25000000, "Tiền mặt", "VÀNG (Vi phạm TT)", "Chi tiền mặt >= 20 triệu không hợp lệ thuế GTGT", "Yêu cầu hủy phiếu, chuyển khoản ngân hàng"],
                ["TT04 & TT05", "Vũ Hoàng My", "Nhà hàng Sen Tây Hồ", "HD-3311/12", 23000000, "Tiền mặt", "CAM (Lách luật)", "Cùng ngày tách 2 hóa đơn cùng NCC tổng 23 triệu", "Yêu cầu giải trình nguyên nhân tách hóa đơn"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 16: Chuyen doi so tien bang so sang chu tieng Viet va tieng Anh
    # =========================================================================
    b16 = WorkspaceBuilder(DEPT, "16-chuyen-so-thanh-chu")
    b16.write_agents_md(
        role_title="Kế toán Thanh toán & Thủ quỹ",
        department_name="Phòng Kế toán - Tài chính",
        constitution_items=[
            "Chuẩn ngữ pháp kế toán tiếng Việt: Viết hoa chữ cái đầu, có chữ 'đồng chẵn' hoặc 'đồng' ở cuối câu (ví dụ: 'Một trăm hai mươi lăm triệu đồng chẵn').",
            "Chuẩn ngữ pháp tiếng Anh: Viết hoa chữ cái đầu, chuẩn tiền tệ Dollars hoặc VN Dong (ví dụ: 'One hundred twenty-five million VND only')."
        ]
    )
    b16.write_rule(
        rule_file_name="quy_chuan_doc_so_thanh_chu.md",
        description="Quy chuẩn đọc số tiền thành chữ song ngữ trên chứng từ kế toán",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Chuyển Đổi Số Tiền Thành Chữ Song Ngữ",
        guidelines=[
            "Chuyển đổi 100% chính xác các hàng tỷ, triệu, nghìn, đồng.",
            "Thêm 2 cột mới vào file: `Bằng chữ (Tiếng Việt)` và `In Words (English)`.",
            "Xuất ra file `Danh_sach_phieu_chi_chuan.xlsx`."
        ]
    )
    b16.write_corporate_styling_rule()
    b16.write_security_hooks(["danh_sach_phieu_chi.xlsx"])
    b16.write_skill(
        skill_name="chuyen-so-thanh-chu",
        description="Use this skill to convert numeric currency values into grammatically correct Vietnamese and English verbal text.",
        skill_title="Quy trình chuyển đổi số thành chữ song ngữ",
        steps=[
            {"name": "Đọc bảng số tiền", "desc": "Nạp file `danh_sach_phieu_chi.xlsx`."},
            {"name": "Quy đổi số thành chữ", "desc": "Áp dụng thuật toán đọc số tự nhiên tiếng Việt và tiếng Anh chuẩn mực kế toán."},
            {"name": "Cập nhật bảng tính", "desc": "Ghi dữ liệu vào các cột mới và lưu file `Danh_sach_phieu_chi_chuan.xlsx`."}
        ]
    )
    b16.write_prompt_demo(
        problem_pain="Excel mặc định không có hàm đọc số thành chữ tiếng Việt. Người dùng thường phải cài Add-in lạ dễ dính virus hoặc lỗi font tiếng Việt.",
        interactive_hook="Theo chuẩn kế toán Việt Nam, con số 2.500.000.000 đọc là 'Hai tỷ năm trăm triệu đồng' hay 'Hai tỷ năm trăm triệu đồng chẵn'?",
        prompt_cmd="Đọc file danh_sach_phieu_chi.xlsx. Thêm 2 cột mới: 'Bằng chữ (Tiếng Việt)' và 'In Words (English)' đọc chính xác số tiền ở cột Số tiền theo đúng chuẩn kế toán (viết hoa chữ đầu, có chữ 'đồng chẵn' ở cuối). Xuất ra file Danh_sach_phieu_chi_chuan.xlsx.",
        prompt_pitfalls="Nếu không quy định 'viết hoa chữ cái đầu', AI có thể trả về chuỗi viết thường toàn bộ làm giảm tính trang trọng của chứng từ kế toán.",
        expected_output="File `Danh_sach_phieu_chi_chuan.xlsx` có đầy đủ 2 cột đọc số thành chữ song ngữ chuẩn chỉnh cho tất cả các con số hàng trăm triệu, hàng tỷ.",
        wow_moment="Không cần cài bất kỳ Add-in hay viết code VBA nào mà vẫn có cột đọc số thành chữ chuẩn xác cả tiếng Việt lẫn tiếng Anh."
    )
    b16.create_excel("danh_sach_phieu_chi.xlsx", {
        "PhieuChi": {
            "headers": ["Số Phiếu", "Ngày Chi", "Người Nhận", "Lý Do Chi", "Số Tiền (VNĐ)"],
            "rows": [
                ["PC-01", "2026-10-10", "Nguyễn Văn An", "Tạm ứng công tác phí Sài Gòn", 15250000],
                ["PC-02", "2026-10-12", "Công ty TNHH Hoàng Mai", "Thanh toán tiền thuê văn phòng T10", 85000000],
                ["PC-03", "2026-10-15", "Trần Đình Khôi", "Mua sắm máy tính xách tay", 28900000],
                ["PC-04", "2026-10-18", "Công ty CP Xây Dựng Số 1", "Tạm ứng đợt 1 sửa chữa văn phòng", 2500000000] # 2.5 tỷ
            ]
        }
    })
    # Reference output
    b16.create_excel("_ket_qua_mau_chuan.xlsx", {
        "PhieuChi_SongNgu": {
            "headers": ["Số Phiếu", "Người Nhận", "Số Tiền (VNĐ)", "Bằng Chữ (Tiếng Việt)", "In Words (English)"],
            "rows": [
                ["PC-01", "Nguyễn Văn An", 15250000, "Mười lăm triệu hai trăm năm mươi nghìn đồng chẵn", "Fifteen million two hundred fifty thousand Vietnamese Dong only"],
                ["PC-02", "Công ty TNHH Hoàng Mai", 85000000, "Tám mươi lăm triệu đồng chẵn", "Eighty-five million Vietnamese Dong only"],
                ["PC-03", "Trần Đình Khôi", 28900000, "Hai mươi tám triệu chín trăm nghìn đồng chẵn", "Twenty-eight million nine hundred thousand Vietnamese Dong only"],
                ["PC-04", "Công ty CP Xây Dựng Số 1", 2500000000, "Hai tỷ năm trăm triệu đồng chẵn", "Two billion five hundred million Vietnamese Dong only"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 17: Du bao dong tien 12 tuan toi (Cashflow Forecast)
    # =========================================================================
    b17 = WorkspaceBuilder(DEPT, "17-du-bao-dong-tien-12-tuan")
    b17.write_agents_md(
        role_title="Chuyên viên Quản trị Tài chính & Dòng tiền",
        department_name="Phòng Kế toán - Tài chính",
        constitution_items=[
            "Cảnh báo nguy cơ thiếu hụt dòng tiền: Báo động đỏ các tuần có số dư tiền mặt cuối kỳ rơi xuống dưới 500 triệu đồng.",
            "Dự báo đa kịch bản: Kịch bản Cơ sở (khách trả đúng hạn) và Kịch bản Thận trọng (khách nợ chậm 2 tuần)."
        ]
    )
    b17.write_rule(
        rule_file_name="quy_chuan_du_bao_dong_tien.md",
        description="Quy chuẩn lập mô hình dự báo dòng tiền 12 tuần đa kịch bản",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Mô Hình Dự Báo Dòng Tiền 12 Tuần",
        guidelines=[
            "Số dư cuối kỳ = Số dư đầu kỳ + Tổng thu trong tuần - Tổng chi trong tuần.",
            "Số dư đầu kỳ tuần N = Số dư cuối kỳ tuần N-1.",
            "Xuất ra file `Du_bao_dong_tien_12_tuan.xlsx` kèm biểu đồ đường biểu diễn dòng tiền."
        ]
    )
    b17.write_corporate_styling_rule()
    b17.write_security_hooks(["ke_hoach_dong_tien.xlsx"])
    b17.write_skill(
        skill_name="du-bao-dong-tien",
        description="Use this skill to model 12-week rolling cash flow forecasts and identify liquidity deficit points.",
        skill_title="Quy trình dự báo dòng tiền 12 tuần",
        steps=[
            {"name": "Đọc lịch thu - chi", "desc": "Nạp file `ke_hoach_dong_tien.xlsx` gồm số dư ban đầu, phải thu và phải trả."},
            {"name": "Mô hình hóa dòng tiền 12 tuần", "desc": "Xây dựng bảng dòng tiền tuần hoàn và áp dụng kịch bản thận trọng."},
            {"name": "Xuất báo cáo & Biểu đồ", "desc": "Lưu file `Du_bao_dong_tien_12_tuan.xlsx`."}
        ]
    )
    b17.write_prompt_demo(
        problem_pain="Doanh nghiệp có lãi trên sổ sách nhưng hết tiền trả nợ và lương vì lệch kỳ hạn thu tiền khách và trả tiền nhà cung cấp.",
        interactive_hook="Doanh nghiệp báo lãi 10 tỷ trên P&L nhưng tài khoản ngân hàng chỉ còn 50 triệu đến ngày trả lương, nguyên nhân phổ biến nhất là gì?",
        prompt_cmd="Dựa trên 3 sheet trong file ke_hoach_dong_tien.xlsx, hãy lập bảng Dự báo dòng tiền (Cashflow Forecast) theo từng tuần trong 12 tuần tới. Giả định 2 kịch bản: Cơ sở và Thận trọng (30% khách hàng lớn trả chậm 2 tuần). Cảnh báo màu đỏ tuần nào số dư cuối kỳ dưới 500 triệu đồng. Xuất ra file Du_bao_dong_tien_12_tuan.xlsx.",
        prompt_pitfalls="Nếu không liên kết số dư đầu kỳ tuần này bằng số dư cuối kỳ tuần trước (Rolling Balance), toàn bộ mô hình dòng tiền sẽ bị tính sai hoàn toàn.",
        expected_output="File `Du_bao_dong_tien_12_tuan.xlsx` với mô hình tài chính 12 tuần, chỉ rõ chính xác tuần nào rơi vào vùng nguy hiểm đứt dòng tiền.",
        wow_moment="Tạo ngay mô hình tài chính đa kịch bản (Scenario Modeling) sắc bén giúp ban lãnh đạo chủ động điều tiết vốn."
    )
    b17.create_excel("ke_hoach_dong_tien.xlsx", {
        "SoDuDauKy": {
            "headers": ["Chỉ Tiêu", "Số Tiền (VNĐ)"],
            "rows": [["Số dư tiền mặt & ngân hàng hiện tại", 1200000000]]
        },
        "LichPhaiThu": {
            "headers": ["Tuần Dự Kiến Thu", "Khách Hàng", "Số Tiền Phải Thu"],
            "rows": [
                ["Tuần 1", "Công ty An Phát", 400000000],
                ["Tuần 2", "Công ty Hoàng Gia", 350000000],
                ["Tuần 3", "Công ty CP Đại Dương", 600000000],
                ["Tuần 4", "Khách hàng lẻ", 150000000]
            ]
        },
        "LichPhaiChi": {
            "headers": ["Tuần Dự Kiến Chi", "Khoản Chi", "Số Tiền Phải Chi"],
            "rows": [
                ["Tuần 1", "Thanh toán NCC Nguyên vật liệu", 500000000],
                ["Tuần 2", "Chi trả lương nhân viên T10", 850000000],
                ["Tuần 3", "Nộp thuế GTGT & TNDN", 300000000],
                ["Tuần 4", "Tiền thuê văn phòng & điện nước", 180000000]
            ]
        }
    })
    # Reference output
    b17.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Du_Bao_Dong_Tien_Co_So": {
            "headers": ["Chỉ Tiêu", "Tuần 1", "Tuần 2", "Tuần 3", "Tuần 4"],
            "rows": [
                ["1. Số dư đầu kỳ", 1200000000, 1100000000, 600000000, 900000000],
                ["2. Tổng thu trong tuần", 400000000, 350000000, 600000000, 150000000],
                ["3. Tổng chi trong tuần", 500000000, 850000000, 300000000, 180000000],
                ["4. Dòng tiền ròng (Thu - Chi)", -100000000, -500000000, 300000000, -30000000],
                ["5. Số dư cuối kỳ", 1100000000, 600000000, 900000000, 870000000],
                ["6. Đánh giá an toàn", "An toàn", "Cận ngưỡng cảnh báo", "An toàn", "An toàn"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 18: Tu dong dinh khoan No/Co tu noi dung dien giai giao dich
    # =========================================================================
    b18 = WorkspaceBuilder(DEPT, "18-dinh-khoan-no-co-tu-dong")
    b18.write_agents_md(
        role_title="Kế toán viên Hạch toán & Định khoản",
        department_name="Phòng Kế toán - Tài chính",
        constitution_items=[
            "Hạch toán theo Thông tư 200/2014/TT-BTC: Gán chính xác tài khoản Nợ và tài khoản Có cho từng nghiệp vụ kinh tế phát sinh.",
            "Chuẩn hóa file import phần mềm: Xuất ra cấu trúc chuẩn để nhập trực tiếp vào phần mềm kế toán MISA/Fast."
        ]
    )
    b18.write_rule(
        rule_file_name="quy_chuan_dinh_khoan_tt200.md",
        description="Quy chuẩn tự động định khoản tài khoản kế toán từ nội dung diễn giải",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Hạch Toán Định Khoản Theo Thông Tư 200",
        guidelines=[
            "Rút tiền gửi ngân hàng nộp quỹ tiền mặt: Nợ 1111 / Có 1121.",
            "Thanh toán tiền điện/nước/văn phòng phẩm: Nợ 642 / Có 1111 hoặc 1121.",
            "Thu tiền bán hàng của khách hàng: Nợ 1121 / Có 131.",
            "Trả tiền nhà cung cấp: Nợ 331 / Có 1121.",
            "Chi trả lương nhân viên: Nợ 334 / Có 1121.",
            "Xuất ra file `Giao_dich_da_dinh_khoan_import_misa.xlsx`."
        ]
    )
    b18.write_corporate_styling_rule()
    b18.write_security_hooks(["giao_dich_raw.xlsx"])
    b18.write_skill(
        skill_name="dinh-khoan-no-co",
        description="Use this skill to parse natural language transaction descriptions and map them to standard debit/credit accounting accounts.",
        skill_title="Quy trình tự động định khoản kế toán",
        steps=[
            {"name": "Đọc sổ nhật ký giao dịch", "desc": "Nạp file `giao_dich_raw.xlsx` chứa ngày, diễn giải và số tiền."},
            {"name": "Phân tích ngữ nghĩa diễn giải", "desc": "Nhận diện bản chất kinh tế của giao dịch (chi phí, thu nợ, trả nợ, lương, thuế)."},
            {"name": "Gán TK Nợ / TK Có", "desc": "Ánh xạ sang hệ thống tài khoản theo Thông tư 200."},
            {"name": "Xuất file MISA Import", "desc": "Lưu file `Giao_dich_da_dinh_khoan_import_misa.xlsx`."}
        ]
    )
    b18.write_prompt_demo(
        problem_pain="Kế toán dịch vụ hoặc nhân viên mới phải ngồi gõ tay Tài khoản Nợ / Có cho hàng trăm dòng sao kê ngân hàng trước khi import vào phần mềm MISA.",
        interactive_hook="Với giao dịch 'Rút séc tiền gửi ngân hàng về nhập quỹ tiền mặt', tài khoản nào ghi Nợ và tài khoản nào ghi Có theo Thông tư 200?",
        prompt_cmd="Đọc file giao_dich_raw.xlsx. Dựa vào cột Nội dung diễn giải (ví dụ: 'Thanh toán tiền điện T10', 'Thu tiền khách hàng ABC', 'Trả lương NV T10', 'Nộp BHXH'), hãy tự động điền Tài khoản Nợ và Tài khoản Có tương ứng theo Thông tư 200, sau đó định dạng lại đúng chuẩn file import phần mềm MISA vào file Giao_dich_da_dinh_khoan_import_misa.xlsx.",
        prompt_pitfalls="Nếu không xác định rõ giao dịch là tiền mặt (111) hay tiền gửi ngân hàng (112), AI có thể gán nhầm sang 1111 dù chứng từ ghi rõ 'UNC/Chuyển khoản'.",
        expected_output="File `Giao_dich_da_dinh_khoan_import_misa.xlsx` với 100% các dòng giao dịch đã được định khoản Nợ/Có chuẩn chỉnh sẵn sàng import.",
        wow_moment="AI đọc hiểu tiếng Việt tự nhiên trong diễn giải giao dịch để tự định khoản kế toán như một kế toán viên kinh nghiệm."
    )
    b18.create_excel("giao_dich_raw.xlsx", {
        "GiaoDich": {
            "headers": ["Ngày", "Nội Dung Diễn Giải", "Số Tiền Thu", "Số Tiền Chi", "Đối Tượng"],
            "rows": [
                ["2026-10-02", "Thu tiền bán hàng chuyển khoản cty An Phát", 45000000, 0, "Công ty An Phát"],
                ["2026-10-05", "Ủy nhiệm chi thanh toán tiền điện tháng 9", 0, 12500000, "Điện lực Hoàn Kiếm"],
                ["2026-10-10", "Chuyển khoản thanh toán tiền mua máy in văn phòng", 0, 8500000, "Văn phòng phẩm Tiến Phát"],
                ["2026-10-15", "UNC chuyển khoản trả lương nhân viên tháng 9", 0, 185000000, "Toàn thể CBNV"],
                ["2026-10-20", "Rút séc tiền gửi ngân hàng về nhập quỹ tiền mặt", 0, 50000000, "Thủ quỹ công ty"]
            ]
        }
    })
    # Reference output
    b18.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Import_MISA": {
            "headers": ["Ngày Hạch Toán", "Diễn Giải Nghiệp Vụ", "TK Nợ", "TK Có", "Số Tiền", "Đối Tượng"],
            "rows": [
                ["2026-10-02", "Thu tiền bán hàng chuyển khoản cty An Phát", "1121", "131", 45000000, "Công ty An Phát"],
                ["2026-10-05", "Ủy nhiệm chi thanh toán tiền điện tháng 9", "6422", "1121", 12500000, "Điện lực Hoàn Kiếm"],
                ["2026-10-10", "Chuyển khoản thanh toán tiền mua máy in văn phòng", "6423", "1121", 8500000, "Văn phòng phẩm Tiến Phát"],
                ["2026-10-15", "UNC chuyển khoản trả lương nhân viên tháng 9", "3341", "1121", 185000000, "Toàn thể CBNV"],
                ["2026-10-20", "Rút séc tiền gửi ngân hàng về nhập quỹ tiền mặt", "1111", "1121", 50000000, "Thủ quỹ công ty"]
            ]
        }
    })

    print(f"--> Successfully generated {DEPT} (9 exercises).")

if __name__ == "__main__":
    generate()
