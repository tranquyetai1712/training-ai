#!/usr/bin/env python3
"""
organize_files.py - Tự động phân loại và dọn dẹp file theo nội dung & phần mở rộng.
Hỗ trợ:
- Cross-platform path resolution
- Chống ghi đè trùng lặp (Collision prevention)
- Ghi log và hoàn tác (Undo / Rollback)
- Lọc bỏ file rác, file hệ thống và file tạm
"""

import os
import sys
import shutil
import argparse
import json
import re
from pathlib import Path
from datetime import datetime

# Đảm bảo mã hóa UTF-8 trên Windows console/stdout/stderr
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

CATEGORIES = {
    "KeToan_TaiChinh": ["hoa don", "invoice", "vat", "sao ke", "bank", "thu", "chi", "thue", "chiet khau", "thanh toan"],
    "NhanSu_TuyenDung": ["cv", "curriculum vitae", "resume", "ung vien", "cham cong", "luong", "hop dong lao dong", "tuyen dung"],
    "HocTap_NghienCuu": ["giao trinh", "luan van", "bai giang", "slide", "ebook", "lecture", "assignment", "de thi", "nghien cuu"],
    "CongViec_DuAn": ["bao gia", "de xuat", "proposal", "bien ban", "hop dong", "spec", "yeu cau", "project"],
    "Media_GiaiTri": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".mp4", ".mkv", ".avi", ".mov", ".mp3", ".wav", ".flac"],
    "PhanMem_CaiDat": [".exe", ".deb", ".dmg", ".msi", ".iso", ".sh", ".apk", ".pkg", ".appimage"]
}

IGNORED_FILE_PATTERNS = [
    r'^\..*',              # File ẩn (e.g. .DS_Store, .git, .organize_history_*)
    r'^\~.*',              # File tạm/lock của MS Office và trình soạn thảo (e.g. ~$Doc.docx, ~temp)
    r'^thumbs\.db$',       # File cache thumbnail Windows
    r'^desktop\.ini$',     # File cấu hình desktop Windows
    r'.*\.crdownload$',    # File đang tải dở của Chrome
    r'.*\.part$',          # File đang tải dở của Firefox
    r'.*\.tmp$',           # File tạm thời
]

def format_file_size(size_bytes: int) -> str:
    """Chuyển đổi kích thước byte thành định dạng dễ đọc (KB, MB, GB)."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

def is_ignored_file(filename: str) -> bool:
    """Kiểm tra xem file có thuộc danh sách bỏ qua (file rác, file hệ thống) không."""
    fn_lower = filename.lower()
    for pattern in IGNORED_FILE_PATTERNS:
        if re.search(pattern, fn_lower):
            return True
    return False

def get_unique_path(target_path: Path) -> tuple[Path, bool]:
    """
    Tạo đường dẫn mới tránh ghi đè nếu file đích đã tồn tại.
    Trả về (unique_path, was_collision).
    """
    if not target_path.exists():
        return target_path, False

    parent = target_path.parent
    stem = target_path.stem
    suffix = target_path.suffix

    counter = 1
    while True:
        new_path = parent / f"{stem}_{counter}{suffix}"
        if not new_path.exists():
            return new_path, True
        counter += 1

def extract_text_sample(file_path: Path, max_bytes: int = 2000) -> str:
    """Trích xuất đoạn văn bản mẫu từ các file text/code để hỗ trợ phân loại."""
    ext = file_path.suffix.lower()
    if ext in [".txt", ".csv", ".json", ".md", ".log", ".yaml", ".yml", ".xml", ".html", ".js", ".ts", ".py"]:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read(max_bytes)
        except Exception:
            return ""
    return ""

def classify_file(file_path: Path) -> tuple[str, str]:
    """Phân loại file dựa trên phần mở rộng, tên file và nội dung mẫu."""
    filename_lower = file_path.name.lower()
    ext = file_path.suffix.lower()

    if ext in CATEGORIES["Media_GiaiTri"]:
        return "Media_GiaiTri", f"Định dạng Media/Giải trí ({ext})"
    if ext in CATEGORIES["PhanMem_CaiDat"]:
        return "PhanMem_CaiDat", f"Định dạng Bộ cài/Phần mềm ({ext})"

    content = filename_lower + " " + extract_text_sample(file_path).lower()

    for category, keywords in CATEGORIES.items():
        if category in ["Media_GiaiTri", "PhanMem_CaiDat"]:
            continue
        for kw in keywords:
            if kw.isalpha() and len(kw) <= 4:
                pattern = r'\b' + re.escape(kw) + r'\b'
                if re.search(pattern, content):
                    readable_type = category.replace("_", " ")
                    return category, f"Phát hiện từ khóa '{kw}' ({readable_type})"
            elif kw in content:
                readable_type = category.replace("_", " ")
                return category, f"Phát hiện từ khóa '{kw}' ({readable_type})"

    return "TepTinKhac", "File không xác định danh mục cụ thể hoặc không đọc được nội dung"

def run_organizer(source_dir: str, dest_dir: str, dry_run: bool = True) -> dict:
    source_path = Path(source_dir).expanduser().resolve()
    dest_path = Path(dest_dir).expanduser().resolve()

    if not source_path.exists() or not source_path.is_dir():
        print(json.dumps({"error": f"Thư mục nguồn '{source_path}' không tồn tại hoặc không phải là thư mục."}, ensure_ascii=False))
        sys.exit(1)

    results = []
    moves_history = []
    
    # Lấy danh sách file và sắp xếp theo tên
    all_entries = sorted(list(source_path.iterdir()), key=lambda p: p.name.lower())
    files = [f for f in all_entries if f.is_file() and not is_ignored_file(f.name)]

    for idx, f in enumerate(files, start=1):
        cat, reason = classify_file(f)
        target_dir = dest_path / cat
        desired_file = target_dir / f.name
        
        # Kiểm tra chống ghi đè
        final_target_file, was_collision = get_unique_path(desired_file)

        file_stat = f.stat()
        file_size_bytes = file_stat.st_size
        file_size_human = format_file_size(file_size_bytes)

        item = {
            "stt": idx,
            "filename": f.name,
            "size_bytes": file_size_bytes,
            "size": file_size_human,
            "category": cat,
            "reason": reason,
            "source": str(f),
            "dest": str(final_target_file),
            "is_collision": was_collision
        }
        if was_collision:
            item["resolved_filename"] = final_target_file.name

        results.append(item)

        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(f), str(final_target_file))
            moves_history.append({
                "source": str(f),
                "dest": str(final_target_file)
            })

    output_data = {
        "mode": "dry-run" if dry_run else "execute",
        "total": len(results),
        "source": str(source_path),
        "dest": str(dest_path),
        "items": results
    }

    if not dry_run and moves_history:
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        history_file = dest_path / f".organize_history_{timestamp_str}.json"
        history_payload = {
            "timestamp": datetime.now().isoformat(),
            "source_dir": str(source_path),
            "dest_dir": str(dest_path),
            "total_moved": len(moves_history),
            "moves": moves_history
        }
        try:
            with open(history_file, "w", encoding="utf-8") as hf:
                json.dump(history_payload, hf, ensure_ascii=False, indent=2)
            output_data["history_file"] = str(history_file)
        except Exception as e:
            output_data["history_error"] = f"Không thể lưu history log: {str(e)}"

    return output_data

def run_undo(history_path_str: str) -> dict:
    """Hoàn tác việc di chuyển file theo file log history."""
    history_file = Path(history_path_str).expanduser().resolve()
    if not history_file.exists():
        print(json.dumps({"error": f"Tệp lịch sử '{history_file}' không tồn tại."}, ensure_ascii=False))
        sys.exit(1)

    try:
        with open(history_file, "r", encoding="utf-8") as f:
            history_data = json.load(f)
    except Exception as e:
        print(json.dumps({"error": f"Không đọc được tệp lịch sử: {str(e)}"}, ensure_ascii=False))
        sys.exit(1)

    moves = history_data.get("moves", [])
    restored = []
    errors = []

    for item in moves:
        src = Path(item["source"])
        dest = Path(item["dest"])

        if not dest.exists():
            errors.append({
                "file": str(dest),
                "error": "Tệp tin tại vị trí mới không còn tồn tại, không thể hoàn tác."
            })
            continue

        src.parent.mkdir(parents=True, exist_ok=True)
        # Nếu vị trí gốc đã có file trùng tên, đảm bảo an toàn bằng get_unique_path
        safe_src, _ = get_unique_path(src)
        try:
            shutil.move(str(dest), str(safe_src))
            restored.append({
                "from": str(dest),
                "to": str(safe_src)
            })
        except Exception as e:
            errors.append({
                "file": str(dest),
                "error": str(e)
            })

    # Đổi tên file history thành .undone để đánh dấu đã hoàn tác
    undone_file = history_file.with_name(history_file.name + ".undone")
    try:
        history_file.rename(undone_file)
    except Exception:
        pass

    return {
        "mode": "undo",
        "total_attempted": len(moves),
        "total_restored": len(restored),
        "errors_count": len(errors),
        "restored": restored,
        "errors": errors,
        "undone_log": str(undone_file) if undone_file.exists() else str(history_file)
    }

def main():
    parser = argparse.ArgumentParser(description="Tự động phân loại, di chuyển file an toàn và hỗ trợ hoàn tác.")
    parser.add_argument("--source", help="Thư mục nguồn cần dọn dẹp")
    parser.add_argument("--dest", help="Thư mục đích lưu trữ theo danh mục")
    parser.add_argument("--dry-run", action="store_true", help="Chế độ kiểm tra xem trước (không di chuyển thật)")
    parser.add_argument("--execute", action="store_true", help="Thực thi di chuyển file")
    parser.add_argument("--undo", help="Đường dẫn file lịch sử .organize_history_*.json để hoàn tác")

    args = parser.parse_args()

    if args.undo:
        results = run_undo(args.undo)
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    if not args.source or not args.dest:
        print(json.dumps({"error": "Cần truyền --source và --dest (hoặc --undo <file_history>)."}, ensure_ascii=False))
        sys.exit(1)

    dry_run = not args.execute
    results = run_organizer(args.source, args.dest, dry_run=dry_run)
    print(json.dumps(results, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
