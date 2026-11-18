"""
Department 04: Marketing - Thuong mai dien tu (8 Exercises: 28 -> 35)
Updated with Security Hooks, Corporate Styling Rules, Reference Output, and 6-part PROMPT_DEMO.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from generator_core import WorkspaceBuilder

DEPT = "04-marketing"

def generate():
    print(f"--> Generating {DEPT} with enhanced controls...")

    # =========================================================================
    # EXERCISE 28: Gop va chuan hoa bao cao quang cao da kenh
    # =========================================================================
    b28 = WorkspaceBuilder(DEPT, "28-gop-bao-cao-ads-da-kenh")
    b28.write_agents_md(
        role_title="Performance Marketing & Data Analyst",
        department_name="Phòng Marketing",
        constitution_items=[
            "Thống nhất đơn vị tiền tệ: Quy đổi toàn bộ chi phí về Việt Nam Đồng (VNĐ).",
            "Chuẩn hóa trường dữ liệu: Ngày, Kênh (Platform), Chiến Dịch, Chi Phí, Lượt Hiển Thị, Clicks, CTR, Chuyển Đổi, CPA."
        ]
    )
    b28.write_rule(
        rule_file_name="quy_chuan_gop_ads.md",
        description="Quy chuẩn gộp báo cáo Facebook Ads, Google Ads, TikTok Ads",
        globs="*.csv, *.xlsx",
        rule_title="Quy Chuẩn Báo Cáo Quảng Cáo Đa Kênh",
        guidelines=[
            "Chuyển đổi bảng mã CSV UTF-8 đúng font tiếng Việt.",
            "Tự động tính: CTR = Clicks / Impressions * 100%, CPA = Chi phí / Chuyển đổi.",
            "Xuất ra file `Master_Ads_Report_T10.xlsx`."
        ]
    )
    b28.write_corporate_styling_rule()
    b28.write_security_hooks(["fb_ads.csv", "gg_ads.csv", "tiktok_ads.xlsx"])
    b28.write_skill(
        skill_name="gop-bao-cao-ads",
        description="Use this skill to consolidate advertising performance reports from Facebook, Google, and TikTok.",
        skill_title="Quy trình hợp nhất báo cáo quảng cáo",
        steps=[
            {"name": "Đọc 3 nguồn báo cáo", "desc": "Nạp file `fb_ads.csv`, `gg_ads.csv` và `tiktok_ads.xlsx`."},
            {"name": "Chuẩn hóa tiêu đề & Định dạng", "desc": "Đồng bộ tên cột và đơn vị tiền tệ."},
            {"name": "Gộp dữ liệu & Tính chỉ số", "desc": "Tính CTR, CPA và tổng chi phí toàn kênh."},
            {"name": "Xuất bảng tổng hợp", "desc": "Lưu file `Master_Ads_Report_T10.xlsx`."}
        ]
    )
    b28.write_prompt_demo(
        problem_pain="Mỗi nền tảng quảng cáo xuất ra định dạng khác nhau (FB gọi là Amount Spent, Google là Cost, TikTok là Total Cost). Mỗi sáng mất 1-2 tiếng để gộp thủ công.",
        interactive_hook="Nếu Facebook ghi nhận Amount Spent là 1.500.000 còn Google ghi Cost là 1.200.000, làm sao để gộp thành 1 cột Chi Phí duy nhất mà không phải đổi tên cột bằng tay?",
        prompt_cmd="Đọc 3 file fb_ads.csv, gg_ads.csv và tiktok_ads.xlsx. Hãy chuẩn hóa về cùng cấu trúc: Ngày, Kênh, Chiến dịch, Chi phí (VNĐ), Impressions, Clicks, CTR, Chuyển đổi, CPA. Gộp tất cả vào file Master_Ads_Report_T10.xlsx và tạo bảng tổng hợp so sánh hiệu quả giữa 3 kênh.",
        prompt_pitfalls="Nếu không ép kiểu trường Date về cùng định dạng chuẩn YYYY-MM-DD, các file CSV có thể bị lẫn lộn giữa ngày/tháng của Mỹ (MM/DD) và Việt Nam (DD/MM).",
        expected_output="File `Master_Ads_Report_T10.xlsx` tích hợp dữ liệu 3 kênh quảng cáo sạch sẽ kèm bảng so sánh hiệu quả.",
        wow_moment="Xử lý sạch lỗi lệch bảng mã CSV, lệch tên cột Anh/Việt và tự tính các chỉ số phái sinh trong 10 giây."
    )
    b28.write_text_file("fb_ads.csv", """Date,Campaign Name,Amount Spent,Impressions,Link Clicks,Purchases
2026-10-15,FB_Ao_Polo_Thu_Dong,1500000,45000,1200,25
2026-10-16,FB_Ao_Polo_Thu_Dong,1800000,52000,1450,30
""")
    b28.write_text_file("gg_ads.csv", """Day,Campaign,Cost,Impr,Clicks,Conversions
2026-10-15,GG_Search_Ao_Nam,1200000,15000,980,18
2026-10-16,GG_Search_Ao_Nam,1100000,14000,920,20
""")
    b28.create_excel("tiktok_ads.xlsx", {
        "TikTok": {
            "headers": ["Stat Date", "Campaign Title", "Total Cost", "Show Count", "Click Count", "Conversion Count"],
            "rows": [
                ["2026-10-15", "TT_Video_GenZ", 950000, 60000, 2100, 15],
                ["2026-10-16", "TT_Video_GenZ", 1050000, 68000, 2400, 19]
            ]
        }
    })
    # Reference output
    b28.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Du_Lieu_Gop": {
            "headers": ["Ngày", "Kênh Quảng Cáo", "Chiến Dịch", "Chi Phí (VNĐ)", "Hiển Thị", "Clicks", "CTR (%)", "Chuyển Đổi", "CPA (VNĐ)"],
            "rows": [
                ["2026-10-15", "Facebook Ads", "FB_Ao_Polo_Thu_Dong", 1500000, 45000, 1200, "2.67%", 25, 60000],
                ["2026-10-16", "Facebook Ads", "FB_Ao_Polo_Thu_Dong", 1800000, 52000, 1450, "2.79%", 30, 60000],
                ["2026-10-15", "Google Ads", "GG_Search_Ao_Nam", 1200000, 15000, 980, "6.53%", 18, 66667],
                ["2026-10-16", "Google Ads", "GG_Search_Ao_Nam", 1100000, 14000, 920, "6.57%", 20, 55000],
                ["2026-10-15", "TikTok Ads", "TT_Video_GenZ", 950000, 60000, 2100, "3.50%", 15, 63333],
                ["2026-10-16", "TikTok Ads", "TT_Video_GenZ", 1050000, 68000, 2400, "3.53%", 19, 55263]
            ]
        },
        "So_Sanh_Kenh": {
            "headers": ["Kênh Quảng Cáo", "Tổng Chi Phí", "Tổng Clicks", "CTR Trung Bình", "Tổng Chuyển Đổi", "CPA Trung Bình"],
            "rows": [
                ["Facebook Ads", 3300000, 2650, "2.73%", 55, 60000],
                ["Google Ads", 2300000, 1900, "6.55%", 38, 60526],
                ["TikTok Ads", 2000000, 4500, "3.52%", 34, 58824]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 29: Doi soat doanh thu va phi san Thuong mai dien tu
    # =========================================================================
    b29 = WorkspaceBuilder(DEPT, "29-doi-soat-doanh-thu-phi-san")
    b29.write_agents_md(
        role_title="Quản lý Tài chính Gian hàng TMĐT (E-commerce Operations)",
        department_name="Phòng Thương mại Điện tử",
        constitution_items=[
            "Minh bạch phí sàn: Bóc tách phí thanh toán, phí cố định, phí hoa hồng tiếp thị liên kết (Affiliate), phí voucher shop tài trợ.",
            "Cảnh báo bán lỗ: Lọc riêng các đơn hàng hoặc mã SKU có Lợi nhuận ròng thực tế < 0."
        ]
    )
    b29.write_rule(
        rule_file_name="quy_chuan_phi_san_tmdt.md",
        description="Quy chuẩn đối soát chi tiết phí sàn Shopee và tính lãi lỗ từng đơn",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Đối Soát Bán Hàng Sàn TMĐT",
        guidelines=[
            "Tiền thực nhận = Doanh thu gốc - Tổng các loại phí sàn thu.",
            "Lợi nhuận ròng = Tiền thực nhận - Giá vốn hàng bán (COGS).",
            "Xuất ra file `Doi_soat_lai_lo_Shopee_T10.xlsx` kèm sheet `Canh_Bao_Ban_Lo` tô màu đỏ."
        ]
    )
    b29.write_corporate_styling_rule()
    b29.write_security_hooks(["shopee_orders.xlsx", "gia_von.xlsx"])
    b29.write_skill(
        skill_name="doi-soat-phi-san-tmdt",
        description="Use this skill to reconcile marketplace deductions, calculate net unit margins, and identify loss-making SKUs.",
        skill_title="Quy trình đối soát doanh thu và phí sàn TMĐT",
        steps=[
            {"name": "Đọc báo cáo đơn sàn & giá vốn", "desc": "Nạp file `shopee_orders.xlsx` và `gia_von.xlsx`."},
            {"name": "Bóc tách ma trận phí", "desc": "Tính tổng các khoản phí sàn và đối trừ giá vốn."},
            {"name": "Khoanh vùng đơn hàng lỗ", "desc": "Lọc các đơn hàng có lợi nhuận âm và lưu file `Doi_soat_lai_lo_Shopee_T10.xlsx`."}
        ]
    )
    b29.write_prompt_demo(
        problem_pain="Bán hàng trên Shopee/TikTok Shop có hàng chục loại phí trừ lắt nhắt. Bán nghìn đơn nhưng không biết đơn nào thực lãi, đơn nào đang gồng lỗ.",
        interactive_hook="Một chiếc áo thun bán giá 99k, sau khi trừ phí sàn cố định 7k, phí thanh toán 3k, voucher shop 30k và phí lệch ship 15k, shop còn thực nhận bao nhiêu tiền?",
        prompt_cmd="Kết hợp file shopee_orders.xlsx và gia_von.xlsx. Với từng đơn hàng và từng mã SKU, hãy tính: Doanh thu, Tổng phí sàn thu, Tiền thực nhận về ví, Giá vốn hàng bán, Lợi nhuận ròng thực tế và % Biên lợi nhuận. Lọc ra danh sách các đơn hàng hoặc mã SKU đang bị bán lỗ ra sheet riêng trong file Doi_soat_lai_lo_Shopee_T10.xlsx.",
        prompt_pitfalls="Nếu quên nhân giá vốn với cột Số lượng sản phẩm trên đơn hàng, toàn bộ bài toán tính lợi nhuận gộp sẽ bị sai lệch nghiêm trọng.",
        expected_output="File `Doi_soat_lai_lo_Shopee_T10.xlsx` chỉ rõ từng đơn lãi/lỗ và cảnh báo mã sản phẩm đang âm tiền.",
        wow_moment="Bóc tách ma trận phí sàn TMĐT và chỉ điểm ngay những mã sản phẩm nhìn tưởng bán chạy nhưng thực chất đang gồng lỗ."
    )
    b29.create_excel("shopee_orders.xlsx", {
        "Shopee": {
            "headers": ["Mã Đơn", "Mã SKU", "Số Lượng", "Doanh Thu Gốc", "Phí Sàn Cố Định", "Phí Thanh Toán", "Phí Voucher Shop", "Phí Vận Chuyển Lệch"],
            "rows": [
                ["SP001", "AO_POLO_DEN", 2, 500000, 35000, 15000, 50000, 10000], # Phí = 110k, Thực nhận = 390k
                ["SP002", "QUAN_JEAN_XANH", 1, 350000, 24500, 10500, 20000, 0],     # Phí = 55k, Thực nhận = 295k
                ["SP003", "AO_THUN_SALE", 1, 99000, 7000, 3000, 30000, 15000]       # Bán phá giá: Phí = 55k, Thực nhận = 44k (Giá vốn 55k -> LỖ!)
            ]
        }
    })
    b29.create_excel("gia_von.xlsx", {
        "GiaVon": {
            "headers": ["Mã SKU", "Tên Sản Phẩm", "Giá Vốn Hàng Bán (VNĐ)"],
            "rows": [
                ["AO_POLO_DEN", "Áo Polo Nam Màu Đen", 140000], # 2 cái = 280k
                ["QUAN_JEAN_XANH", "Quần Jean Slimfit Xanh", 180000],
                ["AO_THUN_SALE", "Áo Thun Basic Xả Kho", 55000]
            ]
        }
    })
    # Reference output
    b29.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Doi_Soat_Chi_Tiet": {
            "headers": ["Mã Đơn", "Mã SKU", "Số Lượng", "Doanh Thu Gốc", "Tổng Phí Sàn", "Thực Nhận Ví", "Tổng Giá Vốn", "Lợi Nhuận Ròng", "Biên Lãi (%)", "Trạng Thái"],
            "rows": [
                ["SP001", "AO_POLO_DEN", 2, 500000, 110000, 390000, 280000, 110000, "22.0%", "Có Lãi"],
                ["SP002", "QUAN_JEAN_XANH", 1, 350000, 55000, 295000, 180000, 115000, "32.9%", "Có Lãi"],
                ["SP003", "AO_THUN_SALE", 1, 99000, 55000, 44000, 55000, -11000, "-11.1%", "BÁN LỖ!"]
            ]
        },
        "Canh_Bao_Ban_Lo": {
            "headers": ["Mã Đơn", "Mã SKU", "Số Tiền Lỗ", "Nguyên Nhân Chính", "Hành Động Khắc Phục"],
            "rows": [
                ["SP003", "AO_THUN_SALE", -11000, "Phí voucher shop (30k) + Lệch ship (15k) quá cao so với giá bán 99k", "Tăng giá bán tối thiểu lên 129k hoặc giảm voucher shop"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 30: Tu dong tao link UTM Tracking va ma QR hang loat
    # =========================================================================
    b30 = WorkspaceBuilder(DEPT, "30-tao-link-utm-tracking-qr")
    b30.write_agents_md(
        role_title="Chuyên viên Tracking & Kỹ thuật Marketing",
        department_name="Phòng Marketing",
        constitution_items=[
            "Chuẩn hóa cú pháp UTM: Chữ thường, không dấu, nối từ bằng dấu gạch ngang (kebab-case).",
            "Bảo toàn tham số: Đầy đủ utm_source, utm_medium, utm_campaign, utm_content."
        ]
    )
    b30.write_rule(
        rule_file_name="quy_chuan_utm_tracking.md",
        description="Quy chuẩn tạo đường dẫn UTM tracking chuẩn SEO và Google Analytics",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Đường Dẫn UTM Tracking",
        guidelines=[
            "Tự động chuyển đổi tiếng Việt có dấu thành không dấu.",
            "Loại bỏ dấu cách và ký tự đặc biệt.",
            "Tạo cột Full_URL và công thức tạo ảnh mã QR.",
            "Xuất ra file `Ke_hoach_UTM_Tracking_Chuan.xlsx`."
        ]
    )
    b30.write_corporate_styling_rule()
    b30.write_security_hooks(["ke_hoach_content.xlsx"])
    b30.write_skill(
        skill_name="tao-link-utm-tracking",
        description="Use this skill to batch generate clean, kebab-cased UTM tracking campaign URLs and QR codes.",
        skill_title="Quy trình tạo link UTM Tracking hàng loạt",
        steps=[
            {"name": "Đọc bảng kế hoạch bài đăng", "desc": "Nạp file `ke_hoach_content.xlsx`."},
            {"name": "Chuẩn hóa chuỗi ký tự", "desc": "Bỏ dấu tiếng Việt và ghép chuỗi tham số URL encode."},
            {"name": "Xuất bảng liên kết", "desc": "Lưu file `Ke_hoach_UTM_Tracking_Chuan.xlsx`."}
        ]
    )
    b30.write_prompt_demo(
        problem_pain="Gắn tham số UTM thủ công cho 50 bài đăng của 10 KOLs rất dễ gõ nhầm dấu cách hoặc chữ hoa/thường làm hỏng báo cáo Google Analytics.",
        interactive_hook="Nếu tên chiến dịch là 'Khuyến Mãi Mùa Thu 2026', đường dẫn UTM campaign chuẩn mực nên là gì để Google Analytics không bị phân mảnh số liệu?",
        prompt_cmd="Đọc file ke_hoach_content.xlsx. Tự động chuẩn hóa Tên chiến dịch, Kênh, Tên KOL về chữ thường không dấu nối bằng dấu gạch ngang, ghép thành đường dẫn Full UTM URL hoàn chỉnh và tạo thêm công thức tạo mã QR. Xuất ra file Ke_hoach_UTM_Tracking_Chuan.xlsx.",
        prompt_pitfalls="Nếu không xử lý ký tự khoảng trắng thành dấu gạch ngang, đường link sẽ sinh ra các ký tự '%20' lộn xộn và dễ bị lỗi khi quét mã QR.",
        expected_output="File `Ke_hoach_UTM_Tracking_Chuan.xlsx` với 100% đường dẫn URL chuẩn chỉnh không sai 1 ký tự.",
        wow_moment="Tự động bỏ dấu tiếng Việt, chuẩn hóa quy tắc đặt tên UTM và sinh mã QR cho hàng trăm link chiến dịch."
    )
    b30.create_excel("ke_hoach_content.xlsx", {
        "Campaigns": {
            "headers": ["Link Gốc", "Tên Chiến Dịch", "Kênh Truyền Thông", "Tên KOL", "Định Dạng Bài"],
            "rows": [
                ["https://shop.com/polo", "Khuyến Mãi Mùa Thu 2026", "Facebook Fanpage", "Châu Bùi", "Video Review"],
                ["https://shop.com/jean", "Xả Hàng Cuối Năm", "TikTok Shop", "Khoai Lang Thang", "Livestream"],
                ["https://shop.com/shoes", "Ra Mắt Giày Sneaker Mới", "Instagram Post", "Khánh Vy", "Hình ảnh Carousel"]
            ]
        }
    })
    # Reference output
    b30.create_excel("_ket_qua_mau_chuan.xlsx", {
        "UTM_Links": {
            "headers": ["Tên Chiến Dịch", "Kênh (Source)", "KOL (Content)", "Full UTM Campaign URL", "Công Thức QR Code"],
            "rows": [
                ["Khuyến Mãi Mùa Thu 2026", "facebook", "chau-bui", "https://shop.com/polo?utm_source=facebook&utm_medium=kol&utm_campaign=khuyen-mai-mua-thu-2026&utm_content=chau-bui", '=IMAGE("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="&ENCODEURL(D2))'],
                ["Xả Hàng Cuối Năm", "tiktok", "khoai-lang-thang", "https://shop.com/jean?utm_source=tiktok&utm_medium=kol&utm_campaign=xa-hang-cuoi-nam&utm_content=khoai-lang-thang", '=IMAGE("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="&ENCODEURL(D3))'],
                ["Ra Mắt Giày Sneaker Mới", "instagram", "khanh-vy", "https://shop.com/shoes?utm_source=instagram&utm_medium=kol&utm_campaign=ra-mat-giay-sneaker-moi&utm_content=khanh-vy", '=IMAGE("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="&ENCODEURL(D4))']
            ]
        }
    })

    # =========================================================================
    # EXERCISE 31: Phan tich danh gia 1-5 sao khach hang tren san TMDT
    # =========================================================================
    b31 = WorkspaceBuilder(DEPT, "31-phan-tich-danh-gia-san-tmdt")
    b31.write_agents_md(
        role_title="Quản lý Chất lượng & Trải nghiệm Mua hàng TMĐT",
        department_name="Phòng Thương mại Điện tử",
        constitution_items=[
            "Phân tích cảm xúc tiêu cực: Tập trung phân loại các đánh giá 1-3 sao.",
            "Gán nhóm lỗi: Chất lượng sản phẩm, Đóng gói/Móp méo, Giao hàng chậm, Tư vấn chậm, Sai mẫu hàng."
        ]
    )
    b31.write_rule(
        rule_file_name="quy_chuan_sentiment_review.md",
        description="Quy chuẩn phân tích nội dung đánh giá sản phẩm sàn TMĐT",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Phân Loại Review Tiêu Cực TMĐT",
        guidelines=[
            "Đọc nội dung bình luận để gán nhãn `Nhóm Lỗi`.",
            "Lập ma trận thống kê mã SKU nào đang bị phàn nàn nhiều nhất về lỗi gì.",
            "Xuất ra file `Phan_tich_Danh_Gia_Shopee_T10.xlsx`."
        ]
    )
    b31.write_corporate_styling_rule()
    b31.write_security_hooks(["shopee_reviews.xlsx"])
    b31.write_skill(
        skill_name="phan-tich-review-tmdt",
        description="Use this skill to perform sentiment classification and root cause analysis on 1-3 star customer reviews.",
        skill_title="Quy trình phân tích đánh giá sản phẩm TMĐT",
        steps=[
            {"name": "Đọc bảng reviews", "desc": "Nạp file `shopee_reviews.xlsx`."},
            {"name": "Lọc đánh giá 1-3 sao", "desc": "Tách các phản hồi tiêu cực để phân tích nguyên nhân."},
            {"name": "Gán nhãn & Thống kê", "desc": "Xuất file `Phan_tich_Danh_Gia_Shopee_T10.xlsx` kèm biểu đồ lỗi."}
        ]
    )
    b31.write_prompt_demo(
        problem_pain="Tải về hàng nghìn bình luận của khách nhưng không biết sản phẩm bị chê vì giao hàng chậm, móp hộp hay do chất lượng vải lỗi.",
        interactive_hook="Nếu khách chấm 2 sao kèm bình luận 'Đặt size L mà giao size M, shop làm ăn tắc trách', lỗi này thuộc về Bộ phận Đóng gói Kho hay Chất lượng Nhà xưởng?",
        prompt_cmd="Phân tích file shopee_reviews.xlsx. Với các đánh giá từ 1 đến 3 sao, hãy đọc nội dung bình luận để phân loại nguyên nhân vào các nhóm: Chất lượng SP, Đóng gói, Vận chuyển, Tư vấn, Sai mẫu. Lập bảng ma trận thống kê từng Mã sản phẩm bị lỗi nào nhiều nhất vào file Phan_tich_Danh_Gia_Shopee_T10.xlsx.",
        prompt_pitfalls="Nếu không hướng dẫn lọc bỏ các đánh giá 4-5 sao hài lòng, bảng phân tích nguyên nhân gốc rễ (Root Cause) sẽ bị loãng bởi các nhận xét tích cực.",
        expected_output="File `Phan_tich_Danh_Gia_Shopee_T10.xlsx` bóc tách chính xác từng nhóm lỗi theo từng mã hàng để làm việc với kho và xưởng may.",
        wow_moment="Biến hàng nghìn bình luận cảm tính thành bảng số liệu định lượng rõ ràng phục vụ cải tiến sản phẩm."
    )
    b31.create_excel("shopee_reviews.xlsx", {
        "Reviews": {
            "headers": ["Mã Đơn", "Mã SKU", "Số Sao", "Nội Dung Đánh Giá Của Khách"],
            "rows": [
                ["DH101", "AO_POLO_DEN", 1, "Vải mỏng tanh giặt 1 lần đã xù lông, đường may chỉ thừa lung tung."],
                ["DH102", "AO_POLO_DEN", 2, "Đặt size L mà giao size M, shop làm ăn tắc trách quá!"],
                ["DH103", "QUAN_JEAN_XANH", 2, "Chờ ship mất 6 ngày mới tới nơi, gọi tổng đài giục mãi."],
                ["DH104", "QUAN_JEAN_XANH", 1, "Hộp carton bị móp méo rách toạc cả túi nilon bên trong."]
            ]
        }
    })
    # Reference output
    b31.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Phan_Loai_Loi": {
            "headers": ["Mã Đơn", "Mã SKU", "Số Sao", "Bình Luận Gốc", "Nhóm Lỗi Chuẩn Hóa", "Bộ Phận Chịu Trách Nhiệm", "Hành Động Khắc Phục"],
            "rows": [
                ["DH101", "AO_POLO_DEN", 1, "Vải mỏng tanh giặt 1 lần xù lông", "Chất Lượng Sản Phẩm", "Bộ phận Thu mua / QC Xưởng", "Đổi nhà cung cấp vải dệt kim"],
                ["DH102", "AO_POLO_DEN", 2, "Đặt size L mà giao size M", "Giao Sai Mẫu / Sai Size", "Bộ phận Đóng gói Kho", "Quét mã vạch kiểm tra trước khi dán đơn"],
                ["DH103", "QUAN_JEAN_XANH", 2, "Chờ ship mất 6 ngày", "Vận Chuyển Chậm", "Đối tác Logistics (3PL)", "Khiếu nại bưu cục giao hàng chậm"],
                ["DH104", "QUAN_JEAN_XANH", 1, "Hộp carton bị móp méo rách toạc", "Đóng Gói / Hư Hỏng", "Bộ phận Đóng gói Kho", "Tăng cường bọc xốp bóng khí 3 lớp"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 32: Lap ke hoach phan bo ngan sach Media Plan
    # =========================================================================
    b32 = WorkspaceBuilder(DEPT, "32-phan-bo-ngan-sach-media-plan")
    b32.write_agents_md(
        role_title="Trưởng phòng Kế hoạch Truyền thông (Media Director)",
        department_name="Phòng Marketing",
        constitution_items=[
            "Tối ưu hóa chi phí trên khách hàng tiềm năng: Dựa trên chỉ số CPL (Cost Per Lead) lịch sử.",
            "Giới hạn ngưỡng bão hòa: Không phân bổ vượt quá dung lượng tối đa của từng kênh."
        ]
    )
    b32.write_rule(
        rule_file_name="quy_chuan_media_plan.md",
        description="Quy chuẩn lập kế hoạch phân bổ ngân sách quảng cáo đa kênh",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Bảng Kế Hoạch Media Plan",
        guidelines=[
            "Phân bổ tổng ngân sách 500 triệu đồng cho các kênh: Facebook, Google Search, TikTok, Zalo, KOLs.",
            "Tạo 2 kịch bản: (1) Tối đa hóa số lượng Lead, (2) Tối đa hóa Doanh thu dự kiến.",
            "Xuất ra file `Ke_hoach_Media_Plan_Q4.xlsx`."
        ]
    )
    b32.write_corporate_styling_rule()
    b32.write_security_hooks(["lich_su_cpl_kenh.xlsx"])
    b32.write_skill(
        skill_name="phan-bo-media-plan",
        description="Use this skill to optimize marketing budget allocation across channels based on historical CPL and conversion rates.",
        skill_title="Quy trình lập bảng phân bổ ngân sách Media Plan",
        steps=[
            {"name": "Đọc hiệu quả lịch sử", "desc": "Nạp file `lich_su_cpl_kenh.xlsx`."},
            {"name": "Chạy thuật toán phân bổ", "desc": "Tối ưu hóa phân bổ 500 triệu theo tỷ lệ chuyển đổi của kênh."},
            {"name": "Xuất bảng kế hoạch", "desc": "Lưu file `Ke_hoach_Media_Plan_Q4.xlsx`."}
        ]
    )
    b32.write_prompt_demo(
        problem_pain="Sếp giao ngân sách 500 triệu mang về 2.500 khách hàng tiềm năng. Marketer phải ngồi thử từng con số trên Excel rất lâu.",
        interactive_hook="Nếu kênh TikTok giá lead rất rẻ (90k) nhưng tỷ lệ chốt chỉ 6%, trong khi Google Search giá lead 220k nhưng tỷ lệ chốt 22%, kênh nào mang lại chi phí trên mỗi đơn mua rẻ hơn?",
        prompt_cmd="Dựa trên dữ liệu trong lich_su_cpl_kenh.xlsx, hãy lập bảng Media Plan phân bổ 500 triệu VNĐ vào các kênh (Facebook, Google, TikTok, Zalo, KOLs) trong Quý 4 sao cho tối đa hóa số khách mua, không vượt quá ngưỡng bão hòa của kênh. Đưa ra 2 kịch bản: Tối ưu Lead và Tối ưu Doanh thu vào file Ke_hoach_Media_Plan_Q4.xlsx.",
        prompt_pitfalls="Nếu dồn hết tiền vào 1 kênh rẻ nhất mà bỏ qua trần bão hòa (Saturation Ceiling), chi phí thực tế sẽ bị đội lên gấp đôi do cạn tệp khách.",
        expected_output="File `Ke_hoach_Media_Plan_Q4.xlsx` với 2 kịch bản phân bổ chi tiết số tiền, số lead và doanh thu kỳ vọng cho từng kênh.",
        wow_moment="Thay thế công cụ Solver phức tạp của Excel bằng lời giải tối ưu hóa ngân sách kèm bảng kế hoạch sẵn sàng trình sếp."
    )
    b32.create_excel("lich_su_cpl_kenh.xlsx", {
        "HieuQuaKenh": {
            "headers": ["Kênh Quảng Cáo", "CPL Trung Bình (VNĐ)", "Tỷ Lệ Chốt Thành Khách (%)", "Ngân Sách Tối Đa Có Thể Tiêu (VNĐ)"],
            "rows": [
                ["Facebook Ads", 150000, 12, 200000000],
                ["Google Search", 220000, 22, 180000000], # Giá đắt hơn nhưng tỷ lệ mua cao
                ["TikTok Ads", 90000, 6, 120000000],      # Rẻ nhưng chốt thấp
                ["Zalo Ads", 140000, 10, 80000000],
                ["KOLs Review", 250000, 18, 100000000]
            ]
        }
    })
    # Reference output
    b32.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Kich_Ban_Toi_Uu_Doanh_Thu": {
            "headers": ["Kênh Quảng Cáo", "Ngân Sách Phân Bổ (VNĐ)", "Tỷ Trọng (%)", "Số Leads Dự Kiến", "Số Khách Mua Dự Kiến", "Chi Phí / 1 Khách Mua (CAC)"],
            "rows": [
                ["Google Search", 180000000, "36.0%", 818, 180, 1000000],
                ["Facebook Ads", 170000000, "34.0%", 1133, 136, 1250000],
                ["KOLs Review", 80000000, "16.0%", 320, 58, 1379310],
                ["TikTok Ads", 70000000, "14.0%", 778, 47, 1489362]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 33: Gom nhom chu de tu khoa SEO (Keyword Clustering)
    # =========================================================================
    b33 = WorkspaceBuilder(DEPT, "33-gom-cum-tu-khoa-seo")
    b33.write_agents_md(
        role_title="Chuyên gia SEO & Chiến lược Nội dung (SEO Strategist)",
        department_name="Phòng Marketing",
        constitution_items=[
            "Phân loại Search Intent chuẩn xác: Informational (Tìm hiểu), Commercial (So sánh), Transactional (Mua hàng).",
            "Gom nhóm ngữ nghĩa (Topic Cluster): Chọn từ khóa có Search Volume cao nhất làm Primary Keyword."
        ]
    )
    b33.write_rule(
        rule_file_name="quy_chuan_seo_clustering.md",
        description="Quy chuẩn gom cụm từ khóa và phân loại ý định tìm kiếm SEO",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Gom Nhóm Từ Khóa SEO",
        guidelines=[
            "Gom các từ khóa cùng chủ đề vào 1 Topic Cluster.",
            "Gợi ý Tiêu đề bài viết chuẩn SEO (SEO Title) cho từng nhóm.",
            "Xuất ra file `Ke_hoach_Topic_Cluster_SEO.xlsx`."
        ]
    )
    b33.write_corporate_styling_rule()
    b33.write_security_hooks(["keywords_ahrefs.xlsx"])
    b33.write_skill(
        skill_name="gom-cum-tu-khoa-seo",
        description="Use this skill to cluster search engine keywords into topic groups and classify user search intent.",
        skill_title="Quy trình gom cụm từ khóa SEO",
        steps=[
            {"name": "Đọc danh sách từ khóa", "desc": "Nạp file `keywords_ahrefs.xlsx`."},
            {"name": "Phân loại ý định & Gom cụm", "desc": "Gom nhóm ngữ nghĩa và phân loại Intent."},
            {"name": "Đề xuất tiêu đề bài viết", "desc": "Lưu file `Ke_hoach_Topic_Cluster_SEO.xlsx`."}
        ]
    )
    b33.write_prompt_demo(
        problem_pain="Xuất 2.000 từ khóa từ Ahrefs ra Excel, ngồi lọc thủ công và chia nhóm bài viết mất cả tuần trời.",
        interactive_hook="Hai từ khóa 'cách phối đồ áo polo nam' và 'mua áo polo nam chính hãng' nên viết chung vào 1 bài hay tách thành 2 bài viết có mục đích tìm kiếm khác nhau?",
        prompt_cmd="Đọc file keywords_ahrefs.xlsx. Hãy phân loại Search Intent, gom các từ khóa cùng chủ đề vào một Topic Cluster (từ có Volume cao nhất làm Primary Keyword) và gợi ý Tiêu đề bài viết chuẩn SEO cho từng nhóm. Xuất ra file Ke_hoach_Topic_Cluster_SEO.xlsx.",
        prompt_pitfalls="Nếu gộp từ khóa Informational (tìm mẹo phối đồ) chung bài với Transactional (tìm mua hàng giảm giá), bài viết sẽ bị hiện tượng Keyword Cannibalization và tụt thứ hạng Google.",
        expected_output="File `Ke_hoach_Topic_Cluster_SEO.xlsx` tổ chức thành các cụm bài viết rõ ràng, có tiêu đề và intent cụ thể.",
        wow_moment="Rút ngắn 1 tuần làm kế hoạch Content SEO xuống còn 1 phút chạy lệnh."
    )
    b33.create_excel("keywords_ahrefs.xlsx", {
        "Keywords": {
            "headers": ["Keyword", "Search Volume", "Difficulty (KD)"],
            "rows": [
                ["cách phối đồ áo polo nam", 4500, 12],
                ["áo polo nam mặc với quần gì", 3200, 10],
                ["mua áo polo nam chính hãng", 5800, 25],
                ["giá áo polo nam cao cấp", 2100, 18],
                ["áo thun polo nam đẹp giá rẻ", 3900, 22]
            ]
        }
    })
    # Reference output
    b33.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Topic_Clusters": {
            "headers": ["Cụm Chủ Đề (Cluster)", "Từ Khóa Chính (Primary)", "Search Intent", "Tổng Volume Cụm", "Từ Khóa Phụ Đi Kèm", "Gợi Ý Tiêu Đề Bài Viết Chuẩn SEO"],
            "rows": [
                ["Hướng dẫn phối đồ Polo", "cách phối đồ áo polo nam", "Informational", 7700, "áo polo nam mặc với quần gì", "10+ Cách Phối Đồ Áo Polo Nam Lịch Lãm & Chuẩn Soái Ca 2026"],
                ["Mua sắm áo polo chính hãng", "mua áo polo nam chính hãng", "Transactional", 11800, "giá áo polo nam cao cấp; áo thun polo đẹp giá rẻ", "Top 5 Địa Chỉ Mua Áo Polo Nam Chính Hãng, Bền Đẹp Giá Tốt Nhất"]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 34: Kiem tra ton kho qua tang POSM va chia hang cho dai ly
    # =========================================================================
    b34 = WorkspaceBuilder(DEPT, "34-chia-qua-tang-posm-dai-ly")
    b34.write_agents_md(
        role_title="Trade Marketing Specialist",
        department_name="Phòng Marketing",
        constitution_items=[
            "Phân bổ theo tỷ trọng doanh số: Đại lý bán tốt nhận nhiều quà tặng hơn.",
            "Quy cách đóng thùng (Packaging Unit): Bắt buộc làm tròn số lượng theo quy cách thùng (ví dụ: 1 thùng = 20 cái), không chia lẻ kiện."
        ]
    )
    b34.write_rule(
        rule_file_name="quy_chuan_chia_posm.md",
        description="Quy chuẩn phân bổ vật phẩm quảng cáo POSM cho các đại lý",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Phân Bổ Quà Tặng POSM",
        guidelines=[
            "Mỗi đại lý nhận tối thiểu 1 thùng.",
            "Tổng số lượng phân bổ cho các đại lý phải khớp đúng 100% số lượng tồn kho.",
            "Xuất ra file `Bang_chia_qua_tang_POSM_Dai_Ly.xlsx`."
        ]
    )
    b34.write_corporate_styling_rule()
    b34.write_security_hooks(["ton_kho_posm.xlsx"])
    b34.write_skill(
        skill_name="chia-posm-dai-ly",
        description="Use this skill to allocate POSM marketing materials to retail partners rounded by packaging box units.",
        skill_title="Quy trình phân bổ quà tặng POSM",
        steps=[
            {"name": "Đọc tồn kho và doanh số đại lý", "desc": "Nạp file `ton_kho_posm.xlsx`."},
            {"name": "Tính tỷ trọng & Làm tròn", "desc": "Tính tỷ lệ phân bổ theo doanh số và làm tròn theo bội số của thùng."},
            {"name": "Cân bằng tổng số lượng", "desc": "Điều chỉnh lệch tổng để khớp đúng 100% lượng tồn kho và lưu file."}
        ]
    )
    b34.write_prompt_demo(
        problem_pain="Chia quà tặng cho hàng chục đại lý theo tỷ lệ doanh thu nhưng phải làm tròn theo thùng (20 cái/thùng) rất hay bị lệch tổng số lượng.",
        interactive_hook="Nếu chia theo tỷ lệ doanh thu ra 3.7 thùng áo mưa, bạn sẽ làm tròn lên 4 thùng hay làm tròn xuống 3 thùng khi tổng kho chỉ còn đúng 20 thùng?",
        prompt_cmd="Dựa vào file ton_kho_posm.xlsx, hãy phân bổ số lượng từng loại quà tặng POSM cho các đại lý theo tỷ trọng doanh số. Lưu ý: mỗi đại lý nhận tối thiểu 1 thùng, làm tròn theo quy cách đóng thùng, và tổng phân bổ khớp 100% tồn kho hiện có. Xuất file Bang_chia_qua_tang_POSM_Dai_Ly.xlsx.",
        prompt_pitfalls="Nếu làm tròn bằng hàm ROUND thông thường cho từng đại lý, tổng cộng các đại lý cộng lại sẽ bị thừa hoặc thiếu từ 1 đến 2 thùng so với kho thực tế.",
        expected_output="File `Bang_chia_qua_tang_POSM_Dai_Ly.xlsx` có bảng chia hàng chuẩn chỉnh, không bị lẻ kiện và khớp số lượng tồn kho.",
        wow_moment="Giải quyết bài toán làm tròn phân bổ (Rounding Allocation) không bị lệch tổng — nỗi ám ảnh kinh điển của Excel."
    )
    b34.create_excel("ton_kho_posm.xlsx", {
        "VatPham": {
            "headers": ["Vật Phẩm POSM", "Tổng Tồn Kho (Cái)", "Quy Cách (Cái/Thùng)"],
            "rows": [
                ["Áo Mưa Logo", 400, 20],   # = 20 thùng
                ["Mũ Bảo Hiểm", 250, 10],   # = 25 thùng
                ["Bình Giữ Nhiệt", 150, 15] # = 10 thùng
            ]
        },
        "DaiLy": {
            "headers": ["Mã Đại Lý", "Tên Đại Lý", "Khu Vực", "Doanh Thu Q3 (VNĐ)"],
            "rows": [
                ["DL01", "Đại lý Tiến Phát", "Hà Nội", 850000000],
                ["DL02", "Đại lý Hoàng Nam", "Hải Phòng", 450000000],
                ["DL03", "Đại lý Sao Mai", "Đà Nẵng", 300000000],
                ["DL04", "Đại lý Miền Nam", "TP.HCM", 900000000]
            ]
        }
    })
    # Reference output
    b34.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Bang_Chia_POSM": {
            "headers": ["Mã Đại Lý", "Tên Đại Lý", "Tỷ Trọng Doanh Số", "Áo Mưa (Thùng)", "Mũ Bảo Hiểm (Thùng)", "Bình Giữ Nhiệt (Thùng)"],
            "rows": [
                ["DL01", "Đại lý Tiến Phát", "34.0%", 7, 9, 3],
                ["DL02", "Đại lý Hoàng Nam", "18.0%", 4, 4, 2],
                ["DL03", "Đại lý Sao Mai", "12.0%", 2, 3, 2],
                ["DL04", "Đại lý Miền Nam", "36.0%", 7, 9, 3]
            ]
        }
    })

    # =========================================================================
    # EXERCISE 35: Tu dong tao Content Calendar va thu muc Google Drive
    # =========================================================================
    b35 = WorkspaceBuilder(DEPT, "35-tao-lich-content-folder-drive")
    b35.write_agents_md(
        role_title="Content Marketing Lead & Điều phối Asset",
        department_name="Phòng Marketing",
        constitution_items=[
            "Cấu trúc thư mục chuẩn: Cú pháp thư mục `[Mã bài] - [Ngày đăng] - [Chủ đề]`.",
            "Tự động điền link: Ghi ngược lại đường dẫn thư mục thiết kế vào file bảng tính Content Calendar."
        ]
    )
    b35.write_rule(
        rule_file_name="quy_chuan_content_calendar.md",
        description="Quy chuẩn lập lịch đăng bài và đặt tên thư mục chứa tài nguyên ảnh/video",
        globs="*.xlsx",
        rule_title="Quy Chuẩn Quản Lý Content Calendar & Drive Folder",
        guidelines=[
            "Chuẩn hóa mã bài viết dạng POST-XXXX.",
            "Tạo cột `Link Thư Mục Thiết Kế` trên bảng tính.",
            "Xuất ra file `Content_Calendar_T11_Updated.xlsx`."
        ]
    )
    b35.write_corporate_styling_rule()
    b35.write_security_hooks(["content_calendar.xlsx"])
    b35.write_skill(
        skill_name="tao-lich-content-folder",
        description="Use this skill to map out content calendars and structure corresponding Google Drive asset folder trees.",
        skill_title="Quy trình tạo lịch đăng bài và tổ chức thư mục",
        steps=[
            {"name": "Đọc lịch bài đăng", "desc": "Nạp file `content_calendar.xlsx`."},
            {"name": "Tổ chức thư mục", "desc": "Tạo các thư mục theo chuẩn quy ước ngày và chủ đề bài viết."},
            {"name": "Cập nhật đường dẫn", "desc": "Ghi đường dẫn thư mục vào bảng tính và lưu file `Content_Calendar_T11_Updated.xlsx`."}
        ]
    )
    b35.write_prompt_demo(
        problem_pain="Lên kế hoạch 30 bài đăng phải vào Google Drive tạo tay 30 folder con rồi copy link dán ngược lại vào file Excel rất tốn công.",
        interactive_hook="Nếu Designer cần tìm ảnh cho bài đăng ngày 12/11, cấu trúc tên folder thế nào sẽ giúp tìm ra ngay trong 3 giây mà không cần hỏi ai?",
        prompt_cmd="Đọc danh sách bài viết trong content_calendar.xlsx. Với mỗi bài, hãy tự động tạo thư mục con theo cú pháp [Mã bài] - [Ngày] - [Chủ đề] bên trong thư mục Assets_T11, sau đó điền đường link của từng thư mục vào cột 'Link Thư Mục Thiết Kế'. Xuất ra Content_Calendar_T11_Updated.xlsx.",
        prompt_pitfalls="Nếu trong chủ đề bài viết có chứa ký tự cấm của hệ điều hành như / : * ? < > |, script tạo folder sẽ bị crash nếu không được làm sạch tên trước.",
        expected_output="File `Content_Calendar_T11_Updated.xlsx` có đầy đủ link thư mục tương ứng được tạo sẵn sàng cho Designer bỏ ảnh vào.",
        wow_moment="Kết hợp hoàn hảo giữa Excel và Google Drive: thư mục tự sinh ra và link tự nhảy vào từng dòng bảng tính."
    )
    b35.create_excel("content_calendar.xlsx", {
        "Calendar": {
            "headers": ["Mã Bài", "Ngày Đăng", "Kênh", "Chủ Đề Bài Viết", "Người Phụ Trách", "Link Thư Mục Thiết Kế"],
            "rows": [
                ["POST-01", "2026-11-05", "Facebook", "Ra mắt bộ sưu tập Mùa Đông", "Lan Anh", ""],
                ["POST-02", "2026-11-08", "TikTok", "Hậu trường buổi chụp lookbook", "Tuấn Minh", ""],
                ["POST-03", "2026-11-12", "Instagram", "Mẹo phối màu áo len thanh lịch", "Lan Anh", ""]
            ]
        }
    })
    # Reference output
    b35.create_excel("_ket_qua_mau_chuan.xlsx", {
        "Content_Calendar_Updated": {
            "headers": ["Mã Bài", "Ngày Đăng", "Kênh", "Chủ Đề Bài Viết", "Người Phụ Trách", "Tên Thư Mục Drive", "Link Thư Mục Thiết Kế"],
            "rows": [
                ["POST-01", "2026-11-05", "Facebook", "Ra mắt bộ sưu tập Mùa Đông", "Lan Anh", "POST-01 - 2026-11-05 - Ra mat BST Mua Dong", "https://drive.google.com/drive/folders/1aBcDeFg_Sample01"],
                ["POST-02", "2026-11-08", "TikTok", "Hậu trường buổi chụp lookbook", "Tuấn Minh", "POST-02 - 2026-11-08 - Hau truong lookbook", "https://drive.google.com/drive/folders/1aBcDeFg_Sample02"],
                ["POST-03", "2026-11-12", "Instagram", "Mẹo phối màu áo len thanh lịch", "Lan Anh", "POST-03 - 2026-11-12 - Meo phoi mau ao len", "https://drive.google.com/drive/folders/1aBcDeFg_Sample03"]
            ]
        }
    })

    print(f"--> Successfully generated {DEPT} (8 exercises).")

if __name__ == "__main__":
    generate()
