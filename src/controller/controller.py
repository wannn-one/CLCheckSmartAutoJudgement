from loguru import logger
import sys
import os
import glob
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

            if lvl in ["ERROR", "CRITICAL"]:
                tag = "error"
            elif lvl == "WARNING":
                tag = "warning"
            elif lvl == "SUCCESS":
                tag = "success"
            else:
                tag = "info"

            self.view.append_log(msg.record["message"], tag)

        logger.add(gui_sink, format="{message}")

    def run_scan(self):
        inputs = self.view.get_inputs()
        
        if not inputs['excel']:
            self.view.alert("Error", "Please select a Folder or File path!", True)
            return

        self.view.clear_logs()
        self.view.append_log("CONNECTING TO PERFORCE...", "info")
        
        if os.system("p4 info >nul 2>&1") != 0:
             self.view.append_log("P4 CLI not reachable! Please install Perforce & Add to PATH.", "error")
             return

        t = threading.Thread(target=self._process_background, args=(inputs,))
        t.start()

    def _process_background(self, inputs):
        input_path = inputs['excel']
        col_name = inputs['col_name']
        
        # 1. Check the path if its a single file or a folder
        if os.path.isfile(input_path) and input_path.endswith(('.xlsm', '.xlsx')):
            files_to_process = [input_path]
        elif os.path.isdir(input_path): # Search all .xlsm file on that folder
            files_to_process = glob.glob(os.path.join(input_path, "*.xlsm"))
        else:
            self.view.append_log(" Error: Invalid path! Please enter the folder that contain CLCheck files.", "error")
            return

        # 2. Validate number of files
        if not files_to_process:
            self.view.append_log(" Warning: No .xlsm files were found in that folder", "warning")
            return

        self.view.append_log(f" Found {len(files_to_process)} excel file(s) to process...", "info")
        
        # 3. Looping process
        success_count = 0
        for i, file_path in enumerate(files_to_process, 1):
            filename = os.path.basename(file_path)
            self.view.append_log("-" * 60, "info")
            self.view.append_log(f"[{i}/{len(files_to_process)}] Processing: {filename}", "info")
            
            # Scan and process
            result_df, status = self.model.scan_excel_and_process(file_path, col_name)
            
            if result_df is not None:
                status_save = ExcelProcessor.save(file_path, result_df, col_name)
                
                if status_save == "OK":
                    self.view.append_log(f" SUCCESS: Report saved to {filename}", "success")
                    success_count += 1
                else:
                    self.view.append_log(f" SAVE FAILED [{filename}]: {status_save}", "error")
            else:
                self.view.append_log(f" SCAN ERROR [{filename}]: {status}", "error")

        # 4. Show Final Summary
        self.view.append_log("-" * 60, "info")
        self.view.append_log(f" PROCESS DONE: {success_count} from {len(files_to_process)} file(s) updated successfully!", "success")