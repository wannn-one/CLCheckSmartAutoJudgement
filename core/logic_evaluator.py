import re
from config.settings import EVALUATOR

class LogicEvaluator:
    @staticmethod
    def evaluate(content_now, content_prev):
        if content_now is None: 
            return "Y", "Gagal membaca file di Target CL"
        if content_prev is None: 
            return "Y", "Gagal membaca file versi sebelumnya (File Baru?)"

        regex_pattern = r'\b[A-Z_][A-Z0-9_]{2,}\b'
        tokens_now = re.findall(regex_pattern, content_now)
        tokens_prev = re.findall(regex_pattern, content_prev)

        def is_relevant(token):
            if token in EVALUATOR.IGNORED_KEYWORDS: 
                return False
            
            if any(token.startswith(p) for p in EVALUATOR.IGNORED_PREFIXES): 
                return False
            
            if token.startswith('__') and token.endswith('__'): 
                return False # Include Guard
            
            return True
        
        def get_unique_ordered(tokens):
            unique_list = []
            seen = set()
            for t in tokens:
                if is_relevant(t) and t not in seen:
                    unique_list.append(t)
                    seen.add(t)
            return unique_list

        list_now = get_unique_ordered(tokens_now)
        list_prev = get_unique_ordered(tokens_prev)

        if not list_prev and not list_now:
            return 'N', 'Aman (Tidak ada definisi logika yang terdeteksi)'
        if list_prev == list_now:
            return 'N', 'Aman (Susunan logika tidak berubah)'
            
        old_len = len(list_prev)
        if list_now[:old_len] == list_prev:
            return 'N', 'Aman: Penambahan item aman di baris terbawah (Append)'

        set_now = set(list_now)
        set_prev = set(list_prev)
        new_items = set_now - set_prev
        deleted_items = set_prev - set_now
        
        details = []
        if new_items:
            details.append(f"INSERTED: {list(new_items)[:3]}")
        if deleted_items:
            details.append(f"DELETED: {list(deleted_items)[:3]}")
            
        if not details: 
            details.append("RE-ORDERED (Tukar Posisi Item)")

        return "Y", f"RISIKO INDEX SHIFTING! ({' | '.join(details)})"