import tkinter as tk
import sqlite3
from tkinter import messagebox
import sys

# ログファイルを開く（追記モード）
log_file = open("app_log.txt", "a")

def log_print(*args, **kwargs):
    print(*args, **kwargs)
    print(*args, **kwargs, file=log_file)
    log_file.flush()

# 以降、printの代わりにlog_printを使う
log_print("アプリ起動しました")

# SQLiteのDBファイルを作成・接続
conn = sqlite3.connect("progress.db")
cur = conn.cursor()

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

# GUI作成
root = tk.Tk()
root.title("学習進捗管理")
root.geometry("1400x900")

title = tk.Label(root, text="進捗確認")
title.pack()

# 入力欄
label = tk.Label(root, text="task")
label.pack()
task = tk.Entry(root, width=40)
task.pack(pady=10)

label = tk.Label(root, text="entry")
label.pack()
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# ボタン
add_button = tk.Button(root, text="submit", command=add_task)
add_button.pack()

# 登録された内容表示
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# 最初に表示更新
update_listbox()

root.mainloop()

# アプリ終了時に接続を閉じる（必要なら）
conn.close()
log_print("アプリ終了しました")
