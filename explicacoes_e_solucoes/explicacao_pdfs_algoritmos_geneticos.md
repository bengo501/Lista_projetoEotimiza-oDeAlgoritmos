# Explicação dos Transcritos: Algoritmos Genéticos e Teorema dos Esquemas

Este documento resume e explica os conceitos teóricos detalhados nos transcritos fornecidos (Prof. Rafael Scopel), cobrindo desde a base de busca local até a teoria matemática profunda dos Algoritmos Genéticos (Teorema do Esquema).

## 1. Contexto: Busca Local e Heurísticas

O texto começa situando os Algoritmos Genéticos (AGs) dentro da família de **Busca Local**.

*   **O que é Busca Local?** É uma estratégia onde você mantém apenas um estado (ou poucos) e tenta melhorá-lo movendo-se para vizinhos próximos.
    *   *Vantagem:* Usa pouca memória e pode achar soluções razoáveis em espaços infinitos.
    *   *Desvantagem:* Pode ficar presa em "ótimos locais" (picos baixos) e nunca achar o "ótimo global" (o pico mais alto).
*   **Metáfora da Paisagem:** Imagine um terreno onde a altitude é a qualidade da solução (Fitness).
    *   **Hill-Climbing (Subida de Encosta):** Tenta sempre subir. Se chegar num topo, para (mesmo que existam montanhas mais altas longe dali).
    *   **Algoritmos Genéticos:** Tentam evitar ficar presos usando uma **população** espalhada pela paisagem e "saltando" através do cruzamento.

## 2. Mecânica dos Algoritmos Genéticos

Os AGs imitam a evolução biológica. O texto destaca os componentes principais:

1.  **Representação (Cromossomo):**
    *   Geralmente uma string binária (ex: `01101`).
    *   Pode ser números reais (Estratégias de Evolução).
2.  **Seleção (Quem vira pai?):**
    *   Baseada na aptidão (Fitness). Indivíduos melhores têm maior probabilidade de serem escolhidos.
    *   Exemplo da Roleta: Se sua aptidão é 31% do total, você tem 31% de chance de ser escolhido.
3.  **Cruzamento (Crossover):**
    *   Combina partes de dois pais.
    *   **Ponto de Corte:** Escolhe-se um ponto aleatório na string. O filho pega a primeira metade do Pai 1 e a segunda do Pai 2.
    *   *Objetivo:* Misturar "blocos de construção" bons de pais diferentes.
4.  **Mutação:**
    *   Inverte um bit aleatoriamente com baixa probabilidade (ex: 0.001).
    *   *Objetivo:* Introduzir diversidade e evitar que a população fique estagnada.

### Exemplos Citados
*   **8 Rainhas:** O texto usa strings de 8 dígitos (ex: `24748552`) onde cada dígito diz a linha da rainha naquela coluna. O fitness é o número de pares de rainhas que NÃO se atacam.
*   **Maximizar $f(x) = x^2$:** Usa strings de 5 bits para representar números de 0 a 31.
    *   Ex: `01000` (8) -> Fitness $8^2 = 64$.
    *   O texto mostra passo a passo como a média da população sobe de uma geração para outra.

---

## 3. A Teoria Profunda: O Teorema do Esquema (Schema Theorem)

Esta é a parte mais complexa e teórica dos textos. Ela tenta responder: **Por que e como os AGs funcionam?**

A resposta reside na ideia de que o AG não processa apenas strings individuais, mas sim **padrões** (templates) chamados **Esquemas**.

### O que é um Esquema (Schema)?
É um padrão que representa um conjunto de strings semelhantes. Usamos o símbolo `*` (curinga) para dizer "qualquer coisa (0 ou 1)".

*   Alfabeto: $\{0, 1, *\}$
*   Exemplo: O esquema `1*0` representa as strings `100` e `110`.
*   Exemplo: O esquema `****` representa TODAS as strings de tamanho 4.

### Propriedades do Esquema
Para entender quais esquemas sobrevivem, definimos duas medidas:

1.  **Ordem $o(H)$:** Número de posições fixas (0 ou 1, não estrelas).
    *   `1*1**` -> Ordem 2.
    *   `011*1` -> Ordem 4 (Mais específico, mais difícil de manter intacto).
2.  **Comprimento de Definição $\delta(H)$:** Distância entre a primeira e a última posição fixa.
    *   `1****1` -> $\delta = 6 - 1 = 5$ (Longo, fácil de ser quebrado pelo cruzamento).
    *   `**11**` -> $\delta = 4 - 3 = 1$ (Curto, difícil de ser cortado no meio).

### O Teorema Fundamental
O teorema calcula quantas cópias de um esquema $H$ esperamos ver na próxima geração $m(H, t+1)$.

A fórmula geral é (simplificada):

$$ m(H, t+1) \ge m(H, t) \cdot \frac{f(H)}{\bar{f}} \cdot [1 - P_c \frac{\delta(H)}{l-1} - o(H)P_m] $$

**O que isso significa em português?**

1.  **Fator de Reprodução $\frac{f(H)}{\bar{f}}$:**
    *   Se o esquema tem fitness média $f(H)$ maior que a média da população $\bar{f}$, ele vai crescer. Se for menor, vai diminuir.
    *   *Conclusão:* Esquemas bons se multiplicam.

2.  **Fator de Destruição pelo Cruzamento $P_c \frac{\delta(H)}{l-1}$:**
    *   Esquemas **longos** (grande $\delta$) têm alta chance de serem cortados ao meio e destruídos.
    *   Esquemas **curtos** (pequeno $\delta$) sobrevivem facilmente.

3.  **Fator de Destruição pela Mutação $o(H)P_m$:**
    *   Esquemas de **alta ordem** (muitos bits fixos) têm mais chance de sofrer uma mutação em um de seus bits importantes.
    *   Esquemas de **baixa ordem** sobrevivem mais.

### Conclusão do Teorema (Blocos de Construção)
O AG funciona porque ele cultiva **Blocos de Construção (Building Blocks)**:
> **Esquemas curtos, de baixa ordem e de alta aptidão crescem exponencialmente na população.**

O algoritmo combina esses pequenos blocos bons (ex: "começar com 1" + "terminar com 00") para formar soluções cada vez melhores e mais complexas.
