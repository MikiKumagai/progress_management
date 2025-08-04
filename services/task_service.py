from models import task_model, progress_model
import sqlite3

# 進捗確認画面：課題のリスト
def get_tasks():
    tasks = task_model.select_tasks()
    return tasks

# 進捗記録画面：課題のリスト
def get_active_tasks():
    tasks = task_model.select_active_tasks()
    return tasks

# 課題登録画面：課題の追加
def add_task(name, progress_unit_id, progress_type_id, total_count, is_wordbook):
    task_model.insert_task(name, progress_unit_id, progress_type_id, total_count, is_wordbook)