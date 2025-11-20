def solve_n_queens(n):
    board = [-1] * n  # board[row] = col means queen at (row, col)
    solutions = []

    def is_safe(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            # Check column conflict
            if prev_col == col:
                return False
            # Check diagonal conflict
            if abs(prev_row - row) == abs(prev_col - col):
                return False
        return True

    def backtrack(row):
        if row == n:
            # Found a solution, make a copy
            solutions.append(list(board))
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1 # Backtrack (not strictly necessary since we overwrite, but good for logic)

    backtrack(0)
    return solutions

def print_board(solution):
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("-" * (n * 2))

if __name__ == "__main__":
    N = 8 # Standard chessboard
    print(f"Resolvendo {N}-Rainhas...")
    solutions = solve_n_queens(N)
    print(f"Encontradas {len(solutions)} soluções.")
    
    if solutions:
        print("Primeira solução:")
        print_board(solutions[0])
