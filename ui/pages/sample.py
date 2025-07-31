import tkinter as tk
from tkinter import ttk

class TemplatePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # ラベル（ページタイトル）
        title_label = ttk.Label(self, text="Template Page", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # 入力項目（例：エントリー）
        self.entry = ttk.Entry(self)
        self.entry.pack(pady=5)

        # ボタン（処理実行）
        submit_button = ttk.Button(self, text="Submit", command=self.on_submit)
        submit_button.pack(pady=5)

        # 戻るボタン（他ページへ遷移）
        back_button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=20)

    def on_submit(self):
        input_value = self.entry.get()
        print(f"入力値: {input_value}")
        # ここでservice層などの処理呼び出しもできる
