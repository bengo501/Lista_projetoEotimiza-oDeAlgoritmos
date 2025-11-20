import random
import math

# Dados de exemplo (pontos que queremos aproximar)
# Vamos gerar pontos baseados em uma função conhecida para testar: 2x^3 - 3x^2 + x + 5
TARGET_COEFFS = [2, -3, 1, 5]
POINTS = []
for x in range(-5, 6):
    y = TARGET_COEFFS[0]*x**3 + TARGET_COEFFS[1]*x**2 + TARGET_COEFFS[2]*x + TARGET_COEFFS[3]
    POINTS.append((x, y))

# Parâmetros do AG
POPULATION_SIZE = 100
GENERATIONS = 500
MUTATION_RATE = 0.1
MUTATION_SCALE = 0.5

class Individual:
    def __init__(self, genes=None):
        if genes:
            self.genes = genes
        else:
            # Inicialização aleatória dos coeficientes [a, b, c, d]
            self.genes = [random.uniform(-10, 10) for _ in range(4)]
        self.fitness = 0

    def calculate_fitness(self):
        error = 0
        a, b, c, d = self.genes
        for x, y_target in POINTS:
            y_pred = a*(x**3) + b*(x**2) + c*x + d
            error += abs(y_pred - y_target)
        self.fitness = error # Queremos minimizar o erro
        return self.fitness

def selection(population):
    # Torneio: escolhe k indivíduos aleatórios e pega o melhor
    tournament_size = 5
    best = None
    for _ in range(tournament_size):
        ind = random.choice(population)
        if best is None or ind.fitness < best.fitness:
            best = ind
    return best

def crossover(parent1, parent2):
    # Crossover aritmético (média ponderada) ou simples troca
    # Vamos usar média simples aqui
    child_genes = []
    for g1, g2 in zip(parent1.genes, parent2.genes):
        child_genes.append((g1 + g2) / 2.0)
    return Individual(child_genes)

def mutate(individual):
    for i in range(len(individual.genes)):
        if random.random() < MUTATION_RATE:
            individual.genes[i] += random.gauss(0, MUTATION_SCALE)

def run_genetic_algorithm():
    # 1. Inicializar população
    population = [Individual() for _ in range(POPULATION_SIZE)]
    for ind in population:
        ind.calculate_fitness()

    best_overall = None

    for gen in range(GENERATIONS):
        # Ordenar população para elitismo (menor fitness é melhor)
        population.sort(key=lambda x: x.fitness)
        
        if best_overall is None or population[0].fitness < best_overall.fitness:
            best_overall = population[0]
        
        if gen % 50 == 0:
            print(f"Geração {gen}: Melhor Erro = {population[0].fitness:.4f} | Coefs: {[round(g, 2) for g in population[0].genes]}")

        # Elitismo: mantém os melhores
        new_population = population[:10]

        # Gerar o resto da nova população
        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population)
            parent2 = selection(population)
            child = crossover(parent1, parent2)
            mutate(child)
            child.calculate_fitness()
            new_population.append(child)

        population = new_population

    print("\n--- Resultado Final ---")
    print(f"Melhor indivíduo encontrado (Erro: {best_overall.fitness:.4f})")
    print(f"Coeficientes encontrados: {[round(g, 4) for g in best_overall.genes]}")
    print(f"Coeficientes reais:       {TARGET_COEFFS}")

if __name__ == "__main__":
    print("Iniciando Algoritmo Genético para Ajuste de Polinômio...")
    print(f"Pontos alvo gerados por: {TARGET_COEFFS[0]}x^3 + {TARGET_COEFFS[1]}x^2 + {TARGET_COEFFS[2]}x + {TARGET_COEFFS[3]}")
    run_genetic_algorithm()
