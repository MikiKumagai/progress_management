from models import task_model, progress_model

# 進捗記録ページ：進捗記録
def add_progress(task_id, progress_value, progress_type):
    progress, total_count = task_model.select_task_data(task_id)
    progress_total, progress_diff = calculate_progress(progress, progress_value, progress_type)
    # 進捗を登録
    if progress_model.select_today_data(task_id) is None:
        progress_model.insert_progress(task_id, progress_diff)
    else:
        progress_model.update_progress(task_id, progress_diff)
    # taskの進捗情報を更新
    task_model.update_task_progress(task_id, progress_total)
    # task完了しているかチェック
    if progress_total == total_count:
        task_model.update_task_completion(task_id)

# 進捗記録ページ：進捗記録データの計算
def calculate_progress(progress, progress_value, progress_type):
    if progress_type == "累計":
        progress_total = progress_value
        progress_diff = progress_value - progress
    elif progress_type == "差分":
        progress_total = progress_value + progress
        progress_diff = progress_value
    else:
        raise ValueError("不明な入力タイプ")
    return progress_total, progress_diff

import math
def get_rate(task_id):
    progress, total_count = task_model.select_task_data(task_id)
    rate = progress / total_count
    return rate * 100 
    