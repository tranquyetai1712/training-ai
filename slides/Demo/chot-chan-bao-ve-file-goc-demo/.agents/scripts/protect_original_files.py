#!/usr/bin/env python3
"""Antigravity PreToolUse hook to block deleting files and overwriting original project files.

Allows creating new files and editing non-protected files while blocking:
- Any file/directory deletion operations (shell commands, Python/Node APIs, delete tools).
- Any write, overwrite, edit, rename, or move targeting protected original project files.
"""

from __future__ import annotations

import fnmatch
import json
import os
from pathlib import Path
import re
import shlex
import sys
from typing import Any

AGENTS_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = AGENTS_DIR.parent
CONFIG_PATH = AGENTS_DIR / "protected_files.json"

DEFAULT_PROTECTED_FILES = ("du_lieu_goc_khach_hang.xlsx",)
DEFAULT_PROTECTED_PATTERNS = (
    "du_lieu_goc_*",
    "*_goc.*",
    "*_goc_*",
    "goc_*",
    "*_tho.*",
    "*_tho_*",
    "*_raw.*",
    "raw_*",
    "*_original.*",
    "original_*",
)

DELETE_TOOLS = {"delete_file"}
WRITE_OR_EDIT_TOOLS = {
    "write_file",
    "edit_file",
    "write_to_file",
    "replace_file_content",
    "multi_replace_file_content",
}

DELETE_CMD_RE = re.compile(
    r"(?:^|[;&|\n\r`]|\s)"
    r"(?:del|erase|rm|rmdir|rd|unlink|remove-item|ri|clear-content|clc)\b"
    r"|\bgit\s+(?:rm|clean)\b"
    r"|\b(?:os\.(?:remove|unlink|rmdir|removedirs)|shutil\.rmtree)\s*\("
    r"|\.(?:unlink|rmdir)\s*\("
    r"|\bfs\.(?:unlink|rm|rmdir)(?:Sync)?\s*\(",
    re.IGNORECASE,
)

MOVE_RENAME_CMD_RE = re.compile(
    r"(?:^|[;&|\n\r`]|\s)(?:mv|move|move-item|mi|ren|rename|rename-item|rni)\b"
    r"|\b(?:shutil\.move|os\.(?:rename|replace))\s*\("
    r"|\.(?:rename|replace)\s*\("
    r"|\bfs\.rename(?:Sync)?\s*\(",
    re.IGNORECASE,
)

COPY_CMD_RE = re.compile(
    r"(?:^|[;&|\n\r`]|\s)(?:cp|copy|copy-item|cpi|xcopy|robocopy)\b"
    r"|\bshutil\.copy(?:2|file)?\s*\("
    r"|\bfs\.copyFile(?:Sync)?\s*\(",
    re.IGNORECASE,
)

INPLACE_EDIT_RE = re.compile(
    r"\binplace\s*=\s*true\b|\bsed\s+-i\b",
    re.IGNORECASE,
)

REDIR_TARGET_RE = re.compile(
    r"(?:>>?\s*|\b(?:out-file|set-content|add-content|tee-object|tee)\b"
    r"(?:\s+-(?:filepath|path|literalpath))?\s+)"
    r"(\"[^\"]+\"|'[^']+'|[^\s;&|]+)",
    re.IGNORECASE,
)

COPY_FUNC_RE = re.compile(
    r"\b(?:shutil\.copy(?:2|file)?|fs\.copyFile(?:Sync)?)\s*\(([^)]*)\)",
    re.IGNORECASE,
)

SAVE_CALL_RE = re.compile(
    r"(?:\.save|\.to_excel|\.to_csv|\.to_json|\.to_parquet|\.write_text|\.write_bytes|pd\.ExcelWriter)\s*\(([^)]*)\)",
    re.IGNORECASE,
)

OPEN_CALL_RE = re.compile(
    r"\bopen\s*\(([^)]*)\)",
    re.IGNORECASE,
)

SCRIPT_EXEC_RE = re.compile(
    r"\b(?:python3?|py|pwsh|powershell|node|bash|sh)\b(?:\s+-[a-zA-Z0-9_]+)*\s+([^\s;&|\"']+|\"[^\"]+\"|'[^']+')",
    re.IGNORECASE,
)


def _load_config() -> tuple[set[str], tuple[str, ...]]:
    files = {f.replace("\\", "/").lower() for f in DEFAULT_PROTECTED_FILES}
    patterns = list(DEFAULT_PROTECTED_PATTERNS)
    if CONFIG_PATH.is_file():
        try:
            data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            cfg_files = data.get("protectedFiles", [])
            cfg_patterns = data.get("protectedPatterns", [])
            if isinstance(cfg_files, list):
                files.update(str(f).replace("\\", "/").lstrip("./").lower() for f in cfg_files if f)
            if isinstance(cfg_patterns, list) and cfg_patterns:
                patterns = [str(p).lower() for p in cfg_patterns if p]
        except Exception:
            pass
    return files, tuple(patterns)


def _normalize_rel_path(raw_path: str, base_dir: Path) -> tuple[str, str]:
    cleaned = raw_path.strip().strip("\"'")
    normalized = cleaned.replace("\\", "/")
    basename = normalized.rsplit("/", 1)[-1].lower()
    try:
        candidate = Path(cleaned)
        if not candidate.is_absolute():
            candidate = base_dir / candidate
        resolved = candidate.resolve()
        rel = os.path.relpath(resolved, PROJECT_ROOT.resolve()).replace("\\", "/").lower()
    except Exception:
        rel = normalized.lstrip("./").lower()
    return rel, basename


def _is_protected_path(
    raw_path: str,
    base_dir: Path,
    protected_files: set[str],
    protected_patterns: tuple[str, ...],
) -> bool:
    if not raw_path:
        return False
    rel, basename = _normalize_rel_path(raw_path, base_dir)
    if rel in protected_files or basename in protected_files:
        return True
    for pat in protected_patterns:
        if fnmatch.fnmatch(basename, pat) or fnmatch.fnmatch(rel, pat):
            return True
    if rel == ".agents" or rel.startswith(".agents/"):
        return True
    return False


def _text_mentions_protected(
    text: str,
    protected_files: set[str],
    protected_patterns: tuple[str, ...],
) -> bool:
    lowered = text.lower().replace("\\", "/")
    for pf in protected_files:
        if pf in lowered or Path(pf).name in lowered:
            return True
    # Check common stems derived from patterns like du_lieu_goc_*, *_goc.*, *_tho.*
    tokens = re.findall(r"[a-z0-9_.\-/]+", lowered)
    for tok in tokens:
        base = tok.rsplit("/", 1)[-1]
        for pat in protected_patterns:
            if fnmatch.fnmatch(base, pat):
                return True
    return False


def _extract_target_path(tool_args: dict[str, Any]) -> str:
    for key in ("Path", "path", "TargetFile", "targetFile", "file_path", "filePath", "FilePath"):
        val = tool_args.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    return ""


def _deny(reason: str) -> dict[str, str]:
    return {"decision": "deny", "reason": reason}


def _check_save_and_open_calls(
    code: str,
    base_dir: Path,
    protected_files: set[str],
    protected_patterns: tuple[str, ...],
) -> str | None:
    mentions_protected = _text_mentions_protected(code, protected_files, protected_patterns)

    for match in SAVE_CALL_RE.finditer(code):
        arg_str = match.group(1).strip()
        first_arg = arg_str.split(",", 1)[0].strip()
        lit = re.match(r"^['\"]([^'\"]+)['\"]$", first_arg)
        if lit:
            if _is_protected_path(lit.group(1), base_dir, protected_files, protected_patterns):
                return f"Khong duoc phep ghi de len file goc duoc bao ve: {lit.group(1)}"
        elif mentions_protected:
            return "Phat hien lenh luu/ghi file co nguy co ghi de len file goc duoc bao ve."

    for match in OPEN_CALL_RE.finditer(code):
        arg_str = match.group(1)
        parts = [p.strip() for p in arg_str.split(",")]
        if not parts:
            continue
        first_arg = parts[0]
        mode_text = ",".join(parts[1:]).lower()
        is_write_mode = bool(re.search(r"['\"][wax+]|mode\s*=\s*['\"][wax+]", mode_text))
        if not is_write_mode:
            continue
        lit = re.match(r"^['\"]([^'\"]+)['\"]$", first_arg)
        if lit:
            if _is_protected_path(lit.group(1), base_dir, protected_files, protected_patterns):
                return f"Khong duoc phep mo ghi de len file goc duoc bao ve: {lit.group(1)}"
        elif mentions_protected:
            return "Phat hien lenh open() ghi file co nguy co ghi de len file goc duoc bao ve."

    return None


def _check_command_text(
    cmd: str,
    base_dir: Path,
    protected_files: set[str],
    protected_patterns: tuple[str, ...],
    depth: int = 0,
) -> str | None:
    if DELETE_CMD_RE.search(cmd):
        return (
            "Bi chan: Khong duoc phep xoa file trong du an. "
            "Chi duoc tao file moi va chinh sua file khong thuoc danh muc bao ve."
        )

    mentions_protected = _text_mentions_protected(cmd, protected_files, protected_patterns)

    if MOVE_RENAME_CMD_RE.search(cmd):
        if mentions_protected or "*" in cmd or "?" in cmd:
            return "Bi chan: Khong duoc phep di chuyen hoac doi ten file goc trong du an."

    if COPY_CMD_RE.search(cmd):
        # Check Python/Node copy(src, dst) calls explicitly.
        for c_match in COPY_FUNC_RE.finditer(cmd):
            args = [a.strip() for a in c_match.group(1).split(",")]
            if len(args) >= 2:
                dst_lit = re.match(r"^['\"]([^'\"]+)['\"]$", args[1])
                if dst_lit:
                    if _is_protected_path(dst_lit.group(1), base_dir, protected_files, protected_patterns):
                        return f"Bi chan: Khong duoc phep copy ghi de len file goc '{dst_lit.group(1)}'."
                elif mentions_protected:
                    return "Bi chan: Lenh copy co nguy co ghi de len file goc."
        # Allow shell copying FROM a protected file to a new destination, block copying ONTO a protected file.
        try:
            tokens = [t for t in shlex.split(cmd, posix=False) if not t.startswith(("-", "/"))]
        except Exception:
            tokens = cmd.split()
        dest = tokens[-1] if tokens else ""
        if dest and _is_protected_path(dest, base_dir, protected_files, protected_patterns):
            return f"Bi chan: Khong duoc phep copy ghi de len file goc '{dest}'."
        if mentions_protected and ("*" in cmd or "?" in cmd):
            return "Bi chan: Lenh copy chua ky tu dai dien co nguy co ghi de len file goc."

    for match in REDIR_TARGET_RE.finditer(cmd):
        target = match.group(1).strip("\"'")
        if target.lower() in {"$null", "nul", "/dev/null"} or target.startswith("&"):
            continue
        if _is_protected_path(target, base_dir, protected_files, protected_patterns):
            return f"Bi chan: Khong duoc phep ghi de len file goc '{target}'."

    if mentions_protected and INPLACE_EDIT_RE.search(cmd):
        return "Bi chan: Khong duoc phep sua truc tiep (in-place) len file goc."

    save_err = _check_save_and_open_calls(cmd, base_dir, protected_files, protected_patterns)
    if save_err:
        return f"Bi chan: {save_err}"

    # Inspect local script files invoked by the command (e.g. `python script.py`).
    if depth == 0:
        for match in SCRIPT_EXEC_RE.finditer(cmd):
            script_token = match.group(1).strip("\"'")
            script_path = Path(script_token)
            if not script_path.is_absolute():
                script_path = base_dir / script_path
            if script_path.is_file() and script_path.suffix.lower() in {".py", ".ps1", ".sh", ".js", ".bat", ".cmd"}:
                try:
                    script_content = script_path.read_text(encoding="utf-8", errors="replace")
                    nested_err = _check_command_text(
                        script_content, base_dir, protected_files, protected_patterns, depth=1
                    )
                    if nested_err:
                        return f"{nested_err} (trong script: {script_token})"
                except Exception:
                    pass

    return None


def main() -> None:
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
        tool_name = str(tool_call.get("name", "")).lower()
        tool_args = tool_call.get("args", {}) or {}
        cwd_raw = payload.get("cwd") or (payload.get("workspacePaths") or [None])[0]
        base_dir = Path(cwd_raw) if cwd_raw else PROJECT_ROOT

        protected_files, protected_patterns = _load_config()

        if tool_name in DELETE_TOOLS:
            print(
                json.dumps(
                    _deny("Bi chan: Khong duoc phep xoa file trong du an."),
                    ensure_ascii=True,
                )
            )
            return

        if tool_name in WRITE_OR_EDIT_TOOLS:
            target = _extract_target_path(tool_args)
            if _is_protected_path(target, base_dir, protected_files, protected_patterns):
                print(
                    json.dumps(
                        _deny(
                            f"Bi chan: '{target}' la file goc duoc bao ve. "
                            "Chi duoc phep tao file moi hoac chinh sua file khac."
                        ),
                        ensure_ascii=True,
                    )
                )
                return
            print(json.dumps({"decision": "allow"}))
            return

        if tool_name == "run_command":
            cmd = str(tool_args.get("CommandLine", ""))
            err = _check_command_text(cmd, base_dir, protected_files, protected_patterns)
            if err:
                print(json.dumps(_deny(err), ensure_ascii=True))
                return

        print(json.dumps({"decision": "allow"}))

    except Exception as exc:
        print(
            json.dumps(
                {
                    "decision": "ask",
                    "reason": f"Can xac nhan thu cong do loi kiem tra hook bao ve file goc: {exc}",
                },
                ensure_ascii=True,
            )
        )


if __name__ == "__main__":
    main()
