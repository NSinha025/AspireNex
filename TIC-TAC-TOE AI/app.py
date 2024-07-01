import numpy as np

# Create the game board
def create_board():
    return np.zeros((3, 3), dtype=int)

# Print the game board
def print_board(board):
    for row in board:
        print(" ".join(['X' if x == 1 else 'O' if x == -1 else '.' for x in row]))
    print()

# Check if a player has won
def check_win(board, player):
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True
    if board[0, 0] == board[1, 1] == board[2, 2] == player or board[0, 2] == board[1, 1] == board[2, 0] == player:
        return True
    return False

# Check if the game is a draw
def check_draw(board):
    return not np.any(board == 0)

# Get all valid moves
def valid_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]

# Minimax algorithm with Alpha-Beta Pruning
def minimax_ab(board, depth, alpha, beta, is_maximizing):
    if check_win(board, 1):
        return 10 - depth
    if check_win(board, -1):
        return depth - 10
    if check_draw(board):
        return 0
    
    if is_maximizing:
        best_score = -np.inf
        for move in valid_moves(board):
            board[move] = 1
            score = minimax_ab(board, depth + 1, alpha, beta, False)
            board[move] = 0
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = np.inf
        for move in valid_moves(board):
            board[move] = -1
            score = minimax_ab(board, depth + 1, alpha, beta, True)
            board[move] = 0
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

# Determine the best move for the AI
def best_move_ab(board):
    best_score = -np.inf
    move = None
    for m in valid_moves(board):
        board[m] = 1
        score = minimax_ab(board, 0, -np.inf, np.inf, False)
        board[m] = 0
        if score > best_score:
            best_score = score
            move = m
    return move

# Human vs AI game loop
def play_game():
    board = create_board()
    while True:
        print_board(board)
        # Human move
        move = tuple(map(int, input("Enter your move (row col): ").split()))
        if board[move] != 0:
            print("Invalid move! Try again.")
            continue
        board[move] = -1
        if check_win(board, -1):
            print_board(board)
            print("You win!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI move
        move = best_move_ab(board)
        board[move] = 1
        if check_win(board, 1):
            print_board(board)
            print("AI wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
play_game()
