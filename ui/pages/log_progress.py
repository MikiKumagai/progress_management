import tkinter as tk
from tkinter import ttk
from services import task_service, progress_service

class LogProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        for i in range(5):
            self.grid_columnconfigure(i, weight=1)

        # ラベル（ページタイトル）
        title_label = ttk.Label(self, text="進捗記録", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="")

        # タスク選択用データ取得（名前だけでなくIDも必要なのでタプルで取得する想定）
        # 例: [ (1, "task1"), (2, "task2") ]
        self.tasks = task_service.get_tasks()  # IDと名前のリストを返す想定

        # コンボボックスに表示する名前リストだけ取り出し
        task_names = [task[1] for task in self.tasks]

        label = ttk.Label(self, text="タスク選択")
        label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.combo = ttk.Combobox(self, values=task_names, state="readonly")
        self.combo.current(0)
        self.combo.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # タスク切り替えボタン
        switch_button = tk.Button(self, text="切替", command=self.on_switch_task)
        switch_button.grid(row=1, column=4, padx=10, pady=5, sticky="ew")

        # 進捗単位
        label1 = ttk.Label(self, text="進捗単位")
        label1.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.progress_unit_label = ttk.Label(self, text="")
        self.progress_unit_label.grid(row=2, column=1, columnspan=4, padx=10, pady=5, sticky="w")

        # 入力タイプ
        label2 = ttk.Label(self, text="入力タイプ")
        label2.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.progress_type_label = ttk.Label(self, text="")
        self.progress_type_label.grid(row=3, column=1, columnspan=4, padx=10, pady=5, sticky="w")

        # 進捗入力
        progress_value = tk.Entry(self, width=40)
        progress_value.grid(row=4, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

        # 登録ボタン
        add_button = tk.Button(self, text="登録", command=self.on_submit)
        add_button.grid(row=4, column=4, padx=10, pady=5, sticky="ew")

        # 遷移ボタン
        nav_task_setup = tk.Button(self, text="新規登録", command=lambda: controller.show_frame("TaskSetupPage"))
        nav_task_setup.grid(row=5, column=0, columnspan=5, padx=10, pady=5, sticky="ew")

        # 遷移ボタン
        nav_progress_overview = tk.Button(self, text="進捗確認", command=lambda: controller.show_frame("ProgressOverviewPage"))
        nav_progress_overview.grid(row=6, column=0, columnspan=5, padx=10, pady=5, sticky="ew")

    def on_switch_task(self):
        # 選択中のタスク名からIDを特定
        selected_index = self.combo.current()
        if selected_index < 0:
            return  # 未選択なら何もしない

        self.selected_task_id = self.tasks[selected_index][0]

        # 進捗単位・入力タイプをサービスから取得して表示更新
        progress_unit = task_service.get_progress_unit(self.selected_task_id)
        progress_type = task_service.get_progress_type(self.selected_task_id)

        self.progress_unit_label.config(text=progress_unit)
        self.progress_type_label.config(text=progress_type)

    def on_submit(self):
        progress_service.add_progress()
        input_value = self.entry.get()
        print(f"入力値: {input_value}")
        # ここでservice層などの処理呼び出しもできる
