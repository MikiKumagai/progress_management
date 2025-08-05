import tkinter as tk
from tkinter import ttk, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from presentations import wordbook_table
from services import wordbook_service
import matplotlib.pyplot as plt
from tksheet import Sheet

class WordbookEditPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        for i in range(6):
            self.grid_columnconfigure(i, weight=1, uniform="a")
        for j in range(7):
            self.grid_rowconfigure(j, weight=0)

        # ページタイトル
        title_label = ttk.Label(self, text="単語帳編集", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")

        # タスクの取得と選択
        self.wordbooks = wordbook_service.get_active_wordbooks()
        wordbook_list = [wordbook[1] for wordbook in self.wordbooks]
        self.selected_task_id = self.wordbooks[0][0] if self.wordbooks else None
        # 課題コンボボックス
        self.selected_task_id = self.wordbooks[0][0] if self.wordbooks else None
        self.wordbook_combo = ttk.Combobox(self, values=wordbook_list, state="readonly")
        self.wordbook_combo.current(0)
        self.wordbook_combo.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
        self.wordbook_combo.bind("<<ComboboxSelected>>", self.on_switch_wordbook)

        self.word_tree = ttk.Treeview(self, columns=('word', 'meaning', 'is_word_learned', 'is_meaning_learned'), show="headings")
        self.word_tree['columns'] = ('word', 'meaning', 'is_word_learned', 'is_meaning_learned')
        self.word_tree.column('word', anchor='w', width=150)
        self.word_tree.column('meaning',anchor='w', width=350)
        self.word_tree.column('is_word_learned',anchor='center', width=30)
        self.word_tree.column('is_meaning_learned',anchor='center', width=30)
        self.word_tree.heading('word', text='単語',anchor='center')
        self.word_tree.heading('meaning', text='意味', anchor='center')
        self.word_tree.heading('is_word_learned', text='単語', anchor='center')
        self.word_tree.heading('is_meaning_learned', text='意味', anchor='center')
        self.word_tree.grid(row=3, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
        self.word_tree.bind('<<TreeviewSelect>>', self.on_select)
        self.on_switch_wordbook(None)

        # 編集用Entry
        self.editing_word = ttk.Label(self, text="")
        self.editing_word.grid(row=4, column=0, columnspan=6, padx=5, pady=5, sticky='nsew')
        self.edit_meaning = ttk.Entry(self)
        self.edit_meaning.grid(row=5, column=0, columnspan=6, padx=5, pady=5, sticky='nsew')

        # 更新ボタン
        update_btn = ttk.Button(self, text="更新", command=self.on_update)
        update_btn.grid(row=6, column=5, padx=5, pady=5, sticky='nsew')
        self.selected_iid = None

        # TODO: ここかタイトル下あたりに単語追加機能（Entry2つと登録ボタン）
        # TODO: tasksも更新する
        # 編集用Entry
        registry_word_label = ttk.Label(self, text="単語")
        registry_word_label.grid(row=7, column=0, columnspan=1, padx=5, pady=5, sticky='nsew')
        self.registry_word = ttk.Entry(self)
        self.registry_word.grid(row=7, column=1, columnspan=5, padx=5, pady=5, sticky='nsew')

        registry_meaning_label = ttk.Label(self, text="意味")
        registry_meaning_label.grid(row=8, column=0, columnspan=1, padx=5, pady=5, sticky='nsew')
        self.registry_meaning = ttk.Entry(self)
        self.registry_meaning.grid(row=8, column=1, columnspan=5, padx=5, pady=5, sticky='nsew')

        # 登録ボタン
        registry_btn = ttk.Button(self, text="登録", command=self.on_registry)
        registry_btn.grid(row=9, column=5, padx=5, pady=5, sticky='nsew')

        # ページ遷移ボタン
        nav_task_setup = ttk.Button(self, text="学習", command=lambda: controller.show_frame("WordbookMeaningPage"))
        nav_task_setup.grid(row=10, column=0, padx=5, pady=5, sticky="nsew")

    def refresh(self):
        self.wordbooks = wordbook_service.get_active_wordbooks()
        wordbook_list = [wordbook[1] for wordbook in self.wordbooks]
        self.wordbook_combo['values'] = wordbook_list
        if wordbook_list:
            self.wordbook_combo.current(0)
            self.selected_task_id = self.wordbooks[0][0]
        else:
            self.wordbook_combo.set("")

    # 初期表示
    def set_default_wordbook(self):
        if not self.wordbooks:
            return
        self.wordbook_combo.current(0)
        self.selected_task_id = self.wordbooks[0][0]
    
    # 切り替え
    def on_switch_wordbook(self, event):
        selected_index = self.wordbook_combo.current()
        if selected_index < 0:
            return
        self.selected_task_id = self.wordbooks[selected_index][0]
        for row in self.word_tree.get_children():
            self.word_tree.delete(row)
        df = wordbook_table.get_wordbook(self.selected_task_id)
        for _, row in df.iterrows():
            if row['is_word_learned']==1:
                is_word_learned = "✓"
            else:
                is_word_learned = ""
            if row['is_meaning_learned']==1:
                is_meaning_learned = "✓"
            else:
                is_meaning_learned = ""
            self.word_tree.insert('', 'end', values=(row['word'], row['meaning'], is_word_learned, is_meaning_learned, int(row['id'])))

    # リストで選択
    def on_select(self, event):
        selected = self.word_tree.selection()
        if not selected:
            return
        self.selected_iid = selected[0]
        values = self.word_tree.item(self.selected_iid, 'values')
        self.editing_word.config(text=values[0])
        self.edit_meaning.delete(0, tk.END)
        self.edit_meaning.insert(0, values[1])

    # meaningの更新
    def on_update(self):
        if self.selected_iid is None:
            return

        current_values = self.word_tree.item(self.selected_iid, 'values')
        word_text = current_values[0]
        is_word_learned = current_values[2]
        is_meaning_learned = current_values[3]

        new_meaning = self.edit_meaning.get()
        wordbook_service.update_wordbook(current_values[4], new_meaning)
        
        self.word_tree.item(
            self.selected_iid,
            values=(word_text, new_meaning, is_word_learned, is_meaning_learned)
        )
    
    def on_registry(self):
        print(self.registry_word.get())
        print(self.registry_meaning.get())
    