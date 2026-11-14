"""
Core Workspace Builder for Antigravity Excel Demos.
Handles consistent generation of:
- AGENTS.md (Constitutional level 1)
- .agents/rules/*.md (Level 2 business constraints + Corporate Excel Styling)
- .agents/skills/*/SKILL.md (Level 3 procedural workflow)
- .agents/hooks.json + .agents/scripts/protect_raw_data.py (Level 4 Hard Security Guard)
- mcp_config.json (Model Context Protocol configs for cross-app exercises)
- PROMPT_DEMO.md (6-part Instructor guide & interactive lecture script)
- _ket_qua_mau_chuan.xlsx (Reference expected output workbook)
"""

import os
import json
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

SCRIPT_DIR = Path(__file__).resolve().parent
DEMO_DIR = SCRIPT_DIR.parent
ROOT_50_DIR = DEMO_DIR / "50-vi-du-excel"

class WorkspaceBuilder:
    def __init__(self, dept_code: str, exercise_slug: str):
        self.dept_code = dept_code
        self.exercise_slug = exercise_slug
        self.ws_dir = ROOT_50_DIR / dept_code / exercise_slug
        self.agents_dir = self.ws_dir / ".agents"
        self.rules_dir = self.agents_dir / "rules"
        self.skills_dir = self.agents_dir / "skills"
        self.scripts_dir = self.agents_dir / "scripts"
        
        # Ensure directories exist
        self.ws_dir.mkdir(parents=True, exist_ok=True)
        self.rules_dir.mkdir(parents=True, exist_ok=True)
        self.scripts_dir.mkdir(parents=True, exist_ok=True)

    def write_agents_md(self, role_title: str, department_name: str, constitution_items: list):
        items_text = "\n".join([f"{i+1}. {item}" for i, item in enumerate(constitution_items)])
        content = f"""# BẢN HIẾN PHÁP DỰ ÁN: {role_title.upper()}
Bạn là {role_title} trực thuộc {department_name}. Khi vận hành trong thư mục này, bạn BẮT BUỘC tuân thủ các nguyên tắc tối cao:

1. TÔNG GIỌNG & NGÔN NGỮ: Giao tiếp 100% bằng tiếng Việt, chuẩn mực, lịch sự, chuyên nghiệp và đi thẳng vào giải pháp nghiệp vụ.
2. AN TOÀN DỮ LIỆU TUYỆT ĐỐI: Không bao giờ được phép xóa hoặc ghi đè làm mất dữ liệu gốc. Mọi kết quả xử lý phải được xuất ra file mới (ví dụ: `..._ket_qua.xlsx` hoặc `..._chuan_hoa.xlsx`).
{items_text}
"""
        (self.ws_dir / "AGENTS.md").write_text(content.strip() + "\n", encoding="utf-8")

    def write_rule(self, rule_file_name: str, description: str, globs: str, rule_title: str, guidelines: list):
        guidelines_text = "\n".join([f"{i+1}. {g}" for i, g in enumerate(guidelines)])
        content = f"""---
trigger: glob
globs: "{globs}"
description: "{description}"
---

# {rule_title.upper()}
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

{guidelines_text}
"""
        (self.rules_dir / rule_file_name).write_text(content.strip() + "\n", encoding="utf-8")

    def write_corporate_styling_rule(self):
        """Writes the dedicated corporate Excel styling and live formula rule."""
        content = """---
trigger: glob
globs: "*.xlsx, *.csv"
description: "Quy chuẩn thẩm mỹ, màu sắc, định dạng số và công thức sống cho bảng tính Excel văn phòng"
---

# QUY CHUẨN THẨM MỸ & CÔNG THỨC EXCEL CHUẨN VĂN PHÒNG
Khi tạo bất kỳ tệp tin bảng tính Excel (.xlsx) nào trong thư mục này, bạn BẮT BUỘC tuân thủ các tiêu chuẩn sau:

1. ĐỊNH DẠNG TIÊU ĐỀ (HEADER STYLING):
   - Font chữ đồng bộ: Arial hoặc Segoe UI, cỡ chữ 11pt, in đậm (Bold).
   - Màu nền tiêu đề (Header Fill): Màu xanh navy chuyên nghiệp `#1F497D`.
   - Màu chữ tiêu đề: Màu trắng `#FFFFFF`, căn giữa (Center Alignment) cả chiều ngang lẫn chiều dọc.

2. ĐỊNH DẠNG DỮ LIỆU SỐ & NGÀY THÁNG:
   - Số tiền tệ: Định dạng phân cách hàng nghìn `#,##0` (ví dụ: `15,000,000 VNĐ`), căn phải (Right Alignment).
   - Tỷ lệ phần trăm: Định dạng có 1 chữ số thập phân `0.0%` (ví dụ: `12.5%`).
   - Ngày tháng: Bắt buộc chuẩn hóa định dạng `DD/MM/YYYY` (ví dụ: `15/10/2026`).

3. TỰ ĐỘNG CĂN CHỈNH ĐỘ RỘNG CỘT (AUTO-FIT COLUMNS):
   - Bắt buộc tính toán độ rộng cột tự động dựa trên độ dài chuỗi dài nhất trong cột cộng thêm 4 ký tự đệm (padding), tuyệt đối không để xảy ra lỗi hiển thị `###` do cột quá hẹp.

4. CÔNG THỨC SỐNG (ACTIVE LIVE FORMULAS):
   - Luôn ưu tiên chèn công thức Excel sống (hàm `SUM`, `AVERAGE`, `IF`, `VLOOKUP`, `XLOOKUP`, `ROUND`) vào các ô tổng cộng hoặc tính toán, TUYỆT ĐỐI KHÔNG dán cứng giá trị tĩnh (Hardcoded static numbers) để bảng tính có tính tương tác cao khi người dùng kiểm tra.
"""
        (self.rules_dir / "chuan_muc_excel_van_phong.md").write_text(content.strip() + "\n", encoding="utf-8")

    def write_skill(self, skill_name: str, description: str, skill_title: str, steps: list):
        target_skill_dir = self.skills_dir / skill_name
        target_skill_dir.mkdir(parents=True, exist_ok=True)
        
        steps_text = ""
        for i, s in enumerate(steps):
            steps_text += f"\n## Bước {i+1}: {s['name']}\n{s['desc']}\n"

        content = f"""---
name: {skill_name}
description: "{description}"
---

# {skill_title.upper()}

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:
{steps_text}
"""
        (target_skill_dir / "SKILL.md").write_text(content.strip() + "\n", encoding="utf-8")

    def write_security_hooks(self, protected_filenames: list):
        """Sets up PreToolUse Hook to hard-block tampering with raw/source files."""
        # 1. Write hooks.json
        hooks_config = {
            "protect-raw-data": {
                "PreToolUse": [
                    {
                        "matcher": "run_command|write_to_file|replace_file_content",
                        "hooks": [
                            {
                                "type": "command",
                                "command": "python3 .agents/scripts/protect_raw_data.py",
                                "timeout": 10
                            }
                        ]
                    }
                ]
            }
        }
        (self.agents_dir / "hooks.json").write_text(json.dumps(hooks_config, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        # 2. Write protect_raw_data.py
        protected_list_repr = repr(protected_filenames)
        hook_script = f"""#!/usr/bin/env python3
import sys
import json

def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input.strip():
            print(json.dumps({{"decision": "allow"}}))
            return

        payload = json.loads(raw_input)
        payload_str = json.dumps(payload).lower()

        # Danh muc tep tin du lieu goc duoc bao ve nghiem ngat
        protected_files = [f.lower() for f in {protected_list_repr}] + ["_raw.", "goc_", "raw_"]
        dangerous_ops = ["write_to_file", "replace_file_content", "rm ", "unlink", "delete", "truncate"]

        # Kiem tra xem payload co nham vao tep tin du lieu goc hay khong
        targets_protected = any(pf in payload_str for pf in protected_files)
        is_dangerous_op = any(op in payload_str for op in dangerous_ops)

        if targets_protected and is_dangerous_op:
            response = {{
                "decision": "deny",
                "reason": "⛔ [CẢNH BÁO AN NINH ANTIGRAVITY]: Tệp tin dữ liệu gốc thuộc danh mục được bảo vệ nghiêm ngặt. Lệnh can thiệp/ghi đè/xóa đã bị chặn cứng! Bạn BẮT BUỘC phải xuất kết quả phân tích sang một tệp tin mới (ví dụ: ..._chuan_hoa.xlsx hoặc ..._ket_qua.xlsx)."
            }}
            print(json.dumps(response, ensure_ascii=False))
            return

        print(json.dumps({{"decision": "allow"}}))

    except Exception:
        print(json.dumps({{"decision": "allow"}}))

if __name__ == "__main__":
    main()
"""
        (self.scripts_dir / "protect_raw_data.py").write_text(hook_script.strip() + "\n", encoding="utf-8")

    def write_mcp_config(self, mcp_type: str = "gmail"):
        """Generates ready-to-use mcp_config.json for cross-app integration."""
        if mcp_type == "gmail":
            cfg = {
                "mcpServers": {
                    "gmail": {
                        "command": "npx",
                        "args": ["-y", "@gongrzhe/server-gmail-autoauth-mcp"],
                        "env": {
                            "GOOGLE_CLIENT_ID": "YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com",
                            "GOOGLE_CLIENT_SECRET": "YOUR_GOOGLE_CLIENT_SECRET",
                            "CREDENTIALS_PATH": "~/.gemini/config/mcp/google-oauth-credentials.json",
                            "GMAIL_TOKEN_PATH": "~/.gemini/config/mcp/gmail-token.json"
                        }
                    }
                }
            }
        elif mcp_type == "google_workspace":
            cfg = {
                "mcpServers": {
                    "google_workspace": {
                        "command": "npx",
                        "args": ["-y", "@google-workspace/mcp-server"],
                        "env": {
                            "WORKSPACE_AUTH_TYPE": "oauth2",
                            "SCOPES": "https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/spreadsheets,https://www.googleapis.com/auth/calendar"
                        }
                    }
                }
            }
        else:
            cfg = {"mcpServers": {}}

        (self.ws_dir / "mcp_config.json").write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def write_prompt_demo(self, problem_pain: str, interactive_hook: str, prompt_cmd: str, prompt_pitfalls: str, expected_output: str, wow_moment: str):
        content = f"""# CẨM NANG HƯỚNG DẪN DEMO: {self.exercise_slug.upper()}

## 1. Nỗi Đau & Bài Toán Thực Tế
{problem_pain}

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "{interactive_hook}"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
{prompt_cmd}
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> {prompt_pitfalls}

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** {expected_output}

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> {wow_moment}
"""
        (self.ws_dir / "PROMPT_DEMO.md").write_text(content.strip() + "\n", encoding="utf-8")

    def write_text_file(self, relative_path: str, content: str):
        target = self.ws_dir / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content.strip() + "\n", encoding="utf-8")

    def create_excel(self, relative_path: str, sheets_data: dict):
        wb = openpyxl.Workbook()
        wb.remove(wb.active)

        header_font = Font(name="Arial", size=11, bold=True, color="FFFFFF")
        header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
        border = Border(
            left=Side(style='thin', color='D9D9D9'),
            right=Side(style='thin', color='D9D9D9'),
            top=Side(style='thin', color='D9D9D9'),
            bottom=Side(style='thin', color='D9D9D9')
        )

        for sheet_name, data in sheets_data.items():
            ws = wb.create_sheet(title=sheet_name)
            headers = data.get("headers", [])
            rows = data.get("rows", [])

            # Write headers
            if headers:
                ws.append(headers)
                for col_idx in range(1, len(headers) + 1):
                    cell = ws.cell(row=1, column=col_idx)
                    cell.font = header_font
                    cell.fill = header_fill
                    cell.alignment = Alignment(horizontal="center", vertical="center")
                    cell.border = border

            # Write data rows
            for row in rows:
                ws.append(row)
                for col_idx in range(1, len(row) + 1):
                    cell = ws.cell(row=ws.max_row, column=col_idx)
                    cell.border = border
                    # Align numbers right, text left
                    if isinstance(cell.value, (int, float)):
                        cell.alignment = Alignment(horizontal="right", vertical="center")
                        if cell.value > 1000:
                            cell.number_format = "#,##0"

            # Auto fit column widths
            for col in ws.columns:
                max_len = max(len(str(cell.value or '')) for cell in col)
                col_letter = openpyxl.utils.get_column_letter(col[0].column)
                ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

        target = self.ws_dir / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        wb.save(target)
        wb.close()
