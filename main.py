import tkinter as tk

root = tk.Tk()
root.geometry("350x150")

# ساخت یک متغیر هوشمند
task_var = tk.StringVar()

# اتصال متغیر به Entry
entry = tk.Entry(root, textvariable=task_var, width=30, font=("Tahoma", 12))
entry.pack(pady=10)

# هر بار که entry تغییر کند، این label هم آپدیت می‌شود
preview_label = tk.Label(root, text="", font=("Tahoma", 11))
preview_label.pack()

def on_change(*args):
    preview_label.config(text=f"پیش‌نمایش: {task_var.get()}")

# وقتی مقدار StringVar تغییر کند، این تابع صدا زده می‌شود
task_var.trace("w", on_change)

root.mainloop()