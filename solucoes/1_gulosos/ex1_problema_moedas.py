"""
exercício 1: problema das moedas com valores 17, 8 e 1 centavos
objetivo: encontrar o menor número de moedas para dar troco
"""

def troco_guloso(valor, moedas):
    """
    algoritmo guloso para o problema das moedas.
    escolhe sempre a maior moeda possível.
    
    args:
        valor: valor do troco a ser dado
        moedas: lista de valores das moedas disponíveis (ordenada decrescente)
    
    returns:
        lista com as moedas usadas
    """
    resultado = []
    restante = valor
    
    for moeda in moedas:
        while restante >= moeda:
            resultado.append(moeda)
            restante -= moeda
    
    return resultado


def verificar_todos_trocos(moedas):
    """
    verifica se o algoritmo funciona corretamente para todos os valores de 1 a 100.
    """
    print(f"testando troco com moedas: {moedas}\n")
    print("valor | moedas usadas | quantidade | total verificado")
    print("-" * 60)
    
    todos_corretos = True
    
    for valor in range(1, 101):
        moedas_usadas = troco_guloso(valor, moedas)
        quantidade = len(moedas_usadas)
        total = sum(moedas_usadas)
        
        # verifica se o troco está correto
        correto = (total == valor)
        
        if not correto:
            todos_corretos = False
        
        status = "ok" if correto else "erro!"
        
        # mostra alguns exemplos
        if valor <= 20 or not correto:
            print(f"{valor:5d} | {str(moedas_usadas):30s} | {quantidade:10d} | {status}")
    
    print("\n" + "=" * 60)
    if todos_corretos:
        print("todos os trocos de 1 a 100 funcionam corretamente!")
    else:
        print("alguns trocos apresentaram erros!")
    
    return todos_corretos


def analise_otimalidade(moedas):
    """
    analisa se o algoritmo guloso sempre retorna o número mínimo de moedas.
    """
    print("\n\nanálise de otimalidade:")
    print("=" * 60)
    
    # para moedas [17, 8, 1], vamos verificar alguns casos específicos
    casos_teste = [
        (1, 1), (8, 1), (9, 2), (16, 2), (17, 1),
        (24, 3), (25, 2), (30, 3), (34, 2), (50, 3)
    ]
    
    print("\nalguns casos de teste com número esperado de moedas:")
    print("valor | moedas usadas | qtd | esperado | otimo?")
    print("-" * 60)
    
    for valor, esperado in casos_teste:
        moedas_usadas = troco_guloso(valor, moedas)
        quantidade = len(moedas_usadas)
        otimo = "sim" if quantidade == esperado else "não"
        
        print(f"{valor:5d} | {str(moedas_usadas):30s} | {quantidade:3d} | {esperado:8d} | {otimo}")


if __name__ == "__main__":
    moedas = [17, 8, 1]  # deve estar em ordem decrescente
    
    # testa para todos os valores de 1 a 100
    verificar_todos_trocos(moedas)
    
    # analisa otimalidade
    analise_otimalidade(moedas)

