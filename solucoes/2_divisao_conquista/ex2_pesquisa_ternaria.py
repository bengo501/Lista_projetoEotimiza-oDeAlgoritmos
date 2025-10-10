"""
exercício 3: pesquisa ternária

modificação da pesquisa binária para dividir em três partes
ao invés de duas.
"""

def pesquisa_ternaria(arr, alvo, inicio=None, fim=None, nivel=0):
    """
    implementa pesquisa ternária recursiva.
    divide o array em três partes ao invés de duas.
    
    args:
        arr: vetor ordenado de inteiros
        alvo: elemento a ser encontrado
        inicio: índice inicial
        fim: índice final
        nivel: nível de recursão (para visualização)
    
    returns:
        índice do elemento se encontrado, -1 caso contrário
    """
    if inicio is None:
        inicio = 0
    if fim is None:
        fim = len(arr) - 1
    
    # caso base: não encontrado
    if inicio > fim:
        return -1
    
    # divide em três partes
    tamanho = fim - inicio + 1
    meio1 = inicio + tamanho // 3
    meio2 = inicio + 2 * tamanho // 3
    
    # visualização do processo
    indent = "  " * nivel
    print(f"{indent}buscando {alvo} em [{inicio}..{fim}]")
    print(f"{indent}  meio1={meio1} (valor={arr[meio1]}), meio2={meio2} (valor={arr[meio2]})")
    
    # verifica se encontrou em um dos pontos de divisão
    if arr[meio1] == alvo:
        print(f"{indent}encontrado na posição {meio1}!")
        return meio1
    if arr[meio2] == alvo:
        print(f"{indent}encontrado na posição {meio2}!")
        return meio2
    
    # busca recursiva no terço apropriado
    if alvo < arr[meio1]:
        print(f"{indent}{alvo} < {arr[meio1]}, buscar no primeiro terço")
        return pesquisa_ternaria(arr, alvo, inicio, meio1 - 1, nivel + 1)
    elif alvo < arr[meio2]:
        print(f"{indent}{arr[meio1]} < {alvo} < {arr[meio2]}, buscar no segundo terço")
        return pesquisa_ternaria(arr, alvo, meio1 + 1, meio2 - 1, nivel + 1)
    else:
        print(f"{indent}{alvo} > {arr[meio2]}, buscar no terceiro terço")
        return pesquisa_ternaria(arr, alvo, meio2 + 1, fim, nivel + 1)


def pesquisa_ternaria_iterativa(arr, alvo):
    """
    versão iterativa da pesquisa ternária.
    """
    inicio = 0
    fim = len(arr) - 1
    
    while inicio <= fim:
        tamanho = fim - inicio + 1
        meio1 = inicio + tamanho // 3
        meio2 = inicio + 2 * tamanho // 3
        
        if arr[meio1] == alvo:
            return meio1
        if arr[meio2] == alvo:
            return meio2
        
        if alvo < arr[meio1]:
            fim = meio1 - 1
        elif alvo < arr[meio2]:
            inicio = meio1 + 1
            fim = meio2 - 1
        else:
            inicio = meio2 + 1
    
    return -1


def testar_pesquisa_ternaria():
    """
    testa pesquisa ternária com o mesmo vetor [0,1,2,...,19]
    """
    vetor = list(range(20))
    
    print("=" * 70)
    print("teste da pesquisa ternária")
    print("=" * 70)
    print(f"vetor: {vetor}\n")
    
    # testa cada elemento
    print("testando todos os elementos:")
    print("-" * 70)
    
    todos_corretos = True
    
    for elemento in vetor:
        indice = pesquisa_ternaria_iterativa(vetor, elemento)
        
        correto = (indice == elemento)
        status = "ok" if correto else "erro!"
        
        if not correto:
            todos_corretos = False
        
        print(f"buscando {elemento:2d}: encontrado no índice {indice:2d} - {status}")
    
    print("-" * 70)
    if todos_corretos:
        print("todos os 20 elementos foram encontrados corretamente!")
    else:
        print("erro: alguns elementos não foram encontrados!")
    
    # demonstração detalhada
    print("\n" + "=" * 70)
    print("demonstração detalhada da busca por 13:")
    print("=" * 70)
    pesquisa_ternaria(vetor, 13)


def comparar_binaria_ternaria():
    """
    compara pesquisa binária e ternária.
    """
    print("\n\n" + "=" * 70)
    print("comparação: pesquisa binária vs ternária")
    print("=" * 70)
    
    print("\npesquisa binária:")
    print("  - divide em 2 partes")
    print("  - 1 comparação por nível")
    print("  - profundidade: log₂(n)")
    print("  - complexidade: o(log₂ n)")
    
    print("\npesquisa ternária:")
    print("  - divide em 3 partes")
    print("  - 2 comparações por nível (verifica meio1 e meio2)")
    print("  - profundidade: log₃(n)")
    print("  - complexidade: o(log₃ n)")
    
    print("\nanálise:")
    print("  - log₃(n) < log₂(n), então menos níveis na ternária")
    print("  - mas cada nível faz 2 comparações ao invés de 1")
    print("  - número total de comparações:")
    print("    binária: ~log₂(n)")
    print("    ternária: ~2*log₃(n) = ~2*log₂(n)/log₂(3) ≈ 1.26*log₂(n)")
    
    print("\nconclusão:")
    print("  - pesquisa binária é mais eficiente!")
    print("  - menos comparações totais")
    print("  - mais simples de implementar")
    print("  - mas pesquisa ternária ilustra bem divisão e conquista")
    
    # teste prático
    import math
    n = 20
    niveis_binaria = math.ceil(math.log2(n))
    niveis_ternaria = math.ceil(math.log(n, 3))
    comp_binaria = niveis_binaria
    comp_ternaria = 2 * niveis_ternaria
    
    print(f"\npara n={n}:")
    print(f"  binária: ~{comp_binaria} comparações")
    print(f"  ternária: ~{comp_ternaria} comparações")


if __name__ == "__main__":
    testar_pesquisa_ternaria()
    comparar_binaria_ternaria()

