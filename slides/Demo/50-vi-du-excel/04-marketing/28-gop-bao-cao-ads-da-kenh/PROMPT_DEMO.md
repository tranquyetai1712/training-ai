# CẨM NANG HƯỚNG DẪN DEMO: 28-GOP-BAO-CAO-ADS-DA-KENH

## 1. Nỗi Đau & Bài Toán Thực Tế
Mỗi nền tảng quảng cáo xuất ra định dạng khác nhau (FB gọi là Amount Spent, Google là Cost, TikTok là Total Cost). Mỗi sáng mất 1-2 tiếng để gộp thủ công.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu Facebook ghi nhận Amount Spent là 1.500.000 còn Google ghi Cost là 1.200.000, làm sao để gộp thành 1 cột Chi Phí duy nhất mà không phải đổi tên cột bằng tay?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc 3 file fb_ads.csv, gg_ads.csv và tiktok_ads.xlsx. Hãy chuẩn hóa về cùng cấu trúc: Ngày, Kênh, Chiến dịch, Chi phí (VNĐ), Impressions, Clicks, CTR, Chuyển đổi, CPA. Gộp tất cả vào file Master_Ads_Report_T10.xlsx và tạo bảng tổng hợp so sánh hiệu quả giữa 3 kênh.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không ép kiểu trường Date về cùng định dạng chuẩn YYYY-MM-DD, các file CSV có thể bị lẫn lộn giữa ngày/tháng của Mỹ (MM/DD) và Việt Nam (DD/MM).

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Master_Ads_Report_T10.xlsx` tích hợp dữ liệu 3 kênh quảng cáo sạch sẽ kèm bảng so sánh hiệu quả.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Xử lý sạch lỗi lệch bảng mã CSV, lệch tên cột Anh/Việt và tự tính các chỉ số phái sinh trong 10 giây.
