# Explicação dos Transcritos: Backtracking

Este documento resume e explica os conceitos teóricos e exemplos detalhados nos transcritos fornecidos (Prof. Rafael Scopel) sobre a técnica **Backtracking**.

## 1. Conceitos Fundamentais

O Backtracking é uma técnica refinada de **busca exaustiva** (força bruta). Enquanto a força bruta gera todas as soluções possíveis e depois verifica quais servem, o Backtracking constrói a solução passo a passo e abandona (poda) um caminho assim que percebe que ele não levará a uma solução válida.

### A Árvore do Espaço de Estados
*   O problema é modelado como uma árvore onde cada nível representa uma escolha para um componente da solução.
*   **Nó Promissor:** Um nó que representa uma solução parcial que ainda pode ser completada para virar uma solução válida.
*   **Nó Não-Promissor:** Um nó que viola alguma restrição. O algoritmo "volta atrás" (backtrack) para o pai deste nó assim que o identifica.
*   **Busca em Profundidade (DFS):** O Backtracking geralmente explora a árvore em profundidade (vai descendo até não dar mais, depois volta).

---

## 2. Exemplos Detalhados

### A. Problema das N-Rainhas (N-Queens)
*   **Objetivo:** Colocar $N$ rainhas num tabuleiro $N \times N$ sem que se ataquem (mesma linha, coluna ou diagonal).
*   **Estratégia:**
    *   Colocamos a rainha 1 na linha 1, rainha 2 na linha 2, etc. A decisão é apenas qual **coluna** escolher para cada linha.
*   **Restrições:**
    *   Colunas distintas ($x_i \neq x_k$).
    *   Diagonais distintas: Duas rainhas em $(i, j)$ e $(k, l)$ se atacam diagonalmente se $|j - l| = |k - i|$.
*   **Função `Place(k, i)`:** Verifica se é seguro colocar a rainha $k$ na coluna $i$, testando contra todas as rainhas anteriores.
*   **Eficiência:** Para $N=8$, força bruta testaria ~4.4 bilhões de posições. Backtracking reduz drasticamente, visitando apenas uma fração minúscula (ex: 40.320 se considerarmos apenas permutações de colunas, e muito menos com as podas diagonais).

### B. Soma dos Subconjuntos (Sum of Subsets)
*   **Objetivo:** Dado um conjunto de pesos $W = \{w_1, \dots, w_n\}$ e um alvo $M$, encontrar subconjuntos cuja soma seja exatamente $M$.
*   **Árvore Binária:**
    *   Filho Esquerdo ($x_i = 1$): Inclui o item $w_i$.
    *   Filho Direito ($x_i = 0$): Exclui o item $w_i$.
*   **Otimizações (Podas):**
    *   Ordenamos os pesos em ordem crescente.
    *   Mantemos a soma atual $s$ e a soma dos itens restantes $r$.
    *   **Poda 1:** Se $s + w_{k+1} > M$ (incluir o próximo já estoura o alvo).
    *   **Poda 2:** Se $s + r < M$ (mesmo pegando tudo o que sobrou, não alcança o alvo).
*   **Algoritmo `SumOfSub(s, k, r)`:** Implementa essa lógica recursivamente.

### C. Ciclo Hamiltoniano
*   **Objetivo:** Encontrar um ciclo num grafo que visite cada vértice exatamente uma vez e volte ao início.
*   **Backtracking:** Começa num vértice, tenta ir para um vizinho não visitado. Se ficar preso (todos vizinhos visitados e não é o fim), volta e tenta outro caminho.

---

## 3. Formalização e Complexidade

### Restrições
*   **Explícitas:** Definem o domínio das variáveis (ex: $x_i \in \{0, 1\}$ ou $x_i \in \{1, \dots, N\}$). Definem o espaço de busca total.
*   **Implícitas:** Definem como as variáveis se relacionam (ex: "não podem se atacar"). São usadas pelas funções delimitadoras (bounding functions) para podar a árvore.

### Estimativa de Tamanho (Método de Knuth)
*   Como saber quanto tempo vai demorar? É difícil calcular analiticamente.
*   **Ideia de Knuth:** Fazer um "passeio aleatório" na árvore.
    *   Começa na raiz.
    *   Vê quantos filhos válidos existem ($c_0$). Escolhe um aleatoriamente.
    *   No próximo nível, vê quantos filhos válidos ($c_1$). Escolhe um.
    *   Repete até uma folha.
    *   A estimativa do total de nós é $1 + c_0 + c_0 c_1 + \dots + c_0 \dots c_k$.
    *   Fazendo isso várias vezes e tirando a média, temos uma estimativa do tamanho da árvore de busca (Monte Carlo).

## Resumo Final
O Backtracking é a "força bruta inteligente". Ele organiza a busca numa árvore e usa as restrições do problema para cortar ramos inteiros o mais cedo possível, tornando viável resolver problemas que seriam impossíveis com força bruta pura.
