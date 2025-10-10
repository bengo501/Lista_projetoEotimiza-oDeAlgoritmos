"""
exercício 6: coloração de grafos usando algoritmo guloso

problema: encontrar o número mínimo de cores necessárias para colorir
um grafo não dirigido tal que nenhum par de nodos vizinhos tenha a mesma cor.

nota: o problema de coloração de grafos é np-completo.
um algoritmo guloso não garante encontrar o número mínimo (cromático),
mas fornece uma aproximação razoável.

se alguém provar que um algoritmo guloso sempre encontra a solução ótima
para todo grafo, ganharia um prêmio importante (problema p=np).
"""

def coloracao_gulosa(grafo):
    """
    algoritmo guloso para coloração de grafos.
    
    estratégia:
    1. ordena os nodos por grau (número de vizinhos) - ordem decrescente
    2. para cada nodo, atribui a menor cor que não conflita com vizinhos
    
    não garante número mínimo de cores, mas é uma boa heurística.
    """
    # calcula grau de cada nodo
    graus = {nodo: len(vizinhos) for nodo, vizinhos in grafo.items()}
    
    # ordena nodos por grau decrescente (heurística: nodos mais conectados primeiro)
    nodos_ordenados = sorted(graus.keys(), key=lambda x: graus[x], reverse=True)
    
    # dicionário para armazenar cores dos nodos
    cores = {}
    
    print("processo de coloração:")
    print("-" * 70)
    
    for nodo in nodos_ordenados:
        # encontra cores dos vizinhos
        cores_vizinhos = set()
        for vizinho in grafo[nodo]:
            if vizinho in cores:
                cores_vizinhos.add(cores[vizinho])
        
        # escolha gulosa: menor cor disponível
        cor = 0
        while cor in cores_vizinhos:
            cor += 1
        
        cores[nodo] = cor
        print(f"nodo {nodo} (grau {graus[nodo]}): vizinhos coloridos com {cores_vizinhos} -> usa cor {cor}")
    
    return cores


def verificar_coloracao(grafo, cores):
    """
    verifica se a coloração é válida (sem vizinhos com mesma cor).
    """
    for nodo, vizinhos in grafo.items():
        for vizinho in vizinhos:
            if cores[nodo] == cores[vizinho]:
                return False, f"conflito: {nodo} e {vizinho} têm a mesma cor"
    return True, "coloração válida"


def visualizar_coloracao(grafo, cores):
    """
    visualiza a coloração do grafo.
    """
    nomes_cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo', 
                   'laranja', 'rosa', 'cinza', 'marrom', 'ciano']
    
    num_cores = max(cores.values()) + 1
    
    print("\n" + "=" * 70)
    print("resultado da coloração:")
    print("=" * 70)
    
    for cor in range(num_cores):
        nodos_com_cor = [nodo for nodo, c in cores.items() if c == cor]
        nome_cor = nomes_cores[cor] if cor < len(nomes_cores) else f"cor_{cor}"
        print(f"{nome_cor}: {sorted(nodos_com_cor)}")
    
    print(f"\ntotal de cores usadas: {num_cores}")


def provar_que_nao_sempre_funciona():
    """
    demonstra casos onde o algoritmo guloso não encontra o número mínimo.
    """
    print("\n\n" + "=" * 70)
    print("por que o algoritmo guloso não sempre encontra o mínimo?")
    print("=" * 70)
    
    # exemplo: grafo bipartido completo k(2,3)
    # número cromático = 2 (é bipartido)
    # mas dependendo da ordem, o guloso pode usar 3 cores
    
    print("\nexemplo 1: grafo onde guloso pode não ser ótimo")
    print("-" * 70)
    
    # um grafo em forma de ciclo ímpar (c5)
    grafo_ciclo = {
        'a': ['b', 'e'],
        'b': ['a', 'c'],
        'c': ['b', 'd'],
        'd': ['c', 'e'],
        'e': ['d', 'a']
    }
    
    print("grafo: ciclo com 5 vértices")
    print("número cromático real: 3 (ciclo ímpar)")
    print("\ncoloração gulosa:")
    cores = coloracao_gulosa(grafo_ciclo)
    visualizar_coloracao(grafo_ciclo, cores)
    valida, msg = verificar_coloracao(grafo_ciclo, cores)
    print(f"\nverificação: {msg}")
    
    print("\n" + "=" * 70)
    print("conclusão:")
    print("=" * 70)
    print("o algoritmo guloso para coloração de grafos:")
    print("  ✓ é guloso (escolhe menor cor disponível a cada passo)")
    print("  ✓ sempre produz uma coloração válida")
    print("  ✗ não garante o número mínimo de cores")
    print("\npor quê?")
    print("  - a ordem de escolha dos vértices afeta o resultado")
    print("  - diferentes heurísticas dão diferentes resultados")
    print("  - o problema é np-completo")
    print("\nse você provar que sempre funciona otimalmente,")
    print("você prova que p=np e ganha um milhão de dólares!")


def testar_varios_grafos():
    """
    testa o algoritmo com diferentes tipos de grafos.
    """
    print("=" * 70)
    print("teste 1: grafo completo k4")
    print("=" * 70)
    grafo_k4 = {
        'a': ['b', 'c', 'd'],
        'b': ['a', 'c', 'd'],
        'c': ['a', 'b', 'd'],
        'd': ['a', 'b', 'c']
    }
    print("número cromático esperado: 4 (todos conectados)")
    cores = coloracao_gulosa(grafo_k4)
    visualizar_coloracao(grafo_k4, cores)
    valida, msg = verificar_coloracao(grafo_k4, cores)
    print(f"verificação: {msg}")
    
    print("\n\n" + "=" * 70)
    print("teste 2: grafo bipartido")
    print("=" * 70)
    grafo_bipartido = {
        'a': ['x', 'y', 'z'],
        'b': ['x', 'y', 'z'],
        'c': ['x', 'y', 'z'],
        'x': ['a', 'b', 'c'],
        'y': ['a', 'b', 'c'],
        'z': ['a', 'b', 'c']
    }
    print("número cromático esperado: 2 (bipartido)")
    cores = coloracao_gulosa(grafo_bipartido)
    visualizar_coloracao(grafo_bipartido, cores)
    valida, msg = verificar_coloracao(grafo_bipartido, cores)
    print(f"verificação: {msg}")
    
    print("\n\n" + "=" * 70)
    print("teste 3: árvore")
    print("=" * 70)
    grafo_arvore = {
        'a': ['b', 'c'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'f'],
        'd': ['b'],
        'e': ['b'],
        'f': ['c']
    }
    print("número cromático esperado: 2 (árvores são bipartidas)")
    cores = coloracao_gulosa(grafo_arvore)
    visualizar_coloracao(grafo_arvore, cores)
    valida, msg = verificar_coloracao(grafo_arvore, cores)
    print(f"verificação: {msg}")


if __name__ == "__main__":
    testar_varios_grafos()
    provar_que_nao_sempre_funciona()

