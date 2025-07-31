from models import task_model, progress_model

# 登録された内容を表示する関数
def update_listbox():
    cur.execute("SELECT name FROM tasks ORDER BY id DESC")
    for row in cur.fetchall():
        options.add(row[0])
        