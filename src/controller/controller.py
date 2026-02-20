# mvc/controller.py
from loguru import logger
import sys
import os
import threading
from core.excel_processor import ExcelProcessor

class LogicTracerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self._setup_logging()

    def _setup_logging(self):
        logger.remove()
        
        if sys.stderr is not None: # if on development, dont log the terminal log
            logger.add(sys.stderr, format="<level>{message}</level>")

        def gui_sink(msg):
            lvl = msg.record["level"].name
            tag = "error" if lvl in ["ERROR", "CRITICAL"] else "warning" if lvl == "WARNING" else "success" if lvl == "SUCCESS" else "info"
            self.view.append_log(msg.record["message"], tag)
        logger.add(gui_sink, format="{message}")

    def run_scan(self):
        inputs = self.view.get_inputs()
        
        if not inputs['excel']:
            self.view.alert("Error", "Please select CLCheck Excel file!", True)
            return

        self.view.clear_logs()
        self.view.append_log("CONNECTING TO PERFORCE...", "info")
        
        if os.system("p4 info >nul 2>&1") != 0:
             self.view.append_log("P4 CLI not reachable! Please install Perforce & Add to PATH.", "error")
             return

        t = threading.Thread(target=self._process_background, args=(inputs,))
        t.start()

    def _process_background(self, inputs):
        result_df, status = self.model.scan_excel_and_process(
            inputs['excel'], 
            inputs['col_name']
        )
        
        if result_df is not None:
            output_path = inputs['excel'].replace(".xlsm", ".xlsx").replace(".xlsx", "_P4_CHECKED.xlsx")
            try:
                ExcelProcessor.save(result_df, output_path)
                self.view.append_log("-" * 50, "info")
                self.view.append_log(f"REPORT GENERATED:", "success")
                self.view.append_log(f"{output_path}", "success")
            except Exception as e:
                self.view.append_log(f"Save Error: {e}", "error")
        else:
            self.view.append_log(f"Scan Error: {status}", "error")