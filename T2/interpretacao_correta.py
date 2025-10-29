#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
interpretação correta da mensagem morse do enunciado
"""

# mensagem original: .- ..∪- .-.-.-∪.. ..−∪.. ..∪..−.-
# analisando melhor, parece que o ∪ não está separando corretamente

# tentativa 1: interpretar ∪ como separador de símbolos individuais
mensagem1 = ".- ..u- .-.-.-u.. ..-u.. ..u..-.-"
print("tentativa 1 - u como separador de segmentos:")
segmentos1 = mensagem1.split('u')
for i, seg in enumerate(segmentos1):
    print(f"  {i+1}: '{seg}'")

# tentativa 2: interpretar ∪ como separador de símbolos individuais
# removendo espaços e dividindo por ∪
mensagem2 = ".-..u-.u.-.-.-u..u..-u..u..u..-.-"
print("\ntentativa 2 - u como separador de simbolos individuais:")
segmentos2 = mensagem2.split('u')
for i, seg in enumerate(segmentos2):
    print(f"  {i+1}: '{seg}'")

# tentativa 3: interpretar a mensagem sem espaços
mensagem3 = ".-..u-.u.-.-.-u..u..-u..u..u..-.-"
print("\ntentativa 3 - sem espacos:")
print(f"mensagem: {mensagem3}")
segmentos3 = mensagem3.split('u')
for i, seg in enumerate(segmentos3):
    print(f"  {i+1}: '{seg}'")

# verificar se o primeiro segmento ".-..-" tem 4 decodificações
from decodificador_morse import decodificador_morse
decod = decodificador_morse()

print("\n=== teste do segmento '.-..-' ===")
segmento_teste = ".-..-"
decodificacoes = decod._contar_decodificacoes_segmento(segmento_teste)
print(f"segmento: {segmento_teste}")
print(f"numero de decodificacoes: {decodificacoes}")

# listar as decodificações
exemplos = decod._listar_decodificacoes_segmento(segmento_teste)
print(f"decodificacoes: {exemplos}")

print(f"\nverificacao: o enunciado diz que '.-..-' tem 4 decodificacoes")
print(f"nosso resultado: {decodificacoes} decodificacoes")
print(f"diferenca: {abs(decodificacoes - 4)}")
