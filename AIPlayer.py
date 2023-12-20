from Player import Player

class AIPlayer(Player):
    def __init__(self, color, depth=3):
        super().__init__(color)
        self.depth = depth 

    def get_move(self, board):
        best_move = None
        best_score = float('-inf') if self.color == board._BLACK else float('inf')

        for move in board.legal_moves():
            if move[0] == self.color:
                board.push(move)
                score = self.minimax(board, self.depth, board._BLACK == self.color)
                board.pop()

                if self.color == board._BLACK and score > best_score or \
                self.color == board._WHITE and score < best_score:
                    best_score = score
                    best_move = move

        return best_move if best_move is not None else [self.color, -1, -1] 


    def minimax(self, board, depth, maximizingPlayer):
        if depth == 0 or board.is_game_over():
            return board.heuristique(self.color)

        if maximizingPlayer:
            maxEval = float('-inf')
            for move in board.legal_moves():
                if move[0] == board._BLACK:
                    board.push(move)
                    eval = self.minimax(board, depth - 1, False)
                    board.pop()
                    maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = float('inf')
            for move in board.legal_moves():
                if move[0] == board._WHITE:
                    board.push(move)
                    eval = self.minimax(board, depth - 1, True)
                    board.pop()
                    minEval = min(minEval, eval)
            return minEval
    


