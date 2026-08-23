# Minimax Algorithm for Tic-Tac-Toe

board = [' ' for _ in range(9)]


def print_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for position in winning_positions:
        if all(board[i] == player for i in position):
            return True

    return False


def is_moves_left():
    return ' ' in board


def minimax(is_maximizing):
    # AI wins
    if check_winner('O'):
        return 1

    # Human wins
    if check_winner('X'):
        return -1

    # Draw
    if not is_moves_left():
        return 0

    if is_maximizing:
        best_score = -float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'

                score = minimax(False)

                board[i] = ' '
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'

                score = minimax(True)

                board[i] = ' '
                best_score = min(best_score, score)

        return best_score


def best_move():
    best_score = -float('inf')
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'

            score = minimax(False)

            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move


# Main Game
print("TIC-TAC-TOE USING MINIMAX")
print("You are X")
print("Computer is O")

while True:

    print_board()

    # Human move
    try:
        position = int(input("Enter your position (0-8): "))

        if position < 0 or position > 8:
            print("Invalid position!")
            continue

        if board[position] != ' ':
            print("Position already occupied!")
            continue

        board[position] = 'X'

    except ValueError:
        print("Enter a valid number!")
        continue

    if check_winner('X'):
        print_board()
        print("You win!")
        break

    if not is_moves_left():
        print_board()
        print("Game Draw!")
        break

    # Computer move using Minimax
    computer_move = best_move()
    board[computer_move] = 'O'

    print("Computer chose position:", computer_move)

    if check_winner('O'):
        print_board()
        print("Computer wins!")
        break

    if not is_moves_left():
        print_board()
        print("Game Draw!")
        break
