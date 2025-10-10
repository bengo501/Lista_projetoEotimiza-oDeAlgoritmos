"""
exercício 4: problema de seleção de atividades

duas estratégias:
(a) escolher as atividades mais curtas
(b) escolher as que terminam o mais cedo possível
"""

def algoritmo_mais_curtas(atividades):
    """
    escolhe atividades dando preferência às mais curtas.
    """
    # ordena por duração (fim - início)
    atividades_ordenadas = sorted(atividades, key=lambda x: x[2] - x[1])
    
    selecionadas = []
    
    for id_ativ, inicio, fim in atividades_ordenadas:
        # verifica se não há conflito com atividades já selecionadas
        conflito = False
        for _, inicio_sel, fim_sel in selecionadas:
            if not (fim <= inicio_sel or inicio >= fim_sel):
                conflito = True
                break
        
        if not conflito:
            selecionadas.append((id_ativ, inicio, fim))
    
    return selecionadas


def algoritmo_termina_cedo(atividades):
    """
    escolhe atividades dando preferência às que terminam mais cedo.
    este é o algoritmo correto e ótimo.
    """
    # ordena por tempo de término
    atividades_ordenadas = sorted(atividades, key=lambda x: x[2])
    
    selecionadas = []
    ultimo_fim = 0
    
    for id_ativ, inicio, fim in atividades_ordenadas:
        # se a atividade começa após o término da última selecionada
        if inicio >= ultimo_fim:
            selecionadas.append((id_ativ, inicio, fim))
            ultimo_fim = fim
    
    return selecionadas


def visualizar_atividades(atividades, selecionadas, titulo):
    """
    visualiza as atividades em formato de linha do tempo.
    """
    print(f"\n{titulo}")
    print("=" * 70)
    
    # cria um conjunto com ids das atividades selecionadas
    ids_selecionadas = {ativ[0] for ativ in selecionadas}
    
    print("\nlinha do tempo:")
    print("atividade | tempo |" + "".join([str(i % 10) for i in range(12)]))
    print("----------|-------|" + "-" * 12)
    
    for id_ativ, inicio, fim in sorted(atividades, key=lambda x: x[0]):
        duracao = fim - inicio
        timeline = [' '] * 12
        
        for t in range(inicio, min(fim, 12)):
            timeline[t] = '█'
        
        marcador = '*' if id_ativ in ids_selecionadas else ' '
        print(f"{marcador}  {id_ativ:2d}     | {inicio:2d}-{fim:2d}  |{''.join(timeline)}")
    
    print("\n* = atividade selecionada")
    print(f"\ntotal de atividades selecionadas: {len(selecionadas)}")
    print("atividades selecionadas:", [a[0] for a in sorted(selecionadas, key=lambda x: x[1])])


def testar_algoritmos():
    """
    testa ambos os algoritmos com as atividades do exercício.
    """
    # dados do exercício
    atividades = [
        (1, 2, 4),
        (2, 1, 4),
        (3, 2, 7),
        (4, 4, 8),
        (5, 4, 9),
        (6, 6, 8),
        (7, 5, 10),
        (8, 7, 9),
        (9, 7, 10),
        (10, 8, 11)
    ]
    
    print("=" * 70)
    print("atividades disponíveis:")
    print("=" * 70)
    print("atividade | início | fim | duração")
    print("-" * 40)
    for id_ativ, inicio, fim in atividades:
        print(f"   {id_ativ:2d}     |   {inicio:2d}   |  {fim:2d} |   {fim-inicio:2d}")
    
    # testa algoritmo (a): mais curtas
    selecionadas_curtas = algoritmo_mais_curtas(atividades)
    visualizar_atividades(atividades, selecionadas_curtas, 
                          "algoritmo (a): atividades mais curtas")
    
    # testa algoritmo (b): terminam mais cedo
    selecionadas_cedo = algoritmo_termina_cedo(atividades)
    visualizar_atividades(atividades, selecionadas_cedo,
                         "algoritmo (b): terminam mais cedo")
    
    # comparação
    print("\n" + "=" * 70)
    print("comparação dos resultados:")
    print("=" * 70)
    print(f"algoritmo (a) - mais curtas: {len(selecionadas_curtas)} atividades")
    print(f"algoritmo (b) - terminam cedo: {len(selecionadas_cedo)} atividades")
    
    if len(selecionadas_cedo) >= len(selecionadas_curtas):
        print("\no algoritmo (b) é superior ou igual ao (a)!")
    else:
        print("\no algoritmo (a) foi melhor neste caso!")
    
    print("\nconclusão:")
    print("  o algoritmo que escolhe as atividades que terminam mais cedo")
    print("  é comprovadamente ótimo para este problema.")
    print("  este é o algoritmo clássico de interval scheduling.")


if __name__ == "__main__":
    testar_algoritmos()

