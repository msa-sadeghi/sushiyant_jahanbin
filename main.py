# import tkinter as tk

# root = tk.Tk()
# root.title("کار با Pack")
# root.geometry("300x250")

# tk.Label(root, text="ردیف 1", bg="lightblue").pack(fill="x")
# tk.Label(root, text="ردیف 2", bg="lightgreen").pack(fill="x")
# tk.Label(root, text="ردیف 3", bg="lightyellow").pack(fill="x")

# root.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.geometry("300x300")

# # بدون fill و expand
# tk.Label(root, text="بدون تنظیمات", bg="lightcoral").pack()

# # با fill="x" - فقط عرض را پر می‌کند
# tk.Label(root, text="fill=x", bg="lightblue").pack(fill="x")

# # با expand=True - فضای اضافی را اشغال می‌کند
# tk.Label(root, text="expand=True", bg="lightgreen").pack(expand=True, fill="both")

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# root.geometry("300x150")

# tk.Button(root, text="چپ").pack(side="right", padx=5, pady=20)
# tk.Button(root, text="وسط").pack(side="right", padx=5, pady=20)
# tk.Button(root, text="راست").pack(side="right", padx=5, pady=20)

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# root.title("کار با Grid")
# root.geometry("300x150")

# tk.Label(root, text="نام:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
# tk.Entry(root).grid(row=0, column=1, padx=10, pady=10)

# tk.Label(root, text="نام خانوادگی:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
# tk.Entry(root).grid(row=1, column=1, padx=10, pady=10)

# tk.Button(root, text="ثبت").grid(row=2, column=0, columnspan=2, pady=10)

# root.mainloop()


import tkinter as tk

root = tk.Tk()
root.geometry("300x150")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
# بدون sticky - وسط سلول قرار می‌گیرد
tk.Label(root, text="بدون sticky", bg="lightcoral").grid(row=0, column=0, padx=5, pady=5)

# sticky="w" - به سمت چپ سلول می‌چسبد
tk.Label(root, text="sticky=w", bg="lightblue").grid(row=1, column=0, padx=5, pady=5, sticky="w")

# sticky="ew" - عرض کامل سلول را پر می‌کند
tk.Label(root, text="sticky=ew", bg="lightgreen").grid(row=2, column=0, padx=5, pady=5, sticky="ewns")

root.mainloop()