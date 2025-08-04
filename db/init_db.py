import sqlite3
import csv

# SQLiteのDBファイルを作成・接続
conn = sqlite3.connect("db/progress.db")
cur = conn.cursor()

# テーブルがあれば削除
with open("db/drop_table.sql", "r", encoding="utf-8") as f:
    drop_table = f.read()
    cur.executescript(drop_table)

# 作成
with open("db/create_table.sql", "r", encoding="utf-8") as f:
    create_table = f.read()
    cur.executescript(create_table)

# 初期データ登録
with open("db/insert_master_data.sql", "r", encoding="utf-8") as f:
    insert_master_data = f.read()
    cur.executescript(insert_master_data)

# tasks.csvから登録
with open("db/tasks.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        is_wordbook = row["is_wordbook"].strip().upper() == "TRUE"
        cur.execute("INSERT INTO tasks (name,progress_unit_id,progress_type_id,total_count,progress,is_wordbook) VALUES (?, ?, ?, ?, ?, ?)", (
            row["name"], int(row["progress_unit_id"]), int(row["progress_type_id"]), int(row["total_count"]), int(row["progress"]), is_wordbook
        ))
        
# progresses.csvから登録
with open("db/progresses.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cur.execute("INSERT INTO progresses (task_id, progress_value, progress_date) VALUES (?, ?, ?)", (
            int(row["task_id"]), int(row["progress_value"]), row["progress_date"]
        ))

# wordbook_entries.csvから登録
with open("db/wordbook_entries.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        is_word_learned = row["is_word_learned"].strip().upper() == "TRUE"
        is_meaning_learned = row["is_meaning_learned"].strip().upper() == "TRUE"
        cur.execute("""
            INSERT INTO wordbook_entries (task_id, word, meaning, is_word_learned, is_meaning_learned, word_learned_at, meaning_learned_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            int(row["task_id"]), row["word"], row["meaning"], is_word_learned, is_meaning_learned, row["word_learned_at"], row["meaning_learned_at"]
        ))
        
conn.commit()
conn.close()