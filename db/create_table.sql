-- 1. 進捗単位マスタ
CREATE TABLE progress_units (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- 2. 進捗形式マスタ
CREATE TABLE progress_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- 3. 学習課題
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    progress_unit_id INTEGER NOT NULL,
    progress_type_id INTEGER NOT NULL,
    total_count INTEGER NOT NULL,
    progress INTEGER NOT NULL DEFAULT 0,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at DATE NOT NULL DEFAULT (DATE('now')),
    FOREIGN KEY (progress_unit_id) REFERENCES progress_units (id),
    FOREIGN KEY (progress_type_id) REFERENCES progress_types (id)
);

-- 4. 進捗記録
CREATE TABLE progresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    progress_value INTEGER NOT NULL,
    progress_date DATE NOT NULL DEFAULT (DATE('now')),
    FOREIGN KEY (task_id) REFERENCES tasks (id),
    CONSTRAINT unique_task_date UNIQUE (task_id, progress_date)
);

-- 5. 単語帳
CREATE TABLE wordbooks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- 6. 各単語（単語帳の中身）
CREATE TABLE wordbook_entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wordbook_id INTEGER NOT NULL,
    word TEXT NOT NULL,
    meaning TEXT NOT NULL DEFAULT "未設定",
    is_word_learned BOOLEAN NOT NULL DEFAULT FALSE,
    is_meaning_learned BOOLEAN NOT NULL DEFAULT FALSE,
    word_learned_at DATE,
    meaning_learned_at DATE,
    FOREIGN KEY (wordbook_id) REFERENCES wordbook (id)
);
