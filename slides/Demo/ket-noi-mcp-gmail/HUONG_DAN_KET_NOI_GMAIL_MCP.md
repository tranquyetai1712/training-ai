# 📬 HƯỚNG DẪN KẾT NỐI GMAIL MCP CHO GOOGLE ANTIGRAVITY

Sổ tay hướng dẫn nhanh 3 bước kích hoạt cổng kết nối **Gmail MCP** để trợ lý AI có thể đọc, lọc và tóm tắt email công việc trực tiếp trên hòm thư Gmail của bạn.

---

## 🚀 3 Bước Thiết Lập Nhanh

### Bước 1: Tạo Khóa Google Cloud OAuth (Miễn Phí 100%)
1. Truy cập [Google Cloud Console](https://console.cloud.google.com/).
2. Bật dịch vụ **Gmail API**.
3. Tạo **OAuth 2.0 Client ID** (chọn loại ứng dụng: *Desktop App*).
4. Tải file `client_secret.json` về và lưu vào thư mục: `~/.gemini/config/mcp/google-oauth-credentials.json`.

### Bước 2: Cấu Hình File `mcp_config.json`
Mở file `~/.gemini/config/mcp_config.json` và thêm cấu hình server `gmail`:

```json
{
  "mcpServers": {
    "gmail": {
      "command": "npx",
      "args": [
        "-y",
        "@gongrzhe/server-gmail-autoauth-mcp"
      ],
      "env": {
        "GOOGLE_CLIENT_ID": "<DÁN_CLIENT_ID_CỦA_BẠN_VÀO_ĐÂY>",
        "GOOGLE_CLIENT_SECRET": "<DÁN_CLIENT_SECRET_CỦA_BẠN_VÀO_ĐÂY>",
        "CREDENTIALS_PATH": "~/.gemini/config/mcp/google-oauth-credentials.json",
        "GMAIL_TOKEN_PATH": "~/.gemini/config/mcp/gmail-token.json"
      }
    }
  }
}
```

### Bước 3: Đăng Nhập Xác Thực Lần Đầu Tiên
* Khi Antigravity khởi động lần đầu, trình duyệt sẽ bật lên yêu cầu cấp quyền đọc Gmail.
* Bạn bấm **Allow (Cho phép)**. Một tệp token lưu tại `gmail-token.json` sẽ được sinh ra tự động.
* Từ thời điểm này trở đi, bạn **không bao giờ phải đăng nhập lại**! AI đã sẵn sàng phục vụ hòm thư của bạn 24/7.

---

## 🛠️ Danh Sách Công Cụ AI Sở Hữu Sau Khi Cắm Gmail MCP
* `search_emails`: Tìm kiếm email theo từ khóa, người gửi hoặc mốc thời gian.
* `read_email`: Đọc chi tiết nội dung email và tệp đính kèm.
* `draft_email`: Soạn trước bản nháp email trả lời đối tác để bạn kiểm duyệt.
* `send_email`: Gửi email trực tiếp khi nhận được sự phê duyệt của bạn.
* `list_email_labels` / `modify_email`: Quản lý và dán nhãn màu phân loại hộp thư.
