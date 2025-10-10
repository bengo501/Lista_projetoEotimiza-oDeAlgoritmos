"""
exercicio: algoritmo genetico para ajuste de polinomio

dado varios pontos (x1,y1), (x2,y2), ..., (xn,yn) que pertencem a
uma funcao desconhecida f(x), queremos aproxima-la por um polinomio
p(x) = ax³ + bx² + cx + d

usar funcao de distancia: d(p) = soma |p(xi) - yi|

passos:
(a) criar populacao de n polinomios
(b) implementar funcao d() para medir qualidade
(c) implementar estrategia de evolucao
(d) fazer populacao evoluir
(e) opcao de usar polinomio de grau maior
"""

import random
import math

class Polinomio:
    """representa um polinomio p(x) = ax³ + bx² + cx + d"""
    
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.fitness = float('inf')
    
    def avaliar(self, x):
        """avalia p(x)."""
        return self.a * x**3 + self.b * x**2 + self.c * x + self.d
    
    def __repr__(self):
        return f"p(x) = {self.a:.4f}x³ + {self.b:.4f}x² + {self.c:.4f}x + {self.d:.4f}"


def criar_polinomio_aleatorio(min_coef=-10, max_coef=10):
    """cria um polinomio com coeficientes aleatorios."""
    a = random.uniform(min_coef, max_coef)
    b = random.uniform(min_coef, max_coef)
    c = random.uniform(min_coef, max_coef)
    d = random.uniform(min_coef, max_coef)
    return Polinomio(a, b, c, d)


def criar_populacao(tamanho, min_coef=-10, max_coef=10):
    """(a) cria uma populacao de polinomios aleatorios."""
    return [criar_polinomio_aleatorio(min_coef, max_coef) for _ in range(tamanho)]


def calcular_fitness(polinomio, pontos):
    """(b) calcula a funcao de distancia d(p) = soma |p(xi) - yi|."""
    distancia_total = 0
    for x, y in pontos:
        y_pred = polinomio.avaliar(x)
        distancia_total += abs(y_pred - y)
    return distancia_total


def avaliar_populacao(populacao, pontos):
    """calcula fitness de toda a populacao."""
    for individuo in populacao:
        individuo.fitness = calcular_fitness(individuo, pontos)


def selecao_torneio(populacao, tamanho_torneio=3):
    """seleciona um individuo usando torneio."""
    competidores = random.sample(populacao, tamanho_torneio)
    return min(competidores, key=lambda p: p.fitness)


def crossover(pai1, pai2):
    """(c) crossover: combina dois polinomios."""
    # crossover aritmetico: media ponderada
    alpha = random.random()
    
    a = alpha * pai1.a + (1 - alpha) * pai2.a
    b = alpha * pai1.b + (1 - alpha) * pai2.b
    c = alpha * pai1.c + (1 - alpha) * pai2.c
    d = alpha * pai1.d + (1 - alpha) * pai2.d
    
    return Polinomio(a, b, c, d)


def mutacao(polinomio, taxa_mutacao=0.1, intensidade=1.0):
    """(c) mutacao: pequenas alteracoes aleatorias."""
    if random.random() < taxa_mutacao:
        polinomio.a += random.gauss(0, intensidade)
    if random.random() < taxa_mutacao:
        polinomio.b += random.gauss(0, intensidade)
    if random.random() < taxa_mutacao:
        polinomio.c += random.gauss(0, intensidade)
    if random.random() < taxa_mutacao:
        polinomio.d += random.gauss(0, intensidade)


def evoluir_populacao(populacao, pontos, taxa_mutacao=0.1):
    """(d) evolui a populacao por uma geracao."""
    nova_populacao = []
    tamanho = len(populacao)
    
    # elitismo: mantem os 2 melhores
    populacao_ordenada = sorted(populacao, key=lambda p: p.fitness)
    nova_populacao.extend(populacao_ordenada[:2])
    
    # gera resto da populacao
    while len(nova_populacao) < tamanho:
        pai1 = selecao_torneio(populacao)
        pai2 = selecao_torneio(populacao)
        
        filho = crossover(pai1, pai2)
        mutacao(filho, taxa_mutacao)
        
        nova_populacao.append(filho)
    
    return nova_populacao


def algoritmo_genetico(pontos, tamanho_pop=100, num_geracoes=1000, 
                       taxa_mutacao=0.1, verbose=True):
    """
    algoritmo genetico completo para ajuste de polinomio.
    """
    # cria populacao inicial
    populacao = criar_populacao(tamanho_pop)
    
    melhor_historico = []
    
    for geracao in range(num_geracoes):
        # avalia fitness
        avaliar_populacao(populacao, pontos)
        
        # encontra melhor individuo
        melhor = min(populacao, key=lambda p: p.fitness)
        melhor_historico.append(melhor.fitness)
        
        # exibe progresso
        if verbose and (geracao % 100 == 0 or geracao == num_geracoes - 1):
            print(f"geracao {geracao:4d}: melhor fitness = {melhor.fitness:.6f}")
        
        # condicao de parada: fitness muito bom
        if melhor.fitness < 0.01:
            if verbose:
                print(f"convergiu na geracao {geracao}!")
            break
        
        # evolui populacao
        populacao = evoluir_populacao(populacao, pontos, taxa_mutacao)
    
    # retorna melhor individuo
    melhor = min(populacao, key=lambda p: p.fitness)
    return melhor, melhor_historico


def testar_algoritmo():
    """
    testa o algoritmo genetico.
    """
    print("=" * 70)
    print("algoritmo genetico para ajuste de polinomio")
    print("=" * 70)
    
    # gera pontos de uma funcao conhecida
    print("\nfuncao verdadeira: f(x) = 2x³ - 3x² + 5x + 1")
    funcao_real = lambda x: 2*x**3 - 3*x**2 + 5*x + 1
    
    # gera pontos
    pontos = []
    for x in range(-5, 6):
        y = funcao_real(x) + random.gauss(0, 2)  # adiciona ruido
        pontos.append((x, y))
    
    print(f"\ngerados {len(pontos)} pontos com ruido gaussiano")
    print("pontos:", pontos[:5], "...")
    
    # executa algoritmo genetico
    print("\n" + "=" * 70)
    print("executando algoritmo genetico")
    print("=" * 70)
    
    melhor, historico = algoritmo_genetico(
        pontos,
        tamanho_pop=100,
        num_geracoes=500,
        taxa_mutacao=0.15,
        verbose=True
    )
    
    print("\n" + "=" * 70)
    print("resultado")
    print("=" * 70)
    
    print(f"\nmelhor polinomio encontrado:")
    print(f"  {melhor}")
    print(f"\nfitness (erro total): {melhor.fitness:.6f}")
    
    print(f"\ncomparacao com funcao real:")
    print(f"  real:       p(x) = 2.0000x³ - 3.0000x² + 5.0000x + 1.0000")
    print(f"  encontrado: {melhor}")
    
    # testa em novos pontos
    print("\n\nteste em novos pontos:")
    print("-" * 50)
    print("x   | f(x) real | p(x) aprox | erro")
    print("-" * 50)
    
    for x in [-3, -1, 0, 2, 4]:
        y_real = funcao_real(x)
        y_aprox = melhor.avaliar(x)
        erro = abs(y_real - y_aprox)
        print(f"{x:3d} | {y_real:9.2f} | {y_aprox:10.2f} | {erro:.2f}")


def visualizar_convergencia():
    """
    visualiza a convergencia do algoritmo.
    """
    print("\n\n" + "=" * 70)
    print("exemplo com funcao nao-polinomial")
    print("=" * 70)
    
    # tenta aproximar uma funcao senoidal (nao e polinomio!)
    print("\nfuncao: f(x) = 10*sin(x) + 5")
    funcao = lambda x: 10 * math.sin(x) + 5
    
    pontos = [(x/2, funcao(x/2)) for x in range(-20, 21)]
    
    print(f"gerados {len(pontos)} pontos")
    
    melhor, historico = algoritmo_genetico(
        pontos,
        tamanho_pop=150,
        num_geracoes=300,
        taxa_mutacao=0.2,
        verbose=False
    )
    
    print(f"\nmelhor polinomio: {melhor}")
    print(f"fitness: {melhor.fitness:.4f}")
    
    print("\nobservacao:")
    print("  polinomio cubico nao pode aproximar perfeitamente uma senoide")
    print("  mas o ag encontra a melhor aproximacao possivel")
    print("  opcao (e): usar polinomio de grau maior ou outra familia")


def explicar_algoritmo():
    """
    explica o algoritmo genetico.
    """
    print("\n\n" + "=" * 70)
    print("como funciona o algoritmo genetico")
    print("=" * 70)
    
    print("\n1. representacao:")
    print("   - individuo = polinomio com coeficientes (a,b,c,d)")
    print("   - populacao = conjunto de polinomios")
    
    print("\n2. funcao de fitness:")
    print("   - d(p) = soma |p(xi) - yi|")
    print("   - quanto menor, melhor")
    
    print("\n3. selecao:")
    print("   - torneio: escolhe entre k aleatorios o melhor")
    print("   - pressao seletiva moderada")
    
    print("\n4. crossover:")
    print("   - combina dois polinomios pais")
    print("   - media ponderada dos coeficientes")
    
    print("\n5. mutacao:")
    print("   - pequenas alteracoes aleatorias")
    print("   - mantem diversidade")
    
    print("\n6. elitismo:")
    print("   - mantem os 2 melhores da geracao")
    print("   - garante que nao pioramos")
    
    print("\nparametros importantes:")
    print("  - tamanho populacao: 50-200")
    print("  - taxa mutacao: 0.1-0.3")
    print("  - geracoes: 100-1000")


if __name__ == "__main__":
    random.seed(42)  # para reproducibilidade
    testar_algoritmo()
    visualizar_convergencia()
    explicar_algoritmo()

