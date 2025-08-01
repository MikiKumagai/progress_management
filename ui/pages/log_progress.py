import tkinter as tk
from tkinter import ttk
from presentations import table
from services import task_service, progress_service, progress_unit_service, progress_type_service

class LogProgressPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        for i in range(6):
            self.grid_columnconfigure(i, weight=1, uniform="a")
        for j in range(7):
            self.grid_rowconfigure(j, weight=1)

        # ラベル（ページタイトル）
        title_label = ttk.Label(self, text="進捗記録", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=12, padx=5, pady=10, sticky="nsew")

        # タスク
        self.tasks = task_service.get_tasks()
        task_list = [task[1] for task in self.tasks]

        label = ttk.Label(self, text="タスク選択")
        label.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        self.combo = ttk.Combobox(self, values=task_list, state="readonly")
        self.combo.current(0)
        self.combo.grid(row=1, column=1, columnspan=4, padx=5, pady=5, sticky="nsew")

        # タスク切り替えボタン
        switch_button = ttk.Button(self, text="切替", command=self.on_switch_task)
        switch_button.grid(row=1, column=5, padx=5, pady=5, sticky="nsew")

        # TODO: タスクに進行中とかのフラグつける
        # 入力タイプ
        progress_type_label = ttk.Label(self, text="入力タイプ")
        progress_type_label.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.progress_type = ttk.Label(self, text="")
        self.progress_type.grid(row=3, column=1, columnspan=4, padx=5, pady=5, sticky="nsew")

        # 進捗入力
        progress_type_label = ttk.Label(self, text="進捗入力")
        progress_type_label.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        self.progress_value = ttk.Entry(self)
        self.progress_value.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

        # 進捗単位
        self.progress_unit = ttk.Label(self, text="")
        self.progress_unit.grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

        # 登録ボタン
        add_button = ttk.Button(self, text="登録", command=self.on_submit)
        add_button.grid(row=4, column=5, padx=5, pady=5, sticky="nsew")

        # 遷移ボタン
        nav_task_setup = ttk.Button(self, text="新規登録", command=lambda: controller.show_frame("TaskSetupPage"))
        nav_task_setup.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

        # 遷移ボタン
        nav_progress_overview = ttk.Button(self, text="進捗確認", command=lambda: controller.show_frame("ProgressOverviewPage"))
        nav_progress_overview.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

        self.after(0, self.set_default_task)

    # TODO: リフレッシュして新しいタスクがリストにちゃんと入るようにする
    def set_default_task(self):
        if not self.tasks:
            return
        self.combo.current(0) 
        self.selected_task_id = self.tasks[0][0]
        progress_unit = progress_unit_service.get_progress_unit(self.selected_task_id)
        progress_type = progress_type_service.get_progress_type(self.selected_task_id)
        self.progress_unit.config(text=progress_unit)
        self.progress_type.config(text=progress_type)
    
    def on_switch_task(self):
        selected_index = self.combo.current()
        if selected_index < 0:
            return 
        self.selected_task_id = self.tasks[selected_index][0]
        progress_unit = progress_unit_service.get_progress_unit(self.selected_task_id)
        progress_type = progress_type_service.get_progress_type(self.selected_task_id)
        self.progress_unit.config(text=progress_unit)
        self.progress_type.config(text=progress_type)

    def on_submit(self):
        selected_index = self.combo.current()
        task_id = self.tasks[selected_index][0]
        progress_value = self.progress_value.get()
        progress_type = self.progress_type
        progress_service.add_progress(task_id, progress_value, progress_type)
        # TODO: Entry空にする、完了通知出す
        # TODO: データ更新？確認画面に反映されないからデータ取得タイミングを考える。遷移時がいい気がする。
