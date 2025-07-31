import sqlite3

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
