import tkinter as tk
from tkinter import ttk
from presentations import progress_table, task_table

class ProgressOverviewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        for i in range(6):
            self.grid_columnconfigure(i, weight=1, uniform="a")
        for j in range(7):
            self.grid_rowconfigure(j, weight=1)

        # ラベル（ページタイトル）
        title_label = ttk.Label(self, text="進捗確認", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="nsew")

        # 表（Treeview）
        columns = ("name", "progress", "total_count", "active")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=10)
        self.tree.heading("name", text="name")
        self.tree.heading("progress", text="progress")
        self.tree.heading("total_count", text="total_count")
        self.tree.heading("active", text="active")
        self.tree.column("name", width=100, anchor="w")
        self.tree.column("progress", width=50, anchor="e")
        self.tree.column("total_count", width=50, anchor="e")
        self.tree.column("active", width=50, anchor="e")
        self.tree.grid(row=1, column=0, columnspan=6, padx=5, pady=10, sticky="nsew")

        task_progress = task_table.get_task_progress()
        for _, row in task_progress.iterrows():
            self.tree.insert("", "end", values=(row["name"], row["progress"], row["total_count"], row["active"]))

        # 表（Treeview）
        columns = ("task_name", "progress_value", "progress_date")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=10)
        self.tree.heading("task_name", text="タスク")
        self.tree.heading("progress_value", text="進捗")
        self.tree.heading("progress_date", text="更新日")
        self.tree.column("task_name", width=100, anchor="w")
        self.tree.column("progress_value", width=50, anchor="e")
        self.tree.column("progress_date", width=150, anchor="e")
        self.tree.grid(row=1, column=0, columnspan=6, padx=5, pady=10, sticky="nsew")

        progress_summary = progress_table.get_progress_summary()
        for _, row in progress_summary.iterrows():
            self.tree.insert("", "end", values=(row["task_name"], row["progress_value"], row["progress_date"]))

        # ページ遷移ボタン
        nav_task_setup = ttk.Button(self, text="進捗記録", command=lambda: controller.show_frame("LogProgressPage"))
        nav_task_setup.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

    def refresh(self):
        # 既存のデータを全部削除
        for item in self.tree.get_children():
            self.tree.delete(item)

        task_progress = task_table.get_task_progress()
        for _, row in task_progress.iterrows():
            self.tree.insert("", "end", values=(row["name"], row["progress"], row["total_count"], row["active"]))

        progress_summary = progress_table.get_progress_summary()
        for _, row in progress_summary.iterrows():
            self.tree.insert("", "end", values=(row["task_name"], row["progress_value"], row["progress_date"]))
