from models import task_model, progress_model

# 進捗記録ページ：進捗記録
def add_progress(task_id, progress_value, progress_type):
    # 1. 進捗をprogressテーブルに追加
    progress, total_count = task_model.select_task_data(task_id)
    print("progress: ", progress)
    print("total_count: ", total_count)
    progress_total = 0
    progress_diff = 0
    if progress_type == "累計":
        progress_total = progress_value
        progress_diff = progress_value - progress
    elif progress_type == "差分":
        progress_total = progress_value + progress
        progress_diff = progress_value
    print("after_estimate_total: ", progress_total)
    print("after_estimate_diff: ", progress_diff)
    progress_model.insert_progress(task_id, progress_diff)
    # 2. 合計進捗を更新
    task_model.update_task_progress(task_id, progress_total)
    # 3. total_countとprogressが同じになったらactiveをFalseにする
    if progress_total == total_count:
        task_model.update_task_completion(task_id)

# 日に2回送られてきたときどうしよかな