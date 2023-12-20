from Player import Player

class HumanPlayer(Player):
    def __init__(self, color):
        super().__init__(color)

    def get_move(self, board):
        valid_move = False
        while not valid_move:
            try:
                move = input("Entrez votre coup (format 'x y'): ").split()
                x, y = int(move[0]), int(move[1])
                if board.is_valid_move(self.color, x, y):
                    valid_move = True
                else:
                    print("Coup invalide, essayez à nouveau.")
            except (IndexError, ValueError):
                print("Format invalide, utilisez 'x y'.")
        return [self.color, x, y]
