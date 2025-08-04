import sqlite3

DB_PATH = "db/progress.db"

# 辞書ページ：単語帳のリストを取得
def select_wordbooks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM wordbooks")
    return cursor.fetchall() 