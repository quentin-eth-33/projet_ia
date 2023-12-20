class Player:
    def __init__(self, color):
        self.color = color  # Couleur du joueur (Board._BLACK ou Board._WHITE)

    def get_move(self, board):
        """
        Méthode abstraite pour obtenir le mouvement du joueur.
        Doit être implémentée par les sous-classes.
        """
        raise NotImplementedError("La méthode get_move doit être implémentée par la sous-classe")
