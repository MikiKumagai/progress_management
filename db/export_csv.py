import csv
from models import task_model, progress_model

# 1. データ取得
task_data = task_model.select_for_export()
progress_data = progress_model.select_for_export()

# 2. CSVに書き出す
with open("db/test_task.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['name','progress_unit_id','progress_type_id','total_count','progress','is_wordbook'])
    for row in task_data:
        writer.writerow(row)

with open("db/test_progress.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['task_id','progress_value','progress_date'])
    for row in progress_data:
        writer.writerow(row)
