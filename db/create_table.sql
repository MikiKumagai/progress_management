-- 進捗単位マスタ
CREATE TABLE progress_units (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- 進捗形式マスタ
CREATE TABLE progress_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

-- 学習課題
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    progress_unit_id INTEGER NOT NULL,
    progress_type_id INTEGER NOT NULL,
    total_count INTEGER NOT NULL,
    progress INTEGER DEFAULT 0 NOT NULL,
    active boolean DEFAULT TRUE NOT NULL,
    created_at DATE NOT NULL DEFAULT (DATE('now')),
    FOREIGN KEY (progress_unit_id) REFERENCES progress_units (id)
    FOREIGN KEY (progress_type_id) REFERENCES progress_types (id)
);

-- 進捗記録
CREATE TABLE progresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_id INTEGER NOT NULL,
    progress_value INTEGER NOT NULL,
    progress_date DATE NOT NULL DEFAULT (DATE('now')),
    FOREIGN KEY (task_id) REFERENCES tasks (id),
    CONSTRAINT unique_task_date UNIQUE (task_id, progress_date)
);
