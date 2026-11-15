import argparse
import json
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter


def create_expense_excel(items: list[dict], output_path: Path, title_period: str = "THÁNG 10/2026") -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Bang_Ke_Chi_Phi"

    # Page setup
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.page_setup.paperSize = ws.PAPERSIZE_A4

    # Styles
    font_country = Font(name="Calibri", size=12, bold=True, color="1E293B")
    font_title = Font(name="Calibri", size=14, bold=True, color="0F172A")
    font_header = Font(name="Calibri", size=11, bold=True, color="0F172A")
    font_body = Font(name="Calibri", size=11, color="1E293B")
    font_total = Font(name="Calibri", size=11, bold=True, color="991B1B")
    font_sign_title = Font(name="Calibri", size=11, bold=True, color="0F172A")
    font_sign_note = Font(name="Calibri", size=10, italic=True, color="475569")

    fill_header = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
    fill_total = PatternFill(start_color="FEF2F2", end_color="FEF2F2", fill_type="solid")

    thin = Side(border_style="thin", color="64748B")
    border_cell = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Row 1 & 2: Titles
    ws.merge_cells("A1:G1")
    ws["A1"] = "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM"
    ws["A1"].font = font_country
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 22

    ws.merge_cells("A2:G2")
    ws["A2"] = f"BẢNG KÊ THANH TOÁN CHI PHÍ CÔNG TÁC {title_period.upper()}"
    ws["A2"].font = font_title
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 28

    # Row 4: Table headers
    headers = [
        "STT",
        "Ngày",
        "Đơn Vị Phát Hành",
        "Nội Dung Chi",
        "Tiền Trước Thuế",
        "Thuế VAT",
        "Tổng Thanh Toán",
    ]
    header_row = 4
    ws.row_dimensions[header_row].height = 26
    for col_idx, text in enumerate(headers, start=1):
        cell = ws.cell(row=header_row, column=col_idx, value=text)
        cell.font = font_header
        cell.fill = fill_header
        cell.border = border_cell
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # Data rows starting at row 5
    start_row = 5
    currency_fmt = '#,##0 "VNĐ"'

    for idx, item in enumerate(items, start=1):
        r = start_row + idx - 1
        ws.row_dimensions[r].height = 22
        pre_tax = int(item.get("tien_truoc_thue", 0))
        vat_amt = int(item.get("tien_vat", 0))

        row_values = [
            idx,
            item.get("ngay", ""),
            item.get("don_vi", ""),
            item.get("noi_dung", ""),
            pre_tax,
            vat_amt,
            f"=E{r}+F{r}",
        ]
        for col_idx, val in enumerate(row_values, start=1):
            c = ws.cell(row=r, column=col_idx, value=val)
            c.font = font_body
            c.border = border_cell
            if col_idx in (1, 2):
                c.alignment = Alignment(horizontal="center", vertical="center")
            elif col_idx in (5, 6, 7):
                c.alignment = Alignment(horizontal="right", vertical="center")
                c.number_format = currency_fmt
            else:
                c.alignment = Alignment(horizontal="left", vertical="center")

    end_row = start_row + len(items) - 1
    total_row = end_row + 1
    ws.row_dimensions[total_row].height = 26

    # Merge A..D for TỔNG CỘNG
    ws.merge_cells(f"A{total_row}:D{total_row}")
    ws[f"A{total_row}"] = "TỔNG CỘNG"
    for col_idx in range(1, 8):
        c = ws.cell(row=total_row, column=col_idx)
        c.font = font_total
        c.fill = fill_total
        c.border = border_cell
        if col_idx == 1:
            c.alignment = Alignment(horizontal="center", vertical="center")
        elif col_idx in (5, 6, 7):
            col_letter = get_column_letter(col_idx)
            c.value = f"=SUM({col_letter}{start_row}:{col_letter}{end_row})"
            c.alignment = Alignment(horizontal="right", vertical="center")
            c.number_format = currency_fmt

    # Signature block
    sign_row = total_row + 2
    ws.row_dimensions[sign_row].height = 22
    ws.row_dimensions[sign_row + 1].height = 18

    ws.merge_cells(f"A{sign_row}:B{sign_row}")
    ws[f"A{sign_row}"] = "Người Lập Bảng"
    ws[f"A{sign_row}"].font = font_sign_title
    ws[f"A{sign_row}"].alignment = Alignment(horizontal="center")

    ws.merge_cells(f"C{sign_row}:D{sign_row}")
    ws[f"C{sign_row}"] = "Kế Toán Trưởng"
    ws[f"C{sign_row}"].font = font_sign_title
    ws[f"C{sign_row}"].alignment = Alignment(horizontal="center")

    ws.merge_cells(f"E{sign_row}:G{sign_row}")
    ws[f"E{sign_row}"] = "Giám Đốc Phê Duyệt"
    ws[f"E{sign_row}"].font = font_sign_title
    ws[f"E{sign_row}"].alignment = Alignment(horizontal="center")

    for col_ref in (f"A{sign_row + 1}", f"C{sign_row + 1}", f"E{sign_row + 1}"):
        ws[col_ref] = "(Ký, ghi rõ họ tên)"
        ws[col_ref].font = font_sign_note
        ws[col_ref].alignment = Alignment(horizontal="center")

    # Column widths
    widths = {1: 7, 2: 14, 3: 26, 4: 28, 5: 19, 6: 17, 7: 20}
    for col_idx, w in widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = w

    output_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Xuất bảng kê chi phí công tác Excel chuẩn =SUM()")
    parser.add_argument("--input", required=True, help="Đường dẫn file JSON danh sách hóa đơn")
    parser.add_argument("--output", required=True, help="Đường dẫn file Excel (.xlsx) đầu ra")
    parser.add_argument("--period", default="THÁNG 10/2026", help="Kỳ thanh toán hiển thị trên tiêu đề")
    args = parser.parse_args()

    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    create_expense_excel(data, Path(args.output), args.period)
    print(f"Created {args.output}")


if __name__ == "__main__":
    main()
