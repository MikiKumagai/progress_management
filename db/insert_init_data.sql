INSERT INTO progress_units (name) VALUES ("ページ"), ("問"), ("章"), ("セクション");

INSERT INTO progress_types (name) VALUES ("累計"), ("差分");

-- 学習タスク
INSERT INTO tasks (
    name,
    progress_unit_id,
    progress_type_id,
    total_count,
    progress
) VALUES ("機械学習", 1, 1, 361, 306), ("G検定", 2, 2, 1636, 533);

-- 進捗記録
INSERT INTO progresses (
    task_id,
    progress_value,
    progress_date
) VALUES ( 1, 19, '2025-05-12'), ( 1, 6, '2025-05-13'), ( 1, 16, '2025-05-14'), ( 1, 14, '2025-05-15');