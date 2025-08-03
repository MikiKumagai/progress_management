import csv
from data import task_model  # 仮のモデル

# 1. データ取得
task_data = task_model.select_for_export()
progress_data = progress_model.select_for_export()

# 2. CSVに書き出す
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['task_id','progress_value','progress_date'])
    for row in task_data:
        writer.writerow(row)
