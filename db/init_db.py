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
with open("db/insert_init_data.sql", "r", encoding="utf-8") as f:
    insert_init_data = f.read()
    cur.executescript(insert_init_data)

# progresses.csvから登録
with open("db/progresses.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cur.execute("INSERT INTO progresses (task_id, progress_value, progress_date) VALUES (?, ?, ?)", (
            int(row["task_id"]), int(row["progress_value"]), row["progress_date"]
        ))
        
conn.commit()
conn.close()