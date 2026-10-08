# Tic-Tac-Toe AI using Minimax
# Human = X, Computer = O

board = [" " for _ in range(9)]

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def winner(player):
    winning_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False

def moves_left():
    return " " in board

def minimax(is_maximizing):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if not moves_left():
        return 0

    if is_maximizing:
        best_score = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)
        return best_score

    else:
        best_score = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)
        return best_score

def computer_move():
    best_score = -100
    best_position = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_position = i

    board[best_position] = "O"

print("TIC-TAC-TOE AI")
print("You are X. Computer is O.")
print("Choose a position from 1 to 9.")

while True:
    show_board()

    try:
        position = int(input("Enter your position (1-9): ")) - 1

        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid position. Try again.")
            continue

        board[position] = "X"

    except ValueError:
        print("Please enter a number.")
        continue

    if winner("X"):
        show_board()
        print("You win!")
        break

    if not moves_left():
        show_board()
        print("It's a draw!")
        break

    computer_move()

    if winner("O"):
        show_board()
        print("Computer wins!")
        break

    if not moves_left():
        show_board()
        print("It's a draw!")
        break
          
