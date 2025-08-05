import tkinter as tk
from tkinter import ttk, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from presentations import dictionary_table
from services import wordbook_service
import matplotlib.pyplot as plt
from tksheet import Sheet

class WordbookWordPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        for i in range(6):
            self.grid_columnconfigure(i, weight=1, uniform="a")
        for j in range(7):
            self.grid_rowconfigure(j, weight=0)

        # ページタイトル
        title_label = ttk.Label(self, text="単語学習", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

        # 画面切り替え（TODO: 課題IDを共有）
        learn_btn = ttk.Button(self, text="学習切替", command=lambda: controller.show_frame("WordbookMeaningPage"))
        learn_btn.grid(row=0, column=5, padx=5, pady=5, sticky='nsew')

        # タスクの取得と選択
        self.wordbooks = wordbook_service.get_active_wordbooks()
        wordbook_list = [wordbook[1] for wordbook in self.wordbooks]
        self.selected_task_id = self.wordbooks[0][0] if self.wordbooks else None
        # 課題コンボボックス
        self.wordbook_combo = ttk.Combobox(self, values=wordbook_list, state="readonly")
        self.wordbook_combo.current(0)
        self.wordbook_combo.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
        self.wordbook_combo.bind("<<ComboboxSelected>>", self.on_switch_wordbook)

        # TODO: 学習切替ボタン：意味列（意味列記入済みの行 AND 学習済み単語が0の行）
        self.word_tree = ttk.Treeview(self, columns=('word', 'meaning', 'is_word_learned'), show="headings")
        self.word_tree['columns'] = ('meaning')
        self.word_tree.column('meaning',anchor='w', width=200)
        self.word_tree.heading('meaning', text='意味', anchor='w')
        self.word_tree.grid(row=3, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
        self.word_tree.bind('<<TreeviewSelect>>', self.on_select)
        self.on_switch_wordbook(None)

        # 単語学習済みチェックボックス
        self.selected_iid = None
        self.is_word_learned = tk.BooleanVar()
        self.is_word_learned_check = ttk.Checkbutton(self, text="", variable=self.is_word_learned, command=self.on_check)
        self.is_word_learned_check.grid(row=4, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")

        # 遷移ボタン
        nav_progress_overview = ttk.Button(self, text="TOP", command=lambda: controller.show_frame("LogProgressPage"))
        nav_progress_overview.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

        # 遷移ボタン（TODO: 課題IDを共有）
        nav_task_setup = ttk.Button(self, text="編集", command=lambda: controller.show_frame("WordbookEditPage"))
        nav_task_setup.grid(row=6, column=5, padx=5, pady=5, sticky="nsew")

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
        # TODO: ランダム取得
        if not self.wordbooks:
            return
        self.wordbook_combo.current(0)
        self.selected_task_id = self.wordbooks[0][0]
    
    # 切り替え
    def on_switch_wordbook(self, event):
        # TODO: ランダム取得
        selected_index = self.wordbook_combo.current()
        if selected_index < 0:
            return
        self.selected_task_id = self.wordbooks[selected_index][0]
        for row in self.word_tree.get_children():
            self.word_tree.delete(row)
        df = dictionary_table.get_wordbook(self.selected_task_id)
        for _, row in df.iterrows():
            self.word_tree.insert('', 'end', values=(
                row['word'], row['meaning'], row['is_word_learned'], int(row['id'])
                ))

    # リストで選択
    def on_select(self, event):
        selected = self.word_tree.selection()
        if not selected:
            return
        self.selected_iid = selected[0]
        values = self.word_tree.item(self.selected_iid, 'values')
        self.selected_meaning = values[1]
        # チェック状態も反映
        is_checked = bool(int(values[2]))
        self.is_word_learned.set(is_checked)
        self.is_word_learned_check.config(text=f"{self.selected_meaning}")

    def on_check(self):
        # TODO: 更新
        current_values = self.word_tree.item(self.selected_iid, 'values')
        print(current_values[3])
        print(self.is_word_learned.get())