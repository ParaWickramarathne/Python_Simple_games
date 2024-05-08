def print_board(board):

    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for _ in range(9):
        row = int(input(f"Player {players[current_player]}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {players[current_player]}, enter column (0, 1, or 2): "))
        
        if board[row][col] == " ":
            board[row][col] = players[current_player]
            print_board(board)
            
            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break
                
            current_player = 1 - current_player
        else:
            print("That position is already taken. Try again.")

    else:
        print("It's a tie!")

# Start the game
tic_tac_toe()
