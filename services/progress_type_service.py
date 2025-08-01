from models import task_model, progress_model
import sqlite3

# TODO: SQLをtask_modelに移動

# 進捗記録画面：入力形式
def get_progress_type(task_id):
    conn = sqlite3.connect("db/progress.db")
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
def get_progress_types():
    conn = sqlite3.connect("db/progress.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM progress_types")
    return cursor.fetchall() 