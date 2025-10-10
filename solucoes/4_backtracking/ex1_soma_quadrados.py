"""
exercicio 1: sequencia com somas quadradas perfeitas

algoritmo baseado em backtracking que recebe um inteiro n e produz
uma sequencia contendo todos os inteiros de 1 a n, com a condicao de que
a soma de um inteiro com o seguinte na sequencia seja sempre um quadrado perfeito.

exemplo para n=15:
8 1 15 10 6 3 13 12 4 5 11 14 2 7 9
"""

import math

def eh_quadrado_perfeito(n):
    """verifica se n e um quadrado perfeito."""
    raiz = int(math.sqrt(n))
    return raiz * raiz == n


def encontrar_sequencia_quadrados(n):
    """
    encontra uma sequencia de 1 a n onde numeros consecutivos somam quadrado perfeito.
    usa backtracking.
    """
    
    def backtrack(sequencia, restantes):
        # caso base: usamos todos os numeros
        if not restantes:
            return sequencia
        
        # se a sequencia esta vazia, podemos comecar com qualquer numero
        if not sequencia:
            for num in sorted(restantes):
                resultado = backtrack([num], restantes - {num})
                if resultado:
                    return resultado
        else:
            # tenta adicionar cada numero restante
            ultimo = sequencia[-1]
            
            for num in sorted(restantes):
                # verifica se a soma e quadrado perfeito
                if eh_quadrado_perfeito(ultimo + num):
                    resultado = backtrack(sequencia + [num], restantes - {num})
                    if resultado:
                        return resultado
        
        # backtrack: nenhuma opcao funcionou
        return None
    
    restantes = set(range(1, n + 1))
    return backtrack([], restantes)


def encontrar_todas_sequencias(n, limite=None):
    """
    encontra todas as sequencias possiveis (ou ate um limite).
    """
    solucoes = []
    
    def backtrack(sequencia, restantes):
        if limite and len(solucoes) >= limite:
            return
        
        if not restantes:
            solucoes.append(sequencia[:])
            return
        
        if not sequencia:
            for num in sorted(restantes):
                backtrack([num], restantes - {num})
        else:
            ultimo = sequencia[-1]
            for num in sorted(restantes):
                if eh_quadrado_perfeito(ultimo + num):
                    backtrack(sequencia + [num], restantes - {num})
    
    restantes = set(range(1, n + 1))
    backtrack([], restantes)
    return solucoes


def testar_algoritmo():
    """
    testa o algoritmo com varios valores de n.
    """
    print("=" * 70)
    print("sequencia com somas quadradas perfeitas")
    print("=" * 70)
    
    print("\ncondicao: a soma de numeros consecutivos deve ser quadrado perfeito")
    print("exemplos de quadrados perfeitos: 1, 4, 9, 16, 25, 36, 49, 64, ...")
    
    # testa varios valores
    for n in [3, 5, 7, 10, 15]:
        print(f"\n\n{'=' * 70}")
        print(f"n = {n}")
        print(f"{'=' * 70}")
        
        sequencia = encontrar_sequencia_quadrados(n)
        
        if sequencia:
            print(f"sequencia encontrada: {' '.join(map(str, sequencia))}")
            
            # verifica a solucao
            print("\nverificacao:")
            valida = True
            for i in range(len(sequencia) - 1):
                soma = sequencia[i] + sequencia[i+1]
                eh_quad = eh_quadrado_perfeito(soma)
                raiz = int(math.sqrt(soma))
                print(f"  {sequencia[i]:2d} + {sequencia[i+1]:2d} = {soma:2d} = {raiz}^2  {'ok' if eh_quad else 'erro!'}")
                if not eh_quad:
                    valida = False
            
            if valida and set(sequencia) == set(range(1, n+1)):
                print("\nsolucao valida!")
            else:
                print("\nsolucao invalida!")
        else:
            print("nenhuma sequencia encontrada!")


def analisar_conectividade():
    """
    analisa a conectividade do grafo para diferentes valores de n.
    """
    print("\n\n" + "=" * 70)
    print("analise de conectividade")
    print("=" * 70)
    
    print("\npodemos ver isso como um grafo onde:")
    print("  - vertices = numeros de 1 a n")
    print("  - arestas = pares cuja soma e quadrado perfeito")
    print("  - problema = encontrar caminho hamiltoniano")
    
    for n in range(1, 21):
        # constroi grafo de adjacencia
        grafo = {i: [] for i in range(1, n+1)}
        
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if eh_quadrado_perfeito(i + j):
                    grafo[i].append(j)
                    grafo[j].append(i)
        
        # conta vertices isolados e graus
        isolados = [v for v in grafo if len(grafo[v]) == 0]
        graus = [len(grafo[v]) for v in grafo]
        grau_min = min(graus) if graus else 0
        grau_max = max(graus) if graus else 0
        
        # tenta encontrar solucao
        sequencia = encontrar_sequencia_quadrados(n)
        tem_solucao = "sim" if sequencia else "nao"
        
        print(f"n={n:2d}: isolados={len(isolados)}, grau_min={grau_min}, grau_max={grau_max}, solucao={tem_solucao}")


def explicar_backtracking():
    """
    explica o algoritmo de backtracking.
    """
    print("\n\n" + "=" * 70)
    print("backtracking")
    print("=" * 70)
    
    print("\n1. estrategia:")
    print("   - tenta construir a sequencia passo a passo")
    print("   - em cada passo, tenta adicionar um numero valido")
    print("   - se chegar em beco sem saida, volta atras (backtrack)")
    
    print("\n2. poda:")
    print("   - verifica se soma e quadrado perfeito antes de continuar")
    print("   - evita explorar caminhos invalidos")
    
    print("\n3. complexidade:")
    print("   - pior caso: o(n!) - tenta todas as permutacoes")
    print("   - pratica: muito mais rapido devido a poda")
    
    print("\n4. otimizacoes possiveis:")
    print("   - ordenar candidatos por grau (menor grau primeiro)")
    print("   - verificar conectividade antes de comecar")
    print("   - usar heuristicas para escolher proximo numero")


if __name__ == "__main__":
    testar_algoritmo()
    analisar_conectividade()
    explicar_backtracking()

