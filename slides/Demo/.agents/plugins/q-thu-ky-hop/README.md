# Plugin `q-thu-ky-hop` — Thư Ký Họp AI: Nghe Ghi Âm, Viết Biên Bản & Đồng Bộ Trello/Slack

Plugin tự động hóa quy trình sau cuộc họp: lắng nghe file ghi âm (`.mp3`, `.m4a`, `.wav`), lọc bỏ chuyện phiếm ngoài lề, xuất **Biên Bản Cuộc Họp** chuẩn 3 phần kèm bảng phân công việc (Action Items), sau đó tự động tạo thẻ công việc trên **Trello** và gửi thông báo tóm tắt vào kênh **Slack**.

---

## 📁 Cấu Trúc Thư Mục

```text
q-thu-ky-hop/
├── plugin.json
├── README.md
├── rules/
│   ├── quy-chuan-bien-ban-hop.md
│   └── quy-chuan-trello-slack.md
└── skills/
    └── thu-ky-hop-tu-dong/
        └── SKILL.md
```

---

## 🚀 Cách Sử Dụng Nhanh

1. Đặt file ghi âm cuộc họp (ví dụ `cuoc_hop_giao_ban_tuan.mp3`) vào thư mục làm việc.
2. **Bước 1 (Tạo biên bản):**
   > *"Hãy lắng nghe file ghi âm `cuoc_hop_giao_ban_tuan.mp3` và lập biên bản cuộc họp lưu thành `bien_ban_hop_giao_ban.md` đúng quy chuẩn giúp tôi."*
3. **Bước 2 (Đẩy việc sang Trello & Slack):**
   > *"Từ bảng phân công việc vừa lập, hãy tạo các thẻ việc trên bảng Trello `Chiến Dịch Tháng 10` (cột `Cần Làm (To Do)`) và gửi tin nhắn tóm tắt vào kênh Slack `#thong-bao-chung`."*
