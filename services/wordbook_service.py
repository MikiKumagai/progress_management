from models import task_model, wordbook_entry_model
import sqlite3

# 辞書画面：単語帳のリスト
def get_wordbooks():
    wordbooks = task_model.select_wordbooks()
    return wordbooks

# 辞書画面：単語帳のリスト
def get_active_wordbooks():
    wordbooks = task_model.select_active_wordbooks()
    return wordbooks

# 単語帳画面：単語帳の更新
def update_wordbook(id, meaning):
    wordbook_entry_model.update_wordbook_entry(id, meaning)

def check_word(id, is_word_learned):
    wordbook_entry_model.update_is_word_learned(id, is_word_learned)

def check_meaning(id, is_meaning_learned):
    wordbook_entry_model.update_is_meaning_learned(id, is_meaning_learned)