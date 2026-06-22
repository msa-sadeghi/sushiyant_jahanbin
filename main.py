import tkinter as tk

def submit():
    title = title_entry.get().strip()
    
    # قانون ۱: خالی نباشد
    if not title:
        show_error("عنوان کار الزامی است")
        title_entry.focus()   # فوکوس برمی‌گردد به Entry
        return
    
    # قانون ۲: حداقل ۳ کاراکتر
    if len(title) < 3:
        show_error("عنوان باید حداقل ۳ کاراکتر باشد")
        title_entry.focus()
        return
    
    # قانون ۳: حداکثر ۵۰ کاراکتر
    if len(title) > 50:
        show_error("عنوان نباید بیش از ۵۰ کاراکتر باشد")
        return
    
    # اگر به اینجا رسیدیم، ورودی معتبر است
    show_error("")
    result_label.config(text=f"ثبت شد: {title}", fg="green")
    title_entry.delete(0, tk.END)

def show_error(msg):
    error_label.config(text=msg, fg="red")

root = tk.Tk()
root.title("اعتبارسنجی")
root.geometry("350x200")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20, fill="both", expand=True)

tk.Label(frame, text="عنوان کار:").grid(row=0, column=0, sticky="e", pady=5)
title_entry = tk.Entry(frame, width=25, font=("Tahoma", 11))
title_entry.grid(row=0, column=1, pady=5)

error_label = tk.Label(frame, text="", fg="red", font=("Tahoma", 9))
error_label.grid(row=1, column=0, columnspan=2)

tk.Button(frame, text="ثبت", command=submit, width=15).grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=0, columnspan=2)

frame.grid_columnconfigure(1, weight=1)
root.mainloop()