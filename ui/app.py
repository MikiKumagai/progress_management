import tkinter as tk
from ui.pages.log_progress import LogProgressPage
from ui.pages.task_setup import TaskSetupPage
from ui.pages.progress_overview import ProgressOverviewPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("学習管理アプリ")
        self.geometry("500x500")

        for i in range(5):
            self.grid_columnconfigure(i, weight=1)

        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")

        self.frames = {}
        for F in (LogProgressPage, TaskSetupPage, ProgressOverviewPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LogProgressPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
