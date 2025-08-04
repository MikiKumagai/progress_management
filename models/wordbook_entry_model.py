import sqlite3

DB_PATH = "db/progress.db"

def fetch_all_wordbook_entry(wordbook_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT word, meaning FROM wordbook_entry WHERE wordbook_id = ?", (wordbook_id,))
    wordbook_entry = cur.fetchall()
    conn.close()
    return wordbook_entry