import sqlite3
from datetime import date

DB_PATH = "db/progress.db"

# 進捗記録ページ：今日2回目以降の登録かチェック
def select_today_data(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    today = date.today().isoformat()
    cur.execute(
        "SELECT 1 FROM progresses WHERE task_id = ? AND progress_date = ?", 
        (task_id, today)
    )
    today_update = cur.fetchone() 
    conn.close()
    return today_update

# 進捗記録ページ：進捗記録
def insert_progress(task_id, progress_value):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    today = date.today().isoformat()
    cur.execute(
        "INSERT INTO progresses (task_id, progress_value, progress_date) VALUES (?, ?, ?)",
        (task_id, progress_value, today)
    )
    conn.commit()
    conn.close()

# 進捗記録ページ：進捗更新（1日の2回目以降の場合）
def update_progress(task_id, progress_value):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    today = date.today().isoformat()
    cur.execute(
        "UPDATE progresses SET progress_value = progress_value + ? WHERE task_id = ? AND progress_date = ?", 
        (progress_value, task_id, today)
    )
    conn.commit()
    conn.close()

# 進捗確認ページ：グラフ用データ取得
def select_progresses_for_chart(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""SELECT 
        t.name, 
        p.task_id, 
        p.progress_value, 
        p.progress_date 
        FROM progresses p
        INNER JOIN tasks t ON p.task_id = t.id""")
    progresses = cur.fetchall() 
    conn.close()
    return progresses
