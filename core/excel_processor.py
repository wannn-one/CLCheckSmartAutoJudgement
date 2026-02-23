import os
import pandas as pd
import win32com.client
from config.settings import EXCEL

class ExcelProcessor:
    @staticmethod
    def load_and_prepare(excel_path, path_col_name):
        """Membaca file Excel, mencari baris header yang tepat, dan menyiapkan kolom output."""
        try:
            with pd.ExcelFile(excel_path) as xl_file:
                if EXCEL.DEFAULT_SHEET_NAME not in xl_file.sheet_names:
                    return None, f"Sheet '{EXCEL.DEFAULT_SHEET_NAME}' tidak ditemukan!"

            df_temp = pd.read_excel(excel_path, sheet_name=EXCEL.DEFAULT_SHEET_NAME, header=None, nrows=EXCEL.MAX_HEADER_ROWS_TO_CHECK)
            header_row_index = -1
            
            for idx, row in df_temp.iterrows():
                row_values = [str(x).strip() for x in row.values]
                if path_col_name in row_values:
                    header_row_index = idx
                    break
            
            if header_row_index == -1:
                return None, f"Kolom '{path_col_name}' tidak ditemukan di {EXCEL.MAX_HEADER_ROWS_TO_CHECK} baris pertama!"
            
            df = pd.read_excel(excel_path, sheet_name=EXCEL.DEFAULT_SHEET_NAME, header=header_row_index)
            df.columns = [str(c).strip() for c in df.columns]
            
            if path_col_name not in df.columns:
                 return None, f"Kolom '{path_col_name}' gagal dibaca."
            
            if 'Target CL' not in df.columns:
                return None, "Kolom 'Target CL' tidak ditemukan di Excel."

            if 'Necessity of Evaluation' not in df.columns:
                df['Necessity of Evaluation'] = ""
            if 'Implementation or Not' not in df.columns:
                df['Implementation or Not'] = ""
            if 'Reason' not in df.columns:
                df['Reason'] = ""

            return df, "OK"
        except Exception as e:
            return None, str(e)

    @staticmethod
    def save(excel_path, df, path_col_name):
        """Menyimpan hasil dengan menimpa Microsoft Excel asli"""
        excel = None
        wb = None
        try:
            # win32com butuh abs_path
            abs_path = os.path.abspath(excel_path)
            
            # Buka aplikasi Excel di background (tidak terlihat)
            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = False
            excel.DisplayAlerts = False # Matikan popup peringatan Excel

            # Buka workbook
            wb = excel.Workbooks.Open(abs_path)
            ws = wb.Sheets(EXCEL.DEFAULT_SHEET_NAME)

            # 1. Cari lokasi baris Header
            header_row_idx = None
            max_col = ws.UsedRange.Columns.Count
            
            for r in range(1, EXCEL.MAX_HEADER_ROWS_TO_CHECK + 1):
                for c in range(1, max_col + 1):
                    val = str(ws.Cells(r, c).Value).strip()
                    if val == path_col_name:
                        header_row_idx = r
                        break
                if header_row_idx:
                    break

            if not header_row_idx:
                wb.Close(SaveChanges=False)
                excel.Quit()
                return "Error: Header kolom tidak ditemukan."

            # 2. Petakan letak (index) setiap kolom
            headers = {}
            for c in range(1, max_col + 5): # Tambah jarak buffer
                val = str(ws.Cells(header_row_idx, c).Value).strip()
                if val and val != "None":
                    headers[val] = c

            # 3. Tulis hasil dari DataFrame
            for i, row_data in enumerate(df.to_dict('records')):
                excel_row = header_row_idx + 1 + i
                
                val_nec = str(row_data.get('Necessity of Evaluation', '')).replace('nan', '')
                val_imp = str(row_data.get('Implementation or Not', '')).replace('nan', '')
                val_rsn = str(row_data.get('Reason', '')).replace('nan', '')
                
                ws.Cells(excel_row, headers['Necessity of Evaluation']).Value = val_nec
                ws.Cells(excel_row, headers['Implementation or Not']).Value = val_imp
                ws.Cells(excel_row, headers['Reason']).Value = val_rsn

            # 4. Save
            wb.Save()
            wb.Close()
            excel.Quit()
            return "OK"

        except Exception as e:
            # Jika ada error, pastikan Excel di-close agar tidak nyangkut di Task Manager
            if wb:
                try: wb.Close(SaveChanges=False)
                except: pass
            if excel:
                try: excel.Quit()
                except: pass
            return f"COM Error: {str(e)}"