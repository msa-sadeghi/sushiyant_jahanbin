import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

DB_NAME = "test.db"


class UserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Manager")
        self.root.geometry("800x500")

        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        toolbar = tk.Frame(self.root)
        toolbar.pack(fill="x", pady=5)

        tk.Button(toolbar, text="Add User", command=self.add_user).pack(side="left", padx=5)
        tk.Button(toolbar, text="Delete User", command=self.delete_user).pack(side="left", padx=5)

        columns = ("id", "name", "email", "age")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, width=150)

        self.tree.pack()

    def add_user(self):

        window = tk.Toplevel(self.root)
        window.title("Add User")

        window.geometry("300x220")

        tk.Label(window, text="name").pack()

        name_entry = tk.Entry(window)
        name_entry.pack()

        tk.Label(window, text="email").pack()

        email_entry = tk.Entry(window)
        email_entry.pack()

        tk.Label(window, text="age").pack()

        age_entry = tk.Entry(window)
        age_entry.pack()

      

        def save():
            name = name_entry.get()
            email = name_entry.get()
            age = name_entry.get()
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users(name, email, age) VALUES (?, ?, ?)", (name, email, age))

            conn.commit()
            user_id = cursor.lastrowid
            conn.close()
            self.tree.insert("", tk.END, values=(user_id, name, email, age))
            window.destroy()

        tk.Button(window, text="save", command=save).pack()
    def delete_user(self):
        pass

    def connect_db(self):
        return sqlite3.connect(DB_NAME)

    def load_data(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        query = """
                SELECT id, name, email, age FROM users
            """
        cursor.execute(query)
        for row in cursor.fetchall():
            self.tree.insert("", tk.END, values=row)

        conn.close()


root = tk.Tk()
app = UserApp(root)

root.mainloop()
