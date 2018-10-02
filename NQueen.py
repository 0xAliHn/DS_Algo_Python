# Ref
# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
# https://www.youtube.com/watch?v=xFv_Hl4B83A


def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQ(board, col):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1

            if solveNQ(board, col + 1):
                return True
            board[i][col] = 0

    return False


N = 4
board = [[0 for _ in range(N)] for _ in range(N)]
if not solveNQ(board, 0):
    print("Solution does not exist")
else:
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
