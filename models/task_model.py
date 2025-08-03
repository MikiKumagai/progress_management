import sqlite3

DB_PATH = "db/progress.db"

# 進捗記録ページ：登録値計算用データ取得
def select_task_data(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT progress, total_count FROM tasks WHERE id = ?", (task_id,))
    progress, total_count = cur.fetchone()
    conn.close()
    return progress, total_count

# 進捗記録ページ：進捗累計を更新
def update_task_progress(task_id, today_progress):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET progress = ? WHERE id = ?", (today_progress, task_id))
    conn.commit()
    conn.close()

# 進捗記録ページ：課題完了フラグを立てる
def update_task_completion(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET active = False WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# 進捗記録ページ：課題のリストを取得
def select_tasks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM tasks WHERE active")
    return cursor.fetchall() 

# 課題登録ページ：新規課題追加
def insert_task(name, progress_unit_id, progress_type_id, total_count):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (name, progress_unit_id, progress_type_id, total_count) VALUES (?, ?, ?, ?)",
        (name, progress_unit_id, progress_type_id, total_count)
    )
    conn.commit()
    conn.close()

# 進捗確認ページ：課題の進捗状況リストを取得
def fetch_all_tasks():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""SELECT 
        name, 
        progress, 
        total_count, 
        active 
        FROM tasks""")
    tasks = cur.fetchall() 
    conn.close()
    return tasks


# 進捗確認ページ：グラフ用データ取得
def select_task_for_chart(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name, total_count FROM tasks WHERE id=?", (task_id,))
    name, total_count = cur.fetchone() 
    conn.close()
    return name, total_count

def select_for_export():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall() 
    conn.close()
    return tasks