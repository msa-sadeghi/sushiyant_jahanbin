import tkinter as tk
from tkinter import messagebox
import json


def show_history():
    try:
        with open("task_save", "r") as f:
            
            recived_data = json.load(f)
            for line in  recived_data:
                print(line)
                print(type(line))
                listbox.insert(tk.END, line["t"])

    except:
        return


all_tasks = []


def add_task():
    listbox.insert(tk.END, task_var.get())
    json_data = {"t": entry.get()}
    all_tasks.append(json_data)
    with open("task_save", "w") as f:
        json.dump(all_tasks, f)


window = tk.Tk()
window.geometry("400x250")
task_var = tk.StringVar()
entry = tk.Entry(window, textvariable=task_var, width=30)
entry.pack()
listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)
add_button = tk.Button(window, text="Add Task", command=add_task)
history_button = tk.Button(window, text="show history", command=show_history).pack()
add_button.pack()
window.bind("<Return>", lambda e: add_task())

show_history()
window.mainloop()
