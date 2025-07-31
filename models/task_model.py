import sqlite3

DB_PATH = "db/progress.db"

def get_all_tasks():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, task, total_count, progress FROM task")
    rows = cur.fetchall()
    conn.close()
    return rows

def create_task(task, progress_type_id, total_count):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO task (task, progress_type_id, total_count, progress) VALUES (?, ?, ?, ?)",
        (task, progress_type_id, total_count, 0)
    )
    conn.commit()
    conn.close()

def update_task_progress(task_id, new_progress):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE task SET progress = ? WHERE id = ?", (new_progress, task_id))
    conn.commit()
    conn.close()
