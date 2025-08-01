from models import task_model, progress_model
import sqlite3

# 進捗記録画面：タスクのリスト
def get_tasks():
    tasks = task_model.select_tasks()
    return tasks

def add_task(name, progress_unit_id, progress_type_id, total_count):
    task_model.insert_task(name, progress_unit_id, progress_type_id, total_count)