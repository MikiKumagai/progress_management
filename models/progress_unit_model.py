import sqlite3
from datetime import datetime

DB_PATH = "db/progress.db"

# 進捗記録画面：進捗単位
def select_progress_unit(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT 
      pu.name 
    FROM 
      tasks t 
      INNER JOIN progress_units pu ON pu.id = t.progress_unit_id 
    WHERE t.id = ?
    """, (task_id,))
    return cursor.fetchone()

# 進捗記録画面：進捗単位のリスト
def select_progress_units():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM progress_units")
    return cursor.fetchall() 