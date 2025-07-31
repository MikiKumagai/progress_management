from models import task_model, progress_model

def record_progress(task_id, today_progress):
    # 1. 進捗をprogressテーブルに追加
    progress_model.insert_progress(task_id, today_progress)

    # 2. 合計進捗を更新
    current = progress_model.get_total_progress_for_task(task_id)
    task_model.update_task_progress(task_id, current)
