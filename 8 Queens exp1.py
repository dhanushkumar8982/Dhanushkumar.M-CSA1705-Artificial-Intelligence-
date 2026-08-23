# Python program to solve the 8-Queens problem using Backtracking

N = 8

def print_solution(board):
    print("Solution:")
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))

def is_safe(board, row, col):
    # Check left side of current row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True

def solve_queens(board, col):
    if col >= N:
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_queens(board, col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False

def main():
    board = [[0 for _ in range(N)] for _ in range(N)]

    if solve_queens(board, 0):
        print_solution(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
