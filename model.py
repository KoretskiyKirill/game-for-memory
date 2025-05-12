import random

class WordPuzzleGameModel:
    LEVELS = [3, 4, 5]  # Количество слов на каждом уровне
    THEMES = {
        "Технологии": [
            "Абстракция", "Бинарный", "Виртуальный", "Генерация", "Декомпозиция",
            "Емкость", "Жесткий", "Запрос", "Инициализация", "Кэширование",
            "Логирование", "Миграция", "Наследование", "Объект", "Параллелизм",
            "Рефакторинг", "Сериализация", "Транзакция", "Унификация", "Фреймворк"
        ],
        "Природа": [
            "Амфибия", "Барсук", "Водоросль", "Геотермальный", "Дождевая",
            "Живородящий", "Землеройка", "Иглобрюх", "Коралловый", "Листопад",
            "Мох", "Норка", "Озерный", "Пещера", "Реликтовый",
            "Саранча", "Тропический", "Утенок", "Фауна", "Цветок"
        ],
        "Кулинария": [
            "Аперитив", "Бланширование", "Гарнир", "Демиглас", "Желе",
            "Зест", "Ингредиент", "Карамелизация", "Лавровый", "Маринад",
            "Нуга", "Обжарка", "Пюре", "Рататуй", "Соус",
            "Тирамису", "Уксус", "Флан", "Холодец", "Чабрец"
        ]
    }

    def __init__(self):
        self.score = 0
        self.level = 0
        self.target_words = []
        self.is_game_running = False
        self.theme_words = []

    def set_theme(self, theme_name):
        self.theme_words = self.THEMES.get(theme_name, [])

    def start_game(self):
        self.score = 0
        self.level = 0
        self.is_game_running = True
        return self.next_level()

    def next_level(self):
        if self.level < len(self.LEVELS):
            self.level += 1
            if len(self.theme_words) < self.LEVELS[self.level - 1]:
                self.is_game_running = False
                return "Недостаточно слов для выбранного уровня."
            self.target_words = random.sample(self.theme_words, self.LEVELS[self.level - 1])
            return self.show_words()
        else:
            self.is_game_running = False
            return f"Игра окончена! Ваш финальный счет: {self.score}"

    def show_words(self):
        return "Запомните слова:\n" + "\n".join(self.target_words)

    def check_words(self, entered_text):
        if not self.is_game_running:
            return "Игра не запущена. Нажмите 'Начать игру' для начала."

        expected = " ".join(self.target_words)
        entered = entered_text.strip()
        if entered == expected:
            self.score += 1
            return self.next_level()
        else:

            return f"Неправильно! Ваш счет: {self.score}\nПопробуйте снова."
