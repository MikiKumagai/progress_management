import tkinter as tk
from tkinter import ttk

class TaskSetupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # ラベル（ページタイトル）
        title_label = ttk.Label(self, text="新規登録", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # 入力欄
        label = tk.Label(self, text="タスク名")
        label.pack()
        name = tk.Entry(self, width=40)
        name.pack(pady=10)

        label = tk.Label(self, text="進捗単位")
        label.pack()
        progress_unit = tk.Entry(self, width=40)
        progress_unit.pack(pady=10)

        label = tk.Label(self, text="ゴール")
        label.pack()
        total_count = tk.Entry(self, width=40)
        total_count.pack(pady=10)

        # ボタン
        add_button = tk.Button(self, text="登録", command=self.on_submit)
        add_button.pack()

        # 遷移ボタン
        nav_task_setup = tk.Button(self, text="進捗記録", command=lambda: controller.show_frame("LogProgressPage"))
        nav_task_setup.pack()

    def on_submit(self):
        input_value = self.entry.get()
        print(f"入力値: {input_value}")
        # ここでservice層などの処理呼び出しもできる
