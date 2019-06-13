from src.numgame import GameBoard

class GameModel():
    difficulties = {
        'easy': 10,
        'medium': 50,
        'hard': 100
    }

    def __init__(self, size):
        self.game = GameBoard(size)

    def new(self, size, difficulty):
        if 1 <= size <= 8 and difficulty in self.difficulties:
            self.game = GameBoard(size)
            self.game.shuffle(self.difficulties[difficulty])

    def swap(self, tile):
        if self.game.can_swap(tile):
            self.game.swap(tile)

    def valid_swap(self, tile):
        return self.game.can_swap(tile)