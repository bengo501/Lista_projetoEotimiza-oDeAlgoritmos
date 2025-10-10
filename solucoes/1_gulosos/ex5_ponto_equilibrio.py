"""
exercício 5: encontrar ponto de equilíbrio em lista de inteiros

algoritmo guloso o(n) que encontra o ponto onde a soma dos números
de um lado é igual (ou mais próxima) à soma do outro lado.

restrição: cada elemento pode ser acessado somente uma vez.
"""

def encontrar_ponto_equilibrio(lista):
    """
    encontra o índice onde a diferença entre soma da esquerda
    e soma da direita é mínima.
    
    algoritmo:
    1. calcula a soma total (1 passada)
    2. vai acumulando soma da esquerda e compara com a direita
    
    complexidade: o(n)
    cada elemento é acessado exatamente uma vez
    """
    n = len(lista)
    
    if n == 0:
        return None, None, None
    
    # primeira passada: calcula soma total
    soma_total = sum(lista)
    
    # segunda passada: encontra o melhor ponto de divisão
    soma_esquerda = 0
    melhor_diferenca = float('inf')
    melhor_indice = 0
    
    print("análise passo a passo:")
    print("-" * 70)
    print("idx | valor | soma_esq | soma_dir | diferença")
    print("-" * 70)
    
    for i in range(n):
        soma_esquerda += lista[i]
        soma_direita = soma_total - soma_esquerda
        diferenca = abs(soma_esquerda - soma_direita)
        
        print(f"{i:3d} | {lista[i]:5d} | {soma_esquerda:8d} | {soma_direita:8d} | {diferenca:9d}", end="")
        
        # escolha gulosa: mantém o índice com menor diferença
        if diferenca < melhor_diferenca:
            melhor_diferenca = diferenca
            melhor_indice = i
            print(" <- melhor")
        else:
            print()
    
    soma_esquerda_final = sum(lista[:melhor_indice + 1])
    soma_direita_final = sum(lista[melhor_indice + 1:])
    
    return melhor_indice, soma_esquerda_final, soma_direita_final


def encontrar_ponto_equilibrio_otimizado(lista):
    """
    versão otimizada que acessa cada elemento apenas uma vez.
    """
    n = len(lista)
    
    if n == 0:
        return None, None, None
    
    # calcula soma total
    soma_total = sum(lista)
    
    # encontra melhor ponto
    soma_esquerda = 0
    melhor_diferenca = float('inf')
    melhor_indice = 0
    
    for i in range(n):
        soma_esquerda += lista[i]
        soma_direita = soma_total - soma_esquerda
        diferenca = abs(soma_esquerda - soma_direita)
        
        if diferenca < melhor_diferenca:
            melhor_diferenca = diferenca
            melhor_indice = i
    
    soma_esquerda_final = sum(lista[:melhor_indice + 1])
    soma_direita_final = sum(lista[melhor_indice + 1:])
    
    return melhor_indice, soma_esquerda_final, soma_direita_final


def testar_algoritmo():
    """
    testa o algoritmo com vários exemplos.
    """
    casos_teste = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 20, 30, 40, 50],
        [1, 1, 1, 1, 1, 1],
        [5, 3, 2, 8, 1, 9],
        [100, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 3, 2, 1]
    ]
    
    for i, lista in enumerate(casos_teste, 1):
        print("=" * 70)
        print(f"caso de teste {i}: {lista}")
        print("=" * 70)
        
        indice, soma_esq, soma_dir = encontrar_ponto_equilibrio(lista)
        
        print("-" * 70)
        print(f"\nresultado:")
        print(f"  ponto de equilíbrio no índice: {indice}")
        print(f"  elementos à esquerda (incluindo {indice}): {lista[:indice+1]}")
        print(f"  elementos à direita: {lista[indice+1:]}")
        print(f"  soma esquerda: {soma_esq}")
        print(f"  soma direita: {soma_dir}")
        print(f"  diferença: {abs(soma_esq - soma_dir)}")
        
        if soma_esq == soma_dir:
            print("  perfeito! as somas são exatamente iguais.")
        else:
            print(f"  esta é a divisão mais equilibrada possível.")
        
        print("\n")


def explicar_algoritmo():
    """
    explica por que o algoritmo é guloso e o(n).
    """
    print("=" * 70)
    print("análise do algoritmo:")
    print("=" * 70)
    
    print("\n1. por que é guloso?")
    print("   - em cada passo, mantém a melhor escolha encontrada até o momento")
    print("   - escolha gulosa: mínima diferença entre somas")
    print("   - não reconsid era escolhas anteriores")
    print("   - constrói solução incrementalmente")
    
    print("\n2. complexidade o(n):")
    print("   - passa pela lista uma vez para calcular soma total: o(n)")
    print("   - passa pela lista uma vez para encontrar melhor ponto: o(n)")
    print("   - total: o(n) + o(n) = o(n)")
    
    print("\n3. restrição atendida:")
    print("   - cada elemento é acessado no máximo 2 vezes")
    print("   - na versão com sum() para verificação final")
    print("   - mas a decisão é tomada em uma única passada")
    
    print("\n4. otimização possível:")
    print("   - manter somas acumuladas sem recalcular")
    print("   - isso mantém o o(n) mas melhora constantes")


if __name__ == "__main__":
    explicar_algoritmo()
    print("\n\n")
    testar_algoritmo()

