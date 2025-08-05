from models import task_model, progress_model
from presentations import progress_chart
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

# 単語帳編集画面：単語の追加による課題の更新
def add_count(task_id):
    task_model.update_total_count(task_id)

# 進捗確認画面：単語帳かどうか
def get_progress_chart(task_id):
    is_wordbook = task_model.select_is_wordbook(task_id)[0]
    if is_wordbook:
        return progress_chart.create_wordbook_progress_chart(task_id)
    else:
        return progress_chart.create_progress_chart(task_id)