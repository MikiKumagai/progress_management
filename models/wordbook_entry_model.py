import sqlite3

DB_PATH = "db/progress.db"

def fetch_all_wordbook_entries(wordbook_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT word, meaning 
        FROM wordbook_entries 
        WHERE TRIM(meaning) != ''
        AND wordbook_id = ?
        """, (wordbook_id,))
    wordbook_entries = cur.fetchall()
    conn.close()
    return wordbook_entries