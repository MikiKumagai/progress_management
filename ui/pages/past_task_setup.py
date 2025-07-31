import tkinter as tk
import sqlite3
from tkinter import messagebox
import sys

# 学習内容をDBに追加する関数
def add_task():
    task = task.get()
    if task.strip() == "":
        messagebox.showwarning("注意", "内容を入力してください")
        return
    cur.execute("INSERT INTO progress (task) VALUES (?)", (task,))
    conn.commit()
    task.delete(0, tk.END)
    update_listbox()

# 登録された内容を表示する関数
def update_listbox():
    listbox.delete(0, tk.END)
    cur.execute("SELECT id, task FROM progress ORDER BY id DESC")
    for row in cur.fetchall():
        listbox.insert(tk.END, f"{row[0]}: {row[1]}")

title = tk.Label(root, text="タスク登録")
title.pack()

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

# 登録された内容表示
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# 最初に表示更新
update_listbox()

