from models import progress_unit_model
import sqlite3

# 進捗記録画面：進捗単位
def get_progress_unit(task_id):
    progress_unit = progress_unit_model.select_progress_unit(task_id)
    return progress_unit

# 進捗記録画面：進捗単位のリスト
def get_progress_units():
    progress_units = progress_unit_model.select_progress_units()
    return progress_units