# solucoes - lista de exercicios de otimizacao de algoritmos

prof. joao b. oliveira

## estrutura

as solucoes estao organizadas por topico:

```
solucoes/
├── 1_gulosos/              # algoritmos gulosos
├── 2_divisao_conquista/    # divisao e conquista
├── 3_programacao_dinamica/ # programacao dinamica
├── 4_backtracking/         # backtracking
└── 5_algoritmos_geneticos/ # algoritmos geneticos
```

## 1. algoritmos gulosos

- **ex1_problema_moedas.py**: problema das moedas (17, 8, 1 centavos)
- **ex2_selectionsort_guloso.py**: explicacao de por que selectionsort e guloso
- **ex3_arvore_cobertura_minima.py**: analise de algoritmo de acm
- **ex4_selecao_atividades.py**: problema de selecao de atividades
- **ex5_ponto_equilibrio.py**: encontrar ponto de equilibrio em o(n)
- **ex6_coloracao_grafos.py**: coloracao de grafos (problema np-completo)

## 2. divisao e conquista

- **ex1_pesquisa_binaria.py**: pesquisa binaria com testes
- **ex2_pesquisa_ternaria.py**: pesquisa ternaria (divisao em 3)
- **ex3_mergesort.py**: mergesort 2 e 3 partes
- **ex4_camponeses_russos.py**: multiplicacao russa (base 2 e 5)
- **ex5_subconjuntos.py**: gerar todos os subconjuntos
- **ex6_indice_fixo.py**: encontrar a[i]=i em o(log n)
- **ex7_subset_sum.py**: subset sum problem
- **ex8_analise_complexidade.py**: analise com teorema mestre
- **ex9_permutacoes.py**: gerar todas as permutacoes

## 3. programacao dinamica

- **ex1_fibonacci.py**: fibonacci com o(1) memoria
- **ex2_calcadas.py**: problema das calcadas coloridas
- **ex3_formula_vovo.py**: formula zn (3 implementacoes)
- **ex4_coisa_nk.py**: funcao coisa(n,k) nao recursiva
- **ex5_formula_vovo_2vars.py**: formula zn,k com duas variaveis

## 4. backtracking

- **ex1_soma_quadrados.py**: sequencia com somas quadradas perfeitas
- **ex2_n_rainhas.py**: problema das n rainhas
- **ex3_passeio_cavalo.py**: passeio do cavalo (knights tour)

## 5. algoritmos geneticos

- **ex1_ajuste_polinomio.py**: ajuste de polinomio por ag

## como executar

cada arquivo python e independente e pode ser executado diretamente:

```bash
# exemplo: executar problema das moedas
python solucoes/1_gulosos/ex1_problema_moedas.py

# exemplo: executar pesquisa binaria
python solucoes/2_divisao_conquista/ex1_pesquisa_binaria.py

# exemplo: executar fibonacci
python solucoes/3_programacao_dinamica/ex1_fibonacci.py

# exemplo: executar n rainhas
python solucoes/4_backtracking/ex2_n_rainhas.py

# exemplo: executar algoritmo genetico
python solucoes/5_algoritmos_geneticos/ex1_ajuste_polinomio.py
```

## caracteristicas das solucoes

- **codigo bem documentado**: cada funcao tem docstrings explicativas
- **exemplos praticos**: casos de teste demonstrando o funcionamento
- **analise de complexidade**: explicacoes de tempo e espaco
- **visualizacoes**: saidas formatadas para facil compreensao
- **comparacoes**: diferentes abordagens quando aplicavel
- **explicacoes teoricas**: conceitos fundamentais explicados

## topicos cobertos

### algoritmos gulosos
- escolha localmente otima
- prova de corretude (quando possivel)
- casos onde guloso falha

### divisao e conquista
- divisao do problema
- resolucao recursiva
- combinacao de solucoes
- teorema mestre

### programacao dinamica
- subestrutura otima
- sobreposicao de subproblemas
- memoizacao (top-down)
- tabulacao (bottom-up)
- otimizacao de espaco

### backtracking
- exploracao do espaco de solucoes
- poda de ramos invalidos
- otimizacao com heuristicas
- problemas classicos (rainhas, cavalo)

### algoritmos geneticos
- representacao de individuos
- funcao de fitness
- selecao
- crossover
- mutacao
- elitismo

## observacoes

- todos os codigos seguem as regras especificadas (minusculas, sem emojis)
- linguagem: python 3.6+
- nao requer bibliotecas externas (apenas stdlib)
- codigo pronto para execucao

## autor

implementacoes desenvolvidas como solucao para a lista de exercicios
do prof. joao b. oliveira.

