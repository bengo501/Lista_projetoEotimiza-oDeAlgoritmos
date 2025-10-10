"""
exercícios 4 e 5: mergesort

implementação de mergesort dividindo em duas partes (convencional)
e também uma versão dividindo em três partes.
"""

def merge(esquerda, direita):
    """
    combina dois arrays ordenados em um único array ordenado.
    """
    resultado = []
    i = j = 0
    
    # mescla elementos comparando
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # adiciona elementos restantes
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado


def mergesort_2_partes(arr):
    """
    mergesort convencional - divide em duas partes.
    
    complexidade: o(n log n)
    """
    # caso base
    if len(arr) <= 1:
        return arr
    
    # divisão: divide ao meio
    meio = len(arr) // 2
    esquerda = arr[:meio]
    direita = arr[meio:]
    
    # conquista: ordena recursivamente
    esquerda_ordenada = mergesort_2_partes(esquerda)
    direita_ordenada = mergesort_2_partes(direita)
    
    # combinação: mescla as partes ordenadas
    return merge(esquerda_ordenada, direita_ordenada)


def merge_3_partes(parte1, parte2, parte3):
    """
    combina três arrays ordenados em um único array ordenado.
    """
    resultado = []
    i = j = k = 0
    
    # mescla os três arrays comparando os elementos
    while i < len(parte1) and j < len(parte2) and k < len(parte3):
        minimo = min(parte1[i], parte2[j], parte3[k])
        
        if minimo == parte1[i]:
            resultado.append(parte1[i])
            i += 1
        elif minimo == parte2[j]:
            resultado.append(parte2[j])
            j += 1
        else:
            resultado.append(parte3[k])
            k += 1
    
    # mescla os dois arrays restantes (usando merge de 2 partes)
    while i < len(parte1) and j < len(parte2):
        if parte1[i] <= parte2[j]:
            resultado.append(parte1[i])
            i += 1
        else:
            resultado.append(parte2[j])
            j += 1
    
    while i < len(parte1) and k < len(parte3):
        if parte1[i] <= parte3[k]:
            resultado.append(parte1[i])
            i += 1
        else:
            resultado.append(parte3[k])
            k += 1
    
    while j < len(parte2) and k < len(parte3):
        if parte2[j] <= parte3[k]:
            resultado.append(parte2[j])
            j += 1
        else:
            resultado.append(parte3[k])
            k += 1
    
    # adiciona elementos restantes
    resultado.extend(parte1[i:])
    resultado.extend(parte2[j:])
    resultado.extend(parte3[k:])
    
    return resultado


def mergesort_3_partes(arr):
    """
    mergesort modificado - divide em três partes.
    
    complexidade: ainda o(n log n), mas com base 3 no logaritmo
    """
    # caso base
    if len(arr) <= 1:
        return arr
    
    # para arrays pequenos, usar merge de 2 partes
    if len(arr) == 2:
        return sorted(arr)
    
    # divisão: divide em três partes
    tamanho = len(arr)
    terco = tamanho // 3
    
    # garante que nenhuma parte fique vazia
    if terco == 0:
        terco = 1
    
    parte1 = arr[:terco]
    parte2 = arr[terco:2*terco]
    parte3 = arr[2*terco:]
    
    # conquista: ordena recursivamente
    parte1_ordenada = mergesort_3_partes(parte1)
    parte2_ordenada = mergesort_3_partes(parte2)
    parte3_ordenada = mergesort_3_partes(parte3)
    
    # combinação: mescla as três partes ordenadas
    return merge_3_partes(parte1_ordenada, parte2_ordenada, parte3_ordenada)


def testar_mergesort():
    """
    testa ambas as versões do mergesort.
    """
    # casos de teste
    casos = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 3, 1],
        [5, 1, 4, 2, 8, 0, 2],
        [1],
        [],
        [3, 3, 3, 3],
        list(range(10, 0, -1))  # ordem reversa
    ]
    
    print("=" * 70)
    print("teste do mergesort (2 partes - convencional)")
    print("=" * 70)
    
    for i, arr in enumerate(casos, 1):
        print(f"\ncaso {i}:")
        print(f"  original:  {arr}")
        ordenado = mergesort_2_partes(arr.copy())
        print(f"  ordenado:  {ordenado}")
        
        # verifica se está realmente ordenado
        if ordenado == sorted(arr):
            print(f"  status: ok")
        else:
            print(f"  status: erro!")
    
    print("\n\n" + "=" * 70)
    print("teste do mergesort (3 partes)")
    print("=" * 70)
    
    for i, arr in enumerate(casos, 1):
        print(f"\ncaso {i}:")
        print(f"  original:  {arr}")
        ordenado = mergesort_3_partes(arr.copy())
        print(f"  ordenado:  {ordenado}")
        
        # verifica se está realmente ordenado
        if ordenado == sorted(arr):
            print(f"  status: ok")
        else:
            print(f"  status: erro!")


def comparar_versoes():
    """
    compara as duas versões do mergesort.
    """
    print("\n\n" + "=" * 70)
    print("comparação: mergesort 2 partes vs 3 partes")
    print("=" * 70)
    
    print("\nmergesort 2 partes (convencional):")
    print("  - divisão: split(n) = 2 * split(n/2)")
    print("  - profundidade: log₂(n)")
    print("  - merge: o(n) em cada nível")
    print("  - complexidade total: o(n log₂ n)")
    print("  - mais simples e eficiente")
    
    print("\nmergesort 3 partes:")
    print("  - divisão: split(n) = 3 * split(n/3)")
    print("  - profundidade: log₃(n)")
    print("  - merge: o(n) em cada nível (mas mais complexo)")
    print("  - complexidade total: o(n log₃ n)")
    print("  - log₃(n) = log₂(n)/log₂(3) ≈ 0.631 * log₂(n)")
    
    print("\nanálise:")
    print("  - ambos têm complexidade o(n log n)")
    print("  - mergesort 3 partes tem menos níveis de recursão")
    print("  - mas cada merge de 3 partes é mais complexo")
    print("  - na prática, 2 partes é mais eficiente")
    print("  - constantes ocultas no big-o importam!")
    
    import math
    n = 1000
    niveis_2 = math.ceil(math.log2(n))
    niveis_3 = math.ceil(math.log(n, 3))
    
    print(f"\npara n={n}:")
    print(f"  mergesort 2 partes: ~{niveis_2} níveis")
    print(f"  mergesort 3 partes: ~{niveis_3} níveis")


def demonstrar_divisao_conquista():
    """
    demonstra o processo de divisão e conquista do mergesort.
    """
    print("\n\n" + "=" * 70)
    print("mergesort como divisão e conquista")
    print("=" * 70)
    
    print("\n1. divisão:")
    print("   - divide o array ao meio (ou em partes)")
    print("   - continua dividindo até ter arrays de tamanho 1")
    
    print("\n2. conquista:")
    print("   - arrays de tamanho 1 já estão ordenados")
    print("   - este é o caso base")
    
    print("\n3. combinação:")
    print("   - mescla os arrays ordenados")
    print("   - mantém a ordem durante a mesclagem")
    print("   - esta é a parte crucial do mergesort")
    
    print("\nexemplo visual para [38, 27, 43, 3]:")
    print("           [38, 27, 43, 3]")
    print("           /            \\")
    print("      [38, 27]        [43, 3]")
    print("      /     \\         /     \\")
    print("    [38]   [27]     [43]   [3]")
    print("      \\     /         \\     /")
    print("      [27, 38]        [3, 43]")
    print("           \\            /")
    print("           [3, 27, 38, 43]")


if __name__ == "__main__":
    testar_mergesort()
    comparar_versoes()
    demonstrar_divisao_conquista()

