---
name: q-tinh-gon-code
description: Rà soát code đã thay đổi theo 4 góc chất lượng (tái sử dụng, đơn giản hóa, hiệu năng, độ sâu) rồi áp dụng bản sửa. Chỉ dọn dẹp chất lượng — không tìm bug tính đúng đắn (dùng skill review-code cho việc đó).
---

# 🧹 Simplify Code — Dọn dẹp & nâng cao chất lượng code

> Quy trình: `Lấy diff` ➔ `Rà soát 4 góc chất lượng` ➔ `Áp dụng bản sửa trực tiếp`

Nhiệm vụ chính: Cải thiện **chất lượng mã nguồn** của các thay đổi vừa tạo (refactor, tối ưu, làm sạch), **KHÔNG** đi tìm bug đúng/sai của logic nghiệp vụ.

> [!IMPORTANT]
> **Nguyên tắc thực thi:** Skill này chạy **tuần tự trong cùng 1 context** (không phân nhánh subagent song song). Hãy rà soát lần lượt đủ cả 4 góc bên dưới trong một lượt duy nhất — tuyệt đối không bỏ sót góc nào.

---

## 📍 Phase 0: Lấy phạm vi rà soát (Diff)

1. **Xác định diff:**
   - Chạy `git diff @{upstream}...HEAD` (hoặc `git diff main...HEAD` / `git diff HEAD~1` nếu không có upstream).
   - Nếu còn thay đổi chưa commit hoặc diff range rỗng: Chạy thêm `git diff HEAD` để bao gồm toàn bộ thay đổi ở working-tree.
   - Nếu người dùng truyền chỉ định PR number, tên branch hoặc file cụ thể: Rà soát đúng mục tiêu đó.
2. **Thiết lập ranh giới:** Xem tập diff này là **phạm vi rà soát duy nhất**.

---

## 🔍 Phase 1: Rà soát chất lượng (4 Góc)

Lần lượt kiểm tra diff qua 4 góc dưới đây. Với mỗi vấn đề phát hiện, ghi nhận cụ thể:
`File` | `Line` | `Tóm tắt vấn đề` | `Chi phí/Lãng phí cụ thể` (tái lặp, lãng phí tài nguyên, hay khó bảo trì).

### 1. Tái sử dụng (Reuse)
- **🔍 Cần rà soát:**
  - Kiểm tra xem code mới có đang viết lại (re-invent) tính năng mà codebase đã có sẵn hay không.
- **💡 Hướng tối ưu:**
  - Grep tìm trong các module shared/utility hoặc file lân cận, chỉ định chính xác helper/service đã tồn tại để tái sử dụng.

### 2. Đơn giản hóa (Simplification) & Dead Code Audit 2 Chiều
- **🔍 Cần rà soát:**
  - State thừa hoặc state có thể tự suy ra từ dữ liệu hiện có.
  - Các đoạn code copy-paste chỉ khác biệt nhỏ.
  - Cấu trúc rẽ nhánh / lồng ghép (nesting) quá sâu.
  - **Dead Code Audit 2 Chiều (Dead Code Cleanup Policy)**:
    - **Forward Scan**: Hàm, target, partial, hay biến mới tạo nhưng chưa có nơi nào gọi.
    - **Reverse Scan (Gỡ UI/Logic)**: Khi xóa/sửa một nút/tính năng UI, quét dọn dẹp các method trong Stimulus JS Controller, Ruby helper/private method, Interaction class mồ côi. ĐẶC BIỆT kiểm tra các tệp locale (`en`, `ja`, `vi`) xem câu văn hướng dẫn (`*_tip_*`, `*_help_*`, `*_description`) có bị outdated do hướng dẫn thao tác vừa bị gỡ hay không [CC-09].
    - **No Broken Binding**: Đảm bảo không xóa hàm JS/Ruby nếu vẫn còn nơi khác tham chiếu đến.
- **💡 Hướng tối ưu:**
  - Đề xuất giải pháp viết lại ngắn gọn, phẳng hơn (flatter structure) mà vẫn đạt cùng mục tiêu, dọn dẹp triệt để mã nguồn mồ côi.

### 3. Hiệu năng (Efficiency)
- **🔍 Cần rà soát:**
  - Tính toán lặp lại hoặc truy xuất I/O/Database dư thừa.
  - Các thao tác độc lập nhưng lại bị chạy tuần tự (blocking hot path / startup).
  - **Cảnh báo rò rỉ bộ nhớ:** Các object sống lâu (long-lived objects) khởi tạo từ closure/environment bị capture, giữ toàn bộ scope xung quanh tồn tại theo vòng đời object.
- **💡 Hướng tối ưu:**
  - Thay thế bằng phương án xử lý rẻ hơn. Chuyển closure capture scope lớn sang class/struct chỉ lưu trữ đúng các trường (fields) cần thiết.

### 4. Độ sâu (Altitude)
- **🔍 Cần rà soát:**
  - Nhận biết các bản vá tạm thời (bandaid solution) hời hợt trên bề mặt.
  - Các điều kiện đặc biệt (`special-case`) viết đè lên hạ tầng dùng chung thay vì giải quyết gốc rễ.
- **💡 Hướng tối ưu:**
  - Nâng độ sâu bản sửa: Tổng quát hóa cơ chế nền tảng thay vì chất thêm các `special-case`.

---

## 🛠️ Phase 2: Áp dụng bản sửa & Tóm tắt

1. **Gộp vết sửa (Deduplicate):** Gộp các phát hiện trùng lặp trỏ tới cùng một dòng code hoặc cùng một cơ chế.
2. **Sửa trực tiếp:** Tiến hành chỉnh sửa code trực tiếp cho các phát hiện đạt tiêu chuẩn.
3. **Tiêu chí BỎ QUA (Skip):** Bỏ qua phát hiện nếu thuộc các trường hợp sau (ghi rõ lý do bỏ qua):
   - 🚫 **Thay đổi hành vi:** Bản sửa làm thay đổi logic/hành vi mong muốn của hệ thống.
   - 🚫 **Vượt phạm vi diff:** Yêu cầu chỉnh sửa các file nằm ngoài phạm vi diff ở Phase 0.
   - 🚫 **False positive:** Phát hiện không chính xác hoặc không mang lại giá trị thực tế.
4. **Tóm tắt kết quả:** Kết thúc bằng báo cáo ngắn:
   - Các điểm đã được dọn dẹp / tối ưu.
   - Các điểm đã bỏ qua (kèm lý do).
   - Xác nhận: *Skill đã hoàn thành 1 lượt rà soát tuần tự trong cùng context.*
