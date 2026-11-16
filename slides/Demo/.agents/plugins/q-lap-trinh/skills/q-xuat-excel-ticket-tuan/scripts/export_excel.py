#!/usr/bin/env python3
# Helper script to export weekly ticket report to a clean Excel (.xlsx) file without external dependencies.

import sys
import json
import xml.etree.ElementTree as ET
import zipfile
import io
import os

STATUS_MAP = {
    "Done": "Merged",
    "Review": "Reviewing",
    "In Progress": "Implementing"
}

def create_excel(data, output_path):
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    # 1. [Content_Types].xml
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
  <Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
  <Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>
</Types>'''

    # 2. _rels/.rels
    dot_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>'''

    # 3. xl/_rels/workbook.xml.rels
    workbook_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>'''

    # 4. xl/workbook.xml
    workbook_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <sheets>
    <sheet name="Report" sheetId="1" r:id="rId1"/>
  </sheets>
</workbook>'''

    # 5. xl/styles.xml - Simple table, bold header, thin borders
    styles_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <fonts count="2">
    <font><sz val="11"/><name val="Calibri"/></font>
    <font><b/><sz val="11"/><name val="Calibri"/></font>
  </fonts>
  <fills count="1">
    <fill><patternFill patternType="none"/></fill>
  </fills>
  <borders count="2">
    <border><left/><right/><top/><bottom/><diagonal/></border>
    <border>
      <left style="thin"><color indexed="64"/></left>
      <right style="thin"><color indexed="64"/></right>
      <top style="thin"><color indexed="64"/></top>
      <bottom style="thin"><color indexed="64"/></bottom>
    </border>
  </borders>
  <cellStyleXfs count="1">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="0"/>
  </cellStyleXfs>
  <cellXfs count="3">
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1"/>
    <xf numFmtId="0" fontId="1" fillId="0" borderId="1" xfId="0" applyFont="1" applyBorder="1"><alignment horizontal="center" vertical="center"/></xf>
    <xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1"><alignment wrapText="1" vertical="center"/></xf>
  </cellXfs>
</styleSheet>'''

    # Helper function to escape XML special chars
    def escape_xml(s):
        if not s:
            return ""
        return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

    rows_xml = []
    # Header row
    rows_xml.append('''    <row r="1">
      <c r="A1" t="inlineStr" s="1"><is><t>Status</t></is></c>
      <c r="B1" t="inlineStr" s="1"><is><t>Ticket ID</t></is></c>
      <c r="C1" t="inlineStr" s="1"><is><t>Link PR</t></is></c>
      <c r="D1" t="inlineStr" s="1"><is><t>StoryPoint</t></is></c>
    </row>''')

    for idx, item in enumerate(data, start=2):
        raw_status = item.get("status", "")
        # Apply Status Mapping
        mapped_status = STATUS_MAP.get(raw_status, raw_status)
        
        status = escape_xml(mapped_status)
        ticket_id = escape_xml(item.get("ticket_id", ""))
        ticket_url = escape_xml(item.get("ticket_url", ""))
        link_pr = escape_xml(item.get("link_pr", ""))
        story_point = escape_xml(item.get("story_point", ""))

        # Build Hyperlink formula for Ticket ID if URL exists
        if ticket_url:
            cell_b = f'<c r="B{idx}" t="str" s="0"><f>HYPERLINK("{ticket_url}", "{ticket_id}")</f><v>{ticket_id}</v></c>'
        else:
            cell_b = f'<c r="B{idx}" t="inlineStr" s="0"><is><t>{ticket_id}</t></is></c>'

        cell_a = f'<c r="A{idx}" t="inlineStr" s="0"><is><t>{status}</t></is></c>'
        cell_c = f'<c r="C{idx}" t="inlineStr" s="2"><is><t>{link_pr}</t></is></c>'
        cell_d = f'<c r="D{idx}" t="inlineStr" s="0"><is><t>{story_point}</t></is></c>'

        rows_xml.append(f'''    <row r="{idx}">
      {cell_a}
      {cell_b}
      {cell_c}
      {cell_d}
    </row>''')

    sheet1_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
  <cols>
    <col min="1" max="1" width="15" customWidth="1"/>
    <col min="2" max="2" width="20" customWidth="1"/>
    <col min="3" max="3" width="55" customWidth="1"/>
    <col min="4" max="4" width="15" customWidth="1"/>
  </cols>
  <sheetData>
{"\n".join(rows_xml)}
  </sheetData>
</worksheet>'''

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('[Content_Types].xml', content_types)
        z.writestr('_rels/.rels', dot_rels)
        z.writestr('xl/_rels/workbook.xml.rels', workbook_rels)
        z.writestr('xl/workbook.xml', workbook_xml)
        z.writestr('xl/styles.xml', styles_xml)
        z.writestr('xl/worksheets/sheet1.xml', sheet1_xml)

    with open(output_path, 'wb') as f:
        f.write(buffer.getvalue())

    print(f"Successfully exported Excel to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 export_excel.py <input_json_path> <output_xlsx_path>")
        sys.exit(1)

    json_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    create_excel(data, output_path)
