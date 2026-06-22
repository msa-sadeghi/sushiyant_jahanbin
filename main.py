# import tkinter as tk

# root = tk.Tk()
# root.geometry("300x200")

# tk.Label(root, text="موقعیت دقیق", bg="lightyellow").place(x=150, y=50)
# tk.Label(root, text="موقعیت نسبی", bg="lightgreen").place(relx=0.5, rely=0.5, anchor="center")

# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("اسکلت برنامه استاندارد")
root.geometry("400x400")

# ---------------- Header ----------------
header_frame = tk.Frame(root, bg="#2c3e50", height=60)
header_frame.pack(fill="x", side="top")

header_label = tk.Label(
    header_frame,
    text="مدیریت کارها",
    bg="#2c3e50",
    fg="white",
    font=("Tahoma", 18, "bold")
)
header_label.pack(pady=15)

# ---------------- Footer (قبل از Body چیده می‌شود تا جا تنگ نشود) ----------------
footer_frame = tk.Frame(root, bg="#ecf0f1", height=50)
footer_frame.pack(fill="x", side="bottom")

status_label = tk.Label(footer_frame, text="آماده", bg="#ecf0f1", fg="#7f8c8d")
status_label.pack(pady=10)

# ---------------- Body ----------------
body_frame = tk.Frame(root, bg="white")
body_frame.pack(fill="both", expand=True, side="top")

# داخل Body می‌توانیم از Grid استفاده کنیم چون یک کانتینر مستقل است
tk.Label(body_frame, text="عنوان کار:", bg="white").grid(row=0, column=0, padx=10, pady=20, sticky="e")
tk.Entry(body_frame, width=30).grid(row=0, column=1, padx=10, pady=20)

body_frame.grid_columnconfigure(1, weight=1)

root.mainloop()