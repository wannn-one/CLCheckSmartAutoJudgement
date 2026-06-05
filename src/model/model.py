# mvc/model.py
from loguru import logger
from core.p4_connector import P4Connector
from core.logic_evaluator import LogicEvaluator
from core.excel_processor import ExcelProcessor

class LogicTracerModel:
    def scan_excel_and_process(self, excel_path, path_col_name):
        logger.info(f" Membaca Excel Tracker: {excel_path}")

        # 1. Load Data (tetap pakai pandas untuk baca awal)
        df, status = ExcelProcessor.load_and_prepare(excel_path, path_col_name)
        if df is None:
            return None, status

        logger.info(f" Mulai mengecek ke Perforce... (Membaca {len(df)} baris data)")

        results = [] 

        # 2. Proses tiap baris
        for index, row in df.iterrows():
            depot_path = str(row[path_col_name]).strip()
            target_cl  = str(row['Target CL']).strip().replace('.0', '')

            # Validasi Dasar
            if not depot_path.endswith('.h'):
                results.append({
                    'depot_path'   : depot_path,
                    'necessity'    : 'N',
                    'impl_or_not'  : 'N',
                    'reason'       : 'Bukan file header (.h)'
                })
                continue

            if target_cl.lower() in ['nan', 'none', '']:
                results.append({
                    'depot_path'   : depot_path,
                    'necessity'    : 'N',
                    'impl_or_not'  : 'N',
                    'reason'       : 'Target CL kosong'
                })
                continue

            logger.info(f"Checking CL {target_cl} | {depot_path}...")

            # Interaksi P4
            rev_now = P4Connector.get_revision_at_cl(depot_path, target_cl)
            if not rev_now:
                results.append({
                    'depot_path'   : depot_path,
                    'necessity'    : 'Y',
                    'impl_or_not'  : '',
                    'reason'       : 'Error: Gagal mendapatkan Nomor Revisi (#) dari Perforce'
                })
                logger.error(f" Gagal mendapat revisi untuk CL {target_cl}")
                continue

            logger.info(f" > Terdeteksi sebagai Revision #{rev_now}")
            content_now  = P4Connector.get_file_content(depot_path, f"#{rev_now}")

            content_prev = None
            if rev_now > 1:
                content_prev = P4Connector.get_file_content(depot_path, f"#{rev_now - 1}")
                logger.info(f" > Berhasil mendapatkan Revision sebelumnya #{rev_now - 1}")

            # Evaluasi
            necessity, reason = LogicEvaluator.evaluate(content_now, content_prev)

            # Tentukan "Implementation or Not"
            # Jika necessity = N → tidak perlu implementasi (N)
            # Jika necessity = Y → perlu ditinjau lebih lanjut, biarkan designer isi (kosong/Y)
            impl_or_not = 'N' if necessity == 'N' else 'Y'

            results.append({
                'depot_path'   : depot_path,
                'necessity'    : necessity,
                'impl_or_not'  : impl_or_not,
                'reason'       : reason
            })

            if necessity == "Y":
                logger.warning(f"FLAG: {reason}")
            else:
                logger.success(f"PASS: {reason}")

        return results, "OK"  # ← Return list, bukan df