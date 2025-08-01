from models import task_model, progress_model

# 進捗記録ページ：進捗記録
def add_progress(task_id, progress_value, progress_type):
    # 1. 進捗をprogressテーブルに追加
    # progress_typeが累計だったら差分に直して登録する
    if progress_type == "累計":
        total_count = task_model.select_total_count(task_id)
        progress_value = progress_value - total_count
    progress_model.insert_progress(task_id, progress_value)

    # 2. 合計進捗を更新
    task_model.update_task_progress(task_id, progress_value)
