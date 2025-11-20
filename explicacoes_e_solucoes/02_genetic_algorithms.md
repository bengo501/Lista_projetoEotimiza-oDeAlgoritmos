# Algoritmos Genéticos - Explicação Detalhada

Algoritmos Genéticos (AGs) são uma forma de **Computação Evolutiva**. Eles não "calculam" a resposta diretamente (como uma fórmula matemática); eles "evoluem" uma resposta, imitando a seleção natural.

É uma técnica excelente para problemas onde não sabemos como resolver diretamente, mas sabemos reconhecer uma boa solução quando a vemos.

---

## O Problema: Ajuste de Curva (Curve Fitting)

**O Problema:**
Temos um conjunto de pontos misteriosos: $(x_1, y_1), (x_2, y_2), \dots$.
Queremos encontrar uma função matemática que passe o mais perto possível desses pontos.
Escolhemos tentar um polinômio de grau 3:
$$ p(x) = ax^3 + bx^2 + cx + d $$
Nosso objetivo é descobrir os números mágicos $a, b, c, d$.

### Teoria e Conceitos Biológicos

1.  **Indivíduo (Cromossomo):**
    -   No nosso caso, um indivíduo é uma lista de 4 números: $[a, b, c, d]$.
    -   Exemplo: `[2.1, -3.0, 0.5, 4.9]` é um "ser vivo" nesta simulação.

2.  **População:**
    -   Um conjunto de 100 ou mais indivíduos. No começo, eles são gerados aleatoriamente (monstros disformes que não se parecem com a curva certa).

3.  **Fitness (Aptidão):**
    -   Como sabemos se um indivíduo é "forte" ou "fraco"?
    -   Calculamos o **Erro Total**: A soma das distâncias entre onde a curva do indivíduo passa e onde os pontos reais estão.
    -   Matematicamente: $Erro = \sum |p(x_{real}) - y_{real}|$
    -   **Menor erro = Maior Fitness.** (Neste caso, estamos minimizando o erro).

4.  **Seleção Natural (Sobrevivência):**
    -   Indivíduos com menor erro têm mais chance de virar pais.
    -   Método do **Torneio**: Pegamos 5 indivíduos aleatórios da população e escolhemos o melhor deles para ser pai. Isso preserva diversidade mas favorece os bons.

5.  **Reprodução (Crossover):**
    -   Pegamos dois pais:
        -   Pai 1: `[2, -3, 1, 5]`
        -   Pai 2: `[4, -1, 0, 2]`
    -   Criamos um filho misturando os genes. Pode ser a média:
        -   Filho: `[3, -2, 0.5, 3.5]`
    -   Isso permite que o filho herde boas características (esperamos) de ambos.

6.  **Mutação (A "Centelha" da Inovação):**
    -   De vez em quando, alteramos um gene aleatoriamente.
    -   Ex: `[3, -2, 0.5, 3.5]` -> `[3, -2, 0.5, 3.6]`
    -   Sem mutação, a população ficaria estagnada, presa num "ótimo local" sem explorar novas possibilidades.

### Passo a Passo da Evolução

1.  **Gênesis:** Criamos 100 polinômios com coeficientes aleatórios entre -10 e 10.
2.  **Avaliação:** Calculamos o erro de todos eles comparando com os pontos alvo.
3.  **Loop de Gerações (Repetir 500 vezes):**
    a.  **Elitismo:** O melhor indivíduo de todos passa direto para a próxima geração (imortalidade para o rei). Isso garante que nunca perdemos a melhor solução encontrada.
    b.  **Nova População:** Enquanto a nova população não estiver cheia:
        i.   Seleciona Pai 1 (Torneio).
        ii.  Seleciona Pai 2 (Torneio).
        iii. Cria Filho (Média dos pais).
        iv.  Aplica Mutação (Pequena chance de alterar os números).
        v.   Adiciona Filho na nova população.
    c.  Substitui a população antiga pela nova.
4.  **Fim:** O melhor indivíduo da última geração é nossa resposta.

### O Código Explicado

```python
class Individual:
    def __init__(self, genes=None):
        # Se não passarmos genes, cria aleatórios
        if genes:
            self.genes = genes
        else:
            self.genes = [random.uniform(-10, 10) for _ in range(4)]
        self.fitness = 0

    def calculate_fitness(self):
        error = 0
        a, b, c, d = self.genes
        # Para cada ponto real (x, y_target)
        for x, y_target in POINTS:
            # Calcula onde ESTE polinômio passa
            y_pred = a*(x**3) + b*(x**2) + c*x + d
            # Soma a diferença (erro absoluto)
            error += abs(y_pred - y_target)
        self.fitness = error
        return self.fitness

def run_genetic_algorithm():
    # 1. Inicializar população
    population = [Individual() for _ in range(POPULATION_SIZE)]
    
    # Avalia a primeira geração
    for ind in population:
        ind.calculate_fitness()

    for gen in range(GENERATIONS):
        # Ordena: Menor erro primeiro
        population.sort(key=lambda x: x.fitness)
        
        # Elitismo: Os 10 melhores passam direto
        new_population = population[:10]

        # Preenche o resto com filhos
        while len(new_population) < POPULATION_SIZE:
            # Seleção
            parent1 = selection(population)
            parent2 = selection(population)
            
            # Crossover (Média)
            child = crossover(parent1, parent2)
            
            # Mutação
            mutate(child)
            
            # Avalia o filho
            child.calculate_fitness()
            new_population.append(child)

        population = new_population
```

### Por que funciona?
A mágica é que não precisamos saber *como* reduzir o erro matematicamente (derivadas, gradientes). Só precisamos saber *quem* tem o menor erro. A pressão seletiva empurra a população inteira em direção à solução correta, como água descendo um morro, mesmo que o morro seja complexo e cheio de buracos.
