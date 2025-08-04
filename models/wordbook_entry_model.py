import sqlite3

DB_PATH = "db/progress.db"

def fetch_all_wordbook_entries(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT word, meaning 
        FROM wordbook_entries 
        WHERE meaning IS NOT NULL
        AND task_id = ?
        """, (task_id,))
    wordbook_entries = cur.fetchall()
    conn.close()
    return wordbook_entries