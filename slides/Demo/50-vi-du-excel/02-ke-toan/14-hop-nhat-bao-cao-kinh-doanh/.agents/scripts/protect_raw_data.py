#!/usr/bin/env python3
import sys
import json

def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input.strip():
            print(json.dumps({"decision": "allow"}))
            return

        payload = json.loads(raw_input)
        payload_str = json.dumps(payload).lower()

        # Danh muc tep tin du lieu goc duoc bao ve nghiem ngat
        protected_files = [f.lower() for f in ['Chi_Nhanh/pl_hanoi.xlsx', 'Chi_Nhanh/pl_danang.xlsx', 'Chi_Nhanh/pl_hcm.xlsx']] + ["_raw.", "goc_", "raw_"]
        dangerous_ops = ["write_to_file", "replace_file_content", "rm ", "unlink", "delete", "truncate"]

        # Kiem tra xem payload co nham vao tep tin du lieu goc hay khong
        targets_protected = any(pf in payload_str for pf in protected_files)
        is_dangerous_op = any(op in payload_str for op in dangerous_ops)

        if targets_protected and is_dangerous_op:
            response = {
                "decision": "deny",
                "reason": "⛔ [CẢNH BÁO AN NINH ANTIGRAVITY]: Tệp tin dữ liệu gốc thuộc danh mục được bảo vệ nghiêm ngặt. Lệnh can thiệp/ghi đè/xóa đã bị chặn cứng! Bạn BẮT BUỘC phải xuất kết quả phân tích sang một tệp tin mới (ví dụ: ..._chuan_hoa.xlsx hoặc ..._ket_qua.xlsx)."
            }
            print(json.dumps(response, ensure_ascii=False))
            return

        print(json.dumps({"decision": "allow"}))

    except Exception:
        print(json.dumps({"decision": "allow"}))

if __name__ == "__main__":
    main()
