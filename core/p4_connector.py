import re
import subprocess
from loguru import logger
from config.settings import P4

class P4Connector:
    @staticmethod
    def get_revision_at_cl(depot_path, cl):
        """Mencari tau file ini ada di Revisi (#) ke-berapa pada CL tertentu."""
        try:
            cmd = f'p4 -Ztag fstat -T headRev "{depot_path}@{cl}"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, errors='ignore', timeout=P4.TIMEOUT)
            
            if result.returncode == 0:
                match = re.search(r'\.\.\.\s+headRev\s+(\d+)', result.stdout)
                if match:
                    return int(match.group(1))
            return None
        except Exception as e:
            logger.error(f"P4 fstat Error pada {depot_path}: {e}")
            return None

    @staticmethod
    def get_file_content(depot_path, revision_specifier=""):
        """Mengambil isi file langsung dari server Perforce."""
        try:
            full_path = f"{depot_path}{revision_specifier}"
            cmd = f'p4 print -q "{full_path}"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, errors='ignore', timeout=P4.TIMEOUT)
            
            if result.returncode != 0:
                return None
            return result.stdout
        except Exception as e:
            logger.error(f"P4 Error pada {full_path}: {e}")
            return None