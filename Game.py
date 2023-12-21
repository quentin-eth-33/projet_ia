from Reversi import Board
from AIPlayer import AIPlayer
from HumanPlayer import HumanPlayer

class Game:
    def __init__(self, board_size=8):
        self.board = Board(board_size)
        self.players = [AIPlayer(Board._BLACK), HumanPlayer(Board._WHITE)]


    def run(self):
        while not self.board.is_game_over():
            current_player = self.players[self.board._nextPlayer - 1]
            print(self.board)
            move = current_player.get_move(self.board)
            if move is not None:
                self.board.push(move)
                print(f"Joueur {current_player.color} joue: {move[1]}, {move[2]}")



if __name__ == "__main__":
    game = Game(board_size=10)
    game.run()
