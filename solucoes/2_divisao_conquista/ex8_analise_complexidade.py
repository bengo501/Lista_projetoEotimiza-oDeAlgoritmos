"""
exercício 11: análise de complexidade de algoritmos

suponha que você esteja escolhendo entre os seguintes três algoritmos:
(a) algoritmo a resolve problemas dividindo-os em cinco subproblemas de metade
    do tamanho, resolvendo recursivamente cada subproblema e, em seguida,
    combinando as soluções em tempo linear.
(b) algoritmo b resolve problemas de tamanho n resolvendo recursivamente dois
    subproblemas de tamanho n-1 e depois combinando as soluções em tempo constante.
(c) algoritmo c resolve problemas de tamanho n dividindo-os em nove subproblemas
    de tamanho n/3, resolvendo recursivamente cada subproblema e, em seguida,
    combinando as soluções em tempo linear.
"""

def analisar_algoritmo_a():
    """
    algoritmo a: t(n) = 5*t(n/2) + o(n)
    """
    print("=" * 70)
    print("algoritmo a")
    print("=" * 70)
    
    print("\nrecorrencia: t(n) = 5*t(n/2) + o(n)")
    print("\nusando teorema mestre:")
    print("  forma: t(n) = a*t(n/b) + f(n)")
    print("  onde: a = 5, b = 2, f(n) = o(n)")
    
    import math
    log_b_a = math.log2(5)
    
    print(f"\n  log_b(a) = log_2(5) ≈ {log_b_a:.3f}")
    print(f"  f(n) = o(n) = o(n^1)")
    print(f"  comparando: n^{log_b_a:.3f} vs n^1")
    print(f"  como log_2(5) > 1, temos caso 1 do teorema mestre")
    
    print(f"\ncomplexidade: o(n^log_2(5)) ≈ o(n^{log_b_a:.3f}) ≈ o(n^2.32)")
    
    return log_b_a


def analisar_algoritmo_b():
    """
    algoritmo b: t(n) = 2*t(n-1) + o(1)
    """
    print("\n\n" + "=" * 70)
    print("algoritmo b")
    print("=" * 70)
    
    print("\nrecorrencia: t(n) = 2*t(n-1) + o(1)")
    print("\nexpandindo a recorrencia:")
    print("  t(n) = 2*t(n-1)")
    print("  t(n) = 2*(2*t(n-2)) = 4*t(n-2)")
    print("  t(n) = 2*(2*(2*t(n-3))) = 8*t(n-3)")
    print("  t(n) = 2^k * t(n-k)")
    print("\nquando n-k = 1, k = n-1")
    print("  t(n) = 2^(n-1) * t(1) = 2^(n-1) * c")
    
    print("\ncomplexidade: o(2^n) - exponencial!")
    print("\neste e o pior! muito ineficiente.")
    
    return float('inf')  # representando exponencial


def analisar_algoritmo_c():
    """
    algoritmo c: t(n) = 9*t(n/3) + o(n)
    """
    print("\n\n" + "=" * 70)
    print("algoritmo c")
    print("=" * 70)
    
    print("\nrecorrencia: t(n) = 9*t(n/3) + o(n)")
    print("\nusando teorema mestre:")
    print("  forma: t(n) = a*t(n/b) + f(n)")
    print("  onde: a = 9, b = 3, f(n) = o(n)")
    
    import math
    log_b_a = math.log(9, 3)
    
    print(f"\n  log_b(a) = log_3(9) = {log_b_a:.3f}")
    print(f"  f(n) = o(n) = o(n^1)")
    print(f"  comparando: n^{log_b_a:.3f} vs n^1")
    print(f"  como log_3(9) = 2, temos n^2 > n")
    print(f"  caso 1 do teorema mestre")
    
    print(f"\ncomplexidade: o(n^log_3(9)) = o(n^2)")
    
    return log_b_a


def comparar_algoritmos():
    """
    compara os três algoritmos.
    """
    print("\n\n" + "=" * 70)
    print("comparacao dos algoritmos")
    print("=" * 70)
    
    print("\nresumo:")
    print("  algoritmo a: o(n^2.32)")
    print("  algoritmo b: o(2^n) - exponencial")
    print("  algoritmo c: o(n^2)")
    
    print("\nordenando por eficiencia (melhor para pior):")
    print("  1. algoritmo c: o(n^2)")
    print("  2. algoritmo a: o(n^2.32)")
    print("  3. algoritmo b: o(2^n)")
    
    print("\nrecomendacao: escolher algoritmo c")
    print("  - tem a menor complexidade")
    print("  - polinomial quadratico")
    print("  - muito melhor que o exponencial do b")
    
    # tabela de comparacao
    print("\n\ntabela de tempo para diferentes valores de n:")
    print("-" * 70)
    print("n     | algoritmo c | algoritmo a | algoritmo b")
    print("      | o(n^2)      | o(n^2.32)   | o(2^n)")
    print("-" * 70)
    
    import math
    for n in [10, 20, 50, 100, 1000]:
        c_time = n ** 2
        a_time = n ** 2.32
        b_time = 2 ** min(n, 30)  # limita para nao explodir
        
        if n <= 30:
            print(f"{n:5d} | {c_time:11.0f} | {a_time:11.0f} | {b_time:11.0f}")
        else:
            print(f"{n:5d} | {c_time:11.0f} | {a_time:11.0f} | >10^9")


def teorema_mestre():
    """
    explica o teorema mestre.
    """
    print("\n\n" + "=" * 70)
    print("teorema mestre para analise de recorrencias")
    print("=" * 70)
    
    print("\npara recorrencias da forma: t(n) = a*t(n/b) + f(n)")
    print("onde a >= 1, b > 1, e f(n) e assintotica positiva")
    
    print("\ncasos:")
    print("  caso 1: se f(n) = o(n^c) onde c < log_b(a)")
    print("          entao t(n) = theta(n^log_b(a))")
    
    print("\n  caso 2: se f(n) = theta(n^c) onde c = log_b(a)")
    print("          entao t(n) = theta(n^c * log n)")
    
    print("\n  caso 3: se f(n) = omega(n^c) onde c > log_b(a)")
    print("          e a*f(n/b) <= k*f(n) para algum k < 1")
    print("          entao t(n) = theta(f(n))")
    
    print("\nexemplos classicos:")
    print("  - merge sort: t(n) = 2*t(n/2) + o(n)")
    print("    a=2, b=2, log_2(2)=1, f(n)=o(n)")
    print("    caso 2: t(n) = o(n log n)")
    
    print("\n  - binary search: t(n) = t(n/2) + o(1)")
    print("    a=1, b=2, log_2(1)=0, f(n)=o(1)")
    print("    caso 2: t(n) = o(log n)")
    
    print("\n  - algoritmo ineficiente: t(n) = 4*t(n/2) + o(n)")
    print("    a=4, b=2, log_2(4)=2, f(n)=o(n)")
    print("    caso 1: t(n) = o(n^2)")


if __name__ == "__main__":
    analisar_algoritmo_a()
    analisar_algoritmo_b()
    analisar_algoritmo_c()
    comparar_algoritmos()
    teorema_mestre()

