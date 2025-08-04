from models import task_model, wordbook_entry_model
import sqlite3

# 辞書画面：単語帳のリスト
def get_wordbooks():
    wordbooks = task_model.select_wordbooks()
    return wordbooks