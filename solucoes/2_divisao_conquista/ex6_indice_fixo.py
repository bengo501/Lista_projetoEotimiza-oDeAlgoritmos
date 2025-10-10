"""
exercício 9: encontrar índice fixo a[i]=i

dado um array ordenado de inteiros diferentes a[0..n],
determinar se existe um índice i tal que a[i]=i.

solução em o(log n) usando divisão e conquista.
"""

def encontrar_indice_fixo(arr, inicio=0, fim=None):
    """
    encontra um índice i tal que a[i] = i usando busca binária.
    
    estratégia:
    - se a[meio] == meio, encontramos!
    - se a[meio] > meio, buscar à esquerda (valores muito grandes)
    - se a[meio] < meio, buscar à direita (valores muito pequenos)
    
    complexidade: o(log n)
    """
    if fim is None:
        fim = len(arr) - 1
    
    # caso base: não encontrado
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2
    
    print(f"  verificando índice {meio}: a[{meio}] = {arr[meio]}")
    
    # encontrou!
    if arr[meio] == meio:
        return meio
    
    # valor muito grande, buscar à esquerda
    if arr[meio] > meio:
        print(f"    a[{meio}] = {arr[meio]} > {meio}, buscar à esquerda")
        return encontrar_indice_fixo(arr, inicio, meio - 1)
    # valor muito pequeno, buscar à direita
    else:
        print(f"    a[{meio}] = {arr[meio]} < {meio}, buscar à direita")
        return encontrar_indice_fixo(arr, meio + 1, fim)


def testar_algoritmo():
    """
    testa o algoritmo com vários casos.
    """
    casos = [
        ([-10, -5, 0, 3, 7], "há índice fixo em 3"),
        ([-10, -5, 2, 3, 7], "há índice fixo em 2 ou 3"),
        ([0, 1, 2, 3, 4], "todos são índices fixos"),
        ([-5, -3, -1, 1, 3], "sem índice fixo"),
        ([10, 20, 30, 40, 50], "sem índice fixo"),
        ([-1, 0, 1, 2, 9], "sem índice fixo")
    ]
    
    print("=" * 70)
    print("teste: encontrar índice fixo a[i]=i")
    print("=" * 70)
    
    for arr, descricao in casos:
        print(f"\narray: {arr}")
        print(f"descrição: {descricao}")
        print("busca:")
        
        resultado = encontrar_indice_fixo(arr)
        
        if resultado != -1:
            print(f"\nencontrado: a[{resultado}] = {arr[resultado]}")
            # verifica
            if arr[resultado] == resultado:
                print("verificação: correto!")
            else:
                print("verificação: erro!")
        else:
            print("\nnão encontrado")
            # verifica se realmente não existe
            existe = any(arr[i] == i for i in range(len(arr)))
            if not existe:
                print("verificação: correto (não existe mesmo)")
            else:
                print("verificação: erro (existe mas não foi encontrado)!")
        
        print("-" * 70)


def encontrar_todos_indices_fixos(arr):
    """
    versão que encontra todos os índices fixos (não apenas um).
    ainda usa divisão e conquista mas busca em ambos os lados.
    """
    def buscar(inicio, fim):
        if inicio > fim:
            return []
        
        meio = (inicio + fim) // 2
        
        resultados = []
        
        # se encontrou, adiciona
        if arr[meio] == meio:
            resultados.append(meio)
        
        # busca à esquerda se possível haver índice fixo lá
        if meio > 0 and arr[meio - 1] >= inicio:
            resultados.extend(buscar(inicio, meio - 1))
        
        # busca à direita se possível haver índice fixo lá
        if meio < len(arr) - 1 and arr[meio + 1] <= fim:
            resultados.extend(buscar(meio + 1, fim))
        
        return resultados
    
    return sorted(set(buscar(0, len(arr) - 1)))


def demonstrar_divisao_conquista():
    """
    demonstra o raciocínio de divisão e conquista.
    """
    print("\n\n" + "=" * 70)
    print("análise do algoritmo")
    print("=" * 70)
    
    print("\npor que funciona?")
    print("  - array é ordenado e tem elementos diferentes")
    print("  - se a[meio] > meio:")
    print("    todos à direita também têm a[i] > i")
    print("    (porque array é ordenado e diferente)")
    print("  - se a[meio] < meio:")
    print("    todos à esquerda também têm a[i] < i")
    
    print("\nexemplo:")
    print("  array: [-10, -5, 0, 3, 7]")
    print("  índices: 0   1   2  3  4")
    print()
    print("  a[2] = 0 < 2, então a[0] e a[1] também são < seus índices")
    print("  a[3] = 3 = 3, encontrado!")
    
    print("\ncomplexidade:")
    print("  - divisão e conquista clássica")
    print("  - a cada passo, descarta metade do array")
    print("  - t(n) = t(n/2) + o(1)")
    print("  - portanto t(n) = o(log n)")
    
    print("\n\nteste: encontrar todos os índices fixos")
    print("-" * 70)
    
    arr = [-1, 0, 1, 3, 5]
    print(f"array: {arr}")
    todos = encontrar_todos_indices_fixos(arr)
    print(f"todos os índices fixos: {todos}")
    
    # verifica
    for i in todos:
        print(f"  a[{i}] = {arr[i]}")


if __name__ == "__main__":
    testar_algoritmo()
    demonstrar_divisao_conquista()

