from Player import Player
import time

class AIPlayer(Player):
    
    def __init__(self, color, depth_limit=20, time_limit=10):
        super().__init__(color)
        self.depth_limit = depth_limit
        self.time_limit = time_limit
        
    def get_move(self, board):
        start_time = time.time()
        best_move = None
        depth = 1

        while depth <= self.depth_limit:
            current_time = time.time()
            if current_time - start_time > self.time_limit:
                break  # Arrête la recherche si le temps limite est atteint

            current_best_move = self.iterative_search(board, depth, start_time)
            if current_best_move:
                best_move = current_best_move

            depth += 1

        return best_move if best_move is not None else [self.color, -1, -1]

    def iterative_search(self, board, depth, start_time):
        best_score = float('-inf') if self.color == board._BLACK else float('inf')
        best_move = None

        for move in board.legal_moves():
            if time.time() - start_time > self.time_limit:
                break 

            board.push(move)
            score = self.minimax(board, depth - 1, False, start_time)
            board.pop()

            if (self.color == board._BLACK and score > best_score) or \
               (self.color == board._WHITE and score < best_score):
                best_score = score
                best_move = move

        return best_move

    def minimax(self, board, depth, maximizingPlayer, start_time):
        if depth == 0 or board.is_game_over() or time.time() - start_time > self.time_limit:
            return board.heuristique(self.color)

        if maximizingPlayer:
            maxEval = float('-inf')
            for move in board.legal_moves():
                if time.time() - start_time > self.time_limit:
                    break 

                board.push(move)
                eval = self.minimax(board, depth - 1, False, start_time)
                board.pop()
                maxEval = max(maxEval, eval)

            return maxEval

        else:
            minEval = float('inf')
            for move in board.legal_moves():
                if time.time() - start_time > self.time_limit:
                    break  

                board.push(move)
                eval = self.minimax(board, depth - 1, True, start_time)
                board.pop()
                minEval = min(minEval, eval)

            return minEval
    #-------------------------------------------------------------------------------------------------------- 
    #--------------------------------------------------------------------------------------------------------  
    #--------------------------------------------------------------------------------------------------------
    
    def get_move_minimax(self, board):
        best_move = None
        best_score = float('-inf') if self.color == board._BLACK else float('inf')
        print(f"Score Initial: {board.heuristique(self.color)}")
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
    
    def get_move_alphabeta(self, board):
        best_move = None
        best_score = float('-inf')
        alpha = float('-inf')
        beta = float('inf')

        for move in board.legal_moves():
            if move[0] == self.color:
                board.push(move)
                score = self.alphaBetaMin(board, alpha, beta, 1, self.depth)  # Utiliser alphaBetaMin ici
                print(f"Coup: {move}, Score: {score}")
                board.pop()
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, score)

        return best_move if best_move is not None else [self.color, -1, -1]


    
    def get_move_negamax(self, board):
        best_move = None
        best_score = float('-inf')
        color = 1 if self.color == board._BLACK else -1

        for move in board.legal_moves():
            if move[0] == self.color:
                board.push(move)
                score = -self.negamax(board, self.depth, -color)
                print(f"Coup: {move}, Score: {score}")
                board.pop()
                if score > best_score:
                    best_score = score
                    best_move = move

        return best_move if best_move is not None else [self.color, -1, -1]

    def get_move_negamax_alphabeta(self, board):
        best_move = None
        best_score = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        color = 1 if self.color == board._BLACK else -1

        for move in board.legal_moves():
            if move[0] == self.color:
                board.push(move)
                score = -self.negamax_alphabeta(board, self.depth, -beta, -alpha, -color)
                print(f"Coup: {move}, Score: {score}")
                board.pop()
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, score)

        return best_move if best_move is not None else [self.color, -1, -1]

    

    def alphaBetaMax(self, board, alpha, beta, l, lmax):
        if board.is_game_over() or (l == lmax):
            return board.heuristique(self.color)

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
            return board.heuristique(self.color)

        possible_moves = board.legal_moves()
        for m in possible_moves:
            board.push(m)
            beta = min(beta, self.alphaBetaMax(board, alpha, beta, l + 1, lmax))
            board.pop()
            if (alpha >= beta):
                return alpha
        return beta




    
    def negamax(self, board, depth, color):
        if depth == 0 or board.is_game_over():
            return color * board.heuristique(self.color)

        maxEval = float('-inf')
        for move in board.legal_moves():
            if move[0] == self.color:
                board.push(move)
                eval = -self.negamax(board, depth - 1, -color)
                board.pop()
                maxEval = max(maxEval, eval)
        return maxEval
    
    def negamax_alphabeta(self, board, depth, alpha, beta, color):
        if depth == 0 or board.is_game_over():
            return color * board.heuristique(self.color)

        maxEval = float('-inf')
        for move in board.legal_moves():
            if move[0] == self.color:
                board.push(move)
                eval = -self.negamax_alphabeta(board, depth - 1, -beta, -alpha, -color)
                board.pop()
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break
        return maxEval


