"""
exercicio 2: problema das n rainhas

algoritmo que resolve o problema das 4 rainhas (e depois n rainhas)
usando backtracking.

objetivo: colocar n rainhas em um tabuleiro n x n de forma que
nenhuma rainha ataque outra.
"""

def eh_seguro(tabuleiro, linha, coluna):
    """
    verifica se e seguro colocar uma rainha em (linha, coluna).
    """
    n = len(tabuleiro)
    
    # verifica coluna
    for i in range(linha):
        if tabuleiro[i] == coluna:
            return False
    
    # verifica diagonal principal (\)
    for i in range(linha):
        if abs(tabuleiro[i] - coluna) == abs(i - linha):
            return False
    
    return True


def resolver_n_rainhas(n):
    """
    resolve o problema das n rainhas usando backtracking.
    retorna uma solucao (primeira encontrada).
    
    representacao: tabuleiro[i] = coluna da rainha na linha i
    """
    tabuleiro = [-1] * n
    
    def backtrack(linha):
        # caso base: todas as rainhas colocadas
        if linha == n:
            return True
        
        # tenta cada coluna
        for coluna in range(n):
            if eh_seguro(tabuleiro, linha, coluna):
                tabuleiro[linha] = coluna
                
                if backtrack(linha + 1):
                    return True
                
                # backtrack
                tabuleiro[linha] = -1
        
        return False
    
    if backtrack(0):
        return tabuleiro
    else:
        return None


def resolver_todas_solucoes(n):
    """
    encontra todas as solucoes para n rainhas.
    """
    solucoes = []
    tabuleiro = [-1] * n
    
    def backtrack(linha):
        if linha == n:
            solucoes.append(tabuleiro[:])
            return
        
        for coluna in range(n):
            if eh_seguro(tabuleiro, linha, coluna):
                tabuleiro[linha] = coluna
                backtrack(linha + 1)
                tabuleiro[linha] = -1
    
    backtrack(0)
    return solucoes


def visualizar_tabuleiro(tabuleiro):
    """
    visualiza o tabuleiro com as rainhas.
    """
    n = len(tabuleiro)
    
    print("  " + " ".join(str(i) for i in range(n)))
    print("  " + "-" * (2 * n - 1))
    
    for i in range(n):
        linha = []
        for j in range(n):
            if tabuleiro[i] == j:
                linha.append('Q')
            else:
                linha.append('.')
        print(f"{i}|" + " ".join(linha))


def testar_n_rainhas():
    """
    testa o algoritmo para diferentes valores de n.
    """
    print("=" * 70)
    print("problema das n rainhas")
    print("=" * 70)
    
    print("\nobjetivo: colocar n rainhas em tabuleiro n x n")
    print("condicao: nenhuma rainha pode atacar outra")
    print("          (mesma linha, coluna ou diagonal)")
    
    # teste para 4 rainhas (conforme pedido)
    print("\n\n" + "=" * 70)
    print("problema das 4 rainhas")
    print("=" * 70)
    
    n = 4
    solucao = resolver_n_rainhas(n)
    
    if solucao:
        print(f"\nsolucao encontrada: {solucao}")
        print("(cada numero representa a coluna da rainha naquela linha)")
        print("\ntabuleiro:")
        visualizar_tabuleiro(solucao)
        
        # encontra todas as solucoes
        todas = resolver_todas_solucoes(n)
        print(f"\ntotal de solucoes para n=4: {len(todas)}")
        
        print("\ntodas as solucoes:")
        for i, sol in enumerate(todas, 1):
            print(f"\nsolucao {i}: {sol}")
            visualizar_tabuleiro(sol)
    else:
        print("nenhuma solucao encontrada!")
    
    # teste para varios valores de n
    print("\n\n" + "=" * 70)
    print("n rainhas para varios valores de n")
    print("=" * 70)
    
    print("\nn  | solucao? | total de solucoes")
    print("-" * 40)
    
    for n in range(1, 13):
        solucao = resolver_n_rainhas(n)
        tem_solucao = "sim" if solucao else "nao"
        
        if n <= 10:
            todas = resolver_todas_solucoes(n)
            num_solucoes = len(todas)
            print(f"{n:2d} | {tem_solucao:8s} | {num_solucoes:5d}")
        else:
            print(f"{n:2d} | {tem_solucao:8s} | (muitas)")
        
        # mostra uma solucao para alguns valores
        if n in [5, 8] and solucao:
            print(f"\nexemplo de solucao para n={n}:")
            visualizar_tabuleiro(solucao)
            print()


def analisar_complexidade():
    """
    analisa a complexidade do algoritmo.
    """
    print("\n\n" + "=" * 70)
    print("analise de complexidade")
    print("=" * 70)
    
    print("\ncomplexidade:")
    print("  - pior caso: o(n!) sem poda")
    print("  - pratica: muito melhor devido ao backtracking")
    print("  - poda: verifica seguranca antes de prosseguir")
    
    print("\nnumero de solucoes:")
    print("  sequencia oeis a000170")
    print("  n=1: 1")
    print("  n=2: 0")
    print("  n=3: 0")
    print("  n=4: 2")
    print("  n=5: 10")
    print("  n=6: 4")
    print("  n=7: 40")
    print("  n=8: 92")
    print("  n=9: 352")
    print("  n=10: 724")
    print("  ...")
    
    print("\nfatos interessantes:")
    print("  - problema classico de backtracking")
    print("  - proposto por gauss em 1850")
    print("  - primeira solucao: nauck, 1850")
    print("  - n=2 e n=3 nao tem solucao")


def explicar_backtracking():
    """
    explica o algoritmo de backtracking.
    """
    print("\n\n" + "=" * 70)
    print("backtracking no problema das rainhas")
    print("=" * 70)
    
    print("\n1. abordagem:")
    print("   - coloca rainhas linha por linha")
    print("   - para cada linha, tenta cada coluna")
    print("   - verifica se a posicao e segura")
    
    print("\n2. verificacao de seguranca:")
    print("   - nao pode haver rainha na mesma coluna")
    print("   - nao pode haver rainha na mesma diagonal")
    print("   - nao precisa verificar linha (colocamos uma por linha)")
    
    print("\n3. backtracking:")
    print("   - se nenhuma coluna e segura, volta para linha anterior")
    print("   - tenta proxima coluna na linha anterior")
    print("   - continua ate encontrar solucao ou esgotar opcoes")
    
    print("\n4. otimizacoes possiveis:")
    print("   - usar sets para rastrear colunas e diagonais ocupadas: o(1)")
    print("   - simetria: reduzir espaco de busca pela metade")
    print("   - heuristicas: escolher posicoes mais restritivas primeiro")


if __name__ == "__main__":
    testar_n_rainhas()
    analisar_complexidade()
    explicar_backtracking()

