import tkinter as tk
from ui.pages.log_progress import LogProgressPage
from ui.pages.task_setup import TaskSetupPage
from ui.pages.progress_overview import ProgressOverviewPage
from ui.pages.dictionary import DictionaryPage
from ui.pages.wordbook_word import WordbookWordPage
from ui.pages.wordbook_meaning import WordbookMeaningPage
from ui.pages.wordbook_edit import WordbookEditPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("学習管理アプリ")
        self.geometry("600x600+600+100")

        for i in range(6):
            self.grid_columnconfigure(i, weight=1)

        container = tk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LogProgressPage, TaskSetupPage, ProgressOverviewPage, DictionaryPage, WordbookWordPage, WordbookMeaningPage, WordbookEditPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LogProgressPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if hasattr(frame, "refresh"):
            frame.refresh()
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
