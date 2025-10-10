"""
exercicio 4: funcao coisa(n,k) nao recursiva

int coisa(int n, int k) {
    if (k == n) return n;
    if (k == 0) return 1;
    return coisa(n-1, k-1) - 3 * coisa(n-1, k);
}

sabe-se que k <= n sempre.
fazer uma versao nao recursiva usando uma tabela auxiliar.
"""

def coisa_recursivo(n, k):
    """
    versao recursiva original.
    """
    if k == n:
        return n
    if k == 0:
        return 1
    return coisa_recursivo(n-1, k-1) - 3 * coisa_recursivo(n-1, k)


def coisa_tabela(n, k):
    """
    versao com tabela (programacao dinamica).
    
    tabela[i][j] = coisa(i, j)
    """
    # cria tabela (n+1) x (k+1)
    tabela = [[0] * (k + 1) for _ in range(n + 1)]
    
    # casos base
    # k == 0: sempre retorna 1
    for i in range(n + 1):
        tabela[i][0] = 1
    
    # k == n: retorna n
    for i in range(min(n, k) + 1):
        if i <= n and i <= k:
            tabela[i][i] = i
    
    # preenche a tabela
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if i == j:
                tabela[i][j] = i
            elif j == 0:
                tabela[i][j] = 1
            else:
                tabela[i][j] = tabela[i-1][j-1] - 3 * tabela[i-1][j]
    
    return tabela[n][k]


def visualizar_tabela(n, k):
    """
    visualiza a tabela de programacao dinamica.
    """
    print(f"tabela coisa(n, k) para n={n}, k={k}:")
    print("=" * 70)
    
    # cria e preenche a tabela
    tabela = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        tabela[i][0] = 1
    
    for i in range(min(n, k) + 1):
        if i <= n and i <= k:
            tabela[i][i] = i
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if i == j:
                tabela[i][j] = i
            elif j == 0:
                tabela[i][j] = 1
            else:
                tabela[i][j] = tabela[i-1][j-1] - 3 * tabela[i-1][j]
    
    # exibe tabela
    print("\n   k:", end="")
    for j in range(k + 1):
        print(f"{j:8d}", end="")
    print("\n n  " + "-" * (9 * (k + 1)))
    
    for i in range(n + 1):
        print(f"{i:2d} |", end="")
        for j in range(k + 1):
            if j <= i:
                print(f"{tabela[i][j]:8d}", end="")
            else:
                print(f"{'---':>8s}", end="")
        print()


def testar_funcao():
    """
    testa a funcao com varios valores.
    """
    print("=" * 70)
    print("funcao coisa(n, k)")
    print("=" * 70)
    
    print("\ndefinicao:")
    print("  coisa(n, k) = {")
    print("    n                          se k == n")
    print("    1                          se k == 0")
    print("    coisa(n-1, k-1) - 3*coisa(n-1, k)  caso contrario")
    print("  }")
    
    # teste com valores pequenos
    print("\n\nteste de alguns valores:")
    print("-" * 50)
    print("n  k  | recursivo | tabela")
    print("-" * 50)
    
    casos = [
        (0, 0), (1, 0), (1, 1),
        (2, 0), (2, 1), (2, 2),
        (3, 0), (3, 1), (3, 2), (3, 3),
        (5, 2), (5, 3),
        (10, 5)
    ]
    
    for n, k in casos:
        rec = coisa_recursivo(n, k)
        tab = coisa_tabela(n, k)
        status = "ok" if rec == tab else "erro!"
        print(f"{n:2d} {k:2d} | {rec:9d} | {tab:9d}  {status}")
    
    # visualiza tabela
    print("\n\n")
    visualizar_tabela(6, 6)


def comparar_desempenho():
    """
    compara recursivo vs tabela.
    """
    print("\n\n" + "=" * 70)
    print("comparacao de desempenho")
    print("=" * 70)
    
    import time
    
    n, k = 10, 5
    
    print(f"\ncoisa({n}, {k}):")
    
    # tabela
    inicio = time.time()
    resultado_tab = coisa_tabela(n, k)
    tempo_tab = time.time() - inicio
    
    print(f"  tabela:    {resultado_tab:15d}  tempo: {tempo_tab:.6f}s")
    
    print("\nanalise de complexidade:")
    print("  recursivo puro:")
    print("    - tempo: exponencial (muitos calculos repetidos)")
    print("    - espaco: o(n) pilha de recursao")
    
    print("\n  com tabela:")
    print("    - tempo: o(n*k)")
    print("    - espaco: o(n*k)")
    print("    - muito mais rapido!")


def explicar_dp():
    """
    explica a abordagem de programacao dinamica.
    """
    print("\n\n" + "=" * 70)
    print("programacao dinamica")
    print("=" * 70)
    
    print("\nabordagem:")
    print("  1. identificar dependencias:")
    print("     coisa(n,k) depende de coisa(n-1, k-1) e coisa(n-1, k)")
    
    print("\n  2. ordem de preenchimento:")
    print("     linha por linha (n crescente)")
    print("     cada linha depende apenas da anterior")
    
    print("\n  3. otimizacao possivel:")
    print("     manter apenas duas linhas (atual e anterior)")
    print("     reduzir espaco de o(n*k) para o(k)")
    
    print("\nexemplo de dependencias:")
    print("  coisa(3,2) depende de:")
    print("    coisa(2,1) e coisa(2,2)")
    print("  coisa(2,1) depende de:")
    print("    coisa(1,0) e coisa(1,1)")
    print("  ...")
    print("  ate chegar nos casos base")


if __name__ == "__main__":
    testar_funcao()
    comparar_desempenho()
    explicar_dp()

