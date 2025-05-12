from model import WordPuzzleGameModel
from view import WordPuzzleGameView

class WordPuzzleGameController:
    def __init__(self, root):
        self.model = WordPuzzleGameModel()
        self.view = WordPuzzleGameView(root, self)

    def get_themes(self):
        return self.model.THEMES.keys()

    def start_game(self, theme):
        self.model.set_theme(theme)
        response = self.model.start_game()
        self.view.update_words(response)
        self.view.clear_entry()
        self.view.update_score(self.model.score)

    def check_words(self, entered_words):
        response = self.model.check_words(entered_words)
        self.view.update_words(response)
        self.view.clear_entry()
        self.view.update_score(self.model.score)

if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    app = WordPuzzleGameController(root)
    root.mainloop()
