import sqlite3

DB_PATH = "db/progress.db"

# 進捗記録ページ：登録値計算用データ取得
def select_task_data(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT progress, total_count FROM tasks WHERE id = ?", (task_id,))
    progress, total_count = cur.fetchone()
    conn.close()
    return progress, total_count

# 進捗記録ページ：進捗累計を更新
def update_task_progress(task_id, today_progress):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET progress = ? WHERE id = ?", (today_progress, task_id))
    conn.commit()
    conn.close()

# 進捗記録ページ：タスク完了フラグを立てる
def update_task_completion(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET active = False WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# 進捗記録ページ：タスクのリストを取得
def select_tasks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM tasks WHERE active")
    return cursor.fetchall() 

# タスク登録ページ：新規タスク追加
def insert_task(name, progress_unit_id, progress_type_id, total_count):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (name, progress_unit_id, progress_type_id, total_count) VALUES (?, ?, ?, ?)",
        (name, progress_unit_id, progress_type_id, total_count)
    )
    conn.commit()
    conn.close()