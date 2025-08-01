import sqlite3
from datetime import datetime

DB_PATH = "db/progress.db"

# 進捗記録ページ：進捗記録
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

# 進捗確認ページ：表取得
def fetch_all_progresses():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""SELECT 
        t.name, 
        p.progress_value, 
        p.progress_date 
        FROM progresses p
        INNER JOIN tasks t ON p.task_id = t.id""")
    progresses = cur.fetchall() 
    conn.close()
    return progresses