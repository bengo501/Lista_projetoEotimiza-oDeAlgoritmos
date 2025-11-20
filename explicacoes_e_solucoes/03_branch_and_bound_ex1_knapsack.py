import heapq

class Item:
    def __init__(self, weight, value, index):
        self.weight = weight
        self.value = value
        self.index = index
        self.ratio = value / weight

    def __lt__(self, other):
        return self.ratio > other.ratio # Sort descending by ratio

class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    def __lt__(self, other):
        return self.bound > other.bound # Max-heap based on bound

def calculate_bound(u, n, W, items):
    if u.weight >= W:
        return 0

    profit_bound = u.profit
    j = u.level + 1
    tot_weight = u.weight

    while j < n and tot_weight + items[j].weight <= W:
        tot_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    if j < n:
        profit_bound += (W - tot_weight) * items[j].ratio

    return profit_bound

def solve_knapsack(W, weights, values):
    n = len(values)
    items = []
    for i in range(n):
        items.append(Item(weights[i], values[i], i))
    
    # Sort items by value/weight ratio
    items.sort()

    # Priority queue for Best-First Search
    pq = []
    
    # Dummy root
    u = Node(-1, 0, 0, 0.0)
    u.bound = calculate_bound(u, n, W, items)
    heapq.heappush(pq, u)

    max_profit = 0
    best_items = [] # To track which items are selected (simplified tracking)
    
    # Note: Tracking the exact items in B&B is a bit more complex, usually done by storing path
    # For simplicity here, we just find the max profit. 
    # To reconstruct the solution, we would need to store parent pointers or the selection state in the node.
    
    while pq:
        u = heapq.heappop(pq)

        if u.bound > max_profit:
            # Branching: Consider next item
            
            # Case 1: Include items[u.level + 1]
            v = Node(u.level + 1, u.profit + items[u.level + 1].value, u.weight + items[u.level + 1].weight, 0.0)
            
            if v.weight <= W and v.profit > max_profit:
                max_profit = v.profit
            
            v.bound = calculate_bound(v, n, W, items)
            if v.bound > max_profit:
                heapq.heappush(pq, v)

            # Case 2: Exclude items[u.level + 1]
            v = Node(u.level + 1, u.profit, u.weight, 0.0)
            v.bound = calculate_bound(v, n, W, items)
            if v.bound > max_profit:
                heapq.heappush(pq, v)

    return max_profit

if __name__ == "__main__":
    W = 10
    values = [40, 42, 25, 12]
    weights = [4, 7, 5, 3]
    
    print(f"Capacidade da Mochila: {W}")
    print(f"Valores: {values}")
    print(f"Pesos: {weights}")
    
    max_val = solve_knapsack(W, weights, values)
    print(f"Valor Máximo Possível: {max_val}")
