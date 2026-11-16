#!/usr/bin/env python3
import json
import re
import sys

PROTECTED_PATTERNS = ("du_lieu_goc_", "goc_")
WRITE_TOOLS = {"write_file", "edit_file", "write_to_file", "replace_file_content"}
DESTRUCTIVE_CMD_RE = re.compile(
    r"(?:"
    r"\b(?:del|erase|rm|remove|remove-item|ri|unlink|rmdir|rd|move|move-item|mv|ren|rename|rename-item|clear-content|clc)\b"
    r"|shutil\.move|os\.(?:remove|unlink|replace|rename)"
    r"|inplace\s*=\s*true"
    r"|(?:>>?|out-file|set-content|add-content)\b"
    r"|open\s*\([^)]*['\"][wax+]"
    r")"
)
SAVE_CALL_RE = re.compile(r"(?:\.save|\.to_excel|\.to_csv)\s*\(([^)]*)\)")


def _targets_protected(text: str) -> bool:
    return any(pat in text for pat in PROTECTED_PATTERNS)


def _has_unsafe_save(cmd: str) -> bool:
    matches = SAVE_CALL_RE.findall(cmd)
    if not matches:
        return False
    for arg_str in matches:
        # Allow saving only when the first argument is an explicit non-protected string literal.
        first_arg = arg_str.split(",", 1)[0].strip()
        literal_match = re.match(r"^['\"]([^'\"]+)['\"]$", first_arg)
        if not literal_match or _targets_protected(literal_match.group(1)):
            return True
    return False


def main():
    try:
        if hasattr(sys.stdin, "reconfigure"):
            sys.stdin.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")

        raw_input = sys.stdin.read()
        if not raw_input.strip():
            print(json.dumps({"decision": "allow"}))
            return

        payload = json.loads(raw_input)
        tool_call = payload.get("toolCall", {})
        tool_name = tool_call.get("name", "").lower()
        tool_args = tool_call.get("args", {})
        tool_args_str = json.dumps(tool_args, ensure_ascii=False).lower()

        if _targets_protected(tool_args_str):
            is_write_tool = tool_name in WRITE_TOOLS
            cmd = str(tool_args.get("CommandLine", "")).lower()
            is_dangerous_cmd = (
                tool_name == "run_command"
                and (bool(DESTRUCTIVE_CMD_RE.search(cmd)) or _has_unsafe_save(cmd))
            )

            if is_write_tool or is_dangerous_cmd:
                response = {
                    "decision": "deny",
                    "reason": (
                        "⛔ [CẢNH BÁO AN NINH]: THAO TÁC BỊ CHẶN ĐỨNG! "
                        "Tệp tin 'du_lieu_goc_khach_hang.xlsx' thuộc danh mục dữ liệu gốc được bảo vệ nghiêm ngặt. "
                        "Lệnh can thiệp trực tiếp đã bị hủy bỏ!"
                    ),
                }
                print(json.dumps(response))
                return

        print(json.dumps({"decision": "allow"}))

    except Exception:
        print(json.dumps({
            "decision": "ask",
            "reason": "Yêu cầu xác nhận từ người dùng do không phân tích được payload an ninh.",
        }))


if __name__ == "__main__":
    main()
