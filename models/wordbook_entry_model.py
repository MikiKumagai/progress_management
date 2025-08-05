import sqlite3
from datetime import date

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
        SELECT word, meaning, is_word_learned, is_meaning_learned, id
        FROM wordbook_entries 
        WHERE task_id = ?
        """, (task_id,))
    wordbook_entries = cur.fetchall()
    conn.close()
    return wordbook_entries

def select_for_learning_word(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT word, meaning, is_word_learned, id
        FROM wordbook_entries 
        WHERE task_id = ?
        AND TRIM(meaning) <> ''
        AND is_word_learned = False
        ORDER BY random()
        """, (task_id,))
    wordbook_entries = cur.fetchall()
    conn.close()
    return wordbook_entries

def select_for_learning_meaning(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT word, meaning, is_meaning_learned, id
        FROM wordbook_entries 
        WHERE task_id = ?
        AND TRIM(meaning) <> ''
        AND is_meaning_learned = False
        ORDER BY random()
        """, (task_id,))
    wordbook_entries = cur.fetchall()
    conn.close()
    return wordbook_entries

def update_wordbook_entry(id, meaning):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE wordbook_entries SET meaning = ? WHERE id = ?", (meaning, id))
    conn.commit()
    conn.close()

def update_is_word_learned(id, is_word_learned):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    today = date.today().isoformat()
    cur.execute("UPDATE wordbook_entries SET is_word_learned = ?, word_learned_at = ? WHERE id = ?", (is_word_learned, today, id))
    conn.commit()
    conn.close()

def update_is_meaning_learned(id, is_meaning_learned):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    today = date.today().isoformat()
    cur.execute("UPDATE wordbook_entries SET is_meaning_learned = ?, meaning_learned_at = ? WHERE id = ?", (is_meaning_learned, today, id))
    conn.commit()
    conn.close()

def insert_record(task_id, word, meaning):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO wordbook_entries (task_id, word, meaning) VALUES(?,?,?)
        """, (task_id, word, meaning))
    conn.commit()
    conn.close()

def select_for_export():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            task_id, 
            word, 
            meaning, 
            is_word_learned, 
            is_meaning_learned, 
            word_learned_at, 
            meaning_learned_at 
        FROM wordbook_entries""")
    wordbook_entries = cur.fetchall() 
    conn.close()
    return wordbook_entries