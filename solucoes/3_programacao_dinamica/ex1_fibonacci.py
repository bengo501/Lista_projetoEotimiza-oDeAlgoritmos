"""
exercicio 1: calcular fibonacci com memoria o(1)

implementacao de fibonacci com espaco constante.
"""

def fibonacci_o1_memoria(n):
    """
    calcula o n-esimo numero de fibonacci com memoria o(1).
    
    estrategia:
    - manter apenas os dois ultimos valores
    - nao precisa de array ou recursao
    
    complexidade:
    - tempo: o(n)
    - espaco: o(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    # apenas duas variaveis para os ultimos valores
    anterior = 0
    atual = 1
    
    print(f"calculando fibonacci({n}):")
    print(f"f(0) = {anterior}")
    print(f"f(1) = {atual}")
    
    for i in range(2, n + 1):
        proximo = anterior + atual
        anterior = atual
        atual = proximo
        
        if i <= 10 or i == n:
            print(f"f({i}) = {atual}")
        elif i == 11:
            print("...")
    
    return atual


def fibonacci_recursivo_memo(n, memo=None):
    """
    versao recursiva com memoizacao para comparacao.
    memoria o(n) devido ao dicionario.
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    memo[n] = fibonacci_recursivo_memo(n-1, memo) + fibonacci_recursivo_memo(n-2, memo)
    return memo[n]


def fibonacci_matriz(n):
    """
    versao usando multiplicacao de matrizes.
    pode ser otimizada para o(log n) com exponenciacao rapida.
    """
    def multiplicar_matrizes(a, b):
        return [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ]
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    # matriz [[1,1],[1,0]]
    matriz_base = [[1, 1], [1, 0]]
    resultado = [[1, 0], [0, 1]]  # matriz identidade
    
    for _ in range(n - 1):
        resultado = multiplicar_matrizes(resultado, matriz_base)
    
    return resultado[0][0]


def testar_fibonacci():
    """
    testa as implementacoes de fibonacci.
    """
    print("=" * 70)
    print("teste: fibonacci com o(1) de memoria")
    print("=" * 70)
    print()
    
    # testa valores pequenos
    for n in [0, 1, 2, 3, 4, 5, 10, 20]:
        resultado = fibonacci_o1_memoria(n)
        print(f"\nfibonacci({n}) = {resultado}")
        print()
    
    # teste com valor maior
    print("=" * 70)
    print("teste com valor grande:")
    print("=" * 70)
    n = 50
    resultado = fibonacci_o1_memoria(n)
    print(f"\nfibonacci({n}) = {resultado}")


def comparar_versoes():
    """
    compara as diferentes implementacoes.
    """
    print("\n\n" + "=" * 70)
    print("comparacao de implementacoes")
    print("=" * 70)
    
    import time
    
    n = 30
    
    # versao o(1)
    inicio = time.time()
    resultado1 = fibonacci_o1_memoria(n)
    tempo1 = time.time() - inicio
    
    # versao com memoizacao
    inicio = time.time()
    resultado2 = fibonacci_recursivo_memo(n)
    tempo2 = time.time() - inicio
    
    # versao matriz
    inicio = time.time()
    resultado3 = fibonacci_matriz(n)
    tempo3 = time.time() - inicio
    
    print(f"\nfibonacci({n}):")
    print(f"  iterativo o(1): {resultado1} - tempo: {tempo1:.6f}s")
    print(f"  recursivo memo: {resultado2} - tempo: {tempo2:.6f}s")
    print(f"  matriz:         {resultado3} - tempo: {tempo3:.6f}s")
    
    print("\nanalise de complexidade:")
    print("  iterativo o(1):")
    print("    - tempo: o(n)")
    print("    - espaco: o(1) - apenas 2 variaveis")
    print("    - mais eficiente em espaco!")
    
    print("\n  recursivo com memoizacao:")
    print("    - tempo: o(n)")
    print("    - espaco: o(n) - dicionario de memoizacao")
    
    print("\n  matriz (com exponenciacao rapida):")
    print("    - tempo: o(log n) - se usar exponenciacao rapida")
    print("    - espaco: o(1)")
    print("    - mais rapido para valores muito grandes!")


def sequencia_fibonacci():
    """
    mostra a sequencia de fibonacci.
    """
    print("\n\n" + "=" * 70)
    print("sequencia de fibonacci")
    print("=" * 70)
    
    print("\ndefinicao:")
    print("  f(0) = 0")
    print("  f(1) = 1")
    print("  f(n) = f(n-1) + f(n-2) para n >= 2")
    
    print("\nprimeiros 20 numeros:")
    for i in range(20):
        print(f"  f({i:2d}) = {fibonacci_o1_memoria(i)}")
    
    print("\npropriedades interessantes:")
    print("  - razao aurea: lim(f(n+1)/f(n)) = phi = (1+sqrt(5))/2")
    print("  - formula de binet: f(n) = (phi^n - psi^n)/sqrt(5)")
    print("  - aparece na natureza: espirais, plantas, conchas")


def razao_aurea():
    """
    demonstra a convergencia para a razao aurea.
    """
    print("\n\n" + "=" * 70)
    print("convergencia para a razao aurea")
    print("=" * 70)
    
    import math
    phi = (1 + math.sqrt(5)) / 2
    
    print(f"\nrazao aurea (phi) = {phi:.10f}")
    print("\nrazao entre termos consecutivos:")
    print("-" * 50)
    
    anterior = fibonacci_o1_memoria(1)
    for i in range(2, 21):
        atual = fibonacci_o1_memoria(i)
        razao = atual / anterior if anterior != 0 else 0
        diferenca = abs(razao - phi)
        print(f"  f({i:2d})/f({i-1:2d}) = {razao:.10f}  (erro: {diferenca:.10f})")
        anterior = atual
    
    print("\na razao converge para phi!")


if __name__ == "__main__":
    testar_fibonacci()
    comparar_versoes()
    sequencia_fibonacci()
    razao_aurea()

