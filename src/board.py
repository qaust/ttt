from itertools import chain

class Cell:
    def __init__(self):
        self.value = " "

    def __repr__(self):
        return str(self.value)

    def _set_value(self, value):
        assert value in {" ", "X", "O"}, 'Value must be in {" ", "X", "O"}'
        self.value = value

class Board:
    """
    3x3 board that holds moves
    """
    def __init__(self) -> None:
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.cell_width = 3

    def __repr__(self):
        repr = ''
        for i, row in enumerate(self.board):
            repr += ' ' + ' | '.join(row) + '\n'
            if i < 2:
                repr += ("-"*(self.cell_width) + '+')*2 + "-"*(self.cell_width)+ '\n'

        return repr

    def is_winner(self, player):

        assert player in {"X", "O"}, 'player must be in {"X", "O"}'

        winning_indices = [
            [(0, 0), (0, 1), (0, 2)],   # First row
            [(1, 0), (1, 1), (1, 2)],   # Second row
            [(2, 0), (2, 1), (2, 2)],   # Third row

            [(0, 0), (1, 1), (2, 2)],   # Diagonal from top left to bottom right
            [(2, 0), (1, 1), (0, 2)],   # Diagonal from bottom left to top right

            [(0, 0), (1, 0), (2, 0)],   # First column
            [(0, 1), (1, 1), (2, 1)],   # Second column
            [(0, 2), (1, 2), (2, 2)],   # Third column
        ]

        for idx in winning_indices:
            if all([self.board[row][col] == player for row, col in idx]):
                return True
        return False

    def is_draw(self):
        return ' ' not in list(chain(*self.board))

    def update_board(self, player, row, col):
        self.board[row][col] = player
        return None

    def is_valid_move(self, row, col):
        if (row is None) or (col is None):
            return False
        elif self.board[row][col] == ' ':
            return True
        else:
            return False
