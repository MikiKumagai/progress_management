import tkinter as tk
from tkinter import ttk, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from presentations import task_table, progress_chart
from services import task_service, progress_service
import matplotlib.pyplot as plt

class ProgressOverviewPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        for i in range(6):
            self.grid_columnconfigure(i, weight=1, uniform="a")
        for j in range(7):
            self.grid_rowconfigure(j, weight=1)

        # ページタイトル
        title_label = ttk.Label(self, text="進捗確認", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")

        # タスクの取得と選択
        self.tasks = task_service.get_tasks()
        task_list = [task[1] for task in self.tasks]
        self.selected_task_id = self.tasks[0][0] if self.tasks else None
        self.tasks = task_service.get_tasks()
        task_list = [task[1] for task in self.tasks]
        # 課題コンボボックス
        self.selected_task_id = self.tasks[0][0] if self.tasks else None
        self.task_combo = ttk.Combobox(self, values=task_list, state="readonly")
        self.task_combo.current(0)
        self.task_combo.grid(row=1, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")
        self.task_combo.bind("<<ComboboxSelected>>", self.on_switch_task)

        # グラフ
        fig = progress_chart.create_progress_chart(self.selected_task_id)
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=6, padx=5, pady=5, sticky="nsew")

        # ページ遷移ボタン
        nav_task_setup = ttk.Button(self, text="進捗記録", command=lambda: controller.show_frame("LogProgressPage"))
        nav_task_setup.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

    def refresh(self):
        self.tasks = task_service.get_tasks()
        task_list = [task[1] for task in self.tasks]
        self.task_combo['values'] = task_list
        if task_list:
            self.task_combo.current(0)
            self.selected_task_id = self.tasks[0][0]
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
    
    # 切り替え
    def on_switch_task(self, event):
        selected_index = self.task_combo.current()
        if selected_index < 0:
            return
        # グラフを更新
        self.selected_task_id = self.tasks[selected_index][0]
        self.canvas.figure = progress_chart.create_progress_chart(self.selected_task_id)
        self.canvas.draw()