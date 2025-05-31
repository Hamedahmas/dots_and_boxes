# main.py
from game import GameState
from ai import minimax

def print_board(state):
    print("Moves made:", len(state.edges), "/", len(state._generate_all_edges()))

def play():
    state = GameState()
    while not state.is_game_over():
        print_board(state)
        if state.current_player == 1:
            _, move = minimax(state, depth=3, alpha=-1e9, beta=1e9, maximizing_player=True)
            print("AI Move:", move)
        else:
            moves = state.get_possible_moves()
            print("Available:", moves)
            move = eval(input("Your move (e.g. ((0,0),(0,1)): "))
        state.make_move(move)

    print("Game Over. Score:", state.score)

if __name__ == "__main__":
    play()
