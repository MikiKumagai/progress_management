import tkinter as tk
from tkinter import ttk
from presentations import table

class ProgressOverviewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # タイトル
        title_label = ttk.Label(self, text="進捗確認", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # 表（Treeview）
        columns = ("task_id", "progress_value", "progress_date")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=10)
        self.tree.heading("task_id", text="タスクID")
        self.tree.heading("progress_value", text="進捗")
        self.tree.heading("progress_date", text="更新日")

        # カラム幅（必要に応じて調整してOK）
        self.tree.column("task_id", width=100, anchor="center")
        self.tree.column("progress_value", width=100, anchor="center")
        self.tree.column("progress_date", width=150, anchor="center")

        self.tree.pack(padx=10, pady=10, fill="x")

        # DataFrame取得
        df = table.get_progress_summary()

        # DataFrameの各行をTreeviewに追加
        for _, row in df.iterrows():
            self.tree.insert("", "end", values=(row["task_id"], row["progress_value"], row["progress_date"]))

        # ページ遷移ボタン
        nav_task_setup = ttk.Button(self, text="進捗記録", command=lambda: controller.show_frame("LogProgressPage"))
        nav_task_setup.pack(pady=10)
