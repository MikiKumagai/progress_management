from models import task_model, progress_model
import sqlite3

# TODO: SQLをtask_modelに移動

# 進捗記録画面：進捗単位
def get_progress_unit(task_id):
    conn = sqlite3.connect("db/progress.db")
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
def get_progress_units():
    conn = sqlite3.connect("db/progress.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM progress_units")
    return cursor.fetchall() 