---
name: q-chao-buoi-sang-agent
description: Use when setting up, testing, or managing daily 5:00 AM automated greetings sent to the Antigravity agent CLI.
---

# 🌅 Tự động gửi lời chào buổi sáng đến Antigravity Agent (daily-greeting)

Skill này cài đặt và quản lý tác vụ Linux Crontab tự động gửi lời chào đến Antigravity agent CLI (`agy`) vào lúc **5:00 AM mỗi sáng hàng ngày**.

## 💬 Nội dung câu hỏi chào hỏi
> "Xin chào buổi sáng bạn có khỏe không, hôm nay bạn có hỗ trợ được tôi xử lý code không ?"

---

## ⚙️ Cách hoạt động

1. **Lịch Crontab**: Đăng ký một cron job chạy vào `0 5 * * *` (5h00 sáng mỗi ngày).
2. **Thực thi CLI**: Script `scripts/send_greeting.sh` sử dụng `/home/tranquyet/.local/bin/agy --print` để gửi câu hỏi chào hỏi đến agent.
3. **Ghi log**: Phản hồi của Agent kèm mốc thời gian được tự động lưu vào `~/.gemini/antigravity/logs/daily_greeting.log`.
4. **Hiển thị Notification**: Gửi thông báo Desktop Notification (thông qua `notify-send`) để người dùng nhận biết khi mở máy.

---

## 🚀 Hướng dẫn cài đặt & Quản lý

### 1. Kích hoạt tự động (Cài đặt Cron Job)

Chạy script cài đặt cron job trong terminal:

```bash
bash /home/tranquyet/.gemini/config/plugins/quyetchasqui/skills/q-chao-buoi-sang-agent/scripts/setup_cron.sh
```

### 2. Kiểm tra xem Cron Job đã được đăng ký chưa

```bash
crontab -l | grep daily-greeting
```

### 3. Chạy thử nghiệm trực tiếp ngay lập tức

Để kiểm tra phản hồi từ Agent và file log mà không cần chờ đến 5:00 AM:

```bash
bash /home/tranquyet/.gemini/config/plugins/quyetchasqui/skills/q-chao-buoi-sang-agent/scripts/send_greeting.sh
```

### 4. Xem nhật ký phản hồi (Logs)

```bash
cat ~/.gemini/antigravity/logs/daily_greeting.log
```

### 5. Gỡ bỏ Cron Job (Dừng gửi lời chào)

```bash
bash /home/tranquyet/.gemini/config/plugins/quyetchasqui/skills/q-chao-buoi-sang-agent/scripts/remove_cron.sh
```
