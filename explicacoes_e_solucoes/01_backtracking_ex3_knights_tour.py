import sys

# Increase recursion depth for larger boards
sys.setrecursionlimit(2000)

def solve_knights_tour(n):
    # Board initialized with -1
    board = [[-1 for _ in range(n)] for _ in range(n)]
    
    # Possible moves for a knight (x, y)
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1

    def backtrack(curr_x, curr_y, move_count):
        if move_count == n * n:
            return True

        # Warnsdorff's heuristic: prioritize moves that have fewer onward moves
        # This makes finding a solution much faster for larger boards
        next_moves = []
        for i in range(8):
            next_x = curr_x + move_x[i]
            next_y = curr_y + move_y[i]
            if is_valid(next_x, next_y):
                # Count valid moves from this next move
                count = 0
                for j in range(8):
                    nn_x = next_x + move_x[j]
                    nn_y = next_y + move_y[j]
                    if is_valid(nn_x, nn_y):
                        count += 1
                next_moves.append((count, next_x, next_y))
        
        # Sort by count (ascending)
        next_moves.sort()

        for _, next_x, next_y in next_moves:
            board[next_x][next_y] = move_count
            if backtrack(next_x, next_y, move_count + 1):
                return True
            board[next_x][next_y] = -1 # Backtrack

        return False

    # Start at (0, 0)
    board[0][0] = 0
    if backtrack(0, 0, 1):
        return board
    else:
        return None

def print_board(board):
    n = len(board)
    for row in board:
        print(" ".join(f"{x:2d}" for x in row))

if __name__ == "__main__":
    N = 8 # Standard chessboard
    print(f"Resolvendo Passeio do Cavalo para tabuleiro {N}x{N}...")
    result = solve_knights_tour(N)
    
    if result:
        print("Solução encontrada:")
        print_board(result)
    else:
        print("Nenhuma solução encontrada.")
