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
        SELECT word,
               meaning, 
               CASE WHEN TRIM(word_learned_at) != '' THEN 1 ELSE 0 END as is_word_learned,
               CASE WHEN TRIM(meaning_learned_at) != '' THEN 1 ELSE 0 END as is_meaning_learned, 
               id
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
        SELECT word, 
               meaning, 
               CASE WHEN TRIM(word_learned_at) != '' THEN 1 ELSE 0 END as is_word_learned, 
               id
        FROM wordbook_entries 
        WHERE task_id = ?
        AND TRIM(meaning) <> ''
        AND (word_learned_at IS NULL OR TRIM(word_learned_at) = '')
        ORDER BY random()
        """, (task_id,))
    wordbook_entries = cur.fetchall()
    conn.close()
    return wordbook_entries

def select_for_learning_meaning(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT word, 
               meaning, 
               CASE WHEN TRIM(meaning_learned_at) != '' THEN 1 ELSE 0 END as is_meaning_learned, 
               id
        FROM wordbook_entries 
        WHERE task_id = ?
        AND TRIM(meaning) <> ''
        AND (meaning_learned_at IS NULL OR TRIM(meaning_learned_at) = '')
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
    if is_word_learned:
        today = date.today().isoformat()
        cur.execute("UPDATE wordbook_entries SET word_learned_at = ? WHERE id = ?", (today, id))
    else:
        cur.execute("UPDATE wordbook_entries SET word_learned_at = '' WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update_is_meaning_learned(id, is_meaning_learned):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    if is_meaning_learned:
        today = date.today().isoformat()
        cur.execute("UPDATE wordbook_entries SET meaning_learned_at = ? WHERE id = ?", (today, id))
    else:
        cur.execute("UPDATE wordbook_entries SET meaning_learned_at = '' WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def insert_record(task_id, word, meaning):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT INTO wordbook_entries (task_id, word, meaning) VALUES(?,?,?)", (task_id, word, meaning))
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
            CASE WHEN TRIM(word_learned_at) != '' THEN 1 ELSE 0 END as is_word_learned,
            CASE WHEN TRIM(meaning_learned_at) != '' THEN 1 ELSE 0 END as is_meaning_learned,
            word_learned_at, 
            meaning_learned_at 
        FROM wordbook_entries""")
    wordbook_entries = cur.fetchall() 
    conn.close()
    return wordbook_entries

def select_task_id(id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    SELECT task_id 
    FROM wordbook_entries 
    WHERE id = ? 
      AND TRIM(word_learned_at) != ''
      AND TRIM(meaning_learned_at) != ''
      """, (id,))
    task_id = cur.fetchone()
    conn.close()
    return task_id

def select_wordbook_progresses_for_chart(task_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT 
        t.name, 
        task_id, 
        word_learned_at, 
        meaning_learned_at 
        FROM wordbook_entries we
        INNER JOIN tasks t ON we.task_id = t.id
        WHERE t.id = ? 
        AND TRIM(word_learned_at) != ''
        AND TRIM(meaning_learned_at) != ''
        """, (task_id,))
    wordbook_entries = cur.fetchall() 
    conn.close()
    return wordbook_entries