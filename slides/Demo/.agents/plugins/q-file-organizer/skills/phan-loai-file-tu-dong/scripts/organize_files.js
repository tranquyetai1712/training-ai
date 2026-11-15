const fs = require('fs');
const path = require('path');

const CATEGORIES = {
    "KeToan_TaiChinh": ["hoa don", "invoice", "vat", "sao ke", "bank", "thu", "chi", "thue", "chiet khau", "thanh toan"],
    "NhanSu_TuyenDung": ["cv", "curriculum vitae", "resume", "ung vien", "cham cong", "luong", "hop dong lao dong", "tuyen dung"],
    "HocTap_NghienCuu": ["giao trinh", "luan van", "bai giang", "slide", "ebook", "lecture", "assignment", "de thi", "nghien cuu"],
    "CongViec_DuAn": ["bao gia", "de xuat", "proposal", "bien ban", "hop dong", "spec", "yeu cau", "project"],
    "Media_GiaiTri": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".mp4", ".mkv", ".avi", ".mov", ".mp3", ".wav", ".flac"],
    "PhanMem_CaiDat": [".exe", ".deb", ".dmg", ".msi", ".iso", ".sh", ".apk", ".pkg", ".appimage"]
};

const IGNORED_FILE_PATTERNS = [
    /^\..*/,              // File ẩn (e.g. .DS_Store, .git, .organize_history_*)
    /^~.*/,               // File tạm/lock của MS Office và trình soạn thảo (e.g. ~$Doc.docx)
    /^thumbs\.db$/i,      // File cache thumbnail Windows
    /^desktop\.ini$/i,    // File cấu hình desktop Windows
    /.*\.crdownload$/i,   // File đang tải dở Chrome
    /.*\.part$/i,         // File đang tải dở Firefox
    /.*\.tmp$/i           // File tạm thời
];

function formatFileSize(bytes) {
    if (bytes < 1024) return `${bytes} B`;
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
    if (bytes < 1024 * 1024 * 1024) return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
    return `${(bytes / (1024 * 1024 * 1024)).toFixed(2)} GB`;
}

function isIgnoredFile(filename) {
    return IGNORED_FILE_PATTERNS.some(pattern => pattern.test(filename));
}

function getUniquePath(targetPath) {
    if (!fs.existsSync(targetPath)) {
        return { uniquePath: targetPath, wasCollision: false };
    }

    const dir = path.dirname(targetPath);
    const ext = path.extname(targetPath);
    const stem = path.basename(targetPath, ext);

    let counter = 1;
    while (true) {
        const candidate = path.join(dir, `${stem}_${counter}${ext}`);
        if (!fs.existsSync(candidate)) {
            return { uniquePath: candidate, wasCollision: true };
        }
        counter++;
    }
}

function extractTextSample(filePath) {
    const ext = path.extname(filePath).toLowerCase();
    if ([".txt", ".csv", ".json", ".md", ".log", ".yaml", ".yml", ".xml", ".html", ".js", ".ts", ".py"].includes(ext)) {
        try {
            const fd = fs.openSync(filePath, 'r');
            const buffer = Buffer.alloc(2000);
            const bytesRead = fs.readSync(fd, buffer, 0, 2000, 0);
            fs.closeSync(fd);
            return buffer.toString('utf-8', 0, bytesRead);
        } catch (e) {
            return "";
        }
    }
    return "";
}

function isAlpha(str) {
    return /^[a-zA-Z]+$/.test(str);
}

function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function classifyFile(filePath) {
    const fileName = path.basename(filePath);
    const filenameLower = fileName.toLowerCase();
    const ext = path.extname(filePath).toLowerCase();

    if (CATEGORIES["Media_GiaiTri"].includes(ext)) {
        return { category: "Media_GiaiTri", reason: `Định dạng Media/Giải trí (${ext})` };
    }
    if (CATEGORIES["PhanMem_CaiDat"].includes(ext)) {
        return { category: "PhanMem_CaiDat", reason: `Định dạng Bộ cài/Phần mềm (${ext})` };
    }

    const sample = extractTextSample(filePath).toLowerCase();
    const content = filenameLower + " " + sample;

    const textCategories = ["KeToan_TaiChinh", "NhanSu_TuyenDung", "HocTap_NghienCuu", "CongViec_DuAn"];
    for (const cat of textCategories) {
        const keywords = CATEGORIES[cat];
        for (const kw of keywords) {
            if (isAlpha(kw) && kw.length <= 4) {
                const regex = new RegExp(`\\b${escapeRegExp(kw)}\\b`, 'i');
                if (regex.test(content)) {
                    const readableType = cat.replace(/_/g, ' ');
                    return { category: cat, reason: `Phát hiện từ khóa '${kw}' (${readableType})` };
                }
            } else if (content.includes(kw)) {
                const readableType = cat.replace(/_/g, ' ');
                return { category: cat, reason: `Phát hiện từ khóa '${kw}' (${readableType})` };
            }
        }
    }

    return { category: "TepTinKhac", reason: "File không xác định danh mục cụ thể hoặc không đọc được nội dung" };
}

function runOrganizer(sourceDir, destDir, dryRun = true) {
    const sourcePath = path.resolve(sourceDir);
    const destPath = path.resolve(destDir);

    if (!fs.existsSync(sourcePath) || !fs.statSync(sourcePath).isDirectory()) {
        console.error(JSON.stringify({ error: `Thư mục nguồn '${sourcePath}' không tồn tại hoặc không phải là thư mục.` }));
        process.exit(1);
    }

    const entries = fs.readdirSync(sourcePath, { withFileTypes: true });
    const files = entries
        .filter(e => e.isFile() && !isIgnoredFile(e.name))
        .map(e => path.join(sourcePath, e.name))
        .sort((a, b) => path.basename(a).localeCompare(path.basename(b)));

    const results = [];
    const movesHistory = [];
    let idx = 1;

    for (const f of files) {
        const fileName = path.basename(f);
        const { category, reason } = classifyFile(f);
        const targetDir = path.join(destPath, category);
        const desiredFile = path.join(targetDir, fileName);

        const { uniquePath: finalTargetFile, wasCollision } = getUniquePath(desiredFile);

        const stat = fs.statSync(f);
        const sizeBytes = stat.size;
        const sizeHuman = formatFileSize(sizeBytes);

        const item = {
            stt: idx++,
            filename: fileName,
            size_bytes: sizeBytes,
            size: sizeHuman,
            category: category,
            reason: reason,
            source: f,
            dest: finalTargetFile,
            is_collision: wasCollision
        };
        if (wasCollision) {
            item.resolved_filename = path.basename(finalTargetFile);
        }

        results.push(item);

        if (!dryRun) {
            if (!fs.existsSync(targetDir)) {
                fs.mkdirSync(targetDir, { recursive: true });
            }
            try {
                fs.renameSync(f, finalTargetFile);
            } catch (err) {
                if (err.code === 'EXDEV') {
                    fs.copyFileSync(f, finalTargetFile);
                    fs.unlinkSync(f);
                } else {
                    throw err;
                }
            }
            movesHistory.push({
                source: f,
                dest: finalTargetFile
            });
        }
    }

    const outputData = {
        mode: dryRun ? "dry-run" : "execute",
        total: results.length,
        source: sourcePath,
        dest: destPath,
        items: results
    };

    if (!dryRun && movesHistory.length > 0) {
        const now = new Date();
        const pad = (n) => String(n).padStart(2, '0');
        const timestampStr = `${now.getFullYear()}${pad(now.getMonth() + 1)}${pad(now.getDate())}_${pad(now.getHours())}${pad(now.getMinutes())}${pad(now.getSeconds())}`;
        const historyFile = path.join(destPath, `.organize_history_${timestampStr}.json`);

        const historyPayload = {
            timestamp: now.toISOString(),
            source_dir: sourcePath,
            dest_dir: destPath,
            total_moved: movesHistory.length,
            moves: movesHistory
        };

        try {
            fs.writeFileSync(historyFile, JSON.stringify(historyPayload, null, 2), 'utf-8');
            outputData.history_file = historyFile;
        } catch (e) {
            outputData.history_error = `Không thể lưu history log: ${e.message}`;
        }
    }

    return outputData;
}

function runUndo(historyPathStr) {
    const historyFile = path.resolve(historyPathStr);
    if (!fs.existsSync(historyFile)) {
        console.error(JSON.stringify({ error: `Tệp lịch sử '${historyFile}' không tồn tại.` }));
        process.exit(1);
    }

    let historyData;
    try {
        historyData = JSON.parse(fs.readFileSync(historyFile, 'utf-8'));
    } catch (e) {
        console.error(JSON.stringify({ error: `Không đọc được tệp lịch sử: ${e.message}` }));
        process.exit(1);
    }

    const moves = historyData.moves || [];
    const restored = [];
    const errors = [];

    for (const item of moves) {
        const src = path.resolve(item.source);
        const dest = path.resolve(item.dest);

        if (!fs.existsSync(dest)) {
            errors.push({
                file: dest,
                error: "Tệp tin tại vị trí mới không còn tồn tại, không thể hoàn tác."
            });
            continue;
        }

        const srcDir = path.dirname(src);
        if (!fs.existsSync(srcDir)) {
            fs.mkdirSync(srcDir, { recursive: true });
        }

        const { uniquePath: safeSrc } = getUniquePath(src);
        try {
            try {
                fs.renameSync(dest, safeSrc);
            } catch (err) {
                if (err.code === 'EXDEV') {
                    fs.copyFileSync(dest, safeSrc);
                    fs.unlinkSync(dest);
                } else {
                    throw err;
                }
            }
            restored.push({
                from: dest,
                to: safeSrc
            });
        } catch (e) {
            errors.push({
                file: dest,
                error: e.message
            });
        }
    }

    const undoneFile = historyFile + ".undone";
    try {
        fs.renameSync(historyFile, undoneFile);
    } catch (e) {}

    return {
        mode: "undo",
        total_attempted: moves.length,
        total_restored: restored.length,
        errors_count: errors.length,
        restored: restored,
        errors: errors,
        undone_log: fs.existsSync(undoneFile) ? undoneFile : historyFile
    };
}

function main() {
    const args = process.argv.slice(2);
    let source = '';
    let dest = '';
    let execute = false;
    let undoPath = '';

    for (let i = 0; i < args.length; i++) {
        if (args[i] === '--source' && i + 1 < args.length) {
            source = args[++i];
        } else if (args[i] === '--dest' && i + 1 < args.length) {
            dest = args[++i];
        } else if (args[i] === '--execute') {
            execute = true;
        } else if (args[i] === '--dry-run') {
            execute = false;
        } else if (args[i] === '--undo' && i + 1 < args.length) {
            undoPath = args[++i];
        }
    }

    if (undoPath) {
        const undoResults = runUndo(undoPath);
        console.log(JSON.stringify(undoResults, null, 2));
        return;
    }

    if (!source || !dest) {
        console.error(JSON.stringify({ error: "Cần truyền --source và --dest (hoặc --undo <file_history>)." }));
        process.exit(1);
    }

    const dryRun = !execute;
    const results = runOrganizer(source, dest, dryRun);
    console.log(JSON.stringify(results, null, 2));
}

main();
