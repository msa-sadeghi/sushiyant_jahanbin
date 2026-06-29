import tkinter as tk
from tkinter import messagebox


class TodoApp:
    """
    Todo List کامل با Tkinter
    امکانات: افزودن، حذف، علامت‌زدن به‌عنوان انجام‌شده،
             پاکسازی کامل، شمارنده‌ی وضعیت
    """

    # ── رنگ‌های برنامه (پالت ثابت) ─────────────────────────
    COLORS = {
        "bg_header":    "#2c3e50",
        "bg_body":      "#f5f6fa",
        "bg_footer":    "#dfe6e9",
        "accent":       "#3498db",
        "accent_hover": "#2980b9",
        "danger":       "#e74c3c",
        "danger_hover": "#c0392b",
        "success":      "#27ae60",
        "done_fg":      "#95a5a6",
        "text_main":    "#2c3e50",
        "text_light":   "#7f8c8d",
        "white":        "#ffffff",
    }

    def __init__(self, root):
        self.root = root
        self.root.title("📝 Todo List")
        self.root.geometry("460x520")
        self.root.resizable(False, False)
        self.root.configure(bg=self.COLORS["bg_body"])

        # داده‌ها
        # هر آیتم یک dict است: {"text": str, "done": bool}
        self.tasks = []

        self._build_ui()
        self._bind_events()
        self._update_status()

    # ════════════════════════════════════════════════════════
    # ساخت رابط کاربری
    # ════════════════════════════════════════════════════════

    def _build_ui(self):
        self._build_header()
        self._build_input_area()
        self._build_list_area()
        self._build_action_buttons()
        self._build_footer()

    def _build_header(self):
        header = tk.Frame(self.root, bg=self.COLORS["bg_header"], height=65)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="📝  لیست کارهای من",
            bg=self.COLORS["bg_header"],
            fg=self.COLORS["white"],
            font=("Tahoma", 17, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

    def _build_input_area(self):
        """ناحیه‌ی ورودی: Entry + دکمه افزودن"""
        input_frame = tk.Frame(
            self.root,
            bg=self.COLORS["bg_body"],
            padx=15, pady=12
        )
        input_frame.pack(fill="x")

        # Entry
        self.task_entry = tk.Entry(
            input_frame,
            font=("Tahoma", 12),
            fg=self.COLORS["text_main"],
            bg=self.COLORS["white"],
            relief="solid",
            bd=1,
            highlightthickness=2,
            highlightcolor=self.COLORS["accent"],
            highlightbackground="#dfe6e9"
        )
        self.task_entry.pack(side="left", fill="x", expand=True, ipady=6)
        self.task_entry.focus()

        # دکمه افزودن
        self.add_btn = tk.Button(
            input_frame,
            text="  +  افزودن  ",
            bg=self.COLORS["accent"],
            fg=self.COLORS["white"],
            font=("Tahoma", 11, "bold"),
            relief="flat",
            cursor="hand2",
            activebackground=self.COLORS["accent_hover"],
            activeforeground=self.COLORS["white"],
            command=self.add_task
        )
        self.add_btn.pack(side="left", padx=(8, 0), ipady=6)

        # Hover effect
        self.add_btn.bind("<Enter>", lambda e: self.add_btn.config(bg=self.COLORS["accent_hover"]))
        self.add_btn.bind("<Leave>", lambda e: self.add_btn.config(bg=self.COLORS["accent"]))

    def _build_list_area(self):
        """ناحیه‌ی لیست: Listbox + Scrollbar"""
        list_container = tk.Frame(
            self.root,
            bg=self.COLORS["bg_body"],
            padx=15
        )
        list_container.pack(fill="both", expand=True)

        # Frame داخلی برای Listbox و Scrollbar
        inner = tk.Frame(
            list_container,
            bg=self.COLORS["white"],
            highlightthickness=1,
            highlightbackground="#dfe6e9"
        )
        inner.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(inner, cursor="arrow")
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            inner,
            font=("Tahoma", 12),
            bg=self.COLORS["white"],
            fg=self.COLORS["text_main"],
            selectbackground=self.COLORS["accent"],
            selectforeground=self.COLORS["white"],
            activestyle="none",
            relief="flat",
            bd=0,
            highlightthickness=0,
            yscrollcommand=scrollbar.set,
            selectmode="single",
            cursor="hand2"
        )
        self.listbox.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        scrollbar.config(command=self.listbox.yview)

    def _build_action_buttons(self):
        """ردیف دکمه‌های عملیاتی"""
        btn_frame = tk.Frame(self.root, bg=self.COLORS["bg_body"], pady=10, padx=15)
        btn_frame.pack(fill="x")

        buttons = [
            ("  انجام شد", self.COLORS["success"], self.COLORS["success"], self.mark_done),
            ("  ویرایش",   self.COLORS["accent"],  self.COLORS["accent"],  self.edit_task),
            ("  حذف",      self.COLORS["danger"],  self.COLORS["danger"],  self.delete_task),
            ("  پاک کردن همه", "#636e72", "#636e72", self.clear_all),
        ]

        for text, bg, hover, cmd in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                bg=bg,
                fg="white",
                font=("Tahoma", 10),
                relief="flat",
                cursor="hand2",
                activeforeground="white",
                activebackground=hover,
                padx=8, pady=4,
                command=cmd
            )
            btn.pack(side="left", padx=3)

            # ذخیره‌ی رنگ برای hover
            _bg = bg
            btn.bind("<Enter>", lambda e, b=btn, c=_bg: b.config(bg=self._darken(c)))
            btn.bind("<Leave>", lambda e, b=btn, c=_bg: b.config(bg=c))

    def _build_footer(self):
        """نوار وضعیت پایین"""
        footer = tk.Frame(self.root, bg=self.COLORS["bg_footer"], height=35)
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)

        self.status_label = tk.Label(
            footer,
            text="",
            bg=self.COLORS["bg_footer"],
            fg=self.COLORS["text_light"],
            font=("Tahoma", 9)
        )
        self.status_label.place(relx=0.5, rely=0.5, anchor="center")

    # ════════════════════════════════════════════════════════
    # اتصال رویدادها
    # ════════════════════════════════════════════════════════

    def _bind_events(self):
        # Enter برای افزودن
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        # Escape برای پاک کردن Entry
        self.task_entry.bind("<Escape>", lambda e: self.task_entry.delete(0, tk.END))

        # Delete روی listbox برای حذف
        self.listbox.bind("<Delete>", lambda e: self.delete_task())

        # Space روی listbox برای علامت‌زدن
        self.listbox.bind("<space>", lambda e: self.mark_done())

        # دابل‌کلیک برای ویرایش
        self.listbox.bind("<Double-Button-1>", lambda e: self.edit_task())

        # کلیدهای میانبر
        self.root.bind("<Control-z>", lambda e: self.delete_last_added())
        self.root.bind("<Control-a>", lambda e: self._select_all())

    # ════════════════════════════════════════════════════════
    # منطق برنامه (Business Logic)
    # ════════════════════════════════════════════════════════

    def add_task(self):
        """افزودن کار جدید"""
        text = self.task_entry.get().strip()

        # اعتبارسنجی
        if not text:
            self._flash_entry()
            return

        if len(text) < 2:
            self._set_status("  عنوان خیلی کوتاه است (حداقل ۲ کاراکتر)", "warning")
            return

        # بررسی تکراری بودن
        existing = [t["text"].lower() for t in self.tasks]
        if text.lower() in existing:
            self._set_status("  این کار قبلاً در لیست است", "warning")
            return

        # افزودن به داده‌ها
        self.tasks.append({"text": text, "done": False})

        # افزودن به Listbox
        self.listbox.insert(tk.END, f"  ○  {text}")
        self.listbox.see(tk.END)

        # پاک کردن Entry و فوکوس
        self.task_entry.delete(0, tk.END)
        self.task_entry.focus()

        self._set_status(f"  «{text}» اضافه شد", "success")
        self._update_status()

    def delete_task(self):
        """حذف کار انتخاب‌شده"""
        selection = self.listbox.curselection()
        if not selection:
            self._set_status("  ابتدا یک کار انتخاب کن", "warning")
            return

        index = selection[0]
        task_text = self.tasks[index]["text"]

        # تأییدیه برای حذف
        confirm = messagebox.askyesno(
            "حذف کار",
            f"آیا مطمئنی که می‌خواهی «{task_text}» را حذف کنی؟"
        )
        if not confirm:
            return

        # حذف از داده‌ها و listbox
        self.tasks.pop(index)
        self.listbox.delete(index)

        self._set_status(f"  «{task_text}» حذف شد", "info")
        self._update_status()

    def mark_done(self):
        """علامت‌زدن کار به‌عنوان انجام‌شده / برگرداندن"""
        selection = self.listbox.curselection()
        if not selection:
            self._set_status("  ابتدا یک کار انتخاب کن", "warning")
            return

        index = selection[0]
        task = self.tasks[index]

        # Toggle وضعیت
        task["done"] = not task["done"]

        if task["done"]:
            # نمایش به‌صورت انجام‌شده
            self.listbox.delete(index)
            self.listbox.insert(index, f"  ✓  {task['text']}")
            self.listbox.itemconfig(index,
                                    fg=self.COLORS["done_fg"],
                                    selectforeground=self.COLORS["done_fg"])
            self._set_status(f"  «{task['text']}» انجام شد!", "success")
        else:
            # برگشت به حالت عادی
            self.listbox.delete(index)
            self.listbox.insert(index, f"  ○  {task['text']}")
            self.listbox.itemconfig(index,
                                    fg=self.COLORS["text_main"],
                                    selectforeground=self.COLORS["white"])
            self._set_status(f"  «{task['text']}» به لیست برگشت", "info")

        # حفظ انتخاب
        self.listbox.selection_set(index)
        self._update_status()

    def edit_task(self):
        """ویرایش کار انتخاب‌شده"""
        selection = self.listbox.curselection()
        if not selection:
            self._set_status("  ابتدا یک کار انتخاب کن", "warning")
            return

        index = selection[0]
        task = self.tasks[index]

        if task["done"]:
            self._set_status("  کارهای انجام‌شده قابل ویرایش نیستند", "warning")
            return

        # باز کردن پنجره‌ی ویرایش
        self._open_edit_window(index, task["text"])

    def _open_edit_window(self, index, current_text):
        """پنجره popup برای ویرایش"""
        popup = tk.Toplevel(self.root)
        popup.title("ویرایش کار")
        popup.geometry("350x140")
        popup.resizable(False, False)
        popup.transient(self.root)   # وابسته به پنجره‌ی اصلی
        popup.grab_set()             # فوکوس قفل شود روی popup

        # وسط صفحه
        popup.geometry("+%d+%d" % (
            self.root.winfo_x() + 55,
            self.root.winfo_y() + 190
        ))

        tk.Label(popup, text="متن جدید:", font=("Tahoma", 11)).pack(pady=(15, 5))

        edit_entry = tk.Entry(popup, width=35, font=("Tahoma", 11))
        edit_entry.pack(padx=20)
        edit_entry.insert(0, current_text)
        edit_entry.select_range(0, tk.END)
        edit_entry.focus()

        def save_edit():
            new_text = edit_entry.get().strip()
            if not new_text:
                return
            if new_text == current_text:
                popup.destroy()
                return

            # آپدیت داده
            self.tasks[index]["text"] = new_text

            # آپدیت listbox
            self.listbox.delete(index)
            self.listbox.insert(index, f"  ○  {new_text}")
            self.listbox.selection_set(index)

            self._set_status(f"  ویرایش شد: «{new_text}»", "info")
            popup.destroy()

        btn_frame = tk.Frame(popup)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="ذخیره",
                  bg=self.COLORS["success"], fg="white",
                  relief="flat", padx=12, pady=4,
                  command=save_edit).pack(side="left", padx=5)

        tk.Button(btn_frame, text="انصراف",
                  bg="#636e72", fg="white",
                  relief="flat", padx=12, pady=4,
                  command=popup.destroy).pack(side="left", padx=5)

        # Enter برای ذخیره، Escape برای لغو
        edit_entry.bind("<Return>", lambda e: save_edit())
        popup.bind("<Escape>", lambda e: popup.destroy())

    def clear_all(self):
        """پاک کردن کل لیست"""
        if not self.tasks:
            self._set_status("  لیست از قبل خالی است", "warning")
            return

        count = len(self.tasks)
        confirm = messagebox.askyesno(
            "پاک کردن همه",
            f"آیا مطمئنی که می‌خواهی {count} کار را پاک کنی؟\nاین عملیات قابل بازگشت نیست."
        )
        if not confirm:
            return

        self.tasks.clear()
        self.listbox.delete(0, tk.END)
        self._set_status("  همه‌ی کارها پاک شدند", "info")
        self._update_status()

    def delete_last_added(self):
        """Ctrl+Z — حذف آخرین کار اضافه‌شده"""
        # آخرین کاری که done نیست پیدا کن و حذف کن
        for i in range(len(self.tasks) - 1, -1, -1):
            if not self.tasks[i]["done"]:
                text = self.tasks[i]["text"]
                self.tasks.pop(i)
                self.listbox.delete(i)
                self._set_status(f"  «{text}» لغو شد (Ctrl+Z)", "info")
                self._update_status()
                return

        self._set_status("  چیزی برای لغو وجود ندارد", "warning")

    def _select_all(self):
        """Ctrl+A — انتخاب همه"""
        self.listbox.selection_set(0, tk.END)

    # ════════════════════════════════════════════════════════
    # توابع کمکی (Helpers)
    # ════════════════════════════════════════════════════════

    def _update_status(self):
        """بروزرسانی نوار وضعیت پایین"""
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["done"])
        pending = total - done

        if total == 0:
            text = "لیست خالی است — یک کار اضافه کن"
        else:
            percent = int((done / total) * 100)
            text = (
                f"مجموع: {total}   |   "
                f"انجام‌شده: {done}   |   "
                f"باقی‌مانده: {pending}   |   "
                f"پیشرفت: {percent}٪"
            )

        self.status_label.config(text=text)

    def _set_status(self, msg, kind="info"):
        """نمایش پیام موقت در نوار وضعیت"""
        colors = {
            "success": self.COLORS["success"],
            "warning": "#e67e22",
            "info":    self.COLORS["text_light"],
        }
        self.status_label.config(text=msg, fg=colors.get(kind, self.COLORS["text_light"]))

        # بعد از ۳ ثانیه به وضعیت پیش‌فرض برگرد
        self.root.after(3000, self._update_status)

    def _flash_entry(self):
        """وقتی Entry خالی است، یک چشمک بزند"""
        original_bg = self.task_entry.cget("bg")
        self.task_entry.config(bg="#ffeaa7")
        self.root.after(300, lambda: self.task_entry.config(bg=original_bg))
        self.task_entry.focus()

    def _darken(self, hex_color):
        """رنگ را کمی تیره‌تر کن برای hover"""
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        factor = 0.85
        r, g, b = int(r * factor), int(g * factor), int(b * factor)
        return f"#{r:02x}{g:02x}{b:02x}"


# ════════════════════════════════════════════════════════
# نقطه‌ی ورود برنامه
# ════════════════════════════════════════════════════════
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()