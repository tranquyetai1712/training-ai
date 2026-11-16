---
name: q-tu-dong-phan-bo-cong-viec-tren-trello
description: "Tự động phân tích danh sách công việc thô (ví dụ: Fix comment CHQ-865(Halo), Review CHQ-1055(Halo), CHQ-1056(Eval)) và tự động tạo các thẻ Trello chuẩn hóa trên bảng My Daily Hub (Dev -> Manager), tự động gắn mã ticket, nhãn màu, checklist và link Jira dự án (Halo -> Board 82, Eval -> Board 115)."
---

# 🚀 SKILL: TỰ ĐỘNG PHÂN BỔ CÔNG VIỆC TRÊN TRELLO

Kỹ năng này giúp tự động bóc tách danh sách công việc dạng chuỗi văn bản do người dùng nhập vào và khởi tạo các thẻ (Card) chuẩn hóa trên bảng **My Daily Hub (Dev -> Manager)** trên Trello.

---

## 1. NGUYÊN TẮC MẬP MẠNH DỰ ÁN & LINK JIRA

Kỹ năng tự động nhận diện từ ngoặc đơn `(TênDựÁn)` để gắn đúng Link Jira tương ứng:

| Mã Dự án trong ngoặc | Tên Dự án | Đường dẫn Jira Board tương ứng |
| :--- | :--- | :--- |
| `(Halo)` | Halo | `https://amap.atlassian.net/jira/software/c/projects/CHQ/boards/82` |
| `(Eval)` | Eval | `https://amap.atlassian.net/jira/software/c/projects/CHQ/boards/115/` |
| Khác (nếu có) | Custom | `https://amap.atlassian.net/browse/{TICKET}` |

---

## 2. QUY TẮC BÓC TÁCH & CHUẨN HÓA DỮ LIỆU

Khi nhận đầu vào ví dụ:
```text
Fix comment CHQ-865(Halo)
Review CHQ-1055(Halo)
CHQ-1051(Halo)
CHQ-1056(Eval)
```

Skill sẽ tự động phân tích thành:
1. **Mã Ticket**: `CHQ-865`, `CHQ-1055`, `CHQ-1051`, `CHQ-1056`.
2. **Hành động (Action)**:
   - `Fix comment` -> Gán nhãn Màu Đỏ (`Jira Project`) + Nhắc nhở thả `:rocket:` khi reply comment.
   - `Review` -> Gán nhãn Màu Vàng (`Collaboration/Review`).
   - Mặc định (không ghi rõ hành động) -> Gán `Implement feature` + Nhãn Màu Đỏ (`Jira Project`).
3. **Link Jira**: Tự động tạo link dạng `{BoardURL}?selectedIssue={TicketCode}`.
4. **Cột mục tiêu**: Tự động đưa vào cột `Weekly Backlog` (hoặc `Q1 Urgent` nếu có từ khóa khẩn cấp).

---

## 3. THỰC THI SCRIPT TỰ ĐỘNG HÓA

Để tạo card trên Trello, chạy script Python sẵn có tại:
`/home/tranquyet/.gemini/config/plugins/quyetchasqui/skills/q-tu-dong-phan-bo-cong-viec-tren-trello/scripts/create_trello_tasks.py`

### Lệnh chạy mẫu:
```bash
/home/tranquyet/.gemini/config/plugins/quyetchasqui/skills/q-tu-dong-phan-bo-cong-viec-tren-trello/scripts/create_trello_tasks.py << 'EOF'
Fix comment CHQ-865(Halo)
Review CHQ-1055(Halo)
CHQ-1051(Halo)
CHQ-1056(Eval)
EOF
```

---

## 4. ĐẦU RA BÁO CÁO (OUTPUT REPORT)

Sau khi tạo xong, skill sẽ xuất báo cáo dạng danh sách kèm link trực tiếp để người dùng bấm vào xem ngay trên Trello và Jira.
