import tkinter as tk
from tkinter import ttk
from presentations import progress_table, task_table

class ProgressOverviewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid_propagate(False)
        
        for i in range(6):
            self.grid_columnconfigure(i, weight=1, uniform="a")
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)

        # ラベル（ページタイトル）
        title_label = ttk.Label(self, text="進捗確認", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="nsew")

        # 表（task）
        columns = ("name", "progress", "total_count", "active")
        self.task_tree = ttk.Treeview(self, columns=columns, show="headings")
        self.task_tree.heading("name", text="name")
        self.task_tree.heading("progress", text="progress")
        self.task_tree.heading("total_count", text="total_count")
        self.task_tree.heading("active", text="active")
        self.task_tree.column("name", width=100, anchor="w")
        self.task_tree.column("progress", width=50, anchor="e")
        self.task_tree.column("total_count", width=50, anchor="e")
        self.task_tree.column("active", width=50, anchor="e")
        self.task_tree.grid(row=1, column=0, columnspan=6, padx=5, pady=10, sticky="nsew")

        task_summary = task_table.get_task_summary()
        for _, row in task_summary.iterrows():
            self.task_tree.insert("", "end", values=(row["name"], row["progress"], row["total_count"], row["active"]))

        # 表（progress）
        columns = ("task_name", "progress_value", "progress_date")
        self.progress_tree = ttk.Treeview(self, columns=columns, show="headings")
        self.progress_tree.heading("task_name", text="タスク")
        self.progress_tree.heading("progress_value", text="進捗")
        self.progress_tree.heading("progress_date", text="更新日")
        self.progress_tree.column("task_name", width=100, anchor="w")
        self.progress_tree.column("progress_value", width=50, anchor="e")
        self.progress_tree.column("progress_date", width=150, anchor="e")
        self.progress_tree.grid(row=2, column=0, columnspan=6, padx=5, pady=10, sticky="nsew")

        progress_summary = progress_table.get_progress_summary()
        for _, row in progress_summary.iterrows():
            self.progress_tree.insert("", "end", values=(row["task_name"], row["progress_value"], row["progress_date"]))

        # ページ遷移ボタン
        nav_task_setup = ttk.Button(self, text="進捗記録", command=lambda: controller.show_frame("LogProgressPage"))
        nav_task_setup.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

    def refresh(self):
        # 既存のデータを全部削除
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)

        for item in self.progress_tree.get_children():
            self.progress_tree.delete(item)

        task_summary = task_table.get_task_summary()
        for _, row in task_summary.iterrows():
            self.task_tree.insert("", "end", values=(row["name"], row["progress"], row["total_count"], row["active"]))

        progress_summary = progress_table.get_progress_summary()
        for _, row in progress_summary.iterrows():
            self.progress_tree.insert("", "end", values=(row["task_name"], row["progress_value"], row["progress_date"]))
