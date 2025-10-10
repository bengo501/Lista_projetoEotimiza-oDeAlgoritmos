"""
exercício 10: subset sum problem

dado um conjunto s e um inteiro k,
verificar se existe um subconjunto de s com soma igual a k.

este é um problema np-completo, mas podemos resolver com
backtracking/divisão e conquista.
"""

def subset_sum_recursivo(conjunto, k, indice=0):
    """
    verifica se existe subconjunto com soma k usando divisão e conquista.
    
    estratégia:
    - caso base: k = 0, encontramos! (subconjunto vazio)
    - caso base: sem mais elementos e k != 0, não encontramos
    - recursão: tenta incluir ou não incluir o elemento atual
    
    complexidade: o(2^n) no pior caso
    """
    # caso base: soma zero (sucesso)
    if k == 0:
        return True, []
    
    # caso base: sem mais elementos (falha)
    if indice >= len(conjunto):
        return False, []
    
    # elemento atual
    elemento = conjunto[indice]
    
    # opção 1: não incluir o elemento atual
    encontrado, subconjunto = subset_sum_recursivo(conjunto, k, indice + 1)
    if encontrado:
        return True, subconjunto
    
    # opção 2: incluir o elemento atual
    if elemento <= k:  # otimização: só tenta se não ultrapassar
        encontrado, subconjunto = subset_sum_recursivo(conjunto, k - elemento, indice + 1)
        if encontrado:
            return True, [elemento] + subconjunto
    
    return False, []


def subset_sum_todos(conjunto, k):
    """
    encontra todos os subconjuntos com soma k.
    """
    def buscar(indice, soma_atual, subconjunto_atual):
        # encontrou uma solução
        if soma_atual == k:
            solucoes.append(subconjunto_atual.copy())
            return
        
        # ultrapassou ou chegou ao fim
        if soma_atual > k or indice >= len(conjunto):
            return
        
        # opção 1: incluir elemento atual
        subconjunto_atual.append(conjunto[indice])
        buscar(indice + 1, soma_atual + conjunto[indice], subconjunto_atual)
        subconjunto_atual.pop()
        
        # opção 2: não incluir elemento atual
        buscar(indice + 1, soma_atual, subconjunto_atual)
    
    solucoes = []
    buscar(0, 0, [])
    return solucoes


def testar_algoritmo():
    """
    testa o algoritmo com vários casos.
    """
    casos = [
        ([3, 34, 4, 12, 5, 2], 9, "sim"),
        ([3, 34, 4, 12, 5, 2], 30, "não"),
        ([1, 2, 3, 4, 5], 10, "sim"),
        ([10, 20, 30, 40], 50, "sim"),
        ([1, 1, 1, 1], 3, "sim"),
        ([5, 10, 15, 20], 17, "não")
    ]
    
    print("=" * 70)
    print("teste: subset sum problem")
    print("=" * 70)
    
    for conjunto, k, esperado in casos:
        print(f"\nconjunto: {conjunto}")
        print(f"soma alvo: {k}")
        print(f"esperado: {esperado}")
        
        encontrado, subconjunto = subset_sum_recursivo(conjunto.copy(), k)
        
        if encontrado:
            soma = sum(subconjunto)
            print(f"encontrado: {subconjunto}")
            print(f"soma: {soma}")
            
            if soma == k:
                print("verificação: correto!")
            else:
                print(f"verificação: erro! soma = {soma} != {k}")
        else:
            print("não encontrado")
        
        # tenta encontrar todas as soluções
        todas = subset_sum_todos(conjunto, k)
        if todas:
            print(f"total de soluções: {len(todas)}")
            if len(todas) <= 5:
                for sol in todas:
                    print(f"  {sol} -> soma = {sum(sol)}")
        
        print("-" * 70)


def demonstrar_divisao_conquista():
    """
    demonstra como este é um algoritmo de divisão e conquista.
    """
    print("\n\n" + "=" * 70)
    print("subset sum como divisão e conquista")
    print("=" * 70)
    
    print("\n1. divisão:")
    print("   - para cada elemento, há duas escolhas:")
    print("   - incluir no subconjunto")
    print("   - não incluir no subconjunto")
    
    print("\n2. conquista:")
    print("   - resolve recursivamente para o restante")
    print("   - ajusta o valor alvo conforme elementos incluídos")
    
    print("\n3. casos base:")
    print("   - soma = 0: sucesso!")
    print("   - sem mais elementos e soma != 0: falha")
    
    print("\nárvore de recursão para s={1,2,3}, k=4:")
    print("                   (0, {})")
    print("              /              \\")
    print("        (1,{1})              (0,{})")
    print("       /      \\             /      \\")
    print("   (3,{1,2}) (1,{1})   (2,{2})   (0,{})")
    print("     /   \\")
    print(" (6,{1,2,3}) (3,{1,2})")
    print("              ^")
    print("          solução!")
    
    print("\ncomplexidade:")
    print("  - tempo: o(2^n) - há 2^n subconjuntos possíveis")
    print("  - espaço: o(n) - profundidade da recursão")
    print("  - este é um problema np-completo")
    print("  - não há solução polinomial conhecida")


def versao_programacao_dinamica():
    """
    versão usando programação dinâmica para comparação.
    complexidade pseudo-polinomial: o(n*k)
    """
    def subset_sum_dp(conjunto, k):
        n = len(conjunto)
        # dp[i][j] = True se é possível soma j usando primeiros i elementos
        dp = [[False] * (k + 1) for _ in range(n + 1)]
        
        # soma 0 sempre é possível (conjunto vazio)
        for i in range(n + 1):
            dp[i][0] = True
        
        # preenche a tabela
        for i in range(1, n + 1):
            for j in range(k + 1):
                # não incluir elemento i-1
                dp[i][j] = dp[i-1][j]
                
                # incluir elemento i-1 (se possível)
                if j >= conjunto[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j - conjunto[i-1]]
        
        return dp[n][k]
    
    print("\n\n" + "=" * 70)
    print("versão com programação dinâmica")
    print("=" * 70)
    
    conjunto = [3, 34, 4, 12, 5, 2]
    k = 9
    
    print(f"conjunto: {conjunto}")
    print(f"soma alvo: {k}")
    
    resultado = subset_sum_dp(conjunto, k)
    print(f"resultado (dp): {'existe' if resultado else 'não existe'}")
    
    print("\ncomplexidade:")
    print("  - tempo: o(n * k)")
    print("  - espaço: o(n * k)")
    print("  - pseudo-polinomial (depende do valor de k)")


if __name__ == "__main__":
    testar_algoritmo()
    demonstrar_divisao_conquista()
    versao_programacao_dinamica()

