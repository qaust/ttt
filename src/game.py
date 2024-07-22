from .board import Board
from .player import Player, AiPlayer
from random import shuffle

class Game:
    def __init__(self, self_play=True):

        dim = None
        while (not isinstance(dim, int)) or dim < 3:
            try:
                dim = int(input("Enter the board dimension >= 3: "))
            except:
                print("Please input an integer value >= 3")
                continue

        self.board = Board(dim)
        if self_play:
            self.players = [Player("X"), Player("O")]
        else:
            available_symbols = {'X', 'O'}
            chosen_symbol = None
            while chosen_symbol not in available_symbols:
                chosen_symbol = input("Select your symbol [X/O]: ")
            self.players = [Player(chosen_symbol), AiPlayer((available_symbols - chosen_symbol).pop())]
        shuffle(self.players)
        self.curr_player_idx = 0

    def switch_players(self):
        self.curr_player_idx = 1 - self.curr_player_idx

    def continue_playing(self):
        player = self.players[self.curr_player_idx]

        print(f"Player {player.symbol} moves".center(self.board.max_len))
        print()

        # Make a move and print the board
        row = None
        col = None
        while not self.board.is_valid_move(row, col):
            print("Please select a valid move...")
            try:
                row = int(input(f"Please select the ROW you want (0-{self.board.dim - 1}): "))
                col = int(input(f"Please select the COLUMN you want (0-{self.board.dim - 1}): "))
            except KeyboardInterrupt:
                print("\nGame ended early :(")
                return False
            except:
                print("Please enter a valid row, col pair")
                continue
        self.board.update_board(player.symbol, row, col)
        print(self.board)

        # Check for win or draw
        if self.board.is_winner(player.symbol):
            print(f"Player {player.symbol} Wins!")
            return False
        elif self.board.is_draw():
            print("The games ends in a draw :/")
            return False
        else:
            self.switch_players()
            return True

    def play(self):
        playing = True    
        print(self.board)    
        while playing:
            playing = self.continue_playing()
            



