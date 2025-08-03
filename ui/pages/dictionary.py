import tkinter as tk
from tkinter import ttk
from services import task_service, progress_service, progress_unit_service, progress_type_service

class DictionaryPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        for i in range(6):
            self.grid_columnconfigure(i, weight=1, uniform="a")
        for j in range(7):
            self.grid_rowconfigure(j, weight=0)

        # ページタイトル
        title_label = ttk.Label(self, text="課題登録", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="nsew")

        # 遷移ボタン
        nav_log_progress = ttk.Button(self, text="進捗記録", command=lambda: controller.show_frame("LogProgressPage"))
        nav_log_progress.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")


    def on_submit(self):
        print("submit")