"""
exercicio 3: formula zn da vovo

zn = {  3,                       se n=0
        4,                       se n=1
        5,                       se n=2
        zn-1 - 2*zn-2 + 3*zn-3,  se n>2 }

(a) implemente usando recursao e calcule z40
(b) implemente sem recursao, usando um vetor
(c) elimine o vetor e use apenas variaveis
"""

def zn_recursivo(n):
    """
    (a) versao recursiva (muito lenta sem memoizacao).
    """
    if n == 0:
        return 3
    if n == 1:
        return 4
    if n == 2:
        return 5
    
    return zn_recursivo(n-1) - 2*zn_recursivo(n-2) + 3*zn_recursivo(n-3)


def zn_recursivo_memo(n, memo=None):
    """
    versao recursiva com memoizacao (rapida).
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 3
    if n == 1:
        return 4
    if n == 2:
        return 5
    
    memo[n] = zn_recursivo_memo(n-1, memo) - 2*zn_recursivo_memo(n-2, memo) + 3*zn_recursivo_memo(n-3, memo)
    return memo[n]


def zn_vetor(n):
    """
    (b) versao com vetor (bottom-up).
    """
    if n == 0:
        return 3
    if n == 1:
        return 4
    if n == 2:
        return 5
    
    # vetor para armazenar todos os valores
    z = [0] * (n + 1)
    z[0] = 3
    z[1] = 4
    z[2] = 5
    
    for i in range(3, n + 1):
        z[i] = z[i-1] - 2*z[i-2] + 3*z[i-3]
    
    return z[n]


def zn_variaveis(n):
    """
    (c) versao com apenas 3 variaveis (mais eficiente em memoria).
    """
    if n == 0:
        return 3
    if n == 1:
        return 4
    if n == 2:
        return 5
    
    # mantem apenas os 3 ultimos valores
    z_menos_3 = 3
    z_menos_2 = 4
    z_menos_1 = 5
    
    for i in range(3, n + 1):
        z_atual = z_menos_1 - 2*z_menos_2 + 3*z_menos_3
        
        # atualiza para proxima iteracao
        z_menos_3 = z_menos_2
        z_menos_2 = z_menos_1
        z_menos_1 = z_atual
    
    return z_menos_1


def testar_implementacoes():
    """
    testa todas as implementacoes.
    """
    print("=" * 70)
    print("formula zn da vovo")
    print("=" * 70)
    
    print("\ndefinicao:")
    print("  z(0) = 3")
    print("  z(1) = 4")
    print("  z(2) = 5")
    print("  z(n) = z(n-1) - 2*z(n-2) + 3*z(n-3)  para n > 2")
    
    # testa valores pequenos
    print("\n\nprimeiros 15 valores:")
    print("-" * 50)
    print("n  | z(n)")
    print("-" * 50)
    
    for n in range(15):
        valor = zn_variaveis(n)
        print(f"{n:2d} | {valor:10d}")
    
    # calcula z(40)
    print("\n\n" + "=" * 70)
    print("calculando z(40)")
    print("=" * 70)
    
    import time
    
    # recursivo com memoizacao
    inicio = time.time()
    resultado_memo = zn_recursivo_memo(40)
    tempo_memo = time.time() - inicio
    
    # com vetor
    inicio = time.time()
    resultado_vetor = zn_vetor(40)
    tempo_vetor = time.time() - inicio
    
    # com variaveis
    inicio = time.time()
    resultado_variaveis = zn_variaveis(40)
    tempo_variaveis = time.time() - inicio
    
    print(f"\nresultados para z(40):")
    print(f"  recursivo com memo:  {resultado_memo:15d}  tempo: {tempo_memo:.6f}s")
    print(f"  com vetor:           {resultado_vetor:15d}  tempo: {tempo_vetor:.6f}s")
    print(f"  com 3 variaveis:     {resultado_variaveis:15d}  tempo: {tempo_variaveis:.6f}s")
    
    if resultado_memo == resultado_vetor == resultado_variaveis:
        print("\ntodas as implementacoes retornaram o mesmo resultado!")
    else:
        print("\nerro: implementacoes retornaram valores diferentes!")


def comparar_complexidade():
    """
    compara a complexidade das implementacoes.
    """
    print("\n\n" + "=" * 70)
    print("analise de complexidade")
    print("=" * 70)
    
    print("\n1. recursivo puro (sem memoizacao):")
    print("   - tempo: o(3^n) - explosao exponencial")
    print("   - espaco: o(n) - profundidade da recursao")
    print("   - impraticavel para n >= 20")
    
    print("\n2. recursivo com memoizacao:")
    print("   - tempo: o(n) - cada subproblema calculado uma vez")
    print("   - espaco: o(n) - dicionario + pilha de recursao")
    
    print("\n3. bottom-up com vetor:")
    print("   - tempo: o(n)")
    print("   - espaco: o(n) - vetor de tamanho n")
    print("   - sem overhead de recursao")
    
    print("\n4. com 3 variaveis:")
    print("   - tempo: o(n)")
    print("   - espaco: o(1) - apenas 3 variaveis")
    print("   - mais eficiente em memoria!")
    
    print("\nmelhor escolha: variaveis (rapido e economico)")


def demonstrar_recursao():
    """
    demonstra a explosao da recursao pura.
    """
    print("\n\n" + "=" * 70)
    print("demonstracao: recursao pura vs memoizacao")
    print("=" * 70)
    
    import time
    
    print("\nteste para valores pequenos (recursao pura):")
    print("-" * 50)
    print("n  | z(n)       | tempo (s)")
    print("-" * 50)
    
    for n in [5, 10, 15, 18]:
        inicio = time.time()
        resultado = zn_recursivo(n)
        tempo = time.time() - inicio
        
        print(f"{n:2d} | {resultado:10d} | {tempo:.6f}")
        
        if tempo > 1.0:
            print("muito lento! parando aqui...")
            break
    
    print("\nmemoizacao permite calcular valores muito maiores rapidamente!")


if __name__ == "__main__":
    testar_implementacoes()
    comparar_complexidade()
    demonstrar_recursao()

