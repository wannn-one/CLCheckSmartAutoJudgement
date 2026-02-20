# mvc/view.py
from tkinter import messagebox

import customtkinter as ctk
from customtkinter import filedialog
from config.settings import GUI, LOG, FONT, resource_path
from PIL import Image

ctk.set_appearance_mode(GUI.APPEARANCE_MODE)
ctk.set_default_color_theme(GUI.COLOR_THEME)

class LogicTracerView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(GUI.WINDOW_TITLE)
        self.geometry(GUI.WINDOW_GEOMETRY)
        self.iconbitmap(resource_path("resources/app_icon.ico"))
        self.controller = None
        self._setup_ui()

    def set_controller(self, controller):
        self.controller = controller

    def _setup_ui(self):
        self.grid_columnconfigure(1, 
                                  weight=1)
        self.grid_rowconfigure(4, 
                               weight=1)

        ctk.CTkLabel(self, 
                     text=GUI.WINDOW_TITLE, 
                     font=(FONT.GENERAL, 24, "bold")).grid(row=0, 
                                                           column=0, 
                                                           columnspan=3, 
                                                           pady=20)

        # 1. INPUT EXCEL
        ctk.CTkLabel(self, text="CLCheck Excel (.xlsm):", 
                     font=(FONT.GENERAL, 16)).grid(row=1, 
                                                   column=0, 
                                                   padx=20, 
                                                   pady=(0, 10), 
                                                   sticky="w")
        self.entry_excel = ctk.CTkEntry(self, 
                                        placeholder_text="Path to CLCheck File ...")
        self.entry_excel.grid(row=1, 
                              column=1, 
                              padx=10, 
                              pady=(0, 10), 
                              sticky="ew")

        ctk.CTkButton(self,
                      width=25,
                      text="",
                      fg_color="transparent",
                      
                      
                      image=ctk.CTkImage((Image.open(resource_path("resources/folder.png"))), 
                                         size=(25,25)),
                      command=lambda: self._browse(self.entry_excel)).grid(row=1, 
                                                                           column=2, 
                                                                           padx=20, 
                                                                           pady=(0, 10))

        # ==============================================================================

        # 2. CONFIG EXCEL
        ctk.CTkLabel(self, 
                     text="Depot Path Column Name:",
                     font=(FONT.GENERAL, 16)).grid(row=2, 
                                                          column=0, 
                                                          padx=20, 
                                                          pady=(0, 10), 
                                                          sticky="w")
        self.entry_col_name = ctk.CTkEntry(self)
        self.entry_col_name.insert(0, "FIle Path")
        self.entry_col_name.grid(row=2, 
                                 column=1, 
                                 padx=10, 
                                 pady=(0, 10), 
                                 sticky="ew") 
        
        # ==============================================================================

        # 3. RUN BUTTON
        self.btn_run = ctk.CTkButton(self, 
                                     text="CONNECT P4 & SCAN", 
                                     height=50, 
                                     font=(FONT.GENERAL, 16, "bold"), 
                                     fg_color="#E02828", 
                                     hover_color="#B00000",
                                     command=self._on_run)
        self.btn_run.grid(row=3, 
                          column=0, 
                          columnspan=3, 
                          pady=(10, 20), 
                          padx=20, 
                          sticky="ew")
        
        # ==============================================================================

        # 4. LOGS
        self.text_area = ctk.CTkTextbox(self, 
                                        font=(FONT.CODE, 16))
        self.text_area.grid(row=4, 
                            column=0, 
                            columnspan=3, 
                            padx=20, 
                            pady=(0,20), 
                            sticky="nsew")
        
        # Setup Log
        self.text_area.tag_config("info", foreground=LOG.INFO)
        self.text_area.tag_config("success", foreground=LOG.SUCCESS)
        self.text_area.tag_config("warning", foreground=LOG.WARNING)
        self.text_area.tag_config("error", foreground=LOG.ERROR)
        
        self.append_log("Ready. Ensure you are logged into Perforce (p4 login) in terminal.", "info")

    def _browse(self, entry):
        path = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx *.xlsm")])
        if path:
            entry.delete(0, ctk.END)
            entry.insert(0, path)

    def _on_run(self):
        if self.controller:
            self.controller.run_scan()

    def get_inputs(self):
        return {
            "excel": self.entry_excel.get(),
            "col_name": self.entry_col_name.get()
        }

    def clear_logs(self): 
        self.text_area.delete("1.0", ctk.END)
        
    def append_log(self, msg, tag="info"):
        prefix = f"[{tag.upper()}] "
        self.text_area.insert(ctk.END, f"{prefix}{msg}\n", tag)
        self.text_area.see(ctk.END)
        
    def alert(self, t, m, e=False):
        if e: 
            messagebox.showerror(t, m)
        else: 
            messagebox.showinfo(t, m)