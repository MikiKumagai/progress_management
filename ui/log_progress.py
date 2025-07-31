import tkinter as tk
import sqlite3
from tkinter import messagebox
import sys

# ログファイルを開く（追記モード）
log_file = open("log/app_log.txt", "a")

def log_print(*args, **kwargs):
    print(*args, **kwargs)
    print(*args, **kwargs, file=log_file)
    log_file.flush()

# 以降、printの代わりにlog_printを使う
log_print("アプリ起動しました")

# SQLiteのDBファイルを作成・接続
conn = sqlite3.connect("db/progress.db")
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
    cur.execute("SELECT name FROM tasks ORDER BY id DESC")
    for row in cur.fetchall():
        options.add(row[0])
        
# 選択された値を表示する関数
def show_selection():
    print("選択された値:", combo.get())

# GUI作成
root = tk.Tk()
root.title("学習進捗管理")
root.geometry("1400x900")

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
add_button = tk.Button(root, text="submit", command=add_task)
add_button.pack()

# 最初に表示更新
update_listbox()
get_task_name()

root.mainloop()

# アプリ終了時に接続を閉じる（必要なら）
conn.close()
log_print("アプリ終了しました")
