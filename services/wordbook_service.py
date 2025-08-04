from models import wordbook_model, wordbook_entry_model
import sqlite3

# 辞書画面：単語帳のリスト
def get_wordbooks():
    wordbooks = wordbook_model.select_wordbooks()
    return wordbooks

# 単語帳登録画面：単語帳の追加
def add_wordbook(name):
    wordbook_model.insert_wordbook(name)