from Reversi import Board
from AIPlayer_id import AIPlayer_id
from HumanPlayer import HumanPlayer
from AIPlayer import AIPlayer

class Game:
    # Initialise une nouvelle partie avec une taille de plateau spécifiée. 
    # Crée un plateau de jeu et initialise les joueurs
    def __init__(self, board_size=10):
        self.board = Board(board_size)
        self.players = [AIPlayer_id(Board._BLACK,8,2), HumanPlayer(Board._WHITE)]



    # Démarre et exécute la boucle de jeu. Continue jusqu'à ce que le jeu soit terminé.
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
