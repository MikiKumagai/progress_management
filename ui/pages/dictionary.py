import tkinter as tk
from tkinter import ttk, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from presentations import dictionary_table
from services import wordbook_service, progress_service
import matplotlib.pyplot as plt

class DictionaryPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        for i in range(6):
            self.grid_columnconfigure(i, weight=1, uniform="a")
        for j in range(7):
            self.grid_rowconfigure(j, weight=0)

        # ページタイトル
        title_label = ttk.Label(self, text="辞書", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")

        # タスクの取得と選択
        self.wordbooks = wordbook_service.get_wordbooks()
        wordbook_list = [wordbook[1] for wordbook in self.wordbooks]
        self.selected_wordbook_id = self.wordbooks[0][0] if self.wordbooks else None
        self.wordbooks = wordbook_service.get_wordbooks()
        wordbook_list = [wordbook[1] for wordbook in self.wordbooks]
        # 課題コンボボックス
        self.selected_wordbook_id = self.wordbooks[0][0] if self.wordbooks else None
        self.wordbook_combo = ttk.Combobox(self, values=wordbook_list, state="readonly")
        self.wordbook_combo.current(0)
        self.wordbook_combo.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
        self.wordbook_combo.bind("<<ComboboxSelected>>", self.on_switch_wordbook)

        # テーブル
        self.word_tree = ttk.Treeview(self, columns=('word', 'mean'), show="headings")
        self.word_tree['columns'] = ('word', 'meaning')
        self.word_tree['columns'] = ('word','meaning')
        self.word_tree.column('word', anchor='w', width=50)
        self.word_tree.column('meaning',anchor='w', width=150)
        self.word_tree.heading('word', text='word',anchor='w')
        self.word_tree.heading('meaning', text='meaning', anchor='w')
        self.word_tree.grid(row=2, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")

        self.on_switch_wordbook(None)

        # ページ遷移ボタン
        nav_task_setup = ttk.Button(self, text="進捗記録", command=lambda: controller.show_frame("LogProgressPage"))
        nav_task_setup.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

    def refresh(self):
        self.wordbooks = wordbook_service.get_wordbooks()
        wordbook_list = [wordbook[1] for wordbook in self.wordbooks]
        self.wordbook_combo['values'] = wordbook_list
        if wordbook_list:
            self.wordbook_combo.current(0)
            self.selected_wordbook_id = self.wordbooks[0][0]
        else:
            self.wordbook_combo.set("")

    # 初期表示
    def set_default_wordbook(self):
        if not self.wordbooks:
            return
        self.wordbook_combo.current(0)
        self.selected_wordbook_id = self.wordbooks[0][0]
    
    # 切り替え
    def on_switch_wordbook(self, event):
        selected_index = self.wordbook_combo.current()
        if selected_index < 0:
            return
        self.selected_wordbook_id = self.wordbooks[selected_index][0]
        # テーブルの中身を一度クリア
        for row in self.word_tree.get_children():
            self.word_tree.delete(row)
        # DataFrame取得して挿入
        df = dictionary_table.get_wordbook_summary(self.selected_wordbook_id)
        for _, row in df.iterrows():
            self.word_tree.insert('', 'end', values=(row['word'], row['meaning']))