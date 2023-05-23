import queue


def is_safe(board, row, col):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def heuristic(board):
    # Heuristic function to estimate the number of conflicts
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                # Check conflicts in the same row
                conflicts -= 1
                for k in range(n):
                    if k != j and board[i][k] == 1:
                        conflicts += 1

                # Check conflicts in the diagonal
                for k in range(1, n):
                    if i + k < n and j + k < n and board[i + k][j + k] == 1:
                        conflicts += 1
                    if i - k >= 0 and j + k < n and board[i - k][j + k] == 1:
                        conflicts += 1

    return conflicts


def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    pq = queue.PriorityQueue()
    pq.put((0 + heuristic(board), 0, board))

    while not pq.empty():
        _, col, current_board = pq.get()
        if col == n:
            return current_board

        for row in range(n):
            if is_safe(current_board, row, col):
                next_board = [current_board[i].copy() for i in range(n)]
                next_board[row][col] = 1
                pq.put((col + heuristic(next_board), col + 1, next_board))

    return None


def print_board(board):
    for row in board:
        print(' '.join('Q' if cell == 1 else '.' for cell in row))


# Example usage
n = 4
solution = solve_nqueens(n)
if solution is not None:
    print(f"Solution for {n}-Queens:")
    print_board(solution)
else:
    print(f"No solution found for {n}-Queens.")
