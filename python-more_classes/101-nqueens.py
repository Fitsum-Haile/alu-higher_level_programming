#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    This function checks the column, and the two diagonals.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    """
    Solve the N-Queens problem and print all solutions.
    """
    def solve(row):
        if row == N:
            # A solution is found, print it
            solution = [[i, board[i]] for i in range(N)]
            print(solution)
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1

    board = [-1] * N
    solve(0)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

if __name__ == "__main__":
    main()

