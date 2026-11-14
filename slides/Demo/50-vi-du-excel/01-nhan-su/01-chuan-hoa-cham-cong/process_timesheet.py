"""
Automated biometric attendance processing script for monthly timesheet reporting.
Compliance with C&B guidelines:
- Shift: 08:30 - 17:30 (Lunch break: 12:00 - 13:00)
- Earliest swipe as Check-in, latest swipe as Check-out
- Single swipe defaults to 0.5 work day with 'Quên quẹt Vào/Ra' note
- Highlight late arrival > 30 mins and missing swipe in red
"""

import os
from datetime import datetime, time
import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def process_attendance():
    # File paths
    input_file = "cham_cong_thang_10_raw.xlsx"
    output_file = "bang_cong_chuan_hoa.xlsx"
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} not found.")
        
    # Read raw attendance logs
    df_raw = pd.read_excel(input_file)
    
    # Ensure correct datetime parsing
    df_raw["Thời Gian Quẹt Thẻ"] = pd.to_datetime(df_raw["Thời Gian Quẹt Thẻ"])
    df_raw["Ngày"] = df_raw["Thời Gian Quẹt Thẻ"].dt.date
    
    # Standard shift times
    shift_start = time(8, 30, 0)
    shift_end = time(17, 30, 0)
    
    # Group by Employee ID, Name, and Date
    grouped = df_raw.groupby(["Mã Nhân Viên", "Họ và Tên", "Ngày"])
    
    daily_records = []
    
    for (emp_id, emp_name, work_date), group in grouped:
        swipes = sorted(group["Thời Gian Quẹt Thẻ"].tolist())
        swipe_count = len(swipes)
        
        first_swipe = swipes[0]
        last_swipe = swipes[-1]
        
        check_in_time = None
        check_out_time = None
        late_minutes = 0
        early_minutes = 0
        work_hours = 0.0
        work_days = 0.0
        notes = []
        is_red_alert = False
        
        if swipe_count == 1:
            # Single swipe: missing either check-in or check-out
            swipe_t = first_swipe.time()
            if swipe_t < time(12, 0, 0):
                check_in_time = swipe_t
                check_out_time = None
            else:
                check_in_time = None
                check_out_time = swipe_t
                
            work_days = 0.5
            notes.append("Quên quẹt Vào/Ra")
            is_red_alert = True  # Red highlight as per C&B rules
            
            # Check late arrival if check-in exists
            if check_in_time:
                if check_in_time > shift_start:
                    diff_seconds = (datetime.combine(work_date, check_in_time) - datetime.combine(work_date, shift_start)).total_seconds()
                    late_minutes = int(diff_seconds // 60)
                    notes.append(f"Đi muộn {late_minutes}p")
                    if late_minutes > 30:
                        is_red_alert = True
        else:
            # At least two swipes: first is check-in, last is check-out
            check_in_time = first_swipe.time()
            check_out_time = last_swipe.time()
            work_days = 1.0
            
            # Calculate late arrival
            if check_in_time > shift_start:
                diff_seconds = (datetime.combine(work_date, check_in_time) - datetime.combine(work_date, shift_start)).total_seconds()
                late_minutes = int(diff_seconds // 60)
                notes.append(f"Đi muộn {late_minutes}p")
                if late_minutes > 30:
                    is_red_alert = True
                    
            # Calculate early departure
            if check_out_time < shift_end:
                diff_seconds = (datetime.combine(work_date, shift_end) - datetime.combine(work_date, check_out_time)).total_seconds()
                early_minutes = int(diff_seconds // 60)
                notes.append(f"Về sớm {early_minutes}p")
                
            # Calculate working hours excluding 1 hour lunch break (12:00 - 13:00)
            total_duration_hours = (datetime.combine(work_date, check_out_time) - datetime.combine(work_date, check_in_time)).total_seconds() / 3600.0
            # If span covers lunch break, deduct 1 hour
            lunch_start_dt = datetime.combine(work_date, time(12, 0, 0))
            lunch_end_dt = datetime.combine(work_date, time(13, 0, 0))
            first_dt = datetime.combine(work_date, check_in_time)
            last_dt = datetime.combine(work_date, check_out_time)
            
            if first_dt <= lunch_start_dt and last_dt >= lunch_end_dt:
                work_hours = max(0.0, round(total_duration_hours - 1.0, 2))
            else:
                work_hours = max(0.0, round(total_duration_hours, 2))
                
        if not notes:
            note_str = "Đúng giờ"
        else:
            note_str = "; ".join(notes)
            
        weekday_names = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
        weekday_str = weekday_names[work_date.weekday()]
        
        daily_records.append({
            "emp_id": emp_id,
            "emp_name": emp_name,
            "work_date": work_date,
            "weekday": weekday_str,
            "check_in": check_in_time.strftime("%H:%M:%S") if check_in_time else "--:--:--",
            "check_out": check_out_time.strftime("%H:%M:%S") if check_out_time else "--:--:--",
            "late_minutes": late_minutes,
            "early_minutes": early_minutes,
            "work_hours": work_hours,
            "work_days": work_days,
            "note": note_str,
            "is_red_alert": is_red_alert,
            "is_late_warning": (0 < late_minutes <= 30) or (early_minutes > 0 and not is_red_alert)
        })
        
    # Sort daily records by date then emp_id
    daily_records.sort(key=lambda r: (r["work_date"], r["emp_id"]))
    
    # Aggregate monthly summary per employee
    emp_summary = {}
    for r in daily_records:
        eid = r["emp_id"]
        if eid not in emp_summary:
            emp_summary[eid] = {
                "emp_id": eid,
                "emp_name": r["emp_name"],
                "total_work_days": 0.0,
                "total_work_hours": 0.0,
                "late_count": 0,
                "late_minutes_total": 0,
                "late_over_30_count": 0,
                "early_count": 0,
                "early_minutes_total": 0,
                "missing_swipe_count": 0
            }
        s = emp_summary[eid]
        s["total_work_days"] += r["work_days"]
        s["total_work_hours"] += r["work_hours"]
        if r["late_minutes"] > 0:
            s["late_count"] += 1
            s["late_minutes_total"] += r["late_minutes"]
            if r["late_minutes"] > 30:
                s["late_over_30_count"] += 1
        if r["early_minutes"] > 0:
            s["early_count"] += 1
            s["early_minutes_total"] += r["early_minutes"]
        if "Quên quẹt" in r["note"]:
            s["missing_swipe_count"] += 1
            
    summary_records = sorted(emp_summary.values(), key=lambda s: s["emp_id"])
    
    # Create workbook with openpyxl
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)
    
    # Styles definition
    font_title = Font(name="Calibri", size=15, bold=True, color="1B365D")
    font_subtitle = Font(name="Calibri", size=10, italic=True, color="555555")
    font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    font_data = Font(name="Calibri", size=11, color="000000")
    font_total = Font(name="Calibri", size=11, bold=True, color="1B365D")
    
    # Alert fonts and fills
    font_red_alert = Font(name="Calibri", size=11, bold=True, color="9C0006")
    fill_red_alert = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    
    font_yellow_alert = Font(name="Calibri", size=11, bold=False, color="9C6500")
    fill_yellow_alert = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
    
    fill_header_blue = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    fill_total_row = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    fill_zebra = PatternFill(start_color="F9FAFB", end_color="F9FAFB", fill_type="solid")
    
    # Borders
    thin_border_side = Side(border_style="thin", color="D3D3D3")
    border_cell = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
    
    border_total = Border(
        left=thin_border_side,
        right=thin_border_side,
        top=Side(border_style="thin", color="1B365D"),
        bottom=Side(border_style="double", color="1B365D")
    )
    
    # ----------------------------------------------------
    # Sheet 1: Chi_Tiet_Hang_Ngay
    # ----------------------------------------------------
    ws_daily = wb.create_sheet(title="Chi_Tiet_Hang_Ngay")
    ws_daily.views.sheetView[0].showGridLines = True
    
    # Header title block
    ws_daily.merge_cells("A1:K1")
    ws_daily["A1"] = "BẢNG CHẤM CÔNG CHI TIẾT HÀNG NGÀY - THÁNG 10/2026"
    ws_daily["A1"].font = font_title
    ws_daily["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws_daily.row_dimensions[1].height = 30
    
    ws_daily.merge_cells("A2:K2")
    ws_daily["A2"] = "Ca hành chính chuẩn: 08:30 - 17:30 (Nghỉ trưa: 12:00 - 13:00) | Đơn vị: Phòng Nhân sự (C&B)"
    ws_daily["A2"].font = font_subtitle
    ws_daily["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws_daily.row_dimensions[2].height = 18
    
    daily_headers = [
        "STT", "Mã NV", "Họ và Tên", "Ngày", "Thứ", 
        "Giờ Vào", "Giờ Ra", "Đi Muộn (phút)", "Về Sớm (phút)", "Số Công", "Ghi Chú"
    ]
    
    header_row_idx = 4
    ws_daily.row_dimensions[header_row_idx].height = 26
    for col_idx, col_name in enumerate(daily_headers, start=1):
        cell = ws_daily.cell(row=header_row_idx, column=col_idx, value=col_name)
        cell.font = font_header
        cell.fill = fill_header_blue
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border_cell
        
    start_row = 5
    for idx, r in enumerate(daily_records, start=1):
        row_num = start_row + idx - 1
        ws_daily.row_dimensions[row_num].height = 22
        
        cells = [
            (idx, "center", None),
            (r["emp_id"], "center", None),
            (r["emp_name"], "left", None),
            (r["work_date"].strftime("%d/%m/%Y"), "center", None),
            (r["weekday"], "center", None),
            (r["check_in"], "center", None),
            (r["check_out"], "center", None),
            (r["late_minutes"], "center", "#,##0"),
            (r["early_minutes"], "center", "#,##0"),
            (r["work_days"], "center", "0.0"),
            (r["note"], "left", None)
        ]
        
        for c_idx, (val, align, num_fmt) in enumerate(cells, start=1):
            cell = ws_daily.cell(row=row_num, column=c_idx, value=val)
            cell.font = font_data
            cell.alignment = Alignment(horizontal=align, vertical="center")
            cell.border = border_cell
            if num_fmt:
                cell.number_format = num_fmt
                
            # Zebra striping for normal rows
            if idx % 2 == 0 and not r["is_red_alert"]:
                cell.fill = fill_zebra
                
            # Apply red highlight for critical violations (Late > 30 mins or Missing swipe)
            if r["is_red_alert"]:
                cell.fill = fill_red_alert
                cell.font = font_red_alert
            elif r["is_late_warning"] and c_idx in [8, 9, 11]:
                # Light yellow warning for minor late or early departure
                cell.fill = fill_yellow_alert
                cell.font = font_yellow_alert
                
    total_row_idx = start_row + len(daily_records)
    ws_daily.row_dimensions[total_row_idx].height = 24
    
    ws_daily.merge_cells(start_row=total_row_idx, start_column=1, end_row=total_row_idx, end_column=7)
    cell_lbl = ws_daily.cell(row=total_row_idx, column=1, value="TỔNG CỘNG TOÀN CÔNG TY")
    cell_lbl.font = font_total
    cell_lbl.alignment = Alignment(horizontal="center", vertical="center")
    
    for c in range(1, 8):
        c_cell = ws_daily.cell(row=total_row_idx, column=c)
        c_cell.fill = fill_total_row
        c_cell.border = border_total
        
    # SUM for Late minutes
    cell_late = ws_daily.cell(row=total_row_idx, column=8, value=f"=SUM(H{start_row}:H{total_row_idx-1})")
    cell_late.font = font_total
    cell_late.alignment = Alignment(horizontal="center", vertical="center")
    cell_late.fill = fill_total_row
    cell_late.border = border_total
    cell_late.number_format = "#,##0"
    
    # SUM for Early minutes
    cell_early = ws_daily.cell(row=total_row_idx, column=9, value=f"=SUM(I{start_row}:I{total_row_idx-1})")
    cell_early.font = font_total
    cell_early.alignment = Alignment(horizontal="center", vertical="center")
    cell_early.fill = fill_total_row
    cell_early.border = border_total
    cell_early.number_format = "#,##0"
    
    # SUM for Work days
    cell_work = ws_daily.cell(row=total_row_idx, column=10, value=f"=SUM(J{start_row}:J{total_row_idx-1})")
    cell_work.font = font_total
    cell_work.alignment = Alignment(horizontal="center", vertical="center")
    cell_work.fill = fill_total_row
    cell_work.border = border_total
    cell_work.number_format = "0.0"
    
    # Note column for total row
    cell_tot_note = ws_daily.cell(row=total_row_idx, column=11, value="")
    cell_tot_note.fill = fill_total_row
    cell_tot_note.border = border_total
    
    # Auto-fit column widths
    for col in ws_daily.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            # Skip title row from calculation
            if cell.row in [1, 2]:
                continue
            val_str = str(cell.value or "")
            if cell.number_format and isinstance(cell.value, (int, float)):
                val_str = f"{cell.value:.1f}"
            max_len = max(max_len, len(val_str))
        ws_daily.column_dimensions[col_letter].width = max(max_len + 5, 12)
        
    # Specific adjustments
    ws_daily.column_dimensions["A"].width = 7
    ws_daily.column_dimensions["B"].width = 12
    ws_daily.column_dimensions["C"].width = 22
    ws_daily.column_dimensions["D"].width = 14
    ws_daily.column_dimensions["E"].width = 12
    ws_daily.column_dimensions["F"].width = 13
    ws_daily.column_dimensions["G"].width = 13
    ws_daily.column_dimensions["H"].width = 16
    ws_daily.column_dimensions["I"].width = 16
    ws_daily.column_dimensions["J"].width = 13
    ws_daily.column_dimensions["K"].width = 28

    # ----------------------------------------------------
    # Sheet 2: Tong_Hop_Thang
    # ----------------------------------------------------
    ws_summary = wb.create_sheet(title="Tong_Hop_Thang")
    ws_summary.views.sheetView[0].showGridLines = True
    
    # Header title block
    ws_summary.merge_cells("A1:K1")
    ws_summary["A1"] = "BẢNG TỔNG HỢP CÔNG & KỶ LUẬT LAO ĐỘNG THÁNG 10/2026"
    ws_summary["A1"].font = font_title
    ws_summary["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws_summary.row_dimensions[1].height = 30
    
    ws_summary.merge_cells("A2:K2")
    ws_summary["A2"] = "Tổng hợp dữ liệu chuyên cần, số phút vi phạm và xếp loại thi đua tháng"
    ws_summary["A2"].font = font_subtitle
    ws_summary["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws_summary.row_dimensions[2].height = 18
    
    summary_headers = [
        "STT", "Mã NV", "Họ và Tên", "Tổng Công (ngày)", "Số Lần Đi Muộn", 
        "Tổng Phút Muộn", "Muộn > 30p (lần)", "Số Lần Về Sớm", "Tổng Phút Sớm", 
        "Quên Quẹt Thẻ", "Xếp Loại Kỷ Luật"
    ]
    
    ws_summary.row_dimensions[header_row_idx].height = 28
    for col_idx, col_name in enumerate(summary_headers, start=1):
        cell = ws_summary.cell(row=header_row_idx, column=col_idx, value=col_name)
        cell.font = font_header
        cell.fill = fill_header_blue
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border_cell
        
    start_row_sum = 5
    for idx, s in enumerate(summary_records, start=1):
        row_num = start_row_sum + idx - 1
        ws_summary.row_dimensions[row_num].height = 22
        
        # Classification
        classification = "Tốt (Đúng giờ)"
        has_severe_violation = False
        if s["late_over_30_count"] > 0 or s["missing_swipe_count"] > 0:
            classification = "Cần Lưu Ý / Vi Phạm"
            has_severe_violation = True
        elif s["late_count"] > 0 or s["early_count"] > 0:
            classification = "Nhắc Nhở Nhẹ"
            
        cells_sum = [
            (idx, "center", None),
            (s["emp_id"], "center", None),
            (s["emp_name"], "left", None),
            (s["total_work_days"], "center", "0.0"),
            (s["late_count"], "center", "#,##0"),
            (s["late_minutes_total"], "center", "#,##0"),
            (s["late_over_30_count"], "center", "#,##0"),
            (s["early_count"], "center", "#,##0"),
            (s["early_minutes_total"], "center", "#,##0"),
            (s["missing_swipe_count"], "center", "#,##0"),
            (classification, "center", None)
        ]
        
        for c_idx, (val, align, num_fmt) in enumerate(cells_sum, start=1):
            cell = ws_summary.cell(row=row_num, column=c_idx, value=val)
            cell.font = font_data
            cell.alignment = Alignment(horizontal=align, vertical="center")
            cell.border = border_cell
            if num_fmt:
                cell.number_format = num_fmt
                
            if idx % 2 == 0:
                cell.fill = fill_zebra
                
            # Highlight severe violation row or cell
            if has_severe_violation:
                if c_idx in [7, 10, 11]:
                    cell.fill = fill_red_alert
                    cell.font = font_red_alert
            elif classification == "Nhắc Nhở Nhẹ" and c_idx in [5, 6, 8, 9, 11]:
                cell.fill = fill_yellow_alert
                cell.font = font_yellow_alert
                
    tot_sum_idx = start_row_sum + len(summary_records)
    ws_summary.row_dimensions[tot_sum_idx].height = 24
    
    ws_summary.merge_cells(start_row=tot_sum_idx, start_column=1, end_row=tot_sum_idx, end_column=3)
    c_lbl = ws_summary.cell(row=tot_sum_idx, column=1, value="TỔNG CỘNG THÁNG")
    c_lbl.font = font_total
    c_lbl.alignment = Alignment(horizontal="center", vertical="center")
    
    for c in range(1, 4):
        cc = ws_summary.cell(row=tot_sum_idx, column=c)
        cc.fill = fill_total_row
        cc.border = border_total
        
    for col_c in range(4, 11):
        col_letter = get_column_letter(col_c)
        c_cell = ws_summary.cell(row=tot_sum_idx, column=col_c, value=f"=SUM({col_letter}{start_row_sum}:{col_letter}{tot_sum_idx-1})")
        c_cell.font = font_total
        c_cell.alignment = Alignment(horizontal="center", vertical="center")
        c_cell.fill = fill_total_row
        c_cell.border = border_total
        if col_c == 4:
            c_cell.number_format = "0.0"
        else:
            c_cell.number_format = "#,##0"
            
    c_end = ws_summary.cell(row=tot_sum_idx, column=11, value="")
    c_end.fill = fill_total_row
    c_end.border = border_total
    
    # Column width adjustments for summary sheet
    ws_summary.column_dimensions["A"].width = 7
    ws_summary.column_dimensions["B"].width = 12
    ws_summary.column_dimensions["C"].width = 22
    ws_summary.column_dimensions["D"].width = 18
    ws_summary.column_dimensions["E"].width = 16
    ws_summary.column_dimensions["F"].width = 16
    ws_summary.column_dimensions["G"].width = 18
    ws_summary.column_dimensions["H"].width = 16
    ws_summary.column_dimensions["I"].width = 16
    ws_summary.column_dimensions["J"].width = 16
    ws_summary.column_dimensions["K"].width = 22

    # Save output file safely
    wb.save(output_file)
    print(f"Attendance processing completed successfully! Output saved to: {output_file}")

if __name__ == "__main__":
    process_attendance()
