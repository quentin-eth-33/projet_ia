from Player import Player

class HumanPlayer(Player):
    
    # Constructeur de la classe HumanPlayer.
    # Initialise un joueur humain avec une couleur spécifiée (noir ou blanc).
    # 'color' détermine la couleur des pièces du joueur dans le jeu.
    def __init__(self, color):
        super().__init__(color)

    # Demande et retourne le coup choisi par le joueur humain.
    # Cette méthode boucle jusqu'à ce qu'un coup valide soit entré par l'utilisateur.
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
