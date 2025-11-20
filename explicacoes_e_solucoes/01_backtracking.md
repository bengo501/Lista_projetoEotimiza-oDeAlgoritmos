# Backtracking - Explicação Detalhada

Backtracking é uma técnica de "tentativa e erro" inteligente. Imagine que você está em um labirinto. Você anda até encontrar uma bifurcação. Você escolhe um caminho e segue. Se encontrar um beco sem saída, você **volta** (backtrack) até a bifurcação e tenta o outro caminho.

Computacionalmente, construímos uma solução passo a passo. Se um passo viola as regras do problema, descartamos aquela tentativa e voltamos para tentar outra opção.

---

## 1. Sequência de Soma Quadrada

**O Problema:**
Dado um número $N$ (ex: 15), queremos organizar os números de $1$ a $N$ em uma linha $[x_1, x_2, ..., x_N]$ de tal forma que a soma de qualquer par vizinho $(x_i + x_{i+1})$ seja um quadrado perfeito ($1, 4, 9, 16, 25, 36, ...$).

### Teoria e Matemática
Este problema pode ser modelado como um **Grafo**.
- **Nós:** Os números de $1$ a $N$.
- **Arestas:** Existe uma ligação entre o número $A$ e o número $B$ se $A+B$ for um quadrado perfeito.

O objetivo é encontrar um **Caminho Hamiltoniano** neste grafo: um caminho que visita todos os nós exatamente uma vez.

**Exemplo para N=15:**
Quais são os vizinhos possíveis para o número 8?
- $8 + 1 = 9$ ($3^2$) -> OK
- $8 + 17 = 25$ ($5^2$) -> (17 não está no intervalo 1-15, então não conta)
- ... verificamos todos.

### Passo a Passo da Solução
1.  **Pré-cálculo (Grafo):** Para cada número de 1 a 15, listamos com quem ele pode se conectar.
    *   Ex: O 8 pode conectar com o 1 (soma 9).
    *   Ex: O 1 pode conectar com 3 (soma 4), 8 (soma 9), 15 (soma 16).
2.  **Busca (Backtracking):**
    *   Começamos tentando colocar o número 1.
    *   Lista atual: `[1]`
    *   Quem pode vir depois do 1? Olhamos a lista de vizinhos: 3, 8, 15.
    *   Tentamos o 3. Lista: `[1, 3]` (Soma 4, OK).
    *   Quem vem depois do 3? Vizinhos do 3: 1, 6, 13. O 1 já foi usado. Tentamos o 6. Lista: `[1, 3, 6]` (Soma 9, OK).
    *   ... continuamos assim.
    *   Se chegarmos em um número que não tem vizinhos disponíveis (todos já usados) e a lista não está completa, voltamos e trocamos a escolha anterior.

### O Código Explicado
```python
def solve_square_sum_sequence(n):
    # 1. Construção do Grafo (Lista de Adjacência)
    # adj[i] conterá a lista de números que somados com i dão um quadrado perfeito
    adj = {i: [] for i in range(1, n + 1)}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if is_perfect_square(i + j):
                adj[i].append(j)
                adj[j].append(i) # A relação é bidirecional

    path = []
    used = [False] * (n + 1) # Para saber quem já usamos em O(1)

    # Função recursiva principal
    def backtrack(current_num):
        path.append(current_num) # Adiciona na tentativa atual
        used[current_num] = True

        # Caso base: Se o caminho tem tamanho N, usamos todos! Sucesso.
        if len(path) == n:
            return True

        # Tenta vizinhos válidos
        for neighbor in adj[current_num]:
            if not used[neighbor]:
                if backtrack(neighbor): # Chamada recursiva
                    return True # Se o filho achou solução, retornamos True

        # Backtracking: Se nenhum vizinho funcionou, desfazemos a escolha
        used[current_num] = False
        path.pop()
        return False

    # Tenta começar o caminho com qualquer número de 1 a N
    for start_node in range(1, n + 1):
        if backtrack(start_node):
            return path # Retorna o primeiro caminho encontrado
```

---

## 2. N-Rainhas (N-Queens)

**O Problema:**
Colocar $N$ rainhas em um tabuleiro $N \times N$ sem que elas se ataquem. No xadrez, a rainha ataca na horizontal, vertical e diagonal.

### Teoria e Matemática
Como temos $N$ rainhas e $N$ linhas, sabemos que **cada linha deve ter exatamente uma rainha**. O mesmo vale para as colunas.
O desafio são as diagonais.

**Matemática das Diagonais:**
Numa matriz (linha $r$, coluna $c$):
- **Diagonal Principal (descendo p/ direita):** A diferença $r - c$ é constante.
- **Diagonal Secundária (subindo p/ direita):** A soma $r + c$ é constante.
- **Verificação simplificada:** Duas rainhas em $(r_1, c_1)$ e $(r_2, c_2)$ se atacam diagonalmente se $|r_1 - r_2| == |c_1 - c_2|$. Ou seja, a distância horizontal é igual à distância vertical.

### Passo a Passo da Solução
1.  Começamos na linha 0.
2.  Tentamos colocar a rainha na coluna 0. Verificamos conflitos. Não há (é a primeira).
3.  Vamos para a linha 1.
4.  Tentamos coluna 0: Conflito vertical com a rainha da linha 0.
5.  Tentamos coluna 1: Conflito diagonal ($|1-0| == |1-0|$).
6.  Tentamos coluna 2: Seguro. Colocamos.
7.  Vamos para a linha 2... e assim por diante.
8.  Se na linha $K$ não conseguirmos colocar em nenhuma coluna, voltamos para a linha $K-1$ e movemos a rainha de lá para a próxima posição possível.

### O Código Explicado
```python
def solve_n_queens(n):
    board = [-1] * n  # board[i] guarda em qual COLUNA está a rainha da LINHA i
    solutions = []

    def is_safe(row, col):
        # Verifica conflitos com as rainhas das linhas anteriores
        for prev_row in range(row):
            prev_col = board[prev_row]
            
            # Mesma coluna?
            if prev_col == col:
                return False
            
            # Mesma diagonal?
            # A diferença de linhas é igual à diferença de colunas?
            if abs(prev_row - row) == abs(prev_col - col):
                return False
        return True

    def backtrack(row):
        # Se chegamos na linha N, significa que colocamos rainhas nas linhas 0 a N-1 com sucesso
        if row == n:
            solutions.append(list(board))
            return

        # Tenta todas as colunas para a linha atual 'row'
        for col in range(n):
            if is_safe(row, col):
                board[row] = col # Coloca a rainha
                backtrack(row + 1) # Tenta resolver para a próxima linha
                board[row] = -1 # Backtrack: remove a rainha para tentar a próxima coluna
```

---

## 3. Passeio do Cavalo (Knight's Tour)

**O Problema:**
Um cavalo de xadrez deve visitar todas as casas de um tabuleiro $N \times N$ exatamente uma vez.

### Teoria e Matemática
O movimento do cavalo é em "L": 2 casas em uma direção e 1 na perpendicular.
Matematicamente, se está em $(x, y)$, pode ir para $(x \pm 2, y \pm 1)$ ou $(x \pm 1, y \pm 2)$.
Isso nos dá até 8 movimentos possíveis.

Este também é um problema de encontrar um **Caminho Hamiltoniano** no grafo onde os nós são as casas do tabuleiro e as arestas são os movimentos válidos do cavalo.

**Heurística de Warnsdorff:**
Para tabuleiros grandes, o backtracking puro é muito lento (exponencial). Usamos uma regra inteligente para escolher o próximo movimento:
*   "Sempre mova para a casa que tenha o **menor número de movimentos possíveis a partir dela**."
*   Isso evita entrar em becos sem saída cedo demais, deixando as casas "fáceis" (com muitas saídas) para depois e visitando as casas "difíceis" (cantos, bordas) logo.

### Passo a Passo da Solução
1.  Começamos em $(0,0)$. Marcamos como passo 0.
2.  Geramos os 8 movimentos possíveis.
3.  Filtramos os que caem fora do tabuleiro ou em casas já visitadas.
4.  Ordenamos esses movimentos pela regra de Warnsdorff (prioridade para quem tem menos saídas).
5.  Escolhemos o melhor movimento, marcamos como passo 1 e recursamos.
6.  Se completarmos $N \times N$ passos, sucesso.

### O Código Explicado
```python
def solve_knights_tour(n):
    # Tabuleiro inicializado com -1 (não visitado)
    board = [[-1 for _ in range(n)] for _ in range(n)]
    
    # Vetores de movimento do cavalo (8 possibilidades)
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    def backtrack(curr_x, curr_y, move_count):
        # Se já fizemos N*N movimentos, visitamos tudo!
        if move_count == n * n:
            return True

        # Gera lista de próximos movimentos candidatos
        next_moves = []
        for i in range(8):
            next_x = curr_x + move_x[i]
            next_y = curr_y + move_y[i]
            if is_valid(next_x, next_y):
                # Heurística: Conta quantas saídas a casa (next_x, next_y) tem
                count = count_valid_moves(next_x, next_y)
                next_moves.append((count, next_x, next_y))
        
        # Ordena: tenta primeiro as casas com MENOS saídas (Warnsdorff)
        next_moves.sort()

        for _, next_x, next_y in next_moves:
            board[next_x][next_y] = move_count # Marca visita
            if backtrack(next_x, next_y, move_count + 1):
                return True
            board[next_x][next_y] = -1 # Backtrack: desmarca

        return False
```
