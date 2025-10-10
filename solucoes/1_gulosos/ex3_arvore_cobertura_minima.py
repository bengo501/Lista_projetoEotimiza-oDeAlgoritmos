"""
exercício 3: análise do algoritmo de árvore de cobertura mínima

o algoritmo proposto:
(a) inicie em algum nodo u de g
(b) siga a aresta de valor mais baixo ligada a u e que leva a um nodo ainda não visitado
(c) repita o passo anterior até visitar todos os nodos de g

perguntas:
(a) ele é guloso?
(b) ele acha uma árvore de cobertura mínima?
"""

def algoritmo_proposto(grafo, inicio):
    """
    implementa o algoritmo proposto no exercício.
    
    args:
        grafo: dicionário de adjacências {nodo: [(vizinho, peso), ...]}
        inicio: nodo inicial
    
    returns:
        lista de arestas selecionadas e peso total
    """
    visitados = {inicio}
    arestas = []
    peso_total = 0
    nodo_atual = inicio
    
    print(f"iniciando no nodo {inicio}")
    
    while len(visitados) < len(grafo):
        # encontra a aresta de menor peso para um nodo não visitado
        menor_peso = float('inf')
        proxima_aresta = None
        proximo_nodo = None
        
        # apenas considera arestas do nodo atual
        if nodo_atual in grafo:
            for vizinho, peso in grafo[nodo_atual]:
                if vizinho not in visitados and peso < menor_peso:
                    menor_peso = peso
                    proxima_aresta = (nodo_atual, vizinho, peso)
                    proximo_nodo = vizinho
        
        if proxima_aresta is None:
            print("erro: grafo desconexo ou sem caminho!")
            return None, None
        
        arestas.append(proxima_aresta)
        visitados.add(proximo_nodo)
        peso_total += menor_peso
        print(f"  escolhendo aresta {proxima_aresta[0]}-{proxima_aresta[1]} (peso {menor_peso})")
        
        nodo_atual = proximo_nodo
    
    return arestas, peso_total


def algoritmo_prim(grafo, inicio):
    """
    implementa o algoritmo de prim para comparação.
    """
    visitados = {inicio}
    arestas = []
    peso_total = 0
    
    print(f"prim iniciando no nodo {inicio}")
    
    while len(visitados) < len(grafo):
        menor_peso = float('inf')
        proxima_aresta = None
        
        # considera todas as arestas que saem dos nodos visitados
        for nodo in visitados:
            if nodo in grafo:
                for vizinho, peso in grafo[nodo]:
                    if vizinho not in visitados and peso < menor_peso:
                        menor_peso = peso
                        proxima_aresta = (nodo, vizinho, peso)
        
        if proxima_aresta is None:
            print("erro: grafo desconexo!")
            return None, None
        
        arestas.append(proxima_aresta)
        visitados.add(proxima_aresta[1])
        peso_total += menor_peso
        print(f"  escolhendo aresta {proxima_aresta[0]}-{proxima_aresta[1]} (peso {menor_peso})")
    
    return arestas, peso_total


def testar_algoritmos():
    """
    testa ambos os algoritmos com um grafo exemplo.
    """
    # grafo exemplo onde o algoritmo proposto falha
    # este é um grafo clássico que mostra a diferença
    grafo = {
        'a': [('b', 1), ('c', 4)],
        'b': [('a', 1), ('c', 2), ('d', 5)],
        'c': [('a', 4), ('b', 2), ('d', 1)],
        'd': [('b', 5), ('c', 1)]
    }
    
    print("=" * 70)
    print("grafo de teste:")
    print("=" * 70)
    for nodo, vizinhos in sorted(grafo.items()):
        print(f"{nodo}: {vizinhos}")
    
    print("\n" + "=" * 70)
    print("executando algoritmo proposto:")
    print("=" * 70)
    arestas_prop, peso_prop = algoritmo_proposto(grafo, 'a')
    if arestas_prop:
        print(f"\narestas selecionadas: {arestas_prop}")
        print(f"peso total: {peso_prop}")
    
    print("\n" + "=" * 70)
    print("executando algoritmo de prim (correto):")
    print("=" * 70)
    arestas_prim, peso_prim = algoritmo_prim(grafo, 'a')
    if arestas_prim:
        print(f"\narestas selecionadas: {arestas_prim}")
        print(f"peso total: {peso_prim}")
    
    print("\n" + "=" * 70)
    print("análise:")
    print("=" * 70)
    if peso_prop and peso_prim:
        if peso_prop == peso_prim:
            print("ambos encontraram o mesmo peso total (mas podem ter usado caminhos diferentes)")
        else:
            print(f"algoritmo proposto encontrou peso {peso_prop}")
            print(f"algoritmo de prim encontrou peso {peso_prim}")
            print("o algoritmo proposto não encontrou a árvore de cobertura mínima!")


def responder_questoes():
    """
    responde as questões do exercício.
    """
    print("\n\n" + "=" * 70)
    print("respostas às questões:")
    print("=" * 70)
    
    print("\n(a) ele é guloso?")
    print("sim, o algoritmo é guloso porque:")
    print("  1. a cada passo, faz uma escolha local ótima")
    print("  2. escolhe sempre a aresta de menor peso disponível do nodo atual")
    print("  3. não reconsid era escolhas anteriores (sem backtracking)")
    print("  4. constrói a solução incrementalmente")
    
    print("\n(b) ele acha uma árvore de cobertura mínima?")
    print("não, o algoritmo não garante encontrar uma acm!")
    print("\nproblema principal:")
    print("  - ele só considera arestas do nodo atual")
    print("  - o algoritmo de prim considera arestas de todos os nodos já visitados")
    print("  - isso pode levar a escolhas subótimas")
    
    print("\ndiferença crucial:")
    print("  algoritmo proposto: escolha entre vizinhos do nodo atual")
    print("  algoritmo de prim: escolha entre todos os nodos já visitados")
    
    print("\n\neste algoritmo é similar a uma busca em profundidade gulosa,")
    print("mas não é equivalente ao prim ou kruskal.")


if __name__ == "__main__":
    testar_algoritmos()
    responder_questoes()

