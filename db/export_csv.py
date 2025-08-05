import csv
from models import task_model, progress_model, wordbook_entry_model

# 1. データ取得
task_data = task_model.select_for_export()
progress_data = progress_model.select_for_export()
wordbook_entry_data = wordbook_entry_model.select_for_export()

# 2. CSVに書き出す
with open("db/export_tasks.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['name','progress_unit_id','progress_type_id','total_count','progress','active','is_wordbook'])
    for row in task_data:
        writer.writerow(row)

with open("db/export_progresses.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['task_id','progress_value','progress_date'])
    for row in progress_data:
        writer.writerow(row)

with open("db/export_wordbook_entries.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['task_id','word','meaning','is_word_learned','is_meaning_learned','word_learned_at','meaning_learned_at'])
    for row in wordbook_entry_data:
        writer.writerow(row)
