from Player import Player
import time

class AIPlayer_id(Player):
    
    #-------------------------------------------------------------------------------------------------------- 
    #-----------AVEC ITERATIVE DEEPENING--------------------------------------------------------------------- 
    #--------------------------------------------------------------------------------------------------------

    # Initialisation de l'IA avec des limites de profondeur et de temps.
    # 'color' détermine la couleur du joueur (noir ou blanc).
    # 'depth_limit' est la profondeur maximale de recherche dans l'arbre de jeu.
    # 'time_limit' est le temps maximal en secondes pour effectuer un coup.
    def __init__(self, color, depth_limit, time_limit, numAlgo):
        super().__init__(color)
        self.depth_limit = depth_limit
        self.time_limit = time_limit
        self.numAlgo = numAlgo
        
    # Détermine le meilleur coup à jouer sur le plateau 'board'.
    # Utilise la recherche itérative pour approfondir progressivement l'exploration.
    # S'arrête lorsque la profondeur limite ou la limite de temps est atteinte.
    def get_move(self, board):
        start_time = time.time()
        best_move = None
        depth = 1

        while depth <= self.depth_limit:
            current_time = time.time()
            if current_time - start_time > self.time_limit:
                break  

            current_best_move = self.IAIterativeDeepening(board, depth, start_time)
            if current_best_move:
                best_move = current_best_move

            depth += 1

        return best_move if best_move is not None else [self.color, -1, -1]

    # Effectue une recherche itérative sur le plateau à une profondeur donnée.
    # Évalue chaque coup légal pour trouver le meilleur coup à cette profondeur.
    # Prend en compte la limite de temps pour arrêter la recherche si nécessaire (Concept de l'Iterative Deepening).
    def IAIterativeDeepening(self, board, depth, start_time):
        best_score = float('-inf')
        best_move = None
        print('================')
        print('  profondeur',depth)
        print('================')
        for move in board.legal_moves():
            print('---->',move)
            if time.time() - start_time > self.time_limit:
                print('FIN DU TEMPS')
                break 
            
            board.push(move)
            print(f"Num Algo: {self.numAlgo}")
            if self.numAlgo == 1:
                score = self.minimax_id(board, depth - 1, False, start_time)
            elif self.numAlgo == 2:
                score = self.alphaBetaMin_id(board, float('-inf'), float('inf'), 1, depth, start_time)
            elif self.numAlgo == 3:
                score = self.negamax_id(board, depth - 1, 1 if self.color == board._BLACK else -1, start_time)
            elif self.numAlgo == 4:
                score = self.negamax_alphabeta_id(board, depth - 1, float('-inf'), float('inf'), 1 if self.color == board._BLACK else -1, start_time)
            else:
                raise ValueError("numAlgo doit être 1, 2, 3 ou 4")

            board.pop()
            print(move, ' : ',score)
            print('best score:', best_score)
            if (score > best_score):
                best_score = score
                best_move = move
            
            print('new best score:', best_score)
        print('best move :', best_move)

        return best_move

    # Implémente l'algorithme NegaMax avec élagage Alpha-Beta dans un contexte avec limite de temps (Iterative Deepening).
    # 'depth' est la profondeur actuelle de recherche.
    # 'alpha' et 'beta' sont les bornes de l'élagage Alpha-Beta.    
    # 'color' est utilisé pour multiplier la valeur heuristiqueV2 et alterne entre chaque niveau de profondeur.
    def negamax_alphabeta_id(self, board, depth, alpha, beta, color, start_time):
        if depth == 0 or board.is_game_over() or time.time() - start_time > self.time_limit:
            return color * board.heuristiqueV2(self.color)

        maxEval = float('-inf')
        for move in board.legal_moves():
            if time.time() - start_time > self.time_limit:
                break

            if (move[0] == 1 and self.color == board._BLACK) or (move[0] == 2 and board._WHITE):
                board.push(move)
                eval = -self.negamax_alphabeta_id(board, depth - 1, -beta, -alpha, -color, start_time)
                board.pop()
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break
        return maxEval

    
    # Implémente l'algorithme NegaMax pour l'IA dans un contexte avec limite de temps (Iterative Deepening).
    def negamax_id(self, board, depth, color, start_time):
        if depth == 0 or board.is_game_over() or time.time() - start_time > self.time_limit:
            return board.heuristiqueV2(self.color)

        maxEval = float('-inf')
        for move in board.legal_moves():
            if time.time() - start_time > self.time_limit:
                break

            if (move[0] == 1 and self.color == board._BLACK) or (move[0] == 2 and board._WHITE):
                board.push(move)
                eval = -self.negamax_id(board, depth - 1, -color, start_time)
                board.pop()
                maxEval = max(maxEval, eval)
        return maxEval
    # Partie maximisante de l'algorithme d'élagage Alpha-Beta.
    # 'l' est le niveau actuel de profondeur et 'lmax' la profondeur maximale.
    # Utilisé pour maximiser le score du joueur actuel.
    def alphaBetaMax_id(self, board, alpha, beta, l, lmax, start_time):
        if board.is_game_over() or (l == lmax) or time.time() - start_time > self.time_limit:
            return board.heuristiqueV2(self.color)

        possible_moves = board.legal_moves()
        for m in possible_moves:
            board.push(m)
            alpha = max(alpha, self.alphaBetaMin_id(board, alpha, beta, l + 1, lmax, start_time))
            board.pop()
            if (alpha >= beta):
                return beta
        return alpha

    # Partie minimisante de l'algorithme d'élagage Alpha-Beta.
    # Utilisé pour minimiser le score de l'adversaire.
    def alphaBetaMin_id(self, board, alpha, beta, l, lmax, start_time):

        if board.is_game_over() or (l == lmax) or time.time() - start_time > self.time_limit:
            return board.heuristiqueV2(self.color)

        possible_moves = board.legal_moves()
        for m in possible_moves:
            board.push(m)
            beta = min(beta, self.alphaBetaMax_id(board, alpha, beta, l + 1, lmax, start_time))
            board.pop()
            if (alpha >= beta):
                return alpha
        return beta

    # Implémente l'algorithme Minimax pour l'IA dans un contexte avec limite de temps (Iterative Deepening).
    # 'maximizingPlayer' indique si l'on est dans une phase de maximisation ou de minimisation.
    def minimax_id(self, board, depth, maximizingPlayer, start_time):
        if depth == 0 or board.is_game_over() or time.time() - start_time > self.time_limit:
            return board.heuristiqueV2(self.color)
        
        if maximizingPlayer:
            maxEval = float('-inf')
            for move in board.legal_moves():
                if time.time() - start_time > self.time_limit:
                    break 

                board.push(move)
                eval = self.minimax_id(board, depth - 1, False, start_time)
                board.pop()
                maxEval = max(maxEval, eval)

            return maxEval

        else:
            minEval = float('inf')
            for move in board.legal_moves():
                if time.time() - start_time > self.time_limit:
                    break  

                board.push(move)
                eval = self.minimax_id(board, depth - 1, True, start_time)
                board.pop()
                minEval = min(minEval, eval)

            return minEval