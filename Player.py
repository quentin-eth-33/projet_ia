class Player:
    # Constructeur de la classe Player.
    # Initialise un joueur avec une couleur spécifiée (noir ou blanc).
    _MINIMAX = 1
    _ALPHA_BETA = 2
    _NEGAMAX = 3
    _NEGA_ALPHA_BETA = 4
    
    def __init__(self, color):
        self.color = color
 
        
    # Méthode abstraite pour obtenir le mouvement du joueur.
    def get_move(self, board):
        raise NotImplementedError("La méthode get_move doit être implémentée par la sous-classe")
