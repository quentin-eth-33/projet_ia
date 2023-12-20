from Player import Player

class AIPlayer(Player):
    def __init__(self, color, depth=3):
        super().__init__(color)
        self.depth = depth 

    
    def get_move(self, board):
        return self.get_move_alphabeta(board)
        
    
    def get_move_minimax(self, board):
        best_move = None
        best_score = float('-inf') if self.color == board._BLACK else float('inf')

        for move in board.legal_moves():
            if move[0] == self.color:
                board.push(move)
                score = self.minimax(board, self.depth, board._BLACK == self.color)
                print(f"Coup: {move}, Score: {score}")
                board.pop()

                if self.color == board._BLACK and score > best_score or \
                self.color == board._WHITE and score < best_score:
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
                score = self.alphabeta(board, self.depth, alpha, beta, True)
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
                board.pop()
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, score)

        return best_move if best_move is not None else [self.color, -1, -1]

    def minimax(self, board, depth, maximizingPlayer):
        if depth == 0 or board.is_game_over():
            return board.heuristiqueV2(self.color)

        if maximizingPlayer:
            maxEval = float('-inf')
            for move in board.legal_moves():
                if move[0] == self.color: 
                    board.push(move)
                    eval = self.minimax(board, depth - 1, False)  
                    board.pop()
                    maxEval = max(maxEval, eval)
            return maxEval if maxEval != float('-inf') else 0  
        else:
            minEval = float('inf')
            for move in board.legal_moves():
                if move[0] != self.color: 
                    board.push(move)
                    eval = self.minimax(board, depth - 1, True)  
                    board.pop()
                    minEval = min(minEval, eval)
            return minEval if minEval != float('inf') else 0  

    def alphabeta(self, board, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or board.is_game_over():
            return board.heuristiqueV2(self.color)

        if maximizingPlayer:
            maxEval = float('-inf')
            for move in board.legal_moves():
                if move[0] == self.color:
                    board.push(move)
                    eval = self.alphabeta(board, depth - 1, alpha, beta, False)
                    board.pop()
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return maxEval
        else:
            minEval = float('inf')
            for move in board.legal_moves():
                if move[0] != self.color:
                    board.push(move)
                    eval = self.alphabeta(board, depth - 1, alpha, beta, True)
                    board.pop()
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return minEval
    
    def negamax(self, board, depth, color):
        if depth == 0 or board.is_game_over():
            return color * board.heuristiqueV2(self.color)

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
            return color * board.heuristiqueV2(self.color)

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


