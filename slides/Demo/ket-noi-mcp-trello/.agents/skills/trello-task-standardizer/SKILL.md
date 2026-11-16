---
name: trello-task-standardizer
description: Tự động chuẩn hóa nội dung yêu cầu công việc thô thành thẻ Trello chuyên nghiệp chuẩn Agile/Scrum (có mục tiêu, checklist chi tiết, tiêu chí nghiệm thu DoD) và tự động tạo thẻ qua Trello MCP.
---

# Chuẩn Hóa Thẻ Việc Trello Chuyên Nghiệp

## Mục đích
Khi người dùng đưa ra một yêu cầu tạo thẻ Trello với câu lệnh thô, ngắn gọn hoặc lủng củng, Skill này sẽ tự động:
1. Đặt lại tiêu đề chuẩn theo cú pháp: `[MÃ_PHÒNG_BAN/PHÂN_HỆ] + Động từ hành động + Đối tượng`.
2. Format mô tả thẻ theo template chuẩn doanh nghiệp (`templates/task_template.md`):
   - 🎯 **Mục tiêu:** Diễn đạt lại mục tiêu rõ ràng, súc tích.
   - 👤 **Phụ trách & Hạn chót:** Trích xuất thông tin người phụ trách (nếu có) và hạn chót.
   - 📋 **Checklist hành động:** Tự động phân rã thành 3-5 bước hành động cụ thể.
   - ✅ **Tiêu chí hoàn thành (DoD):** Xác định điều kiện rõ ràng để nghiệm thu thẻ.
   - ⚠️ **Lưu ý & Ràng buộc:** Ràng buộc ngân sách, đối tác, thời gian.
3. Sử dụng công cụ Trello MCP (`add_card_to_list` hoặc `trelloWriteCard`) để tạo thẻ và thêm danh sách checklist vào đúng cột yêu cầu.
