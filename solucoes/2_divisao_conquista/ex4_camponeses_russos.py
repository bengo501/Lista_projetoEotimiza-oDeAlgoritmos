"""
exercícios 6 e 7: algoritmo dos camponeses russos

multiplicação de inteiros usando o método dos camponeses russos
(também conhecido como multiplicação egípcia ou multiplicação russa)
"""

def camponeses_russos_base2(a, b):
    """
    algoritmo dos camponeses russos para multiplicação.
    
    método:
    1. divide o primeiro número por 2 (arredonda para baixo)
    2. multiplica o segundo número por 2
    3. soma as linhas onde o primeiro número é ímpar
    
    exemplo: 17 × 23
    17  23  <- ímpar, soma
     8  46
     4  92
     2 184
     1 368  <- ímpar, soma
    resultado: 23 + 368 = 391
    """
    resultado = 0
    
    print(f"calculando {a} × {b}:")
    print("-" * 40)
    print("a      b      ímpar?  soma acumulada")
    print("-" * 40)
    
    while a > 0:
        if a % 2 == 1:  # se a é ímpar
            resultado += b
            print(f"{a:5d}  {b:5d}  sim     {resultado}")
        else:
            print(f"{a:5d}  {b:5d}  não     {resultado}")
        
        a = a // 2
        b = b * 2
    
    print("-" * 40)
    return resultado


def camponeses_russos_base5(a, b):
    """
    versão modificada usando base 5 ao invés de base 2.
    
    método:
    1. divide o primeiro número por 5 (arredonda para baixo)
    2. multiplica o segundo número por 5
    3. soma b × (a mod 5) em cada linha
    """
    resultado = 0
    
    print(f"calculando {a} × {b} (base 5):")
    print("-" * 50)
    print("a      b      resto   contrib    soma acum")
    print("-" * 50)
    
    while a > 0:
        resto = a % 5
        contribuicao = b * resto
        resultado += contribuicao
        
        print(f"{a:5d}  {b:5d}  {resto:5d}   {contribuicao:7d}    {resultado}")
        
        a = a // 5
        b = b * 5
    
    print("-" * 50)
    return resultado


def explicar_algoritmo():
    """
    explica por que o algoritmo funciona.
    """
    print("=" * 70)
    print("por que o algoritmo dos camponeses russos funciona?")
    print("=" * 70)
    
    print("\nbase matemática (versão base 2):")
    print("  - qualquer número pode ser representado em binário")
    print("  - exemplo: 17 = 16 + 1 = 2⁴ + 2⁰")
    print("  - então: 17 × 23 = (16 + 1) × 23 = 16×23 + 1×23")
    
    print("\nprocesso:")
    print("  - dividir por 2 é deslocar bits para direita")
    print("  - multiplicar por 2 é deslocar bits para esquerda")
    print("  - somar quando ímpar captura cada bit 1")
    
    print("\nversão base 5:")
    print("  - usa representação em base 5")
    print("  - cada dígito pode ser 0,1,2,3,4")
    print("  - contribuição = b × (a mod 5)")
    print("  - equivale a: a×b = (a₀ + 5a₁ + 25a₂ + ...)×b")


def testar_algoritmos():
    """
    testa ambas as versões com vários casos.
    """
    casos = [
        (17, 23),
        (12, 15),
        (7, 9),
        (100, 25),
        (1, 999)
    ]
    
    print("=" * 70)
    print("teste: algoritmo dos camponeses russos (base 2)")
    print("=" * 70)
    print()
    
    for a, b in casos:
        resultado = camponeses_russos_base2(a, b)
        esperado = a * b
        status = "ok" if resultado == esperado else "erro!"
        print(f"\nresultado: {resultado}")
        print(f"esperado:  {esperado}")
        print(f"status: {status}")
        print()
    
    print("\n" + "=" * 70)
    print("teste: algoritmo dos camponeses russos (base 5)")
    print("=" * 70)
    print()
    
    for a, b in casos:
        resultado = camponeses_russos_base5(a, b)
        esperado = a * b
        status = "ok" if resultado == esperado else "erro!"
        print(f"\nresultado: {resultado}")
        print(f"esperado:  {esperado}")
        print(f"status: {status}")
        print()


def comparar_bases():
    """
    compara as duas versões.
    """
    print("=" * 70)
    print("comparação: base 2 vs base 5")
    print("=" * 70)
    
    print("\nalgoritmo base 2:")
    print("  - mais simples (apenas ímpar/par)")
    print("  - operações: divisão por 2, multiplicação por 2")
    print("  - eficiente em hardware (shift de bits)")
    print("  - o(log₂ n) iterações")
    
    print("\nalgoritmo base 5:")
    print("  - precisa calcular mod 5")
    print("  - operações: divisão por 5, multiplicação por 5")
    print("  - menos eficiente que base 2")
    print("  - o(log₅ n) iterações - menos iterações!")
    
    print("\nanálise:")
    print("  - log₅(n) < log₂(n), então base 5 tem menos passos")
    print("  - mas cada passo da base 5 é mais complexo")
    print("  - base 2 é preferível na prática")
    
    # exemplo numérico
    import math
    n = 1000
    passos_2 = math.ceil(math.log2(n))
    passos_5 = math.ceil(math.log(n, 5))
    
    print(f"\npara n={n}:")
    print(f"  base 2: ~{passos_2} passos")
    print(f"  base 5: ~{passos_5} passos")


def demonstrar_divisao_conquista():
    """
    mostra como este é um algoritmo de divisão e conquista.
    """
    print("\n\n" + "=" * 70)
    print("camponeses russos como divisão e conquista")
    print("=" * 70)
    
    print("\n1. divisão:")
    print("   - divide o problema a×b em subproblemas")
    print("   - reduz 'a' pela metade (ou por 5)")
    
    print("\n2. conquista:")
    print("   - resolve iterativamente (pode ser recursivo)")
    print("   - cada passo resolve uma parte do problema")
    
    print("\n3. combinação:")
    print("   - soma as contribuições de cada passo")
    print("   - acumula resultado parcial")
    
    print("\nrecorrência (base 2):")
    print("   multiply(a, b) = {")
    print("      b + multiply(a//2, 2b)  se a é ímpar")
    print("      multiply(a//2, 2b)      se a é par")
    print("   }")
    print("   caso base: a = 0, retorna 0")


if __name__ == "__main__":
    explicar_algoritmo()
    print("\n\n")
    testar_algoritmos()
    comparar_bases()
    demonstrar_divisao_conquista()

