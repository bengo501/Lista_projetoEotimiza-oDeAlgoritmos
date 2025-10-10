"""
exercício 8: gerar todos os subconjuntos de um conjunto

algoritmo de divisão e conquista para gerar todos os subconjuntos.
"""

def gerar_subconjuntos_recursivo(conjunto):
    """
    gera todos os subconjuntos de um conjunto usando divisão e conquista.
    
    estratégia:
    - para conjunto vazio: retorna [[]]
    - para conjunto [x, ...resto]:
      - gera subconjuntos do resto
      - para cada subconjunto, cria duas versões: com e sem x
    
    complexidade: o(2^n) - há 2^n subconjuntos
    """
    # converte para lista se necessário
    if isinstance(conjunto, set):
        conjunto = list(conjunto)
    
    # caso base: conjunto vazio tem apenas o subconjunto vazio
    if len(conjunto) == 0:
        return [[]]
    
    # divisão: separa o primeiro elemento do resto
    primeiro = conjunto[0]
    resto = conjunto[1:]
    
    # conquista: gera subconjuntos do resto recursivamente
    subconjuntos_resto = gerar_subconjuntos_recursivo(resto)
    
    # combinação: para cada subconjunto do resto, cria dois:
    # um sem o primeiro elemento e um com o primeiro elemento
    resultado = []
    
    # subconjuntos sem o primeiro elemento
    for sub in subconjuntos_resto:
        resultado.append(sub)
    
    # subconjuntos com o primeiro elemento
    for sub in subconjuntos_resto:
        resultado.append([primeiro] + sub)
    
    return resultado


def gerar_subconjuntos_iterativo(conjunto):
    """
    versão iterativa para comparação.
    usa técnica de bits.
    """
    if isinstance(conjunto, set):
        conjunto = list(conjunto)
    
    n = len(conjunto)
    resultado = []
    
    # há 2^n subconjuntos
    for i in range(2 ** n):
        subconjunto = []
        
        # verifica cada bit
        for j in range(n):
            # se o bit j está setado, inclui o elemento j
            if i & (1 << j):
                subconjunto.append(conjunto[j])
        
        resultado.append(subconjunto)
    
    return resultado


def visualizar_subconjuntos(conjunto, subconjuntos):
    """
    visualiza os subconjuntos de forma organizada.
    """
    print(f"subconjuntos de {conjunto}:")
    print(f"total: {len(subconjuntos)}")
    print("-" * 50)
    
    # organiza por tamanho
    por_tamanho = {}
    for sub in subconjuntos:
        tam = len(sub)
        if tam not in por_tamanho:
            por_tamanho[tam] = []
        por_tamanho[tam].append(sub)
    
    # exibe por tamanho
    for tam in sorted(por_tamanho.keys()):
        print(f"\ntamanho {tam}: ({len(por_tamanho[tam])} subconjuntos)")
        for sub in sorted(por_tamanho[tam]):
            print(f"  {sub}")


def testar_geracao():
    """
    testa a geração de subconjuntos com vários casos.
    """
    casos = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
        ['a', 'b', 'c', 'd'],
        [10, 20, 30, 40, 50]
    ]
    
    print("=" * 70)
    print("teste: geração de subconjuntos (recursivo)")
    print("=" * 70)
    print()
    
    for conjunto in casos:
        print("=" * 70)
        subconjuntos = gerar_subconjuntos_recursivo(conjunto)
        visualizar_subconjuntos(conjunto, subconjuntos)
        
        # verifica se a quantidade está correta
        esperado = 2 ** len(conjunto)
        if len(subconjuntos) == esperado:
            print(f"\nverificação: ok (2^{len(conjunto)} = {esperado})")
        else:
            print(f"\nverificação: erro! esperado {esperado}, obtido {len(subconjuntos)}")
        
        print()


def comparar_metodos():
    """
    compara método recursivo e iterativo.
    """
    print("\n" + "=" * 70)
    print("comparação: recursivo vs iterativo")
    print("=" * 70)
    
    conjunto = [1, 2, 3, 4]
    
    print(f"\nconjunto de teste: {conjunto}")
    
    subconjuntos_rec = gerar_subconjuntos_recursivo(conjunto)
    subconjuntos_iter = gerar_subconjuntos_iterativo(conjunto)
    
    print(f"\nrecursivo: {len(subconjuntos_rec)} subconjuntos")
    print(f"iterativo: {len(subconjuntos_iter)} subconjuntos")
    
    # ordena para comparar
    sub_rec_ordenados = [sorted(s) for s in subconjuntos_rec]
    sub_iter_ordenados = [sorted(s) for s in subconjuntos_iter]
    sub_rec_ordenados.sort()
    sub_iter_ordenados.sort()
    
    if sub_rec_ordenados == sub_iter_ordenados:
        print("\nambos os métodos geraram os mesmos subconjuntos!")
    else:
        print("\nerro: métodos geraram subconjuntos diferentes!")


def explicar_divisao_conquista():
    """
    explica como este é um algoritmo de divisão e conquista.
    """
    print("\n\n" + "=" * 70)
    print("geração de subconjuntos como divisão e conquista")
    print("=" * 70)
    
    print("\n1. divisão:")
    print("   - separa um elemento do conjunto")
    print("   - problema: subconjuntos de [x, y, z]")
    print("   - divide em: x e subconjuntos de [y, z]")
    
    print("\n2. conquista:")
    print("   - resolve recursivamente para o resto")
    print("   - caso base: conjunto vazio tem apenas {}")
    
    print("\n3. combinação:")
    print("   - para cada subconjunto do resto:")
    print("   - cria versão sem x")
    print("   - cria versão com x")
    
    print("\nexemplo visual para {1, 2, 3}:")
    print("                    {1,2,3}")
    print("                   /      \\")
    print("         sem 1: {2,3}      com 1: 1+{2,3}")
    print("               /    \\            /       \\")
    print("       sem 2:{3}   com 2:2+{3}  ...")
    print("           / \\        / \\")
    print("          {}  {3}   {2} {2,3}")
    
    print("\nrecorrencia:")
    print("  subsets(S) = {")
    print("    {{}}                             se S = {}")
    print("    subsets(resto) uniao {x}+subsets(resto)  caso contrario")
    print("  }")
    
    print("\ncomplexidade:")
    print("  - número de subconjuntos: 2^n")
    print("  - tempo: o(n * 2^n) - precisa copiar cada subconjunto")
    print("  - espaço: o(n * 2^n) - armazena todos os subconjuntos")


def formula_combinatoria():
    """
    mostra a fórmula combinatória relacionada.
    """
    print("\n\n" + "=" * 70)
    print("relação com combinatória")
    print("=" * 70)
    
    print("\nnúmero de subconjuntos de tamanho k de um conjunto de tamanho n:")
    print("  c(n,k) = n! / (k! * (n-k)!)")
    
    print("\ntotal de subconjuntos:")
    print("  soma de c(n,k) para k=0 até n = 2^n")
    
    import math
    
    n = 5
    print(f"\nexemplo para n={n}:")
    total = 0
    for k in range(n + 1):
        comb = math.comb(n, k)
        total += comb
        print(f"  tamanho {k}: c({n},{k}) = {comb}")
    
    print(f"\ntotal: {total} = 2^{n} = {2**n}")


if __name__ == "__main__":
    testar_geracao()
    comparar_metodos()
    explicar_divisao_conquista()
    formula_combinatoria()

