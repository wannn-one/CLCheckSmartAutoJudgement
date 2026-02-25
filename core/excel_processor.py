import os
import pandas as pd
import win32com.client
from config.settings import EXCEL

class ExcelProcessor:
    @staticmethod
    def load_and_prepare(excel_path, path_col_name):
        """Reads the Excel file, uses the specific header row, and prepares the output columns."""
        try:
            with pd.ExcelFile(excel_path) as xl_file:
                if EXCEL.DEFAULT_SHEET_NAME not in xl_file.sheet_names:
                    return None, f"Sheet '{EXCEL.DEFAULT_SHEET_NAME}' not found!"

            # 23rd Row in Excel = Index 22nd in Pandas
            header_row_index = EXCEL.FILE_PATH_HEADER_ROW - 1 

            df = pd.read_excel(excel_path, sheet_name=EXCEL.DEFAULT_SHEET_NAME, header=header_row_index)
            df.columns = [str(c).strip() for c in df.columns]
            
            if path_col_name not in df.columns:
                return None, f"Column '{path_col_name}' failed to read at row {EXCEL.FILE_PATH_HEADER_ROW}."

            if 'Target CL' not in df.columns:
                return None, "The column 'Target CL' was not found in Excel."

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
        """Saves results by overwriting the original Microsoft Excel"""
        excel = None
        wb = None
        try:
            # win32com need abs_path
            abs_path = os.path.abspath(excel_path)
            
            # open Excel on background
            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = False
            excel.DisplayAlerts = False # Turn off Excel warning popups

            # open workbook
            wb = excel.Workbooks.Open(abs_path)
            ws = wb.Sheets(EXCEL.DEFAULT_SHEET_NAME)

            # 1. search header
            header_row_idx = EXCEL.FILE_PATH_HEADER_ROW
            max_col = ws.UsedRange.Columns.Count
            
            val = str(ws.Cells(EXCEL.FILE_PATH_HEADER_ROW, EXCEL.FILE_PATH_HEADER_COL).Value).strip()

            if val != path_col_name:
                wb.Close(SaveChanges=False)
                excel.Quit()
                return f"Error: Expected '{path_col_name}' at row {header_row_idx}, but found '{val}' instead."

            # 2. Map the location (index) of each column
            headers = {}
            for c in range(1, max_col + 5): # buffer
                val = str(ws.Cells(header_row_idx, c).Value).strip()
                if val and val != "None":
                    headers[val] = c

            # 3. write to dataframe
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
            # If there is an error, make sure Excel is closed so it doesn't get stuck in Task Manager.
            if wb:
                try: wb.Close(SaveChanges=False)
                except: pass
            if excel:
                try: excel.Quit()
                except: pass
            return f"COM Error: {str(e)}"