import tkinter as tk
from tkinter import ttk

class ProgressOverviewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # ラベル（ページタイトル）
        title_label = ttk.Label(self, text="進捗確認", font=("Helvetica", 16))
        title_label.pack(pady=10)
        
        # テキスト
        title_label = ttk.Label(self, text="作成中")
        title_label.pack(pady=10)

        # 遷移ボタン
        nav_task_setup = tk.Button(self, text="進捗記録", command=lambda: controller.show_frame("LogProgressPage"))
        nav_task_setup.pack()

    def on_submit(self):
        input_value = self.entry.get()
        print(f"入力値: {input_value}")
        # ここでservice層などの処理呼び出しもできる
