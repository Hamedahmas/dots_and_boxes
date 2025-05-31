# ai.py
import math

def minimax(state, depth, alpha, beta, maximizing_player):
    if depth == 0 or state.is_game_over():
        return evaluate(state), None

    best_move = None
    moves = state.get_possible_moves()

    if maximizing_player:
        max_eval = -math.inf
        for move in moves:
            new_state = state.clone()
            new_state.make_move(move)
            eval, _ = minimax(new_state, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in moves:
            new_state = state.clone()
            new_state.make_move(move)
            eval, _ = minimax(new_state, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def evaluate(state):
    return state.score.get(1, 0) - state.score.get(-1, 0)
