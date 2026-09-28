# Laravel & Modern PHP Agent Guidelines

Áp dụng cho mọi tác vụ phát triển, bảo trì và refactor mã nguồn trong dự án Laravel.

---

## 1. Tiêu chuẩn PHP & Laravel (PHP 8.2+ / 8.3+)
- **Strict Typing:** Luôn khai báo `declare(strict_types=1);` ở đầu mọi file PHP.
- **Type Hinting:** Bắt buộc định nghĩa rõ ràng kiểu dữ liệu cho toàn bộ method arguments, properties và return types.
- **Constructor Property Promotion:** Sử dụng cú pháp rút gọn của PHP 8 cho dependency injection trong constructor.
- **Enums & Match:** Ưu tiên sử dụng PHP Enums thay vì magic string/numbers; dùng biểu thức `match` thay cho `switch-case` phức tạp.
- **Chuẩn PSR-12 & Pint:** Tuân thủ chuẩn PSR-12 và quy chuẩn coding style của Laravel Pint.

---

## 2. Kiến trúc & Tầng nghiệp vụ (Architecture)
- **Thin Controllers (Controller mỏng):**
  - Controller chỉ làm nhiệm vụ tiếp nhận request, gọi tầng xử lý nghiệp vụ và trả về response.
  - Tuyệt đối không viết business logic, query database phức tạp trực tiếp trong Controller.
- **Form Request:**
  - Tách toàn bộ logic validate và authorize dữ liệu vào Form Request riêng (`php artisan make:request`).
  - Luôn sử dụng `$request->validated()` thay vì `$request->all()`.
- **Actions / Services:**
  - Đóng gói các tác vụ nghiệp vụ phức tạp vào Single Action classes (Invocable classes với method `__invoke()`) hoặc Service classes.
- **API Resources:**
  - Định dạng toàn bộ dữ liệu trả về cho Frontend thông qua Eloquent API Resource (`php artisan make:resource`), không return Model thô.
- **Queue & Async:**
  - Đẩy các tác vụ nặng (gửi mail, thông báo, xử lý file, gọi third-party API) vào Queue Jobs (`ShouldQueue`).

---

## 3. Database & Eloquent ORM
- **Phòng chống N+1 Queries:**
  - Luôn chủ động sử dụng Eager Loading (`with()`) khi truy vấn danh sách có kèm quan hệ.
  - Sử dụng `lazyById()` hoặc `chunk()` khi xử lý tập dữ liệu lớn để tránh tràn bộ nhớ.
- **Database Transactions:**
  - Luôn bọc trong `DB::transaction(function () { ... })` khi thực hiện chuỗi thay đổi ảnh hưởng đến nhiều bảng.
- **Scopes & Relationships:**
  - Khai báo rõ ràng return type cho các quan hệ (`HasMany`, `BelongsTo`, `BelongsToMany`...).
  - Định nghĩa Local Scopes trên Model để tái sử dụng logic query thay vì lặp lại các mệnh đề `where(...)`.

---

## 4. Kiểm thử & Công cụ (Testing & Tooling)
- **Pest PHP / PHPUnit:**
  - Mọi chức năng mới hoặc sửa đổi quan trọng phải đi kèm Feature Test hoặc Unit Test.
  - Cấu trúc test rõ ràng theo mẫu Arrange - Act - Assert.
- **Lệnh Artisan:**
  - Ưu tiên dùng các lệnh `php artisan make:...` để tạo file nhằm đảm bảo namespace, boilerplate và cấu trúc chuẩn của framework.

## 5.Quy ước phản hồi
- Luôn mở đầu câu trả lời bằng tiền tố: `[LARAVEL-SENIOR-RULE-ACTIVE 🚀]`