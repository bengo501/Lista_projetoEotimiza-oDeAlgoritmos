# Explicação dos Transcritos: Branch and Bound

Este documento resume e explica os conceitos teóricos e exemplos detalhados nos transcritos fornecidos (Prof. Rafael Scopel) sobre a técnica **Branch and Bound** (Ramificar e Limitar).

## 1. Conceitos Fundamentais

O Branch and Bound é uma melhoria do **Backtracking** focada em **Problemas de Otimização** (Minimizar custos ou Maximizar valores).

### A Diferença Chave
*   **Backtracking:** Corta um ramo apenas quando ele viola uma restrição (ex: duas rainhas se atacando).
*   **Branch and Bound:** Corta um ramo quando podemos **provar matematicamente** que ele não pode conter uma solução melhor do que uma que já encontramos.

### Os Dois Pilares
Para funcionar, precisamos de duas coisas em cada nó da árvore:
1.  **Limite (Bound):** Uma estimativa otimista.
    *   Se queremos **minimizar** custo, o Bound é um **Limite Inferior** (Lower Bound) - "O custo daqui pra frente será *pelo menos* X".
    *   Se queremos **maximizar** valor, o Bound é um **Limite Superior** (Upper Bound) - "O valor daqui pra frente será *no máximo* Y".
2.  **Melhor Solução Atual:** O valor da melhor solução completa que já encontramos até agora.

**Regra de Poda:** Se o *Bound* de um nó é pior que a *Melhor Solução Atual*, cortamos o nó.

---

## 2. Exemplos Práticos do Texto

### A. Problema de Alocação de Tarefas (Assignment Problem)
*   **Objetivo:** Atribuir $N$ pessoas a $N$ tarefas com custo mínimo.
*   **Cálculo do Bound (Inferior):** Soma dos menores elementos de cada linha da matriz.
    *   *Lógica:* Mesmo que escolhêssemos o melhor para cada pessoa (ignorando conflitos de coluna), o custo seria X. Se esse custo idealizado já é ruim, o real será pior.
*   **Estratégia:** O texto usa **Best-First Search** (Melhor-Primeiro), sempre expandindo o nó com o menor limite inferior.

### B. Problema da Mochila (Knapsack Problem)
*   **Objetivo:** Maximizar valor sem estourar peso.
*   **Cálculo do Bound (Superior):** Relaxação Linear.
    *   Enchemos a mochila com os itens mais valiosos (por kg). Se sobrar espaço, pegamos uma **fração** do próximo item. Isso dá um valor que é impossível de superar apenas com itens inteiros.
*   **Árvore:** Binária (Esquerda = Incluir item, Direita = Excluir item).

---

## 3. Formalização e Estratégias de Busca

O texto formaliza como navegamos na árvore de estados.

### Tipos de Busca
1.  **FIFO (First-In First-Out):** Busca em Largura (Breadth-First). Explora nível por nível. É "cega" quanto à qualidade dos nós.
2.  **LIFO (Last-In First-Out):** Busca em Profundidade (Depth-First). Vai fundo num ramo. Também "cega".
3.  **LC-Search (Least Cost Search):** Busca de Menor Custo. É a mais inteligente.
    *   Usa uma função de custo estimada $\hat{c}(x)$ para decidir quem expandir.
    *   Fórmula: $\hat{c}(x) = f(h(x)) + \hat{g}(x)$
        *   $f(h(x))$: Custo para chegar até o nó atual (passado).
        *   $\hat{g}(x)$: Estimativa do custo do nó atual até a solução (futuro).

### Exemplo: Jogo do 15 (15-Puzzle)
*   **Problema:** Deslizar peças num quadro 4x4 para ordená-las.
*   **Teorema de Alcançabilidade:** Nem todo estado inicial pode chegar no objetivo. O texto apresenta uma fórmula baseada em inversões (`less(i)`) para checar se é possível resolver antes de tentar.
*   **Heurística $\hat{g}(x)$:** Número de peças fora do lugar.
    *   É um limite inferior, pois cada peça fora do lugar precisa de *pelo menos* um movimento.
*   **LC-Search no Jogo do 15:** O texto mostra que usar a heurística torna a busca muito mais direta, focando nos caminhos que parecem estar mais próximos da solução, evitando explorar estados inúteis.

### Exemplo: Escalonamento de Tarefas (Job Sequencing)
*   **Problema:** Tarefas com prazos e penalidades.
*   **Bound:** Soma das penalidades das tarefas não escolhidas + estimativa das futuras.
*   O exemplo mostra como a poda elimina ramos onde a penalidade acumulada já excede uma solução conhecida.

---

## Resumo Final

O Branch and Bound é sobre **não trabalhar à toa**.
1.  Usamos **heurísticas** (Bounds) para prever o futuro de um ramo.
2.  Usamos **estratégias de busca** (LC-Search) para focar no que parece mais promissor.
3.  Se a previsão for ruim, **podamos** o ramo.
