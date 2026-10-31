#!/usr/bin/env python3
import sys
import json

def main():
    try:
        # Read payload from stdin
        raw_input = sys.stdin.read()
        if not raw_input.strip():
            print(json.dumps({"decision": "allow"}))
            return

        payload = json.loads(raw_input)
        payload_str = json.dumps(payload).lower()

        # Sensitive keywords and modification patterns
        protected_patterns = ["du_lieu_goc_", "goc_"]
        dangerous_actions = ["write_to_file", "replace_file_content", "del ", "rm ", "remove", "unlink"]

        # Check if any protected file pattern is being targeted
        is_targeting_protected = any(pat in payload_str for pat in protected_patterns)

        if is_targeting_protected:
            # Hard block dangerous file tampering
            response = {
                "decision": "deny",
                "reason": "⛔ [CẢNH BÁO AN NINH]: Tệp tin 'du_lieu_goc_khach_hang.xlsx' thuộc danh mục dữ liệu gốc được bảo vệ nghiêm ngặt. Lệnh can thiệp trực tiếp đã bị hủy bỏ!"
            }
            print(json.dumps(response))
            return

        # Otherwise allow execution
        print(json.dumps({"decision": "allow"}))

    except Exception:
        # On any parsing failure, fallback safely to ask
        print(json.dumps({"decision": "ask", "reason": "Yêu cầu xác nhận từ người dùng do không phân tích được payload an ninh."}))

if __name__ == "__main__":
    main()
