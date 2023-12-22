class Player:
    # Constructeur de la classe Player.
    # Initialise un joueur avec une couleur spécifiée (noir ou blanc).
    def __init__(self, color):
        self.color = color
 
        
    # Méthode abstraite pour obtenir le mouvement du joueur.
    def get_move(self, board):
        raise NotImplementedError("La méthode get_move doit être implémentée par la sous-classe")
