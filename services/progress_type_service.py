from models import progress_type_model
import sqlite3

# 進捗記録画面：入力形式
def get_progress_type(task_id):
    progress_type = progress_type_model.select_progress_type(task_id)
    return progress_type

# 進捗記録画面：入力形式のリスト
def get_progress_types():
    progress_types = progress_type_model.select_progress_types()
    return progress_types