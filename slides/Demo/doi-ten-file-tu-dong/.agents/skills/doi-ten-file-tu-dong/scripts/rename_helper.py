import os
import sys
import json
import re
import argparse
from pathlib import Path

def sanitize_slug(text: str) -> str:
    """Chuyển đổi chuỗi tiếng Việt thành slug snake_case chuẩn."""
    vietnamese_map = {
        'à': 'a', 'á': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
        'ă': 'a', 'ằ': 'a', 'ắ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
        'â': 'a', 'ầ': 'a', 'ấ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
        'đ': 'd',
        'è': 'e', 'é': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
        'ê': 'e', 'ề': 'e', 'ế': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
        'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
        'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
        'ô': 'o', 'ồ': 'o', 'ố': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
        'ơ': 'o', 'ờ': 'o', 'ớ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
        'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
        'ư': 'u', 'ừ': 'u', 'ứ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
        'ỳ': 'y', 'ý': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
    }
    
    text = text.lower()
    for char, replacement in vietnamese_map.items():
        text = text.replace(char, replacement)
        
    text = re.sub(r'[^a-z0-9_]', '_', text)
    text = re.sub(r'_+', '_', text)
    return text.strip('_')

def extract_file_content_snippet(file_path: Path, max_length: int = 1000) -> str:
    """Trích xuất đoạn văn bản xem trước từ file để phục vụ phân tích."""
    ext = file_path.suffix.lower()
    
    if ext in ['.txt', '.md', '.json', '.csv', '.py', '.js', '.ts', '.html', '.css', '.xml', '.yaml', '.yml', '.ini', '.conf', '.sh', '.bat', '.ps1']:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read(max_length)
        except Exception as e:
            return f"[Không đọc được file văn bản: {str(e)}]"
            
    elif ext in ['.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp']:
        return f"[Tệp hình ảnh {ext.upper()} - Cần dùng AI vision phân tích trực quan]"
        
    elif ext == '.pdf':
        try:
            import pypdf
            reader = pypdf.PdfReader(str(file_path))
            text = ""
            for page in reader.pages[:2]:
                text += page.extract_text() or ""
            return text[:max_length] if text else "[PDF không chứa text hoặc là ảnh scan]"
        except Exception:
            return "[Tệp PDF - Cần trích xuất văn bản hoặc xem trực tiếp]"
            
    elif ext == '.docx':
        try:
            import docx
            doc = docx.Document(str(file_path))
            full_text = [p.text for p in doc.paragraphs if p.text]
            return "\n".join(full_text)[:max_length]
        except Exception:
            return "[Tệp Word DOCX - Cần trích xuất văn bản]"
            
    return f"[Tệp {ext.upper()} - Cần phân tích theo định dạng]"

def get_unique_path(target_path: Path) -> Path:
    """Tạo đường dẫn mới tránh bị trùng lặp tên file đã tồn tại."""
    if not target_path.exists():
        return target_path
    
    parent = target_path.parent
    stem = target_path.stem
    ext = target_path.suffix
    
    counter = 1
    while True:
        new_path = parent / f"{stem}_{counter}{ext}"
        if not new_path.exists():
            return new_path
        counter += 1

def main():
    parser = argparse.ArgumentParser(description="Helper đổi tên file tự động dựa trên nội dung.")
    parser.add_argument("--path", type=str, required=True, help="Đường dẫn thư mục hoặc file cần đổi tên")
    parser.add_argument("--execute", action="store_true", help="Thực thi đổi tên thật")
    parser.add_argument("--rename-mapping", type=str, help="Chuỗi JSON mapping đổi tên {old_name: new_name}")

    args = parser.parse_args()
    target_path = Path(args.path).resolve()

    if not target_path.exists():
        print(json.dumps({"error": f"Đường dẫn '{target_path}' không tồn tại."}))
        sys.exit(1)

    if args.execute and args.rename_mapping:
        mapping = json.loads(args.rename_mapping)
        results = []
        for old_name, new_name in mapping.items():
            old_file = target_path / old_name if target_path.is_dir() else target_path
            ext = old_file.suffix
            
            # Đảm bảo phần mở rộng chuẩn
            if not new_name.lower().endswith(ext.lower()):
                new_name = new_name + ext
                
            clean_stem = sanitize_slug(Path(new_name).stem)
            new_file_name = f"{clean_stem}{ext}"
            
            desired_path = old_file.parent / new_file_name
            final_path = get_unique_path(desired_path)
            
            try:
                old_file.rename(final_path)
                results.append({
                    "old": old_file.name,
                    "new": final_path.name,
                    "status": "success"
                })
            except Exception as e:
                results.append({
                    "old": old_file.name,
                    "new": final_path.name,
                    "status": "error",
                    "error": str(e)
                })
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    # Mặc định: Scan danh sách file và trích xuất thông tin
    files_info = []
    files_to_scan = [target_path] if target_path.is_file() else list(target_path.iterdir())
    
    for f in files_to_scan:
        if f.is_file():
            snippet = extract_file_content_snippet(f)
            files_info.append({
                "filename": f.name,
                "extension": f.suffix,
                "size_bytes": f.stat().st_size,
                "content_snippet": snippet
            })

    print(json.dumps(files_info, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
