#!/usr/bin/env python3
"""
Master Generator Script for 50 Excel Antigravity Demo Workspaces.
Orchestrates generation across all 6 departments:
1. 01-nhan-su (9 exercises)
2. 02-ke-toan (9 exercises)
3. 03-kinh-doanh (9 exercises)
4. 04-marketing (8 exercises)
5. 05-kho-van (8 exercises)
6. 06-hanh-chinh (7 exercises)
Total: 50 fully functional Antigravity workspaces.
"""

import sys
import time
from pathlib import Path

# Add depts to sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR / "depts"))

import dept_01_nhan_su
import dept_02_ke_toan
import dept_03_kinh_doanh
import dept_04_marketing
import dept_05_kho_van
import dept_06_hanh_chinh

def main():
    start_time = time.time()
    print("=================================================================")
    print("🚀 STARTING BATCH GENERATION OF 50 EXCEL ANTIGRAVITY WORKSPACES")
    print("=================================================================\n")

    dept_01_nhan_su.generate()
    dept_02_ke_toan.generate()
    dept_03_kinh_doanh.generate()
    dept_04_marketing.generate()
    dept_05_kho_van.generate()
    dept_06_hanh_chinh.generate()

    elapsed = time.time() - start_time
    print("\n=================================================================")
    print(f"🎉 GENERATION COMPLETED IN {elapsed:.2f} SECONDS!")
    print("=================================================================")

if __name__ == "__main__":
    main()
