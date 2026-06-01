import tkinter as tk


class TodoApp:
    def __init__(self):
        self.root = tk.Tk()
        self.app_title = "Todo App"
        self.window_width = 1000
        self.window_height = 650
        self.min_width = 900
        self.min_height = 600
        self.background_color = "#F5F7FB"
        # self.btn_exit = tk.Button(self.root, text="exit", command=self.root.destroy)
        # self.btn_settings = tk.Button(self.root, text="settings", command=self.open_settings_window)
        self.setup_window()

    def setup_window(self):
        self.root.title(self.app_title)
        self.root.configure(bg=self.background_color)
        # self.btn_exit.pack()
        # self.btn_settings.pack()
        self.root.minsize(self.min_width, self.min_height)

        self.center_window()
        self.create_widgets()

    def run(self):
        self.root.mainloop()

    def open_settings_window(self):
        window = tk.Toplevel(self.root)
        tk.Label(window, text="salaam").pack()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = screen_width // 2 - self.window_width // 2
        y = screen_height // 2 - self.window_height // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg="#FFFFFF")
        main_frame.pack(fill="both", expand=True, padx=40, pady=40)

        title_label = tk.Label(
            main_frame, text="Todo App", font=("Arial", 28, "bold"), bg=self.background_color, fg="#1F2937"
        )
        title_label.pack(pady=(40, 10))
        subtitle_label = tk.Label(
            main_frame,
            text="Manage your daily tasks professionally",
            font=("Arial", 28, "bold"),
            bg=self.background_color,
            fg="#1F2937",
        )
        subtitle_label.pack()


app = TodoApp()
app.run()
