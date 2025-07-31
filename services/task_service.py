from models import task_model, progress_model

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