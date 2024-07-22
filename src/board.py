from itertools import chain
from pprint import pprint

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
    def __init__(self, dim=3) -> None:
        self.dim = dim
        self.board = [[' ' for _ in range(dim)] for _ in range(dim)]
        self.cell_width = 3
        self.hpadding = 10
        self.max_len = self.cell_width * dim + (dim - 1) + 2 * self.hpadding

    def __repr__(self):
        repr = '\n'
        repr += '~~ TIC-TAC-TOE ~~'.center(self.max_len) + '\n\n'
        for i, row in enumerate(self.board):
            repr += (' | '.join(row)).center(self.max_len) + '\n'
            if i < self.dim - 1:
                repr += (("-"*(self.cell_width) + '+')*(self.dim - 1) + "-"*(self.cell_width)).center(self.max_len)
                repr += '\n'

        return repr

    def get_horizontals(self):
        horizontals = [[(r, c) for r in range(self.dim)] for c in range(self.dim)]
        return horizontals

    def get_verticals(self):
        verticals = [[(r, c) for c in range(self.dim)] for r in range(self.dim)]
        return verticals

    def get_diagonals(self):
        diagonals = []
        diagonals.append([(i, i) for i in range(self.dim)])
        diagonals.append([(i, self.dim - i - 1) for i in range(self.dim - 1, -1, -1)])
        return diagonals

    def is_winner(self, player):
        horizontals = self.get_horizontals()
        verticals = self.get_verticals()
        diagonals = self.get_diagonals()
        winners = [*horizontals, *verticals, *diagonals]

        for winner in winners:
            if all([self.board[row][col] == player for row, col in winner]):
                return True
        return False

    def is_draw(self):
        return ' ' not in list(chain(*self.board))

    def update_board(self, player, row, col):
        self.board[row][col] = player
        return None

    def is_valid_move(self, row, col):
        if isinstance(row, int) and isinstance(col, int):
            if (row >= self.dim) or (col >= self.dim):
                return False
            elif self.board[row][col] == ' ':
                return True
            else:
                return False
        elif (row is None) or (col is None):
            return False
        else:
            return False
