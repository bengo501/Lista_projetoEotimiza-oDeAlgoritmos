"""
exercício 2: explicação de por que o selectionsort é um algoritmo guloso

o selectionsort é um algoritmo guloso porque:

1. em cada iteração, ele faz uma escolha "gulosa" localmente ótima:
   - procura o menor elemento restante no array não ordenado
   - coloca esse elemento na próxima posição da parte ordenada

2. esta escolha é irrevogável - uma vez colocado o elemento em sua posição,
   ele não é mais movido

3. não há "olhar para trás" ou reconsideração de escolhas anteriores

4. a estratégia gulosa é: "sempre escolha o menor elemento disponível"

5. essa escolha gulosa leva à solução globalmente ótima (array ordenado)

características do selectionsort como algoritmo guloso:
- escolha gulosa: selecionar o mínimo/máximo a cada passo
- subestrutura ótima: ordenar n elementos = escolher o menor + ordenar n-1
- sem backtracking: decisões não são revertidas
- solução incremental: constrói a solução passo a passo
"""

def selection_sort(arr):
    """
    implementação do selectionsort com comentários explicando
    a natureza gulosa do algoritmo.
    """
    n = len(arr)
    print("ordenando array:", arr)
    print("\npasso a passo:")
    print("-" * 60)
    
    for i in range(n):
        # escolha gulosa: encontrar o menor elemento no restante do array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # colocar o menor elemento na posição atual (escolha irrevogável)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(f"iteração {i+1}: escolhido {arr[i]:2d} (posição {min_idx}) -> {arr}")
    
    print("-" * 60)
    return arr


def demonstrar_natureza_gulosa():
    """
    demonstra por que o selectionsort é guloso com exemplos.
    """
    print("=" * 70)
    print("por que o selectionsort é um algoritmo guloso?")
    print("=" * 70)
    
    print("\n1. estratégia gulosa:")
    print("   - a cada passo, escolhe o menor elemento disponível")
    print("   - esta é uma decisão local ótima")
    
    print("\n2. escolhas irrevogáveis:")
    print("   - uma vez posicionado, o elemento não é mais movido")
    print("   - não há backtracking ou reconsideração")
    
    print("\n3. construção incremental:")
    print("   - a solução é construída passo a passo")
    print("   - cada passo estende a parte ordenada do array")
    
    print("\n4. otimalidade global:")
    print("   - as escolhas gulosas locais levam à solução global ótima")
    print("   - o array fica completamente ordenado")
    
    print("\n\nexemplo prático:")
    print("=" * 70)
    
    arr = [64, 25, 12, 22, 11]
    resultado = selection_sort(arr.copy())
    
    print(f"\narray original: [64, 25, 12, 22, 11]")
    print(f"array ordenado: {resultado}")
    
    print("\n\ncomparação com outros algoritmos gulosos:")
    print("=" * 70)
    print("similaridade com outros algoritmos gulosos:")
    print("- dijkstra: escolhe o vértice mais próximo")
    print("- prim: escolhe a aresta de menor peso")
    print("- selectionsort: escolhe o menor elemento")
    print("\ntodos fazem escolhas localmente ótimas e irrevogáveis!")


if __name__ == "__main__":
    demonstrar_natureza_gulosa()
    
    print("\n\ntestando com outro exemplo:")
    print("=" * 70)
    arr2 = [3, 7, 1, 9, 2]
    selection_sort(arr2)

