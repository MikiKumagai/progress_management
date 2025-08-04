import sqlite3

DB_PATH = "db/progress.db"

# 意味が分かってる単語を取得
def select_done_wordbook_entries(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT word, meaning 
        FROM wordbook_entries 
        WHERE TRIM(meaning) != ''
        AND task_id = ?
        """, (task_id,))
    wordbook_entries = cur.fetchall()
    conn.close()
    return wordbook_entries

def select_all_wordbook_entries(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT word, meaning, is_word_learned, is_meaning_learned
        FROM wordbook_entries 
        WHERE task_id = ?
        """, (task_id,))
    wordbook_entries = cur.fetchall()
    conn.close()
    return wordbook_entries