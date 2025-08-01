import sqlite3

DB_PATH = "db/progress.db"

# 進捗記録ページ：登録値計算用データ取得
def select_total_count(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT total_count FROM tasks WHERE id = ?", (task_id))
    total = cur.fetchone()[0] or 0
    conn.close()
    return total

# 進捗記録ページ：進捗累計を更新
def update_task_progress(task_id, new_progress):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET progress = ? WHERE id = ?", (new_progress, task_id))
    conn.commit()
    conn.close()

# 進捗記録ページ：タスクのリストを取得
def select_tasks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM tasks")
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