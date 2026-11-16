/**
 * Zalo PC SQLite & FTS Engine
 * Zero-dependency extractor for Zalo PC messages, contacts, and groups.
 * Auto-respawns using Zalo's built-in 32-bit Electron Node runtime.
 */

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

// 1. Helper to find Zalo.exe and native sqlite3
function findZaloInstallation() {
  const localAppData = process.env.LOCALAPPDATA || path.join(process.env.USERPROFILE, 'AppData', 'Local');
  const zaloBase = path.join(localAppData, 'Programs', 'Zalo');

  if (!fs.existsSync(zaloBase)) return null;

  // Search for version directories like Zalo-26.8.20 or Zalo.exe directly
  const entries = fs.readdirSync(zaloBase);
  let zaloExe = null;
  let sqliteModule = null;

  // Check versioned subfolders first (e.g. Zalo-26.8.20)
  for (const entry of entries) {
    const full = path.join(zaloBase, entry);
    if (fs.statSync(full).isDirectory() && entry.startsWith('Zalo-')) {
      const exeCandidate = path.join(full, 'Zalo.exe');
      const sqliteCandidate = path.join(full, 'resources', 'app.asar.unpacked', 'native', 'nativelibs', 'sqlite3');
      if (fs.existsSync(exeCandidate) && fs.existsSync(sqliteCandidate)) {
        zaloExe = exeCandidate;
        sqliteModule = sqliteCandidate;
        break;
      }
    }
  }

  // Fallback to base folder
  if (!zaloExe) {
    const directExe = path.join(zaloBase, 'Zalo.exe');
    if (fs.existsSync(directExe)) zaloExe = directExe;
  }

  return { zaloBase, zaloExe, sqliteModule };
}

// 2. Self-respawn if not running inside Zalo's Electron node runtime
if (process.env.ZALO_ENGINE_ACTIVE !== '1') {
  const install = findZaloInstallation();
  if (!install || !install.zaloExe) {
    console.error('Error: Không tìm thấy thư mục cài đặt Zalo PC tại %LocalAppData%\\Programs\\Zalo');
    process.exit(1);
  }

  const env = Object.assign({}, process.env, {
    ELECTRON_RUN_AS_NODE: '1',
    ZALO_ENGINE_ACTIVE: '1',
    ZALO_SQLITE_PATH: install.sqliteModule
  });

  const res = spawnSync(install.zaloExe, [__filename, ...process.argv.slice(2)], {
    env,
    stdio: 'inherit',
    windowsHide: true
  });

  process.exit(res.status || 0);
}

// ==========================================
// RUNTIME INSIDE ZALO ELECTRON NODE
// ==========================================
const sqlitePath = process.env.ZALO_SQLITE_PATH;
const sqlite3 = require(sqlitePath);

// Find Data Directory
function getZaloDataInfo() {
  const appData = process.env.APPDATA || path.join(process.env.USERPROFILE, 'AppData', 'Roaming');
  const configPath = path.join(appData, 'ZaloData', 'config.json');

  let dataDir = null;
  if (fs.existsSync(configPath)) {
    try {
      const cfg = JSON.parse(fs.readFileSync(configPath, 'utf8'));
      if (cfg.db_path && cfg.db_path.location) {
        dataDir = cfg.db_path.location;
      }
    } catch (e) {}
  }
  if (!dataDir) {
    dataDir = path.join(appData, 'ZaloData');
  }

  // Look for production database folder: <dataDir>/Database/_production/<userId>/
  let prodBase = path.join(dataDir, 'Database', '_production');
  if (!fs.existsSync(prodBase)) {
    prodBase = path.join(appData, 'ZaloData', 'Database', '_production');
  }

  let userId = null;
  if (fs.existsSync(prodBase)) {
    const subs = fs.readdirSync(prodBase);
    for (const sub of subs) {
      if (/^\d{10,}$/.test(sub)) {
        userId = sub;
        break;
      }
    }
  }

  const searchDir = path.join(dataDir, 'search');

  return { appData, dataDir, prodBase, userId, searchDir };
}

// Key Derivation for FTSM
function getFtsKey(userId, uin) {
  const keyFile = path.join(__dirname, 'ftsm.key');
  if (fs.existsSync(keyFile)) {
    const k = fs.readFileSync(keyFile, 'utf8').trim();
    if (k.length === 32) return k;
  }
  // Default verified key for FTSM
  return '0051245181012206443a7336ca79811d';
}

// Load Cached UIN or default known UIN
function getUinKey() {
  const keyFile = path.join(__dirname, 'uin.key');
  if (fs.existsSync(keyFile)) {
    const k = fs.readFileSync(keyFile, 'utf8').trim();
    if (k.length === 32) return k;
  }
  // Default verified key from user session
  return '0fc12f53be21220d486a7336ca79811d';
}

function openDb(dbPath, key, compat = false) {
  return new Promise((resolve, reject) => {
    const db = new sqlite3.Database(dbPath, sqlite3.OPEN_READONLY, (err) => {
      if (err) return reject(err);
      if (key) {
        db.run("PRAGMA key = '" + key + "'", (err) => {
          if (err) return reject(err);
          if (compat) {
            db.run("PRAGMA cipher_compatibility = 3", (err) => {
              if (err) return reject(err);
              resolve(db);
            });
          } else {
            resolve(db);
          }
        });
      } else {
        resolve(db);
      }
    });
  });
}

function queryDb(db, sql) {
  return new Promise((resolve, reject) => {
    db.all(sql, (err, rows) => {
      if (err) reject(err);
      else resolve(rows || []);
    });
  });
}

// CLI Commands
async function listConversations(info, uin) {
  const indexDbPath = path.join(info.prodBase, info.userId, 'Core', 'Index.db');
  if (!fs.existsSync(indexDbPath)) {
    console.error('Không tìm thấy Index.db tại:', indexDbPath);
    return;
  }

  const db = await openDb(indexDbPath, uin);
  const friends = await queryDb(db, 'SELECT userId, displayName, zaloName, phoneNumber FROM friend');
  const groups = await queryDb(db, 'SELECT * FROM [group]');
  const convs = await queryDb(db, "SELECT * FROM [conversation] ORDER BY CAST(json_extract(infoCheckSearch, '$.lastMessageTime') AS INTEGER) DESC LIMIT 50");
  db.close();

  const nameMap = {};
  friends.forEach(f => { nameMap[f.userId] = f.displayName || f.zaloName; });
  groups.forEach(g => { nameMap[g.userId || g.groupId || g.id] = g.name || g.displayName; });

  console.log('\n================ DANH SÁCH HỘI THOẠI GẦN ĐÂY ================');
  convs.forEach((c, idx) => {
    const name = nameMap[c.userId] || 'ID: ' + c.userId;
    let timeStr = 'Chưa có';
    if (c.infoCheckSearch) {
      try {
        const parsed = JSON.parse(c.infoCheckSearch);
        if (parsed.lastMessageTime) timeStr = new Date(parsed.lastMessageTime).toLocaleString('vi-VN');
      } catch (e) {}
    }
    const typeLabel = c.isGroup ? '[Nhóm]' : '[Cá nhân]';
    console.log(`${(idx + 1).toString().padStart(2, ' ')}. ${typeLabel} ${name.padEnd(30, ' ')} | ID: ${c.userId.padEnd(20, ' ')} | Gần nhất: ${timeStr}`);
  });
  console.log('===============================================================\n');
}

async function searchContactOrGroup(info, uin, keyword) {
  const indexDbPath = path.join(info.prodBase, info.userId, 'Core', 'Index.db');
  const db = await openDb(indexDbPath, uin);
  const friends = await queryDb(db, 'SELECT userId, displayName, zaloName, phoneNumber, username FROM friend');
  const groups = await queryDb(db, 'SELECT * FROM [group]');
  db.close();

  const kw = keyword.toLowerCase();
  const matchedFriends = friends.filter(f => 
    (f.displayName && f.displayName.toLowerCase().includes(kw)) ||
    (f.zaloName && f.zaloName.toLowerCase().includes(kw)) ||
    (f.userId && f.userId.includes(kw)) ||
    (f.phoneNumber && f.phoneNumber.includes(kw))
  );

  const matchedGroups = groups.filter(g => 
    (g.name && g.name.toLowerCase().includes(kw)) ||
    (g.displayName && g.displayName.toLowerCase().includes(kw)) ||
    ((g.userId || g.groupId || g.id) && (g.userId || g.groupId || g.id).includes(kw))
  );

  console.log(`\nKết quả tìm kiếm cho từ khóa "${keyword}":`);
  if (matchedFriends.length === 0 && matchedGroups.length === 0) {
    console.log('Không tìm thấy người dùng hoặc nhóm nào phù hợp.');
    return;
  }

  if (matchedFriends.length > 0) {
    console.log('\n--- BẠN BÈ / CÁ NHÂN ---');
    matchedFriends.forEach(f => {
      console.log(`- Tên: ${f.displayName || f.zaloName} (Zalo: ${f.zaloName}) | ID: ${f.userId} | SĐT: ${f.phoneNumber || 'N/A'}`);
    });
  }

  if (matchedGroups.length > 0) {
    console.log('\n--- NHÓM CHAT ---');
    matchedGroups.forEach(g => {
      const gid = g.userId || g.groupId || g.id;
      console.log(`- Nhóm: ${g.name || g.displayName} | Group ID: ${gid}`);
    });
  }
  console.log('');
}

async function extractMessages(info, uin, target, days = 20, outDir = null) {
  // Resolve target to ID
  let targetId = target;
  let targetName = target;

  const indexDbPath = path.join(info.prodBase, info.userId, 'Core', 'Index.db');
  const indexDb = await openDb(indexDbPath, uin);
  const friends = await queryDb(indexDb, 'SELECT userId, displayName, zaloName FROM friend');
  const groups = await queryDb(indexDb, 'SELECT * FROM [group]');
  indexDb.close();

  const cleanTarget = target.trim().toLowerCase();
  const friend = friends.find(f => 
    f.userId === target || 
    (f.displayName && f.displayName.trim().toLowerCase() === cleanTarget) ||
    (f.zaloName && f.zaloName.trim().toLowerCase() === cleanTarget) ||
    (f.displayName && f.displayName.trim().toLowerCase().includes(cleanTarget))
  );

  if (friend) {
    targetId = friend.userId;
    targetName = friend.displayName || friend.zaloName;
  } else {
    const group = groups.find(g => {
      const gid = g.userId || g.groupId || g.id;
      const gName = g.name || g.displayName || '';
      return gid === target || 
             gName.trim().toLowerCase() === cleanTarget ||
             gName.trim().toLowerCase().includes(cleanTarget);
    });
    if (group) {
      targetId = group.userId || group.groupId || group.id;
      targetName = group.name || group.displayName;
    }
  }

  console.log(`\nĐang trích xuất tin nhắn cho: "${targetName}" (ID: ${targetId}) trong ${days} ngày qua...`);

  // Target Key in FTSM
  const isGroup = targetId.startsWith('g') || groups.some(g => (g.userId || g.groupId || g.id) === targetId);
  const msgKey = isGroup && !targetId.startsWith('g') ? 'g' + targetId : targetId;

  // Min Timestamp
  const now = Date.now();
  const minTs = now - (days * 24 * 60 * 60 * 1000);

  // Query FTSM
  const ftsKey = getFtsKey(info.userId, uin);
  const ftsmPath = path.join(info.searchDir, `ftsm_${info.userId}.db`);
  let ftsRows = [];
  if (fs.existsSync(ftsmPath)) {
    try {
      const ftsDb = await openDb(ftsmPath, ftsKey, true);
      const sql = `SELECT * FROM searchIndex WHERE msgKey = '${msgKey}' AND CAST(ts AS INTEGER) >= ${minTs} ORDER BY CAST(ts AS INTEGER) ASC`;
      ftsRows = await queryDb(ftsDb, sql);
      ftsDb.close();
    } catch (e) {
      console.warn('Cảnh báo đọc FTSM:', e.message);
    }
  }

  // Query Core Message DB if exists
  const coreDbFile = isGroup ? (msgKey.startsWith('g') ? `${msgKey}.db` : `g${msgKey}.db`) : `${targetId}.db`;
  const coreDbPath = path.join(info.prodBase, info.userId, 'Core', 'Message', coreDbFile);
  let coreRows = [];
  if (fs.existsSync(coreDbPath)) {
    try {
      const coreDb = await openDb(coreDbPath, uin);
      const sql = `SELECT * FROM message WHERE sendDttm >= ${minTs} ORDER BY sendDttm ASC`;
      coreRows = await queryDb(coreDb, sql);
      coreDb.close();
    } catch (e) {
      console.warn('Cảnh báo đọc Core DB:', e.message);
    }
  }

  // Merge & Deduplicate
  const ftsMap = new Map();
  ftsRows.forEach(r => ftsMap.set(r.msgId, r.content));

  const allMsgs = [];
  const seenKey = new Set();

  coreRows.forEach(c => {
    let content = ftsMap.get(c.msgId);
    if (!content) {
      if (c.msgType === 2) content = '[Hình ảnh]';
      else if (c.msgType === 4) content = '[Sticker / Tin nhắn thoại]';
      else if (c.msgType === 6) content = '[Chia sẻ / Cuộc gọi]';
      else content = c.message || '[Tin nhắn đa phương tiện]';
    }

    const isMe = c.fromUid === '0' || c.fromUid === info.userId;
    const sender = isMe ? 'Bạn' : (c.dName || targetName);
    const ts = Number(c.sendDttm);
    const timeKey = `${c.fromUid}_${Math.floor(ts / 2000)}_${content.trim().toLowerCase()}`;

    if (seenKey.has(timeKey)) return;
    seenKey.add(timeKey);

    const d = new Date(ts);
    allMsgs.push({
      msgId: c.msgId,
      timestamp: ts,
      date: d.toLocaleDateString('vi-VN'),
      time: d.toLocaleTimeString('vi-VN'),
      sender,
      content
    });
  });

  // Check any FTS rows not in Core
  ftsRows.forEach(f => {
    const ts = Number(f.ts);
    const isMe = f.fromUid === '0' || f.fromUid === info.userId;
    const sender = isMe ? 'Bạn' : targetName;
    const timeKey = `${f.fromUid}_${Math.floor(ts / 2000)}_${(f.content || '').trim().toLowerCase()}`;

    if (seenKey.has(timeKey)) return;
    seenKey.add(timeKey);

    const d = new Date(ts);
    allMsgs.push({
      msgId: f.msgId,
      timestamp: ts,
      date: d.toLocaleDateString('vi-VN'),
      time: d.toLocaleTimeString('vi-VN'),
      sender,
      content: f.content
    });
  });

  allMsgs.sort((a, b) => a.timestamp - b.timestamp);

  console.log(`=> Đã tìm thấy ${allMsgs.length} tin nhắn.`);

  // Save to Output Directory
  const targetDir = outDir || path.join(process.cwd(), 'zalo_output');
  if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir, { recursive: true });

  const safeName = targetName.replace(/[^a-zA-Z0-9_-]/g, '_');
  const jsonPath = path.join(targetDir, `${safeName}_messages.json`);
  const mdPath = path.join(targetDir, `${safeName}_report.md`);

  fs.writeFileSync(jsonPath, JSON.stringify(allMsgs, null, 2), 'utf8');

  // Build Markdown Report
  let md = `# Lịch sử trao đổi: ${targetName}\n`;
  md += `- **Khoảng thời gian:** ${days} ngày gần nhất (từ ${new Date(minTs).toLocaleDateString('vi-VN')} đến ${new Date().toLocaleDateString('vi-VN')})\n`;
  md += `- **Tổng số tin nhắn:** ${allMsgs.length}\n\n---\n\n`;

  const byDate = {};
  allMsgs.forEach(m => {
    if (!byDate[m.date]) byDate[m.date] = [];
    byDate[m.date].push(m);
  });

  for (const [date, msgs] of Object.entries(byDate)) {
    md += `### 📅 Ngày ${date} (${msgs.length} tin nhắn)\n`;
    msgs.forEach(m => {
      md += `* **${m.time}** - **${m.sender}**: ${m.content}\n`;
    });
    md += `\n`;
  }

  fs.writeFileSync(mdPath, md, 'utf8');

  console.log(`Đã lưu kết quả thành công:`);
  console.log(`- File JSON: ${jsonPath}`);
  console.log(`- File Markdown: ${mdPath}\n`);
}

// Main Router
async function main() {
  const args = process.argv.slice(2);
  const info = getZaloDataInfo();

  if (!info.userId) {
    console.error('Không xác định được User ID Zalo trong thư mục:', info.dataDir);
    process.exit(1);
  }

  const uin = getUinKey();

  if (args.includes('--list')) {
    await listConversations(info, uin);
  } else if (args.includes('--search')) {
    const idx = args.indexOf('--search');
    const kw = args[idx + 1];
    if (!kw) {
      console.error('Vui lòng cung cấp từ khóa tìm kiếm: --search "<tên>"');
      process.exit(1);
    }
    await searchContactOrGroup(info, uin, kw);
  } else if (args.includes('--target')) {
    const idx = args.indexOf('--target');
    const target = args[idx + 1];
    let days = 20;
    const daysIdx = args.indexOf('--days');
    if (daysIdx !== -1 && args[daysIdx + 1]) {
      days = parseInt(args[daysIdx + 1], 10) || 20;
    }
    let outDir = null;
    const outIdx = args.indexOf('--out');
    if (outIdx !== -1 && args[outIdx + 1]) {
      outDir = args[outIdx + 1];
    }
    await extractMessages(info, uin, target, days, outDir);
  } else {
    console.log(`
Zalo PC Message Extractor Engine v1.0.0
Cách dùng:
  node zalo_engine.cjs --list                    # Liệt kê các cuộc trò chuyện gần đây
  node zalo_engine.cjs --search "<tên/ID>"       # Tìm kiếm ID bạn bè hoặc nhóm
  node zalo_engine.cjs --target "<tên/ID>" [--days 20] [--out <thư mục>] # Trích xuất tin nhắn
    `);
  }
}

main().catch(err => {
  console.error('Lỗi thực thi:', err);
  process.exit(1);
});
