import sqlite3
from datetime import datetime

DB_PATH = "db/progress.db"

def insert_progress(task_id, this_progress):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    now = datetime.now().isoformat()
    cur.execute(
        "INSERT OR REPLACE INTO progress (task_id, this_progress, updated_at) VALUES (?, ?, ?)",
        (task_id, this_progress, now)
    )
    conn.commit()
    conn.close()

def get_total_progress_for_task(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT SUM(this_progress) FROM progress WHERE task_id = ?", (task_id,))
    total = cur.fetchone()[0] or 0
    conn.close()
    return total
