"""
exercicio 2: problema das calcadas coloridas

voce pode construir uma calcada da sua casa ate a casa da vovo usando
pedras verdes, azuis e amarelas. as pedras sao quadradas, tem 1m x 1m,
e a casa da vovo fica a 50 metros de distancia.

perguntas:
(a) quantas calcadas com coloridos diferentes sao possiveis?
(b) quantas sao possiveis se a vovo nao quer duas pedras amarelas lado a lado?
(c) ... e se a vovo tambem nao deixa que duas pedras azuis fiquem lado a lado?
"""

def calcadas_simples(n):
    """
    (a) quantas calcadas diferentes sao possiveis com 3 cores?
    
    sem restricoes: cada posicao pode ter 3 cores
    resposta: 3^n
    """
    return 3 ** n


def calcadas_sem_amarelas_consecutivas_recursivo(n, memo=None):
    """
    (b) calcadas sem duas pedras amarelas consecutivas.
    
    usando memoizacao (programacao dinamica top-down).
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    # caso base
    if n == 0:
        return 1
    if n == 1:
        return 3  # verde, azul ou amarela
    
    # ultima pedra verde ou azul: pode colocar qualquer cor depois
    # ultima pedra amarela: nao pode colocar amarela depois
    
    # verde ou azul na posicao n: 2 * f(n-1)
    # amarela na posicao n: apenas se a anterior nao for amarela
    #   = todas as combinacoes de n-1 pedras - as que terminam em amarelo
    #   = f(n-1) - (amarelas em n-1)
    #   = f(n-1) - [f(n-2) se n >= 2]
    
    # melhor abordagem: contar por cor da ultima pedra
    # f(n) = (verde ou azul) + (amarela possivel)
    # f(n) = 2 * f(n-1) + 1 * (f(n-2) * 2)  [se anterior nao for amarela]
    
    # formula: f(n) = 2*f(n-1) + 2*f(n-2)
    memo[n] = 2 * calcadas_sem_amarelas_consecutivas_recursivo(n-1, memo) + \
              2 * calcadas_sem_amarelas_consecutivas_recursivo(n-2, memo) if n >= 2 else 3
    
    return memo[n]


def calcadas_sem_amarelas_consecutivas(n):
    """
    versao bottom-up (mais eficiente).
    """
    if n == 0:
        return 1
    if n == 1:
        return 3
    
    # dp[i][cor] = numero de calcadas de tamanho i terminando na cor
    # cor: 0=verde, 1=azul, 2=amarela
    
    dp = [[0] * 3 for _ in range(n + 1)]
    
    # caso base: 1 pedra
    dp[1][0] = 1  # verde
    dp[1][1] = 1  # azul
    dp[1][2] = 1  # amarela
    
    # preenche a tabela
    for i in range(2, n + 1):
        # verde: pode vir depois de qualquer cor
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        
        # azul: pode vir depois de qualquer cor
        dp[i][1] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        
        # amarela: pode vir depois de verde ou azul (nao amarela)
        dp[i][2] = dp[i-1][0] + dp[i-1][1]
    
    return dp[n][0] + dp[n][1] + dp[n][2]


def calcadas_sem_amarelas_nem_azuis_consecutivas(n):
    """
    (c) sem amarelas consecutivas e sem azuis consecutivas.
    """
    if n == 0:
        return 1
    if n == 1:
        return 3
    
    # dp[i][cor] = numero de calcadas de tamanho i terminando na cor
    # cor: 0=verde, 1=azul, 2=amarela
    
    dp = [[0] * 3 for _ in range(n + 1)]
    
    # caso base
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 1
    
    for i in range(2, n + 1):
        # verde: pode vir depois de qualquer cor
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        
        # azul: pode vir depois de verde ou amarela (nao azul)
        dp[i][1] = dp[i-1][0] + dp[i-1][2]
        
        # amarela: pode vir depois de verde ou azul (nao amarela)
        dp[i][2] = dp[i-1][0] + dp[i-1][1]
    
    return dp[n][0] + dp[n][1] + dp[n][2]


def resolver_problema():
    """
    resolve o problema completo.
    """
    n = 50
    
    print("=" * 70)
    print("problema das calcadas coloridas")
    print("=" * 70)
    
    print(f"\ndistancia ate a casa da vovo: {n} metros")
    print("cores disponiveis: verde, azul, amarela")
    
    # parte (a)
    resultado_a = calcadas_simples(n)
    print(f"\n(a) sem restricoes:")
    print(f"    total de calcadas possiveis: {resultado_a}")
    print(f"    formula: 3^{n}")
    
    # parte (b)
    resultado_b = calcadas_sem_amarelas_consecutivas(n)
    print(f"\n(b) sem duas amarelas consecutivas:")
    print(f"    total de calcadas possiveis: {resultado_b}")
    
    # parte (c)
    resultado_c = calcadas_sem_amarelas_nem_azuis_consecutivas(n)
    print(f"\n(c) sem duas amarelas e sem duas azuis consecutivas:")
    print(f"    total de calcadas possiveis: {resultado_c}")
    
    print("\n" + "=" * 70)
    print("comparacao:")
    print("=" * 70)
    print(f"  sem restricoes:                     {resultado_a:.2e}")
    print(f"  sem amarelas consecutivas:          {resultado_b:.2e}")
    print(f"  sem amarelas nem azuis consecutivas: {resultado_c:.2e}")


def demonstrar_casos_pequenos():
    """
    demonstra para valores pequenos de n.
    """
    print("\n\n" + "=" * 70)
    print("demonstracao para valores pequenos")
    print("=" * 70)
    
    print("\n" + "-" * 70)
    print("n  | sem restr. | sem amarelas | sem amarelas e azuis")
    print("-" * 70)
    
    for n in range(1, 11):
        a = calcadas_simples(n)
        b = calcadas_sem_amarelas_consecutivas(n)
        c = calcadas_sem_amarelas_nem_azuis_consecutivas(n)
        print(f"{n:2d} | {a:10d} | {b:12d} | {c:20d}")


def explicar_programacao_dinamica():
    """
    explica a abordagem de programacao dinamica.
    """
    print("\n\n" + "=" * 70)
    print("programacao dinamica")
    print("=" * 70)
    
    print("\nabordagem:")
    print("  1. definir estado: dp[i][cor] = calcadas de tamanho i terminando em cor")
    print("  2. caso base: dp[1][*] = 1 (uma pedra de cada cor)")
    print("  3. transicao: dp[i][cor] = soma de dp[i-1][cores validas]")
    
    print("\nrestriçoes afetam as transicoes:")
    print("  - sem amarelas consecutivas: dp[i][amarela] += apenas dp[i-1][verde/azul]")
    print("  - sem azuis consecutivas: dp[i][azul] += apenas dp[i-1][verde/amarela]")
    
    print("\ncomplexidade:")
    print("  - tempo: o(n * cores) = o(n)")
    print("  - espaco: o(n * cores) = o(n)")
    print("  - pode ser reduzido a o(1) mantendo apenas linha anterior")


if __name__ == "__main__":
    resolver_problema()
    demonstrar_casos_pequenos()
    explicar_programacao_dinamica()

