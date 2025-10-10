"""
exercicio 12: gerar todas as permutacoes de elementos de um conjunto

algoritmo de divisao e conquista para gerar permutacoes.
"""

def gerar_permutacoes_recursivo(elementos):
    """
    gera todas as permutacoes de um conjunto usando divisao e conquista.
    
    estrategia:
    - caso base: conjunto vazio tem apenas permutacao vazia
    - caso base: conjunto com 1 elemento tem apenas ele mesmo
    - recursao: para cada elemento, fixe-o e permute o resto
    
    complexidade: o(n! * n) - ha n! permutacoes e cada uma leva o(n) para criar
    """
    # converte para lista se necessario
    if isinstance(elementos, set):
        elementos = list(elementos)
    
    # caso base
    if len(elementos) == 0:
        return [[]]
    
    if len(elementos) == 1:
        return [elementos]
    
    resultado = []
    
    # para cada elemento, fixe-o como primeiro e permute o resto
    for i in range(len(elementos)):
        elemento_atual = elementos[i]
        resto = elementos[:i] + elementos[i+1:]
        
        # conquista: gera permutacoes do resto
        permutacoes_resto = gerar_permutacoes_recursivo(resto)
        
        # combinacao: adiciona elemento atual no inicio de cada permutacao do resto
        for perm in permutacoes_resto:
            resultado.append([elemento_atual] + perm)
    
    return resultado


def gerar_permutacoes_iterativo(elementos):
    """
    versao iterativa usando algoritmo de heap.
    mais eficiente em python.
    """
    import itertools
    if isinstance(elementos, set):
        elementos = list(elementos)
    return list(itertools.permutations(elementos))


def visualizar_permutacoes(conjunto, permutacoes):
    """
    visualiza as permutacoes de forma organizada.
    """
    print(f"permutacoes de {conjunto}:")
    print(f"total: {len(permutacoes)}")
    print("-" * 50)
    
    for i, perm in enumerate(permutacoes, 1):
        print(f"{i:3d}. {perm}")


def testar_geracao():
    """
    testa a geracao de permutacoes com varios casos.
    """
    import math
    
    casos = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        ['a', 'b', 'c', 'd']
    ]
    
    print("=" * 70)
    print("teste: geracao de permutacoes")
    print("=" * 70)
    print()
    
    for conjunto in casos:
        print("=" * 70)
        permutacoes = gerar_permutacoes_recursivo(conjunto)
        
        if len(conjunto) <= 4:
            visualizar_permutacoes(conjunto, permutacoes)
        else:
            print(f"conjunto: {conjunto}")
            print(f"total de permutacoes: {len(permutacoes)}")
            print("(muito grande para exibir todas)")
        
        # verifica se a quantidade esta correta
        esperado = math.factorial(len(conjunto))
        if len(permutacoes) == esperado:
            print(f"\nverificacao: ok ({len(conjunto)}! = {esperado})")
        else:
            print(f"\nverificacao: erro! esperado {esperado}, obtido {len(permutacoes)}")
        
        print()


def comparar_metodos():
    """
    compara metodo recursivo e iterativo.
    """
    print("\n" + "=" * 70)
    print("comparacao: recursivo vs iterativo")
    print("=" * 70)
    
    conjunto = [1, 2, 3, 4]
    
    print(f"\nconjunto de teste: {conjunto}")
    
    perm_rec = gerar_permutacoes_recursivo(conjunto)
    perm_iter = gerar_permutacoes_iterativo(conjunto)
    
    print(f"\nrecursivo: {len(perm_rec)} permutacoes")
    print(f"iterativo: {len(perm_iter)} permutacoes")
    
    # converte tuplas em listas para comparar
    perm_iter_listas = [list(p) for p in perm_iter]
    
    # ordena para comparar
    perm_rec_ordenadas = sorted([tuple(p) for p in perm_rec])
    perm_iter_ordenadas = sorted([tuple(p) for p in perm_iter_listas])
    
    if perm_rec_ordenadas == perm_iter_ordenadas:
        print("\nambos os metodos geraram as mesmas permutacoes!")
    else:
        print("\nerro: metodos geraram permutacoes diferentes!")


def explicar_divisao_conquista():
    """
    explica como este e um algoritmo de divisao e conquista.
    """
    print("\n\n" + "=" * 70)
    print("geracao de permutacoes como divisao e conquista")
    print("=" * 70)
    
    print("\n1. divisao:")
    print("   - escolhe um elemento para ser o primeiro")
    print("   - problema: permutacoes de [1,2,3]")
    print("   - divide em: 1+permutacoes([2,3]), 2+permutacoes([1,3]), etc")
    
    print("\n2. conquista:")
    print("   - resolve recursivamente para o resto")
    print("   - caso base: lista vazia ou com 1 elemento")
    
    print("\n3. combinacao:")
    print("   - para cada elemento escolhido:")
    print("   - combina com todas as permutacoes do resto")
    
    print("\nexemplo visual para [1, 2, 3]:")
    print("                    [1,2,3]")
    print("           /          |         \\")
    print("      1+[2,3]     2+[1,3]     3+[1,2]")
    print("       /  \\         /  \\         /  \\")
    print("    [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]")
    
    print("\nrecorrencia:")
    print("  perm(S) = {")
    print("    [[]]              se S = []")
    print("    [S]               se |S| = 1")
    print("    uniao de x+perm(S-{x}) para todo x em S  caso contrario")
    print("  }")
    
    print("\ncomplexidade:")
    print("  - numero de permutacoes: n!")
    print("  - tempo: o(n! * n) - para criar cada permutacao")
    print("  - espaco: o(n! * n) - armazena todas as permutacoes")
    
    print("\ncrescimento fatorial:")
    import math
    print("  n  | n!")
    print("  ---|-------")
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(f"  {n:2d} | {math.factorial(n):7d}")


def aplicacoes():
    """
    mostra aplicacoes praticas de permutacoes.
    """
    print("\n\n" + "=" * 70)
    print("aplicacoes praticas")
    print("=" * 70)
    
    print("\n1. problema do caixeiro viajante (tsp):")
    print("   - encontrar a rota mais curta visitando todas as cidades")
    print("   - abordagem de forca bruta: testar todas as permutacoes")
    
    print("\n2. agendamento de tarefas:")
    print("   - encontrar a melhor ordem para executar tarefas")
    print("   - minimizar tempo total ou custo")
    
    print("\n3. criptografia:")
    print("   - permutacoes sao usadas em cifras")
    print("   - embaralhamento de posicoes")
    
    print("\n4. combinatorica:")
    print("   - analise de possibilidades")
    print("   - teoria dos jogos")
    
    print("\nexemplo: tsp simplificado")
    print("-" * 70)
    
    # matriz de distancias entre cidades
    cidades = ['A', 'B', 'C', 'D']
    distancias = {
        ('A','B'): 10, ('B','A'): 10,
        ('A','C'): 15, ('C','A'): 15,
        ('A','D'): 20, ('D','A'): 20,
        ('B','C'): 35, ('C','B'): 35,
        ('B','D'): 25, ('D','B'): 25,
        ('C','D'): 30, ('D','C'): 30
    }
    
    print(f"\ncidades: {cidades}")
    print("encontrando a rota mais curta...")
    
    # gera todas as rotas possiveis (exceto a primeira cidade fixa)
    rotas = gerar_permutacoes_recursivo(cidades[1:])
    
    melhor_rota = None
    melhor_distancia = float('inf')
    
    for rota in rotas:
        rota_completa = [cidades[0]] + rota + [cidades[0]]
        distancia_total = 0
        
        for i in range(len(rota_completa) - 1):
            distancia_total += distancias.get((rota_completa[i], rota_completa[i+1]), 0)
        
        if distancia_total < melhor_distancia:
            melhor_distancia = distancia_total
            melhor_rota = rota_completa
    
    print(f"\nmelhor rota: {' -> '.join(melhor_rota)}")
    print(f"distancia total: {melhor_distancia}")


if __name__ == "__main__":
    testar_geracao()
    comparar_metodos()
    explicar_divisao_conquista()
    aplicacoes()

