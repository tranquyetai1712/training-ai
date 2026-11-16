---
name: q-sync-agents
description: Đồng bộ hóa 3 chiều các AI Agents và Workflows giữa Gemini, Copilot và Antigravity.
---

# 🤖 Đồng bộ hóa AI Agents & Workflows (sync_agents)

Skill này giúp thực hiện đồng bộ hóa 3 chiều (3-way synchronization) các định nghĩa AI Agents và Workflows (.md, .sh) giữa các thư mục cấu hình:
1. `/home/tranquyet/.gemini/agents`
2. `/home/tranquyet/.copilot/agents`
3. `/home/tranquyet/.gemini/antigravity/global_workflows`

## ⚙️ Cách hoạt động

Skill thực hiện chạy script `sync_agents.sh` nằm trong thư mục của skill.
Nó sẽ quét toàn bộ các file `.md` và `.sh` trong 3 thư mục trên, tìm phiên bản có thời gian sửa đổi (mtime) mới nhất của từng file, và đồng bộ sang các thư mục còn lại nếu file chưa tồn tại hoặc nội dung khác biệt.

## 🚀 Cách sử dụng

Bạn có thể kích hoạt skill bằng cách chạy script trực tiếp trên terminal:

```bash
# Run 3-way synchronization for agents and workflows
bash /home/tranquyet/.gemini/config/plugins/quyetchasqui/skills/q-sync-agents/sync_agents.sh
```
