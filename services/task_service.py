from models import task_model, progress_model
import sqlite3

# TODO: SQLをtask_modelに移動
# 進捗記録画面：タスクのリスト
def get_tasks():
    conn = sqlite3.connect("db/progress.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM tasks")
    return cursor.fetchall() 