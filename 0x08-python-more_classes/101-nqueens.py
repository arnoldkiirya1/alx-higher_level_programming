#!/usr/bin/python3
"""
N Queens puzzle
"""


import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper diagonal on the right side
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row):
    """
    Solve the N Queens problem using backtracking
    """
    if row == N:
        # Print the solution
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1)
            board[row][col] = 0


def print_solution(board):
    """
    Print the board configuration as a list of positions of the queens
    """
    solution = []
    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check the value of N
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty board
    board = [[0 for col in range(N)] for row in range(N)]

    # Solve the N Queens problem
    solve_nqueens(board, 0)
