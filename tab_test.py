import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Notebook Example")
root.geometry("300x200")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# タブ1
tab1 = tk.Frame(notebook)
label1 = tk.Label(tab1, text="これはタブ1です")
label1.pack(padx=10, pady=10)
notebook.add(tab1, text="タブ1")

# タブ2
tab2 = tk.Frame(notebook)
label2 = tk.Label(tab2, text="これはタブ2です")
label2.pack(padx=10, pady=10)
notebook.add(tab2, text="タブ2")

root.mainloop()
