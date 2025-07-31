import tkinter as tk
from tkinter import ttk

class LogProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # ラベル（ページタイトル）
        title_label = ttk.Label(self, text="進捗記録", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Comboboxの作成
        options = []
        combo = ttk.Combobox(root, values=options, state="readonly")
        combo.current(0)
        combo.pack()
        btn = tk.Button(root, text="確認", command=show_selection)
        btn.pack()

        # 入力欄
        label = tk.Label(root, text="progress_value")
        label.pack()
        progress_value = tk.Entry(root, width=40)
        progress_value.pack(pady=10)

        # ボタン
        add_button = tk.Button(root, text="submit", command=progress_service.add_progress)
        add_button.pack()

        # ボタン
        nav_task_setup = tk.Button(root, text="submit", command=progress_service.add_progress)
        nav_task_setup.pack()

    def on_submit(self):
        input_value = self.entry.get()
        print(f"入力値: {input_value}")
        # ここでservice層などの処理呼び出しもできる
