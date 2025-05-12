import tkinter as tk

class WordPuzzleGameView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Игра для развития памяти")
        self.root.geometry("450x520")
        self.root.configure(bg="#2c3e50")

        self.selected_theme_name = tk.StringVar(value="Технологии")

        # Заголовок
        self.title_label = tk.Label(root, text="Memory game",
                                    font=("Helvetica", 24, "bold"),
                                    bg="#2c3e50", fg="#ecf0f1")
        self.title_label.pack(pady=(20, 10))

        # Выбор тематики
        theme_frame = tk.Frame(root, bg="#2c3e50")
        theme_frame.pack(pady=10)

        theme_label = tk.Label(theme_frame, text="Выберите тематику:",
                               font=("Helvetica", 14), bg="#2c3e50", fg="#ecf0f1")
        theme_label.pack(side="left", padx=5)

        theme_options = list(self.controller.get_themes())
        self.theme_menu = tk.OptionMenu(theme_frame, self.selected_theme_name, *theme_options)
        self.theme_menu.config(font=("Helvetica", 14), bg="#34495e", fg="#ecf0f1", activebackground="#2980b9", relief="flat")
        self.theme_menu["menu"].config(bg="#34495e", fg="#ecf0f1", font=("Helvetica", 12))
        self.theme_menu.pack(side="left", padx=5)

        # Кнопка начала игры
        self.start_button = tk.Button(root, text="Начать игру",
                                      font=("Helvetica", 14, "bold"),
                                      bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white",
                                      relief="flat",
                                      command=self.on_start_click)
        self.start_button.pack(pady=15, ipadx=10, ipady=5)

        # Метка для слов и сообщений
        self.words_label = tk.Label(root, text="",
                                    font=("Helvetica", 16),
                                    bg="#34495e", fg="#ecf0f1",
                                    justify="center",
                                    wraplength=400,
                                    relief="ridge",
                                    bd=3,
                                    padx=10,
                                    pady=10)
        self.words_label.pack(pady=15, fill='both', expand=False)

        # Поле ввода
        self.entry = tk.Entry(root, font=("Helvetica", 16), justify="center", bd=3, relief="flat")
        self.entry.pack(pady=10, ipadx=5, ipady=5, fill='x', padx=30)

        # Кнопка проверки
        self.check_button = tk.Button(root, text="Проверить",
                                      font=("Helvetica", 14, "bold"),
                                      bg="#e67e22", fg="white", activebackground="#d35400", activeforeground="white",
                                      relief="flat",
                                      command=self.on_check_click)
        self.check_button.pack(pady=15, ipadx=10, ipady=5)

        # Подпись с текущим счетом
        self.score_label = tk.Label(root, text="Счет: 0",
                                    font=("Helvetica", 14, "bold"),
                                    bg="#2c3e50", fg="#f1c40f")
        self.score_label.pack(pady=(5, 15))

    def on_start_click(self):
        theme = self.selected_theme_name.get()
        self.controller.start_game(theme)

    def on_check_click(self):
        entered = self.entry.get()
        self.controller.check_words(entered)

    def update_words(self, text):
        self.words_label.config(text=text)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def update_score(self, score):
        self.score_label.config(text=f"Счет: {score}")
