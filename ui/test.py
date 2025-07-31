import tkinter as tk
from tkinter import messagebox

def on_check():
    if chk_var.get():
        print("げんき")
    else:
        print("げんき じゃない")

def on_select(event):
    print(f"{listbox.get(listbox.curselection())} おいしい")

def on_click():
    text = entry.get()
    print(f"そうだね {text} だね")
    custom_message("そうだね",f"{text} だね")

def custom_message(title, message):
    win = tk.Toplevel()
    win.title(title)
    win.geometry("200x100")
    win.resizable(False, False)
    tk.Label(win, text=message).pack(pady=10)
    tk.Button(win, text="OK", command=win.destroy).pack(pady=5)

root = tk.Tk()
root.title("progress_management")
root.geometry("450x350+350+250")

# ラベル
label = tk.Label(root, text="ぽちぽちしよう")
label.pack(pady=5)

# EntryとButtonを横並びにするフレーム
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

# エントリー（入力欄）
entry = tk.Entry(input_frame)
entry.pack(side="left")

# ボタン
button = tk.Button(input_frame, text="おくる", command=on_click)
button.pack(side="left", padx=5)

# チェックボックス
chk_var = tk.BooleanVar()
check = tk.Checkbutton(root, text="げんき？", variable=chk_var, command=on_check)
check.pack(pady=5)

# リストボックス
listbox = tk.Listbox(root)
for item in ["おすし", "おにく", "ごはん"]:
    listbox.insert(tk.END, item)
listbox.bind("<<ListboxSelect>>", on_select)
listbox.pack(pady=5)

# メインループ
root.mainloop()
