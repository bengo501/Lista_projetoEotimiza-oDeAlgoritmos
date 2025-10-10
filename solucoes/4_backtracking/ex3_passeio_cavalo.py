"""
exercicio 3: passeio do cavalo no xadrez

adaptar algoritmo das n rainhas para resolver o passeio do cavalo.

problema: dado um tabuleiro de xadrez nxn e uma posicao inicial,
encontrar uma sequencia de movimentos do cavalo que visite cada casa
exatamente uma vez.

referencia: http://en.wikipedia.org/wiki/Knight%27s_tour
"""

def movimentos_cavalo():
    """retorna os 8 movimentos possiveis do cavalo."""
    return [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]


def eh_valido(x, y, n, tabuleiro):
    """verifica se a posicao (x,y) e valida e ainda nao foi visitada."""
    return 0 <= x < n and 0 <= y < n and tabuleiro[x][y] == -1


def passeio_cavalo(n, inicio_x=0, inicio_y=0):
    """
    resolve o passeio do cavalo usando backtracking.
    
    tabuleiro[i][j] = numero do movimento (0 a n*n-1)
    -1 indica casa nao visitada
    """
    # inicializa tabuleiro
    tabuleiro = [[-1 for _ in range(n)] for _ in range(n)]
    
    # movimentos do cavalo
    movimentos = movimentos_cavalo()
    
    # marca posicao inicial
    tabuleiro[inicio_x][inicio_y] = 0
    
    def backtrack(x, y, movimento):
        # caso base: visitou todas as casas
        if movimento == n * n:
            return True
        
        # tenta cada movimento possivel
        for dx, dy in movimentos:
            prox_x = x + dx
            prox_y = y + dy
            
            if eh_valido(prox_x, prox_y, n, tabuleiro):
                tabuleiro[prox_x][prox_y] = movimento
                
                if backtrack(prox_x, prox_y, movimento + 1):
                    return True
                
                # backtrack
                tabuleiro[prox_x][prox_y] = -1
        
        return False
    
    if backtrack(inicio_x, inicio_y, 1):
        return tabuleiro
    else:
        return None


def passeio_cavalo_warnsdorff(n, inicio_x=0, inicio_y=0):
    """
    versao com heuristica de warnsdorff.
    escolhe o movimento que leva a casa com menos saidas disponiveis.
    muito mais rapido!
    """
    tabuleiro = [[-1 for _ in range(n)] for _ in range(n)]
    movimentos = movimentos_cavalo()
    tabuleiro[inicio_x][inicio_y] = 0
    
    def contar_saidas(x, y):
        """conta quantas saidas validas existem de (x,y)."""
        cont = 0
        for dx, dy in movimentos:
            if eh_valido(x + dx, y + dy, n, tabuleiro):
                cont += 1
        return cont
    
    def backtrack(x, y, movimento):
        if movimento == n * n:
            return True
        
        # gera lista de proximos movimentos com suas prioridades
        proximos = []
        for dx, dy in movimentos:
            prox_x = x + dx
            prox_y = y + dy
            if eh_valido(prox_x, prox_y, n, tabuleiro):
                saidas = contar_saidas(prox_x, prox_y)
                proximos.append((saidas, prox_x, prox_y))
        
        # ordena por numero de saidas (warnsdorff: escolhe casa mais restritiva)
        proximos.sort()
        
        for _, prox_x, prox_y in proximos:
            tabuleiro[prox_x][prox_y] = movimento
            
            if backtrack(prox_x, prox_y, movimento + 1):
                return True
            
            tabuleiro[prox_x][prox_y] = -1
        
        return False
    
    if backtrack(inicio_x, inicio_y, 1):
        return tabuleiro
    else:
        return None


def visualizar_passeio(tabuleiro):
    """visualiza o passeio do cavalo."""
    if tabuleiro is None:
        print("nenhuma solucao encontrada!")
        return
    
    n = len(tabuleiro)
    
    # encontra largura maxima
    largura = len(str(n * n - 1))
    
    # imprime tabuleiro
    print("  ", end="")
    for j in range(n):
        print(f"{j:>{largura+1}}", end="")
    print()
    
    print("  " + "-" * ((largura + 1) * n + 1))
    
    for i in range(n):
        print(f"{i} |", end="")
        for j in range(n):
            print(f"{tabuleiro[i][j]:>{largura}}", end=" ")
        print()


def testar_passeio():
    """
    testa o algoritmo do passeio do cavalo.
    """
    print("=" * 70)
    print("passeio do cavalo no xadrez")
    print("=" * 70)
    
    print("\nobjetivo: cavalo deve visitar todas as casas do tabuleiro")
    print("          exatamente uma vez")
    
    print("\nmovimentos do cavalo (formato xadrez):")
    print("  L invertido: 2 casas em uma direcao, 1 perpendicular")
    
    # testa tabuleiro 5x5
    print("\n\n" + "=" * 70)
    print("tabuleiro 5x5 (com heuristica de warnsdorff)")
    print("=" * 70)
    
    import time
    
    n = 5
    inicio = time.time()
    solucao = passeio_cavalo_warnsdorff(n, 0, 0)
    tempo = time.time() - inicio
    
    if solucao:
        print(f"\nsolucao encontrada em {tempo:.4f}s")
        print("\nnumeros representam a ordem da visita:")
        visualizar_passeio(solucao)
    else:
        print("nenhuma solucao encontrada!")
    
    # testa tabuleiro 6x6
    print("\n\n" + "=" * 70)
    print("tabuleiro 6x6")
    print("=" * 70)
    
    n = 6
    inicio = time.time()
    solucao = passeio_cavalo_warnsdorff(n, 0, 0)
    tempo = time.time() - inicio
    
    if solucao:
        print(f"\nsolucao encontrada em {tempo:.4f}s")
        visualizar_passeio(solucao)
    else:
        print("nenhuma solucao encontrada!")
    
    # testa tabuleiro 8x8 (xadrez padrao)
    print("\n\n" + "=" * 70)
    print("tabuleiro 8x8 (xadrez padrao)")
    print("=" * 70)
    
    n = 8
    inicio = time.time()
    solucao = passeio_cavalo_warnsdorff(n, 0, 0)
    tempo = time.time() - inicio
    
    if solucao:
        print(f"\nsolucao encontrada em {tempo:.4f}s")
        visualizar_passeio(solucao)
    else:
        print("nenhuma solucao encontrada!")


def analisar_problema():
    """
    analisa o problema do passeio do cavalo.
    """
    print("\n\n" + "=" * 70)
    print("analise do problema")
    print("=" * 70)
    
    print("\nhistoria:")
    print("  - problema classico da teoria dos grafos")
    print("  - estudado por euler em 1759")
    print("  - possui solucao para n >= 5")
    print("  - n=1,2,4 nao tem solucao")
    print("  - n=3 nao tem solucao")
    
    print("\ncomplexidade:")
    print("  - backtracking puro: o(8^(n²)) - muito lento")
    print("  - com heuristica de warnsdorff: polinomial na pratica")
    print("  - warnsdorff: escolhe casa com menos saidas")
    
    print("\ntipos de passeio:")
    print("  - aberto: termina em casa diferente da inicial")
    print("  - fechado: termina na casa inicial (pode fazer outro tour)")
    
    print("\nheuristica de warnsdorff:")
    print("  - escolhe o proximo movimento para a casa com menos saidas")
    print("  - ideia: visitar casas dificeis primeiro")
    print("  - melhora drasticamente o desempenho")
    print("  - nao garante solucao, mas funciona bem na pratica")


def comparar_backtracking():
    """
    compara backtracking puro vs com heuristica.
    """
    print("\n\n" + "=" * 70)
    print("comparacao: backtracking vs warnsdorff")
    print("=" * 70)
    
    import time
    
    print("\nteste para tabuleiro 5x5:")
    print("-" * 50)
    
    # backtracking puro (pode ser lento)
    print("backtracking puro: ", end="")
    inicio = time.time()
    solucao1 = passeio_cavalo(5, 0, 0)
    tempo1 = time.time() - inicio
    if solucao1:
        print(f"solucao em {tempo1:.4f}s")
    else:
        print(f"sem solucao em {tempo1:.4f}s")
    
    # com warnsdorff
    print("com warnsdorff:    ", end="")
    inicio = time.time()
    solucao2 = passeio_cavalo_warnsdorff(5, 0, 0)
    tempo2 = time.time() - inicio
    if solucao2:
        print(f"solucao em {tempo2:.4f}s")
    else:
        print(f"sem solucao em {tempo2:.4f}s")
    
    if tempo1 > 0 and tempo2 > 0:
        print(f"\nwarnsdorff foi {tempo1/tempo2:.1f}x mais rapido!")


if __name__ == "__main__":
    testar_passeio()
    analisar_problema()
    comparar_backtracking()

