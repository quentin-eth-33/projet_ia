from Player import Player

class AIPlayer(Player):
    
    #-------------------------------------------------------------------------------------------------------- 
    #-----------SANS ITERATIVE DEEPENING--------------------------------------------------------------------- 
    #--------------------------------------------------------------------------------------------------------
    
    
    # Initialise une instance de AIPlayer avec une couleur spécifiée et une profondeur de recherche par défaut.
    def __init__(self, color, depth, numAlgo):
        super().__init__(color)
        self.depth = depth 
        self.numAlgo = numAlgo

    # Sélectionne et retourne le meilleur coup possible sur le plateau actuel. 
    # Cette méthode est le point d'entrée pour déterminer quel coup l'IA doit jouer en fonction de l'état actuel du jeu.
    def get_move(self, board):
        if self.numAlgo == 1:
            return self.get_move_minimax(board)
        elif self.numAlgo == 2:
            return self.get_move_alphabeta(board)
        elif self.numAlgo == 3:
            return self.get_move_negamax(board)
        elif self.numAlgo == 4:
            return self.get_move_negamax_alphabeta(board)
        else:
            raise ValueError("numAlgo doit être 1, 2, 3 ou 4")

    
    
    # Implémente l'algorithme MiniMax pour choisir le meilleur coup. 
    def get_move_minimax(self, board):
        best_move = None
        best_score = float('-inf') if self.color == board._BLACK else float('inf')
        for move in board.legal_moves():
            board.push(move)
            score = self.minimax(board, self.depth -1, board._BLACK != self.color)
            print(f"Coup: {move}, Score: {score}")
            board.pop()

            if (self.color == board._BLACK and score > best_score) or \
                (self.color == board._WHITE and score < best_score):
                best_score = score
                best_move = move

        return best_move if best_move is not None else [self.color, -1, -1]

    # Algorithme récursif MiniMax qui calcule la meilleure évaluation pour un état de jeu 
    # donné en explorant récursivement les coups possibles jusqu'à une profondeur spécifiée.
    def minimax(self, board, depth, maximizingPlayer):
        if depth == 0 or board.is_game_over():
            return board.heuristiqueV2(self.color)

        if maximizingPlayer:
            maxEval = float('-inf')
            for move in board.legal_moves():
                board.push(move)
                eval = self.minimax(board, depth - 1, False)
                board.pop()
                maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = float('inf')
            for move in board.legal_moves():
                board.push(move)
                eval = self.minimax(board, depth - 1, True)
                board.pop()
                minEval = min(minEval, eval)
            return minEval

    
    
    # Implémente l'algorithme MiniMax avec élagage alpha-bêta. 
    def get_move_alphabeta(self, board):
        best_move = None
        best_score = float('-inf')
        alpha = float('-inf')
        beta = float('inf')

        for move in board.legal_moves():
            if move[0] == self.color:
                board.push(move)
                score = self.alphaBetaMin(board, alpha, beta, 1, self.depth)  
                print(f"Coup: {move}, Score: {score}")
                board.pop()
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, score)

        return best_move if best_move is not None else [self.color, -1, -1]
    

    # Ces méthodes sont les composantes de l'algorithme alpha-bêta, 
    # où alphaBetaMax maximise le score et alphaBetaMin minimise le score. 
    def alphaBetaMax(self, board, alpha, beta, l, lmax):
        if board.is_game_over() or (l == lmax):
            return board.heuristiqueV2(self.color)

        possible_moves = board.legal_moves()
        for m in possible_moves:
            board.push(m)
            alpha = max(alpha, self.alphaBetaMin(board, alpha, beta, l + 1, lmax))
            board.pop()
            if (alpha >= beta):
                return beta
        return alpha

    def alphaBetaMin(self, board, alpha, beta, l, lmax):

        if board.is_game_over() or (l == lmax):
            return board.heuristiqueV2(self.color)

        possible_moves = board.legal_moves()
        for m in possible_moves:
            board.push(m)
            beta = min(beta, self.alphaBetaMax(board, alpha, beta, l + 1, lmax))
            board.pop()
            if (alpha >= beta):
                return alpha
        return beta
    

    # Implémente l'algorithme NegaMax, une variante simplifiée de MiniMax. 
    def get_move_negamax(self, board):
        best_score = float('-inf')
        best_move = None
        for move in board.legal_moves():
            board.push(move)
            score = self.negamax(board, self.depth -1, 1 if self.color == board._BLACK else -1)
            board.pop()
            print(move, ' : ',score)
            print('best score:', best_score)
            if (score > best_score):
                best_score = score
                best_move = move
        return best_move if best_move is not None else [self.color, -1, -1]


    # Algorithme NegaMax récursif qui évalue le meilleur coup en alternant les perspectives des joueurs à chaque niveau de l'arbre de recherche.
    def negamax(self, board, depth, color):
        if depth == 0 or board.is_game_over():
            return board.heuristiqueV2(self.color)

        maxEval = float('-inf')
        for move in board.legal_moves():
            if (move[0] == 1 and self.color == board._BLACK) or (move[0] == 2 and board._WHITE):
                board.push(move)
                eval = -self.negamax(board, depth - 1, -color)
                board.pop()
                maxEval = max(maxEval, eval)
        return maxEval  



    # Combine l'algorithme NegaMax avec l'élagage alpha-bêta pour choisir le meilleur coup. 
    # Cette méthode optimise la recherche de NegaMax en élaguant les branches peu prometteuses de l'arbre du jeu.
    def get_move_negamax_alphabeta(self, board):
        best_score = float('-inf')
        best_move = None
        for move in board.legal_moves():
            board.push(move)
            score = self.negamax_alphabeta(board, self.depth - 1, float('-inf'), float('inf'), 1 if self.color == board._BLACK else -1)
            board.pop()
            print(move, ' : ',score)
            print('best score:', best_score)
            if (score > best_score):
                best_score = score
                best_move = move
        return best_move if best_move is not None else [self.color, -1, -1]

    
    # Implémente la logique de l'algorithme NegaMax avec élagage alpha-bêta. 
    # Cette méthode est la version améliorée de NegaMax, qui utilise les paramètres alpha et bêta pour élaguer l'arbre de recherche plus efficacement.
    def negamax_alphabeta(self, board, depth, alpha, beta, color):
        if depth == 0 or board.is_game_over():
            return board.heuristiqueV2(self.color)

        maxEval = float('-inf')
        for move in board.legal_moves():
            if (move[0] == 1 and self.color == board._BLACK) or (move[0] == 2 and board._WHITE):
                board.push(move)
                eval = -self.negamax_alphabeta(board, depth - 1, -beta, -alpha, -color)
                board.pop()
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break
        return maxEval