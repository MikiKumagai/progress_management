import sqlite3
from datetime import datetime

DB_PATH = "db/progress.db"

# 進捗記録画面：入力形式
def select_progress_type(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT 
      pt.name 
    FROM 
      tasks t 
      INNER JOIN progress_types pt ON pt.id = t.progress_type_id 
    WHERE t.id = ?
    """, (task_id,))
    return cursor.fetchone()

# 進捗記録画面：入力形式のリスト
def select_progress_types():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM progress_types")
    return cursor.fetchall() 