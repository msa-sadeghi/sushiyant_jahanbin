import tkinter as tk

class SmartForm:
    """
    فرم هوشمند با اعتبارسنجی، رویدادها و ورودی کامل
    """

    def __init__(self, root):
        self.root = root
        self.root.title("فرم هوشمند - تمرین فصل ۳ و ۴")
        self.root.geometry("420x320")
        self.root.resizable(False, False)

        self.tasks = []
        self._build_ui()
        self._bind_events()

    def _build_ui(self):
        # ── Header ──────────────────────────────
        header = tk.Frame(self.root, bg="#2c3e50")
        header.pack(fill="x")
        tk.Label(header, text="➕ افزودن کار جدید",
                 bg="#2c3e50", fg="white",
                 font=("Tahoma", 14, "bold")).pack(pady=12)

        # ── Form ────────────────────────────────
        form = tk.Frame(self.root, padx=20, pady=15)
        form.pack(fill="both")

        # ردیف ۱: عنوان
        tk.Label(form, text="عنوان کار *", anchor="e",
                 width=14).grid(row=0, column=0, sticky="e", pady=6)
        self.title_entry = tk.Entry(form, width=28, font=("Tahoma", 11))
        self.title_entry.grid(row=0, column=1, sticky="ew", pady=6)

        # ردیف ۲: اولویت
        tk.Label(form, text="اولویت", anchor="e",
                 width=14).grid(row=1, column=0, sticky="e", pady=6)

        priority_frame = tk.Frame(form)
        priority_frame.grid(row=1, column=1, sticky="w")

        self.priority_var = tk.StringVar(value="معمولی")
        for p in ["کم", "معمولی", "بالا"]:
            tk.Radiobutton(priority_frame, text=p,
                           variable=self.priority_var,
                           value=p).pack(side="left", padx=5)

        # ردیف ۳: پیام خطا
        self.error_label = tk.Label(form, text="",
                                    fg="red", font=("Tahoma", 9))
        self.error_label.grid(row=2, column=0, columnspan=2)

        # ردیف ۴: دکمه‌ها
        btn_frame = tk.Frame(form)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.add_btn = tk.Button(btn_frame, text="افزودن  [Enter]",
                                 bg="#27ae60", fg="white",
                                 font=("Tahoma", 10, "bold"),
                                 padx=15, pady=5,
                                 cursor="hand2",
                                 command=self.add_task)
        self.add_btn.pack(side="left", padx=5)

        tk.Button(btn_frame, text="پاک کردن  [Esc]",
                  bg="#e74c3c", fg="white",
                  font=("Tahoma", 10),
                  padx=15, pady=5,
                  cursor="hand2",
                  command=self.clear_form).pack(side="left", padx=5)

        form.grid_columnconfigure(1, weight=1)

        # ── Footer ──────────────────────────────
        self.footer = tk.Frame(self.root, bg="#ecf0f1")
        self.footer.pack(fill="x", side="bottom")
        self.status_label = tk.Label(self.footer,
                                     text="آماده — Enter برای افزودن",
                                     bg="#ecf0f1", fg="#7f8c8d",
                                     font=("Tahoma", 9))
        self.status_label.pack(pady=6)

    def _bind_events(self):
        # Enter برای submit
        self.root.bind("<Return>", lambda e: self.add_task())

        # Escape برای پاک کردن
        self.root.bind("<Escape>", lambda e: self.clear_form())

        # Ctrl+Z برای لغو آخرین کار
        self.root.bind("<Control-z>", lambda e: self.undo_last())

        # وقتی روی Entry فوکوس می‌رود، خطا پاک شود
        self.title_entry.bind("<FocusIn>", lambda e: self.error_label.config(text=""))

        # Hover روی دکمه‌ی افزودن
        self.add_btn.bind("<Enter>", lambda e: self.add_btn.config(bg="#2ecc71"))
        self.add_btn.bind("<Leave>", lambda e: self.add_btn.config(bg="#27ae60"))

    def validate(self):
        title = self.title_entry.get().strip()

        if not title:
            self.error_label.config(text=" عنوان کار الزامی است")
            self.title_entry.focus()
            return None

        if len(title) < 3:
            self.error_label.config(text=" عنوان باید حداقل ۳ کاراکتر باشد")
            self.title_entry.focus()
            return None

        if len(title) > 50:
            self.error_label.config(text=" عنوان نباید بیش از ۵۰ کاراکتر باشد")
            return None

        if title in self.tasks:
            self.error_label.config(text=" این کار قبلاً ثبت شده است")
            return None

        return title

    def add_task(self):
        title = self.validate()
        if title is None:
            return

        priority = self.priority_var.get()
        task = f"[{priority}] {title}"
        self.tasks.append(title)

        self.error_label.config(text="", fg="red")
        self.status_label.config(
            text=f" «{title}» با اولویت {priority} اضافه شد  |  مجموع: {len(self.tasks)} کار",
            fg="#27ae60"
        )
        self.clear_form()
        print(f"کار اضافه شد: {task}")

    def clear_form(self):
        self.title_entry.delete(0, tk.END)
        self.priority_var.set("معمولی")
        self.error_label.config(text="")
        self.title_entry.focus()

    def undo_last(self):
        if self.tasks:
            removed = self.tasks.pop()
            self.status_label.config(
                text=f" «{removed}» حذف شد  |  مجموع: {len(self.tasks)} کار",
                fg="#e67e22"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartForm(root)
    root.mainloop()