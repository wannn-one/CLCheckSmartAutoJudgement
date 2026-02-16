import pandas as pd
from config.settings import EXCEL

class ExcelProcessor:
    @staticmethod
    def load_and_prepare(excel_path, path_col_name):
        """Membaca file Excel, mencari baris header yang tepat, dan menyiapkan kolom output."""
        try:
            xl_file = pd.ExcelFile(excel_path)
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
            if 'Reason' not in df.columns:
                df['Reason'] = ""

            return df, "OK"
        except Exception as e:
            return None, str(e)

    @staticmethod
    def save(df, output_path):
        """Menyimpan DataFrame kembali ke Excel."""
        df.to_excel(output_path, index=False)