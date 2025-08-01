import sqlite3
from datetime import datetime

DB_PATH = "db/progress.db"

def insert_progress(task_id, progress_value):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    now = datetime.now().isoformat()
    cur.execute(
        "INSERT OR REPLACE INTO progresses (task_id, progress_value, updated_at) VALUES (?, ?, ?)",
        (task_id, progress_value, now)
    )
    conn.commit()
    conn.close()

def get_total_progress_for_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT SUM(progress_value) FROM progresses WHERE task_id = ?", (task_id,))
    total = cur.fetchone()[0] or 0
    conn.close()
    return total

def fetch_all_progresses():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT task_id, progress_value, progress_date FROM progresses")
    progresses = cur.fetchall() 
    conn.close()
    return progresses