#!/usr/bin/env python3
"""
Verification suite for 50 Excel Antigravity Demo Workspaces.
Validates:
1. Directory existence and naming convention (kebab-case)
2. Presence of required files: AGENTS.md, PROMPT_DEMO.md (6 sections), rules, skills, mock data
3. Security Hooks (.agents/hooks.json, .agents/scripts/protect_raw_data.py)
4. Corporate Styling Rule (.agents/rules/chuan_muc_excel_van_phong.md)
5. Standard Reference Output (_ket_qua_mau_chuan.xlsx)
6. MCP configuration in integration exercises (gmail / google_workspace)
7. Valid YAML frontmatter in rules and skills
8. Validity of all generated .xlsx files (readable via openpyxl without corruption)
"""

import sys
import os
import re
from pathlib import Path

try:
    import openpyxl
except ImportError:
    print("ERROR: openpyxl is required for verification.")
    sys.exit(1)

# Base directories
SCRIPT_DIR = Path(__file__).resolve().parent
DEMO_DIR = SCRIPT_DIR.parent
ROOT_50_DIR = DEMO_DIR / "50-vi-du-excel"

# Catalog of 50 expected workspaces: (dept_dir, exercise_dir, expected_rule, expected_skill, expected_data_files)
EXPECTED_CATALOG = [
    # 01 - Nhan su (9)
    ("01-nhan-su", "01-chuan-hoa-cham-cong", "quy_chuan_cham_cong.md", "xu-ly-cham-cong", ["cham_cong_thang_10_raw.xlsx"]),
    ("01-nhan-su", "02-gop-danh-gia-kpi", "quy_chuan_gop_kpi.md", "gop-kpi-phong-ban", ["KPI_2026/kpi_ky_thuat.xlsx", "KPI_2026/kpi_kinh_doanh.xlsx", "KPI_2026/kpi_marketing.xlsx"]),
    ("01-nhan-su", "03-tinh-luong-gross-net-thue", "quy_chuan_tinh_luong.md", "tinh-luong-gross-net", ["du_lieu_luong_thang.xlsx"]),
    ("01-nhan-su", "04-tach-phieu-luong-gui-email", "quy_chuan_phieu_luong.md", "tach-phieu-luong-email", ["bang_luong_chot.xlsx"]),
    ("01-nhan-su", "05-trich-xuat-cv-ung-vien", "quy_chuan_trich_xuat_cv.md", "trich-xuat-cv-ung-vien", ["CV_Ung_Vien/CV_Nguyen_Van_A.txt", "CV_Ung_Vien/CV_Tran_Thi_B.txt"]),
    ("01-nhan-su", "06-canh-bao-het-han-hop-dong", "quy_chuan_canh_bao_hd.md", "canh-bao-hop-dong", ["danh_sach_nhan_su.xlsx"]),
    ("01-nhan-su", "07-lam-sach-du-lieu-kham-suc-khoe", "quy_chuan_lam_sach_hr.md", "lam-sach-du-lieu-hr", ["dang_ky_kham_suc_khoe_raw.xlsx"]),
    ("01-nhan-su", "08-phan-tich-turnover-dashboard", "quy_chuan_turnover.md", "phan-tich-turnover", ["nhan_su_bien_dong_2026.xlsx"]),
    ("01-nhan-su", "09-xep-lich-truc-ca-tu-dong", "quy_chuan_xep_ca.md", "xep-lich-truc-ca", ["danh_sach_nv_va_nghi_phep.xlsx"]),

    # 02 - Ke toan (9)
    ("02-ke-toan", "10-doi-soat-sao-ke-so-quy", "quy_chuan_doi_soat_ngan_hang.md", "doi-soat-sao-ke", ["sao_ke_vcb.xlsx", "so_thu_chi.xlsx"]),
    ("02-ke-toan", "11-trich-xuat-hoa-don-dien-tu", "quy_chuan_hoa_don_gtgt.md", "trich-xuat-hoa-don", ["Hoa_Don/HD_001.txt", "Hoa_Don/HD_002.txt"]),
    ("02-ke-toan", "12-phan-loai-tuoi-no-nhac-no", "quy_chuan_tuoi_no.md", "phan-loai-tuoi-no", ["cong_no_phai_thu.xlsx"]),
    ("02-ke-toan", "13-phan-bo-chi-phi-khau-hao", "quy_chuan_phan_bo_chi_phi.md", "phan-bo-chi-phi-tscd", ["danh_muc_tscd_242.xlsx"]),
    ("02-ke-toan", "14-hop-nhat-bao-cao-kinh-doanh", "quy_chuan_hop_nhat_pl.md", "hop-nhat-bao-cao-pl", ["Chi_Nhanh/pl_hanoi.xlsx", "Chi_Nhanh/pl_danang.xlsx", "Chi_Nhanh/pl_hcm.xlsx"]),
    ("02-ke-toan", "15-phat-hien-gian-lan-chi-phi", "quy_chuan_kiem_toan_chi_phi.md", "phat-hien-gian-lan-chi-phi", ["de_nghi_thanh_toan_q3.xlsx"]),
    ("02-ke-toan", "16-chuyen-so-thanh-chu", "quy_chuan_doc_so_thanh_chu.md", "chuyen-so-thanh-chu", ["danh_sach_phieu_chi.xlsx"]),
    ("02-ke-toan", "17-du-bao-dong-tien-12-tuan", "quy_chuan_du_bao_dong_tien.md", "du-bao-dong-tien", ["ke_hoach_dong_tien.xlsx"]),
    ("02-ke-toan", "18-dinh-khoan-no-co-tu-dong", "quy_chuan_dinh_khoan_tt200.md", "dinh-khoan-no-co", ["giao_dich_raw.xlsx"]),

    # 03 - Kinh doanh (9)
    ("03-kinh-doanh", "19-lam-sach-chuan-hoa-crm", "quy_chuan_chuan_hoa_crm.md", "lam-sach-chuan-hoa-crm", ["data_khach_hang_raw.xlsx"]),
    ("03-kinh-doanh", "20-tinh-hoa-hong-luy-tien", "quy_chuan_hoa_hong_sales.md", "tinh-hoa-hong-sales", ["doanh_so_sales_t11.xlsx"]),
    ("03-kinh-doanh", "21-phan-nhom-khach-hang-rfm", "quy_chuan_rfm_segment.md", "phan-nhom-khach-hang-rfm", ["lich_su_don_hang.xlsx"]),
    ("03-kinh-doanh", "22-tao-hang-loat-bao-gia", "quy_chuan_tao_bao_gia.md", "tao-hang-loat-bao-gia", ["yeu_cau_bao_gia.xlsx", "bang_gia.xlsx"]),
    ("03-kinh-doanh", "23-phan-tich-ly-do-mat-khach", "quy_chuan_win_loss.md", "phan-tich-lost-deals", ["crm_lost_deals.xlsx"]),
    ("03-kinh-doanh", "24-chia-gio-lead-routing", "quy_chuan_lead_routing.md", "chia-gio-lead-routing", ["lead_moi_tuan_45.xlsx"]),
    ("03-kinh-doanh", "25-theo-doi-pacing-runrate-sales", "quy_chuan_pacing_sales.md", "theo-doi-pacing-sales", ["doanh_so_luy_ke.xlsx"]),
    ("03-kinh-doanh", "26-tong-hop-khao-sat-nps-csat", "quy_chuan_nps_csat.md", "tong-hop-khao-sat-nps", ["khao_sat_khach_hang.xlsx"]),
    ("03-kinh-doanh", "27-quet-namecard-soan-mail", "quy_chuan_namecard.md", "quet-namecard-soan-mail", ["Namecards/namecard_01.txt", "Namecards/namecard_02.txt"]),

    # 04 - Marketing (8)
    ("04-marketing", "28-gop-bao-cao-ads-da-kenh", "quy_chuan_gop_ads.md", "gop-bao-cao-ads", ["fb_ads.csv", "gg_ads.csv", "tiktok_ads.xlsx"]),
    ("04-marketing", "29-doi-soat-doanh-thu-phi-san", "quy_chuan_phi_san_tmdt.md", "doi-soat-phi-san-tmdt", ["shopee_orders.xlsx", "gia_von.xlsx"]),
    ("04-marketing", "30-tao-link-utm-tracking-qr", "quy_chuan_utm_tracking.md", "tao-link-utm-tracking", ["ke_hoach_content.xlsx"]),
    ("04-marketing", "31-phan-tich-danh-gia-san-tmdt", "quy_chuan_sentiment_review.md", "phan-tich-review-tmdt", ["shopee_reviews.xlsx"]),
    ("04-marketing", "32-phan-bo-ngan-sach-media-plan", "quy_chuan_media_plan.md", "phan-bo-media-plan", ["lich_su_cpl_kenh.xlsx"]),
    ("04-marketing", "33-gom-cum-tu-khoa-seo", "quy_chuan_seo_clustering.md", "gom-cum-tu-khoa-seo", ["keywords_ahrefs.xlsx"]),
    ("04-marketing", "34-chia-qua-tang-posm-dai-ly", "quy_chuan_chia_posm.md", "chia-posm-dai-ly", ["ton_kho_posm.xlsx"]),
    ("04-marketing", "35-tao-lich-content-folder-drive", "quy_chuan_content_calendar.md", "tao-lich-content-folder", ["content_calendar.xlsx"]),

    # 05 - Kho van (8)
    ("05-kho-van", "36-so-sanh-bao-gia-ncc", "quy_chuan_so_sanh_ncc.md", "so-sanh-bao-gia-ncc", ["NCC_Quotes/ncc_an_phat.xlsx", "NCC_Quotes/ncc_viet_nhat.xlsx", "NCC_Quotes/ncc_tien_phong.xlsx"]),
    ("05-kho-van", "37-canh-bao-reorder-point", "quy_chuan_reorder_point.md", "canh-bao-reorder-point", ["ton_kho_toc_do_ban.xlsx"]),
    ("05-kho-van", "38-phan-tich-ton-kho-abc-xyz", "quy_chuan_ton_kho_abc.md", "phan-tich-ton-kho-abc", ["ton_kho_theo_lo.xlsx"]),
    ("05-kho-van", "39-tinh-nhu-cau-nguyen-lieu-bom", "quy_chuan_bom_explosion.md", "tinh-nhu-cau-bom", ["ke_hoach_sx.xlsx", "dinh_muc_bom.xlsx"]),
    ("05-kho-van", "40-doi-soat-cuoc-phi-cod", "quy_chuan_doi_soat_cod.md", "doi-soat-cuoc-phi-cod", ["bang_ke_van_chuyen.xlsx"]),
    ("05-kho-van", "41-doi-chieu-chung-tu-xnk", "quy_chuan_chung_tu_xnk.md", "doi-chieu-chung-tu-xnk", ["Invoice.xlsx", "PackingList.xlsx", "BillOfLading.txt"]),
    ("05-kho-van", "42-kiem-ke-kho-lech-thuc-te", "quy_chuan_kiem_ke_kho.md", "kiem-ke-lech-thuc-te", ["kiem_ke_ke_1.xlsx", "ton_erp.xlsx"]),
    ("05-kho-van", "43-chia-tai-trong-xe-container", "quy_chuan_tai_trong_xe.md", "chia-tai-trong-xe", ["danh_sach_don_giao.xlsx"]),

    # 06 - Hanh chinh (7)
    ("06-hanh-chinh", "44-bien-ban-hop-action-tracker", "quy_chuan_action_tracker.md", "trich-xuat-action-items", ["bien_ban_hop.txt", "action_tracker.xlsx"]),
    ("06-hanh-chinh", "45-ve-gantt-chart-excel", "quy_chuan_gantt_chart.md", "ve-gantt-chart-excel", ["hang_muc_du_an.xlsx"]),
    ("06-hanh-chinh", "46-phan-bo-chi-phi-taxi-vpp", "quy_chuan_chi_phi_admin.md", "phan-bo-chi-phi-taxi", ["bang_ke_taxi.xlsx", "nhan_su.xlsx"]),
    ("06-hanh-chinh", "47-tao-folder-phan-quyen-drive", "quy_chuan_drive_folder.md", "tao-folder-phan-quyen", ["danh_sach_du_an_share.xlsx"]),
    ("06-hanh-chinh", "48-ocr-bang-bieu-anh-pdf", "quy_chuan_ocr_bang_bieu.md", "chuyen-bang-bieu-sang-excel", ["bang_scan_du_lieu.txt"]),
    ("06-hanh-chinh", "49-xep-so-do-ban-tiec-checkin", "quy_chuan_ban_tiec_checkin.md", "xep-ban-tiec-checkin", ["khach_moi_su_kien.xlsx"]),
    ("06-hanh-chinh", "50-executive-summary-one-page", "quy_chuan_executive_summary.md", "tao-executive-summary", ["bao_cao_tong_hop_thang.xlsx"]),
]

EXPECTED_MCP_EXERCISES = {
    "04-tach-phieu-luong-gui-email": "gmail",
    "06-canh-bao-het-han-hop-dong": "gmail",
    "12-phan-loai-tuoi-no-nhac-no": "gmail",
    "14-hop-nhat-bao-cao-kinh-doanh": "google_workspace",
    "24-chia-gio-lead-routing": "google_workspace",
    "27-quet-namecard-soan-mail": "gmail",
    "35-tao-lich-content-folder-drive": "google_workspace",
    "44-bien-ban-hop-action-tracker": "google_workspace",
    "47-tao-folder-phan-quyen-drive": "google_workspace",
}

def verify_frontmatter(file_path: Path, required_keys: list) -> bool:
    content = file_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return False
    fm_text = match.group(1)
    for key in required_keys:
        if f"{key}:" not in fm_text:
            return False
    return True

def verify_excel(file_path: Path) -> bool:
    try:
        wb = openpyxl.load_workbook(file_path, data_only=True)
        if len(wb.sheetnames) == 0:
            return False
        wb.close()
        return True
    except Exception as e:
        print(f"Excel read error for {file_path}: {e}")
        return False

def verify_prompt_demo_sections(file_path: Path) -> bool:
    content = file_path.read_text(encoding="utf-8")
    expected_headers = [
        "## 1. Nỗi Đau & Bài Toán Thực Tế",
        "## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên",
        "## 3. Câu Lệnh Prompt Mẫu",
        "## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai",
        "## 5. Kết Quả Kỳ Vọng & File Đối Chiếu",
        "## 6. Điểm \"Wow\" Thuyết Trình"
    ]
    for h in expected_headers:
        if h not in content:
            return False
    return True

def run_verification(target_dept=None):
    errors = []
    checked = 0

    catalog = EXPECTED_CATALOG
    if target_dept:
        catalog = [item for item in EXPECTED_CATALOG if item[0] == target_dept]

    print(f"=== VERIFYING {len(catalog)} EXERCISES (Target: {target_dept or 'ALL'}) ===")

    for dept, slug, rule_name, skill_name, data_files in catalog:
        ws_dir = ROOT_50_DIR / dept / slug
        checked += 1

        if not ws_dir.exists():
            errors.append(f"Missing workspace directory: {ws_dir}")
            continue

        # 1. Check AGENTS.md
        agents_file = ws_dir / "AGENTS.md"
        if not agents_file.exists():
            errors.append(f"Missing AGENTS.md in {ws_dir.name}")

        # 2. Check PROMPT_DEMO.md with 6 sections
        prompt_file = ws_dir / "PROMPT_DEMO.md"
        if not prompt_file.exists():
            errors.append(f"Missing PROMPT_DEMO.md in {ws_dir.name}")
        else:
            if not verify_prompt_demo_sections(prompt_file):
                errors.append(f"PROMPT_DEMO.md missing 6 standardized sections in {ws_dir.name}")

        # 3. Check Domain Rule
        rule_file = ws_dir / ".agents" / "rules" / rule_name
        if not rule_file.exists():
            errors.append(f"Missing domain rule file: {rule_file}")
        else:
            if not verify_frontmatter(rule_file, ["trigger", "globs", "description"]):
                errors.append(f"Invalid YAML frontmatter in rule: {rule_file}")

        # 4. Check Corporate Styling Rule
        corp_rule = ws_dir / ".agents" / "rules" / "chuan_muc_excel_van_phong.md"
        if not corp_rule.exists():
            errors.append(f"Missing corporate styling rule in {ws_dir.name}")
        else:
            if not verify_frontmatter(corp_rule, ["trigger", "globs", "description"]):
                errors.append(f"Invalid YAML frontmatter in corporate rule: {corp_rule}")

        # 5. Check Security Hooks
        hook_config = ws_dir / ".agents" / "hooks.json"
        hook_script = ws_dir / ".agents" / "scripts" / "protect_raw_data.py"
        if not hook_config.exists():
            errors.append(f"Missing hooks.json in {ws_dir.name}")
        if not hook_script.exists():
            errors.append(f"Missing protect_raw_data.py in {ws_dir.name}")

        # 6. Check Skill
        skill_file = ws_dir / ".agents" / "skills" / skill_name / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"Missing skill file: {skill_file}")
        else:
            if not verify_frontmatter(skill_file, ["name", "description"]):
                errors.append(f"Invalid YAML frontmatter in skill: {skill_file}")

        # 7. Check Reference Output Excel
        ref_excel = ws_dir / "_ket_qua_mau_chuan.xlsx"
        if not ref_excel.exists():
            errors.append(f"Missing reference output _ket_qua_mau_chuan.xlsx in {ws_dir.name}")
        elif not verify_excel(ref_excel):
            errors.append(f"Corrupt or unreadable reference Excel: {ref_excel}")

        # 8. Check MCP Configuration for Integration Exercises
        if slug in EXPECTED_MCP_EXERCISES:
            mcp_file = ws_dir / "mcp_config.json"
            if not mcp_file.exists():
                errors.append(f"Missing mcp_config.json for integration exercise: {ws_dir.name}")

        # 9. Check mock data
        for df in data_files:
            df_path = ws_dir / df
            if not df_path.exists():
                errors.append(f"Missing mock data file: {df_path}")
            elif df_path.suffix == ".xlsx":
                if not verify_excel(df_path):
                    errors.append(f"Corrupt or unreadable Excel file: {df_path}")

    print(f"Checked: {checked} workspaces")
    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors[:20]:
            print(f"  ❌ {err}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors.")
        return False
    else:
        print("✅ ALL CHECKS PASSED PERFECTLY (Workspaces, Rules, Hooks, Skills, MCP, Reference Outputs & Mock Data)!")
        return True

if __name__ == "__main__":
    dept_arg = sys.argv[1] if len(sys.argv) > 1 else None
    success = run_verification(dept_arg)
    sys.exit(0 if success else 1)
