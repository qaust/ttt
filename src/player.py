class Player:
    def __init__(self, symbol):
        assert symbol in {"X", "O"}, 'symbol must be in {"X", "O"}'
        self.symbol = symbol

    def make_move(self, board, row, col):
        return board.make_move(self.symbol, row, col)


class AiPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
        pass