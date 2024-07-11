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
    # ... rest of your code ...


def main():
    # ... rest of your code ...

if __name__ == "__main__":
    main()
