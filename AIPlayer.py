from Player import Player

class AIPlayer(Player):
    def __init__(self, color, depth=8):
        super().__init__(color)
        self.depth = depth 

    
    def get_move(self, board):
        return self.get_move_alphabeta(board)
        
    
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

    def minimax(self, board, depth, maximizingPlayer):
        if depth == 0 or board.is_game_over():
            return board.heuristique(self.color)

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

    #-------------------------------------------------------------------------------------------------------- 
    #--------------------------------------------------------------------------------------------------------  
    #--------------------------------------------------------------------------------------------------------
    
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


