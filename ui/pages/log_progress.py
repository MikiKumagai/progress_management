import tkinter as tk
from tkinter import ttk
from services import task_service, progress_service, progress_unit_service, progress_type_service

class LogProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        for i in range(6):
            self.grid_columnconfigure(i, weight=1, uniform="a")
        for j in range(7):
            self.grid_rowconfigure(j, weight=0)

        # ページタイトル
        title_label = ttk.Label(self, text="進捗記録", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=10, sticky="nsew")

        # 課題
        label = ttk.Label(self, text="課題選択")
        label.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.tasks = task_service.get_active_tasks()
        task_list = [task[1] for task in self.tasks]
        self.task_combo = ttk.Combobox(self, values=task_list, state="readonly")
        self.task_combo.current(0)
        self.task_combo.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky="nsew")
        self.task_combo.bind("<<ComboboxSelected>>", self.on_switch_task)

        # 入力タイプ
        self.progress_type = ttk.Label(self, text="")
        self.progress_type.grid(row=3, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # 進捗入力
        self.progress_value = ttk.Entry(self)
        self.progress_value.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

        # 進捗単位
        self.progress_unit = ttk.Label(self, text="")
        self.progress_unit.grid(row=3, column=4, padx=5, pady=5, sticky="nsew")

        # 登録ボタン
        add_button = ttk.Button(self, text="登録", command=self.on_submit)
        add_button.grid(row=3, column=5, padx=5, pady=5, sticky="nsew")

        # バリデーションメッセージ
        self.error_label = tk.Label(self, text="", fg="red")
        self.error_label.grid(row=4, column=0, columnspan=6, padx=5, pady=5, sticky="e")

        # 遷移ボタン
        nav_task_setup = ttk.Button(self, text="課題登録", command=lambda: controller.show_frame("TaskSetupPage"))
        nav_task_setup.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # 遷移ボタン
        nav_progress_overview = ttk.Button(self, text="進捗確認", command=lambda: controller.show_frame("ProgressOverviewPage"))
        nav_progress_overview.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # 遷移ボタン
        nav_dictionary = ttk.Button(self, text="辞書", command=lambda: controller.show_frame("DictionaryPage"))
        nav_dictionary.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        
        # 遷移ボタン
        nav_wordbook = ttk.Button(self, text="単語帳", command=lambda: controller.show_frame("WordbookPage"))
        nav_wordbook.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")   
        
        self.after(0, self.set_default_task)

    # データ取得共通メソッド
    def update_task_labels(self, task_id):
        progress_unit = progress_unit_service.get_progress_unit(task_id)
        progress_type = progress_type_service.get_progress_type(task_id)
        self.progress_unit.config(text=progress_unit)
        self.progress_type.config(text=progress_type)

    # 画面表示時の再取得
    def refresh(self):
        self.tasks = task_service.get_active_tasks()
        task_list = [task[1] for task in self.tasks]
        self.task_combo['values'] = task_list
        if task_list:
            self.task_combo.current(0)
            self.selected_task_id = self.tasks[0][0]
            self.update_task_labels(self.selected_task_id)
        else:
            self.task_combo.set("")
            self.progress_unit.config(text="")
            self.progress_type.config(text="")
    
    # 初期表示
    def set_default_task(self):
        if not self.tasks:
            return
        self.task_combo.current(0)
        self.selected_task_id = self.tasks[0][0]
        self.update_task_labels(self.selected_task_id)
    
    # 切り替え
    def on_switch_task(self, event):
        selected_index = self.task_combo.current()
        if selected_index < 0:
            return
        self.selected_task_id = self.tasks[selected_index][0]
        self.update_task_labels(self.selected_task_id)
    
    # 登録ボタン押下
    def on_submit(self):
        selected_index = self.task_combo.current()
        task_id = self.tasks[selected_index][0]
        try:
            progress_value = int(self.progress_value.get())
        except ValueError:
            self.error_label.config(text="進捗は数値を入力してください")
            return
        progress_type = self.progress_type.cget("text")
        progress_service.add_progress(task_id, progress_value, progress_type)
        self.progress_value.delete(0, tk.END)
       
