from .board import Board
from .player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.curr_player_idx = 0

    def switch_players(self):
        self.curr_player_idx = 1 - self.curr_player_idx

    def continue_playing(self):
        player = self.players[self.curr_player_idx]

        # Make a move and print the board
        row = None
        col = None
        while not self.board.is_valid_move(row, col):
            print("Please select a valid move...")
            row = int(input("Please select the row you want (0-2): "))
            col = int(input("Please select the column you want (0-2): "))
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
        while playing:
            print(self.board)
            playing = self.continue_playing()
            



