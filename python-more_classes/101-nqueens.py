#!/usr/bin/python3
"""
N Queens Puzzle Solver
"""
import sys


def print_usage_and_exit():
    """Prints usage message and exits with status 1"""
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message):
    """Prints error message and exits with status 1"""
    print(message)
    sys.exit(1)


def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at board[row][col]
    This means checking if there's no queen in the same column,
    or the diagonals.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """
    Solves the N Queens problem and returns a list of solutions
    where each solution is represented by a list of column indices
    for each row.
    """
    def solve(row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)

    board = [-1] * N
    solutions = []
    solve(0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error_and_exit("N must be a number")

    if N < 4:
        print_error_and_exit("N must be at least 4")

    solutions = solve_nqueens(N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if __name__ == "__main__":
    main()

