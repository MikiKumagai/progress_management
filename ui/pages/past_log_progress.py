import tkinter as tk
import sqlite3
from tkinter import messagebox
import sys
from services import task_service, progress_service

# 選択された値を表示する関数
def show_selection():
    print("選択された値:", combo.get())

# 進捗記録ページ
title = tk.Label(root, text="進捗記録")
title.pack()

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

# 最初に表示更新
task_service.update_listbox()

root.mainloop()

