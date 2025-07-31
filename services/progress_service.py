from models import task_model, progress_model

def record_progress(task_id, today_progress):
    # 1. 進捗をprogressテーブルに追加
    progress_model.insert_progress(task_id, today_progress)

    # 2. 合計進捗を更新
    current = progress_model.get_total_progress_for_task(task_id)
    task_model.update_task_progress(task_id, current)

# 学習内容をDBに追加する関数
def add_progress():
    task = task.get()
    if task.strip() == "":
        messagebox.showwarning("注意", "内容を入力してください")
        return
    cur.execute("INSERT INTO progress (task) VALUES (?)", (task,))
    conn.commit()
    task.delete(0, tk.END)
    update_listbox()