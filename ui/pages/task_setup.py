import tkinter as tk
from tkinter import ttk

class TaskSetupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # ラベル（ページタイトル）
        title_label = ttk.Label(self, text="学習進捗管理", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # 入力欄
        label = tk.Label(root, text="name")
        label.pack()
        name = tk.Entry(root, width=40)
        name.pack(pady=10)

        label = tk.Label(root, text="progress_unit")
        label.pack()
        progress_unit = tk.Entry(root, width=40)
        progress_unit.pack(pady=10)

        label = tk.Label(root, text="total_count")
        label.pack()
        total_count = tk.Entry(root, width=40)
        total_count.pack(pady=10)

        # ボタン
        add_button = tk.Button(root, text="submit", command=add_task)
        add_button.pack()

    def on_submit(self):
        input_value = self.entry.get()
        print(f"入力値: {input_value}")
        # ここでservice層などの処理呼び出しもできる
