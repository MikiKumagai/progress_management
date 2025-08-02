INSERT INTO progress_units (name) VALUES ("ページ"), ("問"), ("章"), ("セクション");

INSERT INTO progress_types (name) VALUES ("累計"), ("差分");

-- 学習課題
INSERT INTO tasks (
    name,
    progress_unit_id,
    progress_type_id,
    total_count,
    progress
) VALUES ("機械学習", 1, 1, 361, 306), ("G検定", 2, 2, 1636, 533);
