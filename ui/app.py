import tkinter as tk

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="タスク登録ページ")
        label.pack()
        button = tk.Button(self, text="進捗入力ページへ",
                           command=lambda: controller.show_frame("PageTwo"))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="進捗入力ページ")
        label.pack()
        button = tk.Button(self, text="グラフページへ",
                           command=lambda: controller.show_frame("PageThree"))
        button.pack()
        back_button = tk.Button(self, text="← タスク登録へ",
                           command=lambda: controller.show_frame("PageOne"))
        back_button.pack()

class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="グラフページ")
        label.pack()
        button = tk.Button(self, text="タスク登録ページへ戻る",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("進捗管理アプリ")
        self.geometry("400x300")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageOne")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
