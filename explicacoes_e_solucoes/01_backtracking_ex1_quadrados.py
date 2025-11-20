import math

def is_perfect_square(n):
    root = int(math.isqrt(n))
    return root * root == n

def solve_square_sum_sequence(n):
    # Adjacency list: graph[i] contains all j such that i+j is a perfect square
    adj = {i: [] for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if is_perfect_square(i + j):
                adj[i].append(j)
                adj[j].append(i)

    # Sort neighbors to try to find a solution faster (heuristic: fewer neighbors first? or just numerical order)
    # Numerical order is fine for standard backtracking.
    
    path = []
    used = [False] * (n + 1)

    def backtrack(current_num):
        path.append(current_num)
        used[current_num] = True

        if len(path) == n:
            return True

        # Try neighbors
        for neighbor in adj[current_num]:
            if not used[neighbor]:
                if backtrack(neighbor):
                    return True

        # Backtrack
        used[current_num] = False
        path.pop()
        return False

    # Try starting from each number 1 to n
    for start_node in range(1, n + 1):
        if backtrack(start_node):
            return path

    return None

if __name__ == "__main__":
    N = 15
    print(f"Procurando sequência para N={N}...")
    result = solve_square_sum_sequence(N)
    if result:
        print("Solução encontrada:")
        print(result)
        
        # Verify solution
        valid = True
        for i in range(len(result) - 1):
            s = result[i] + result[i+1]
            if not is_perfect_square(s):
                print(f"ERRO: {result[i]} + {result[i+1]} = {s} (não é quadrado perfeito)")
                valid = False
        if valid:
            print("Verificação: OK")
    else:
        print("Nenhuma solução encontrada.")
