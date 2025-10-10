"""
exercicio 5: formula zn,k com duas variaveis

zn,k = {  n,                                  se k=0
          3,                                  se n=0
          4,                                  se n=1
          5,                                  se n=2
          zn-1,k - 2*zn-2,k-1 + 3*zn-3,k-2,   se n>2 }

refazer as implementacoes (recursiva, com vetor, com variaveis).
"""

def znk_recursivo_memo(n, k, memo=None):
    """
    versao recursiva com memoizacao.
    """
    if memo is None:
        memo = {}
    
    if (n, k) in memo:
        return memo[(n, k)]
    
    # casos base
    if k == 0:
        resultado = n
    elif n == 0:
        resultado = 3
    elif n == 1:
        resultado = 4
    elif n == 2:
        resultado = 5
    else:
        resultado = (znk_recursivo_memo(n-1, k, memo) -
                    2*znk_recursivo_memo(n-2, k-1, memo) +
                    3*znk_recursivo_memo(n-3, k-2, memo))
    
    memo[(n, k)] = resultado
    return resultado


def znk_tabela(n, k):
    """
    versao com tabela (programacao dinamica).
    tabela[i][j] = z(i, j)
    """
    # cria tabela (n+1) x (k+1)
    tabela = [[0] * (k + 1) for _ in range(n + 1)]
    
    # casos base
    # k == 0: z(n, 0) = n
    for i in range(n + 1):
        tabela[i][0] = i
    
    # n == 0, 1, 2 para k > 0
    for j in range(1, k + 1):
        tabela[0][j] = 3
        if n >= 1:
            tabela[1][j] = 4
        if n >= 2:
            tabela[2][j] = 5
    
    # preenche a tabela
    for i in range(3, n + 1):
        for j in range(1, k + 1):
            val1 = tabela[i-1][j]
            val2 = tabela[i-2][j-1] if j >= 1 else 0
            val3 = tabela[i-3][j-2] if j >= 2 else 0
            
            tabela[i][j] = val1 - 2*val2 + 3*val3
    
    return tabela[n][k]


def znk_otimizado(n, k):
    """
    versao otimizada em espaco.
    mantem apenas as ultimas 3 linhas.
    """
    if k == 0:
        return n
    if n == 0:
        return 3
    if n == 1:
        return 4
    if n == 2:
        return 5
    
    # mantem 3 linhas (n-3, n-2, n-1)
    linha_menos_3 = [i for i in range(k + 1)]
    linha_menos_2 = [i for i in range(k + 1)]
    linha_menos_1 = [i for i in range(k + 1)]
    
    # inicializa as tres primeiras linhas
    for j in range(1, k + 1):
        linha_menos_3[j] = 3  # n=0
        linha_menos_2[j] = 4  # n=1
        linha_menos_1[j] = 5  # n=2
    
    # calcula linha por linha
    for i in range(3, n + 1):
        linha_atual = [i]  # k=0 sempre e i
        
        for j in range(1, k + 1):
            val1 = linha_menos_1[j]
            val2 = linha_menos_2[j-1] if j >= 1 else 0
            val3 = linha_menos_3[j-2] if j >= 2 else 0
            
            linha_atual.append(val1 - 2*val2 + 3*val3)
        
        # atualiza linhas
        linha_menos_3 = linha_menos_2
        linha_menos_2 = linha_menos_1
        linha_menos_1 = linha_atual
    
    return linha_menos_1[k]


def visualizar_tabela(n_max, k_max):
    """
    visualiza a tabela z(n,k).
    """
    print(f"tabela z(n,k) para n ate {n_max}, k ate {k_max}:")
    print("=" * 70)
    
    # cria e preenche tabela
    tabela = [[0] * (k_max + 1) for _ in range(n_max + 1)]
    
    for i in range(n_max + 1):
        tabela[i][0] = i
    
    for j in range(1, k_max + 1):
        tabela[0][j] = 3
        if n_max >= 1:
            tabela[1][j] = 4
        if n_max >= 2:
            tabela[2][j] = 5
    
    for i in range(3, n_max + 1):
        for j in range(1, k_max + 1):
            val1 = tabela[i-1][j]
            val2 = tabela[i-2][j-1] if j >= 1 else 0
            val3 = tabela[i-3][j-2] if j >= 2 else 0
            tabela[i][j] = val1 - 2*val2 + 3*val3
    
    # exibe tabela
    print("\n   k:", end="")
    for j in range(k_max + 1):
        print(f"{j:7d}", end="")
    print("\n n  " + "-" * (8 * (k_max + 1)))
    
    for i in range(n_max + 1):
        print(f"{i:2d} |", end="")
        for j in range(k_max + 1):
            print(f"{tabela[i][j]:7d}", end="")
        print()


def testar_implementacoes():
    """
    testa todas as implementacoes.
    """
    print("=" * 70)
    print("formula z(n,k) da vovo")
    print("=" * 70)
    
    print("\ndefinicao:")
    print("  z(n,k) = {")
    print("    n                                 se k=0")
    print("    3                                 se n=0")
    print("    4                                 se n=1")
    print("    5                                 se n=2")
    print("    z(n-1,k) - 2*z(n-2,k-1) + 3*z(n-3,k-2)  se n>2")
    print("  }")
    
    # testa varios valores
    print("\n\nteste de valores:")
    print("-" * 70)
    print("n  k  | recursivo | tabela | otimizado")
    print("-" * 70)
    
    casos = [
        (0, 0), (1, 0), (2, 0),
        (3, 0), (3, 1), (3, 2),
        (5, 0), (5, 2), (5, 4),
        (10, 5), (10, 8),
        (15, 10)
    ]
    
    for n, k in casos:
        rec = znk_recursivo_memo(n, k)
        tab = znk_tabela(n, k)
        opt = znk_otimizado(n, k)
        
        if rec == tab == opt:
            status = "ok"
        else:
            status = "erro!"
        
        print(f"{n:2d} {k:2d} | {rec:9d} | {tab:9d} | {opt:9d}  {status}")
    
    # visualiza tabela pequena
    print("\n\n")
    visualizar_tabela(8, 6)


def comparar_complexidade():
    """
    compara as implementacoes.
    """
    print("\n\n" + "=" * 70)
    print("analise de complexidade")
    print("=" * 70)
    
    print("\n1. recursivo com memoizacao:")
    print("   - tempo: o(n*k)")
    print("   - espaco: o(n*k) dicionario")
    
    print("\n2. tabela completa:")
    print("   - tempo: o(n*k)")
    print("   - espaco: o(n*k)")
    
    print("\n3. otimizado (3 linhas):")
    print("   - tempo: o(n*k)")
    print("   - espaco: o(k) - apenas 3 linhas")
    print("   - mais eficiente em memoria!")


def calcular_valores_especiais():
    """
    calcula alguns valores especiais pedidos pela vovo.
    """
    print("\n\n" + "=" * 70)
    print("valores especiais para a vovo")
    print("=" * 70)
    
    valores_especiais = [
        (20, 10),
        (30, 15),
        (40, 20),
        (50, 25)
    ]
    
    print("\nvalores z(n,k):")
    print("-" * 50)
    print("n   k   | z(n,k)")
    print("-" * 50)
    
    for n, k in valores_especiais:
        resultado = znk_otimizado(n, k)
        print(f"{n:3d} {k:3d} | {resultado:15d}")


if __name__ == "__main__":
    testar_implementacoes()
    comparar_complexidade()
    calcular_valores_especiais()

