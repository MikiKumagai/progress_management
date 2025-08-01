import tkinter as tk
from tkinter import ttk
from services import task_service, progress_service, progress_unit_service, progress_type_service

class TaskSetupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # ラベル（ページタイトル）
        title_label = ttk.Label(self, text="新規登録", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=12, padx=5, pady=10, sticky="nsew")

        # タスク
        name_label = tk.Label(self, text="タスク名")
        name_label.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.name = tk.Entry(self, width=40)
        self.name.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky="nsew")

        # 進捗単位
        self.progress_units = progress_unit_service.get_progress_units()
        progress_unit_list = [progress_unit[1] for progress_unit in self.progress_units]
        label = ttk.Label(self, text="進捗単位")
        label.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.progress_unit = ttk.Combobox(self, values=progress_unit_list, state="readonly")
        self.progress_unit.current(0)
        self.progress_unit.grid(row=2, column=1, columnspan=5, padx=5, pady=5, sticky="nsew")

        # 入力形式
        self.progress_types = progress_type_service.get_progress_types()
        progress_type_list = [progress_type[1] for progress_type in self.progress_types]
        label = ttk.Label(self, text="入力形式")
        label.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.progress_type = ttk.Combobox(self, values=progress_type_list, state="readonly")
        self.progress_type.current(0)
        self.progress_type.grid(row=3, column=1, columnspan=5, padx=5, pady=5, sticky="nsew")

        # ゴール
        total_count_label = tk.Label(self, text="ゴール")
        total_count_label.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        self.total_count = tk.Entry(self, width=40)
        self.total_count.grid(row=4, column=1, columnspan=5, padx=5, pady=5, sticky="nsew")

        # 登録ボタン
        add_button = tk.Button(self, text="登録", command=self.on_submit)
        add_button.grid(row=5, column=5, padx=5, pady=5, sticky="nsew")

        # 遷移ボタン
        nav_log_progress = tk.Button(self, text="進捗記録", command=lambda: controller.show_frame("LogProgressPage"))
        nav_log_progress.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

    def on_submit(self):
        name = self.name.get()
        selected_progress_unit = self.progress_unit.current()
        progress_unit_id = self.progress_units[selected_progress_unit][0]
        selected_progress_type = self.progress_type.current()
        progress_type_id = self.progress_types[selected_progress_type][0]
        total_count = self.total_count.get()
        task_service.add_task(name, progress_unit_id, progress_type_id, total_count)
