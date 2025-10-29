# solução t2 - decodificador de código morse

## problema

contar quantas decodificações diferentes são possíveis para uma mensagem em código morse, considerando que quando não há separadores ∪, os pontos e traços podem ser segmentados de várias formas válidas.

## mensagem de exemplo

```
.- ..∪- .-.-.-∪.. ..−∪.. ..∪..−.-
```

resultado esperado: 383408 decodificações

## implementação

### arquivos criados

1. **decodificador_morse.py** - implementação completa com interface interativa
2. **decodificador_simples.py** - versão simplificada focada no algoritmo
3. **teste_morse.py** - testes básicos
4. **solucao_final.py** - análise de diferentes interpretações
5. **README.md** - esta documentação

### algoritmo

utiliza programação dinâmica para contar decodificações eficientemente:

```python
def contar_decodificacoes_segmento(self, segmento):
    n = len(segmento)
    dp = [0] * (n + 1)
    dp[0] = 1  # string vazia tem 1 decodificação
    
    for i in range(1, n + 1):
        for j in range(i):
            codigo_candidato = segmento[j:i]
            if codigo_candidato in self.codigo_para_caracteres:
                dp[i] += dp[j]
    
    return dp[n]
```

### códigos morse utilizados

baseado nas observações fornecidas, inclui:

- **letras a-z**: códigos de 1 a 4 caracteres
- **números 0-9**: códigos de 5 caracteres
- **pontuação**: códigos de 2 a 6 caracteres
- **prosigns**: sinais operacionais

## resultados obtidos

### interpretação da mensagem

testei diferentes interpretações do símbolo ∪:

1. **com espaços**: 0 decodificações (segmentos inválidos)
2. **sem espaços**: 193536 decodificações
3. **separador de símbolos**: 193536 decodificações

### comparação com esperado

- **resultado esperado**: 383408
- **melhor resultado obtido**: 193536
- **diferença**: 189872

## análise do problema

### discrepâncias encontradas

1. **segmento ".-..-"**: 
   - enunciado diz: 4 decodificações
   - algoritmo encontra: 15 decodificações

2. **mensagem completa**:
   - enunciado diz: 383408 decodificações
   - algoritmo encontra: 193536 decodificações

### possíveis causas

1. **conjunto de códigos diferente**: o enunciado pode estar usando um conjunto mais restrito
2. **interpretação da mensagem**: pode haver erro na interpretação dos símbolos ∪ e −
3. **códigos especiais**: alguns códigos podem não estar incluídos no conjunto básico

## como usar

### execução básica

```bash
python decodificador_simples.py
```

### execução completa

```bash
python decodificador_morse.py
```

### teste de interpretações

```bash
python solucao_final.py
```

## funcionalidades

- ✅ contagem eficiente de decodificações
- ✅ listagem de decodificações possíveis
- ✅ análise de segmentos individuais
- ✅ interface para entrada de mensagens
- ✅ tratamento de separadores ∪
- ✅ dicionário completo de códigos morse

## limitações

- há discrepância entre resultado esperado e obtido
- possível problema na interpretação da mensagem original
- conjunto de códigos pode estar diferente do esperado

## conclusão

a implementação está funcional e utiliza algoritmos eficientes, mas há uma discrepância significativa entre o resultado esperado (383408) e o obtido (193536). isso sugere que pode haver um problema na interpretação da mensagem original ou no conjunto de códigos morse utilizado.
