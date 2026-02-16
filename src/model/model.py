# mvc/model.py
from loguru import logger
from core.p4_connector import P4Connector
from core.logic_evaluator import LogicEvaluator
from core.excel_processor import ExcelProcessor

class LogicTracerModel:
    def scan_excel_and_process(self, excel_path, path_col_name):
        logger.info(f" Membaca Excel Tracker: {excel_path}")
        
        # 1. Load Data
        df, status = ExcelProcessor.load_and_prepare(excel_path, path_col_name)
        if df is None:
            return None, status

        logger.info(f" Mulai mengecek ke Perforce... (Membaca {len(df)} baris data)")

        # 2. Proses tiap baris
        for index, row in df.iterrows():
            depot_path = str(row[path_col_name]).strip()
            target_cl = str(row['Target CL']).strip().replace('.0', '')
            
            # Validasi Dasar
            if not depot_path.endswith('.h'):
                df.at[index, 'Necessity of Evaluation'] = 'N'
                df.at[index, 'Reason'] = 'Bukan file header (.h)'
                continue
                
            if target_cl.lower() in ['nan', 'none', '']:
                df.at[index, 'Necessity of Evaluation'] = 'N'
                df.at[index, 'Reason'] = 'Target CL kosong'
                continue

            logger.info(f"Checking CL {target_cl} | {depot_path}...")
            
            # Interaksi P4
            rev_now = P4Connector.get_revision_at_cl(depot_path, target_cl)
            if not rev_now:
                df.at[index, 'Necessity of Evaluation'] = 'Y'
                df.at[index, 'Reason'] = 'Error: Gagal mendapatkan Nomor Revisi (#) dari Perforce'
                logger.error(f" Gagal mendapat revisi untuk CL {target_cl}")
                continue
                
            logger.info(f" > Terdeteksi sebagai Revision #{rev_now}")
            content_now = P4Connector.get_file_content(depot_path, f"#{rev_now}")
            
            content_prev = None
            if rev_now > 1:
                content_prev = P4Connector.get_file_content(depot_path, f"#{rev_now - 1}")
                logger.info(f" > Berhasil mendapatkan Revision sebelumnya #{rev_now - 1}")

            # Evaluasi
            necessity, reason = LogicEvaluator.evaluate(content_now, content_prev)
            
            df.at[index, 'Necessity of Evaluation'] = necessity
            df.at[index, 'Reason'] = reason
            
            if necessity == "Y":
                logger.warning(f"FLAG: {reason}")
            else:
                logger.success(f"PASS: {reason}")

        return df, "OK"