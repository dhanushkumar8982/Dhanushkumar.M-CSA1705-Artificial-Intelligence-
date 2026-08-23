# Tic-Tac-Toe Game

# Create an empty board
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


def is_draw():
    return ' ' not in board


# Main game
current_player = 'X'

print("TIC-TAC-TOE GAME")
print("Positions are numbered from 0 to 8:")
print("0 | 1 | 2")
print("--+---+--")
print("3 | 4 | 5")
print("--+---+--")
print("6 | 7 | 8")

while True:
    print_board()

    print("Player", current_player, "'s turn")

    try:
        position = int(input("Enter position (0-8): "))

        if position < 0 or position > 8:
            print("Invalid position! Choose between 0 and 8.")
            continue

        if board[position] != ' ':
            print("Position already occupied!")
            continue

        board[position] = current_player

    except ValueError:
        print("Please enter a valid number.")
        continue

    # Check winner
    if check_winner(current_player):
        print_board()
        print("Player", current_player, "wins!")
        break

    # Check draw
    if is_draw():
        print_board()
        print("The game is a draw!")
        break

    # Switch player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'
