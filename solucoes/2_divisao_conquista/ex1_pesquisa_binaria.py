"""
exercício 1 e 2: pesquisa binária

implementação de pesquisa binária sobre um vetor de inteiros
e testes com vetor [0,1,2,...,19]
"""

def pesquisa_binaria(arr, alvo, inicio=None, fim=None, nivel=0):
    """
    implementa pesquisa binária recursiva.
    
    args:
        arr: vetor ordenado de inteiros
        alvo: elemento a ser encontrado
        inicio: índice inicial (None usa 0)
        fim: índice final (None usa len(arr)-1)
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
    
    # calcula o meio
    meio = (inicio + fim) // 2
    
    # visualização do processo
    indent = "  " * nivel
    print(f"{indent}buscando {alvo} em [{inicio}..{fim}], meio={meio} (valor={arr[meio]})")
    
    # caso base: encontrado
    if arr[meio] == alvo:
        print(f"{indent}encontrado na posição {meio}!")
        return meio
    
    # busca recursiva
    if alvo < arr[meio]:
        print(f"{indent}{alvo} < {arr[meio]}, buscar à esquerda")
        return pesquisa_binaria(arr, alvo, inicio, meio - 1, nivel + 1)
    else:
        print(f"{indent}{alvo} > {arr[meio]}, buscar à direita")
        return pesquisa_binaria(arr, alvo, meio + 1, fim, nivel + 1)


def pesquisa_binaria_iterativa(arr, alvo):
    """
    versão iterativa da pesquisa binária (mais eficiente em python).
    """
    inicio = 0
    fim = len(arr) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if arr[meio] == alvo:
            return meio
        elif alvo < arr[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    
    return -1


def testar_pesquisa_binaria():
    """
    testa pesquisa binária com vetor [0,1,2,...,19]
    procurando cada um dos 20 elementos.
    """
    # cria vetor [0,1,2,...,19]
    vetor = list(range(20))
    
    print("=" * 70)
    print("teste da pesquisa binária")
    print("=" * 70)
    print(f"vetor: {vetor}\n")
    
    # testa cada elemento
    print("testando todos os elementos:")
    print("-" * 70)
    
    todos_corretos = True
    
    for elemento in vetor:
        # usa versão iterativa para os testes (mais limpo)
        indice = pesquisa_binaria_iterativa(vetor, elemento)
        
        correto = (indice == elemento)  # índice deve ser igual ao valor
        status = "ok" if correto else "erro!"
        
        if not correto:
            todos_corretos = False
        
        print(f"buscando {elemento:2d}: encontrado no índice {indice:2d} - {status}")
    
    print("-" * 70)
    if todos_corretos:
        print("todos os 20 elementos foram encontrados corretamente!")
    else:
        print("erro: alguns elementos não foram encontrados!")
    
    # testa busca de elemento inexistente
    print("\n" + "=" * 70)
    print("testando elementos inexistentes:")
    print("=" * 70)
    
    inexistentes = [-1, 20, 25, 100]
    for elemento in inexistentes:
        indice = pesquisa_binaria_iterativa(vetor, elemento)
        print(f"buscando {elemento:3d}: índice {indice:2d} (não encontrado, como esperado)")
    
    # demonstração detalhada com um elemento
    print("\n" + "=" * 70)
    print("demonstração detalhada da busca por 13:")
    print("=" * 70)
    pesquisa_binaria(vetor, 13)
    
    # análise de complexidade
    print("\n" + "=" * 70)
    print("análise de complexidade:")
    print("=" * 70)
    print("pesquisa binária:")
    print("  - complexidade de tempo: o(log n)")
    print("  - complexidade de espaço: o(1) iterativa, o(log n) recursiva")
    print(f"  - para n=20: máximo de {len(vetor).bit_length()} comparações")
    print("\ncomparação com busca linear:")
    print("  - busca linear: o(n) - até 20 comparações")
    print("  - busca binária: o(log n) - até ~5 comparações")
    print("  - ganho: ~4x mais rápida para n=20")


def demonstrar_divisao_conquista():
    """
    explica por que pesquisa binária é divisão e conquista.
    """
    print("\n\n" + "=" * 70)
    print("por que pesquisa binária é divisão e conquista?")
    print("=" * 70)
    
    print("\n1. divisão:")
    print("   - divide o problema em subproblemas menores")
    print("   - a cada passo, divide o vetor ao meio")
    
    print("\n2. conquista:")
    print("   - resolve o subproblema recursivamente")
    print("   - busca apenas na metade relevante")
    
    print("\n3. combinação:")
    print("   - neste caso, não há fase de combinação")
    print("   - o resultado vem diretamente do subproblema")
    
    print("\n4. redução do problema:")
    print("   - a cada chamada recursiva, o tamanho é reduzido pela metade")
    print("   - n -> n/2 -> n/4 -> n/8 -> ... -> 1")
    print("   - número de passos: log₂(n)")


if __name__ == "__main__":
    testar_pesquisa_binaria()
    demonstrar_divisao_conquista()

