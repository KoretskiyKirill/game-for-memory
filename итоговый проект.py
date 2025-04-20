import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Константы
LEVELS = [3, 4, 5]  # Количество слов на каждом уровне
WORDS = [
    "Асимптотический", "Когерентность", "Детерминированный", "Интерполяция", "Модульность",
    "Синхронизация", "Парадигма", "Алгоритмический", "Криптографический", "Декодирование",
    "Энкапсуляция", "Метафора", "Семантика", "Аналогия", "Классификация",
    "Оптимизация", "Рекурсия", "Синтаксис", "Трансформация", "Функциональность"
]

# Хранение состояния игры
games = {}

class WordPuzzleGame:
    def __init__(self):
        self.score = 0
        self.level = 0
        self.target_words = []
        self.is_game_running = False

    def start_game(self):
        self.score = 0
        self.level = 0
        self.is_game_running = True
        return self.next_level()

    def next_level(self):
        if self.level < len(LEVELS):
            self.level += 1
            self.target_words.append(random.sample(WORDS, LEVELS[self.level - 1]))
            return self.show_words()
        else:
            return "Игра окончена! Ваш финальный счет: {}".format(self.score)

    def show_words(self):
        return "Запомните слова:\n" + "\n".join(self.target_words)

    def check_words(self, entered_words):
        print("".join(self.target_words))
        if not self.is_game_running:
            return "Игра не запущена. Используйте /start для начала."

        if entered_words == "".join(self.target_words):
            self.score += 1
            return self.next_level()
        else:
            self.score -= 1
            return "Неправильно! Ваш счет: {}\nПопробуйте снова.".format(self.score)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    games[user_id] = WordPuzzleGame()
    response = games[user_id].start_game()
    await update.message.reply_text(response)

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_id not in games:
        await update.message.reply_text("Сначала начните игру с помощью /start.")
        return

    entered_words = context.args
    response = games[user_id].check_words(entered_words)
    await update.message.reply_text(response)

def main():
    application = ApplicationBuilder().token("7861939196:AAEOD3zvgE6Bi80n0rgrLe-8XsB4mGuPfv8").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("check", check))

    application.run_polling()

if __name__ == '__main__':
    main()