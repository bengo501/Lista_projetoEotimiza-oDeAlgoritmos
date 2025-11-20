# Branch and Bound - Explicação Detalhada

Branch and Bound (Ramificar e Limitar) é uma técnica poderosa para resolver problemas de **Otimização Combinatória** (como Caixeiro Viajante, Mochila, Alocação de Tarefas).

Ao contrário do Backtracking simples, que explora cegamente até encontrar uma falha, o Branch and Bound usa **inteligência** (limites matemáticos) para prever se um caminho *pode* levar a uma solução melhor do que a que já temos. Se a previsão for ruim, cortamos o mal pela raiz (poda).

---

## O Problema da Mochila 0/1 (Knapsack Problem)

**O Problema:**
Você é um ladrão com uma mochila que aguenta no máximo $W$ kg.
Existem $N$ itens na loja. Cada item tem um **peso** ($w_i$) e um **valor** ($v_i$).
Você deve escolher quais itens levar para maximizar o valor total, sem rasgar a mochila (peso total $\le W$).
A regra "0/1" significa que você não pode quebrar os itens: ou leva o item inteiro (1), ou deixa (0).

### Teoria e Estratégias

Para usar Branch and Bound, precisamos de duas coisas fundamentais:

1.  **Ramificação (Branching):** Como dividimos o problema?
    -   A cada passo (nível da árvore), tomamos a decisão sobre **um item**.
    -   Ramo Esquerdo: **Incluir** o item.
    -   Ramo Direito: **Excluir** o item.

2.  **Limitação (Bounding):** Como sabemos se um ramo é promissor?
    -   Precisamos de uma estimativa otimista (Upper Bound).
    -   Imagine que chegamos num nó onde já temos \$40 de valor e sobram 2kg na mochila.
    -   Se o melhor item restante tem densidade \$10/kg, no *melhor cenário mágico* (onde podemos derreter o item), conseguiríamos mais $2 \text{kg} \times \$10 = \$20$.
    -   Total estimado = \$40 + \$20 = \$60.
    -   Se já encontramos uma solução completa em outro lugar que vale \$70, então **não adianta** seguir por este caminho, pois o máximo que ele daria é \$60. **Podamos a árvore!**

### A Matemática do Limite (Relaxação Linear)

Para calcular o limite superior (Upper Bound) de um nó, usamos a versão "fracionária" do problema da mochila (que é fácil de resolver com algoritmo guloso).

**Fórmula do Bound:**
$$ Bound = \text{ValorAtual} + \sum (\text{Itens Inteiros que Cabem}) + (\text{Fração do Próximo Item}) $$

1.  Ordenamos todos os itens por **Densidade** ($\frac{\text{valor}}{\text{peso}}$) decrescente.
2.  Enchemos a capacidade restante com os itens mais densos.
3.  Se um item não couber inteiro, pegamos a fração dele que cabe.

**Exemplo:**
Mochila Cap=10.
Item A: Peso 4, Valor 40 (Densidade 10)
Item B: Peso 7, Valor 42 (Densidade 6)
Item C: Peso 5, Valor 25 (Densidade 5)

Estamos num nó onde já pegamos o Item A.
- Peso Atual: 4. Valor Atual: 40.
- Capacidade Restante: $10 - 4 = 6$.
- Itens disponíveis: B e C.
- O Item B pesa 7. Só temos 6 de espaço.
- Pegamos $\frac{6}{7}$ do Item B.
- Valor extra estimado: $\frac{6}{7} \times 42 = 6 \times 6 = 36$.
- **Bound (Limite Superior):** $40 + 36 = 76$.

Isso significa: "Neste ramo, é *matematicamente impossível* conseguir mais que 76".

### Passo a Passo da Resolução

Vamos usar o exemplo acima: Cap=10. Itens: A(4, 40), B(7, 42), C(5, 25), D(3, 12).
Ordenados por densidade: A(10), B(6), C(5), D(4).

1.  **Raiz (Nível -1):**
    -   Valor=0, Peso=0.
    -   Calculamos Bound: Pegamos A(4kg), sobram 6. Pegamos $\frac{6}{7}$ de B. Valor = $40 + 36 = 76$.
    -   `Pilha: [Raiz(Bound=76)]`
    -   `MelhorSolucao = 0`

2.  **Explorar Raiz:**
    -   Filho 1 (Com A): Peso 4, Valor 40. Bound = 76. -> Adiciona na pilha.
    -   Filho 2 (Sem A): Peso 0, Valor 0. Bound? (Pegamos B inteiro, sobram 3. Pegamos $\frac{3}{5}$ de C. $42 + 0.6 \times 25 = 42 + 15 = 57$). -> Adiciona na pilha.
    -   `Pilha: [SemA(57), ComA(76)]` (Ordenada pelo Bound para explorar o melhor primeiro - Best First Search).

3.  **Explorar ComA (Bound 76):**
    -   Decisão sobre B.
    -   Filho 1 (Com A, Com B): Peso $4+7=11$. **Estoura capacidade!** (Poda por inviabilidade).
    -   Filho 2 (Com A, Sem B): Peso 4, Valor 40. Capacidade restante 6. Próximo é C.
        -   Bound: Pegamos C(5kg), sobra 1. Pegamos $\frac{1}{3}$ de D.
        -   Valor = $40 + 25 + (\frac{1}{3} \times 12) = 65 + 4 = 69$.
    -   `Pilha: [SemA(57), ComA_SemB(69)]`

4.  **Explorar ComA_SemB (Bound 69):**
    -   Decisão sobre C.
    -   Filho 1 (Com A, Sem B, Com C): Peso $4+5=9$. Valor $40+25=65$.
        -   É uma folha válida (ou quase, falta decidir D).
        -   Bound: Sobra 1kg. Pegamos $\frac{1}{3}$ de D. Valor $65+4=69$.
        -   `MelhorSolucao = 65` (Pois chegamos num nó viável com valor 65).
    -   Filho 2 (Com A, Sem B, Sem C): ... Bound menor.

5.  **Poda:**
    -   Se em algum momento tirarmos da pilha um nó com `Bound <= MelhorSolucao` (ex: 65), nós o descartamos imediatamente. Não há esperança de superar o que já temos.

### O Código Explicado

```python
class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level      # Qual item estamos decidindo (índice)
        self.profit = profit    # Valor acumulado até agora
        self.weight = weight    # Peso acumulado até agora
        self.bound = bound      # O potencial máximo deste ramo

    # Para a fila de prioridade (Heap) funcionar, precisamos comparar nós.
    # Queremos explorar primeiro quem tem MAIOR bound (Best-First).
    def __lt__(self, other):
        return self.bound > other.bound

def calculate_bound(u, n, W, items):
    if u.weight >= W: return 0 # Se já estourou, bound é 0

    profit_bound = u.profit
    j = u.level + 1
    tot_weight = u.weight

    # Algoritmo Guloso para estimar o resto
    while j < n and tot_weight + items[j].weight <= W:
        tot_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # Se ainda sobrou espaço e tem item, pega fração
    if j < n:
        profit_bound += (W - tot_weight) * items[j].ratio

    return profit_bound

def solve_knapsack(W, weights, values):
    # ... inicialização e ordenação dos itens por densidade ...

    # Fila de prioridade guarda os nós "vivos" da árvore
    pq = []
    
    # Cria a raiz (nenhum item decidido ainda)
    u = Node(-1, 0, 0, 0.0)
    u.bound = calculate_bound(u, n, W, items)
    heapq.heappush(pq, u)

    max_profit = 0

    while pq:
        u = heapq.heappop(pq) # Pega o nó com maior potencial

        # PODA: Se o potencial deste nó é pior que o que eu já garanti, joga fora.
        if u.bound > max_profit:
            
            # Ramo 1: INCLUIR o próximo item
            v = Node(u.level + 1, u.profit + items[u.level + 1].value, 
                     u.weight + items[u.level + 1].weight, 0.0)
            
            # Se couber na mochila e já for melhor que o recorde atual, atualiza recorde
            if v.weight <= W and v.profit > max_profit:
                max_profit = v.profit
            
            # Calcula o potencial deste novo ramo
            v.bound = calculate_bound(v, n, W, items)
            
            # Só adiciona na fila se o potencial prometer superar o recorde
            if v.bound > max_profit:
                heapq.heappush(pq, v)

            # Ramo 2: EXCLUIR o próximo item
            v = Node(u.level + 1, u.profit, u.weight, 0.0)
            v.bound = calculate_bound(v, n, W, items)
            
            if v.bound > max_profit:
                heapq.heappush(pq, v)

    return max_profit
```
