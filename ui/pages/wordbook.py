import tkinter as tk
from tkinter import ttk
from services import task_service, progress_service, progress_unit_service, progress_type_service

class WordbookPage(tk.Frame):
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
        
        # 課題名
        name_label = ttk.Label(self, text="課題名")
        name_label.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.name = ttk.Entry(self)
        self.name.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky="nsew")

        # 登録ボタン
        add_button = ttk.Button(self, text="登録", command=self.on_submit)
        add_button.grid(row=5, column=5, padx=5, pady=5, sticky="nsew")

        # バリデーションメッセージ
        self.name_error_label = tk.Label(self, text="", fg="red")
        self.name_error_label.grid(row=6, column=0, columnspan=6, padx=5, pady=5, sticky="e")
        self.count_error_label = tk.Label(self, text="", fg="red")
        self.count_error_label.grid(row=6, column=0, columnspan=6, padx=5, pady=5, sticky="e")

        # 遷移ボタン
        nav_log_progress = ttk.Button(self, text="進捗記録", command=lambda: controller.show_frame("LogProgressPage"))
        nav_log_progress.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")


    def on_submit(self):
        print("onsubmit")