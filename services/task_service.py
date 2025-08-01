from models import task_model, progress_model
import sqlite3

# TODO: SQLをtask_modelに移動
# 進捗記録画面：タスクのリスト
def get_tasks():
    conn = sqlite3.connect("db/progress.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM tasks")
    return cursor.fetchall() 

# 進捗記録画面：進捗単位のリスト
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

# 進捗記録画面：タスク名のリスト
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