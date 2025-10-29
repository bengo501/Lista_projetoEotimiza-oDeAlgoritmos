#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
análise da mensagem morse do enunciado
"""

# mensagem original do enunciado: .- ..∪- .-.-.-∪.. ..−∪.. ..∪..−.-
# vou analisar cada parte separadamente

# usando caracteres ascii para evitar problemas de codificação
mensagem_original = ".- ..u- .-.-.-u.. ..-u.. ..u..-.-"

print("mensagem original (com u substituindo ∪):", mensagem_original)
print("tamanho:", len(mensagem_original))

# dividir por u
segmentos = mensagem_original.split('u')
print(f"numero de segmentos: {len(segmentos)}")

for i, segmento in enumerate(segmentos):
    print(f"segmento {i+1}: '{segmento}' (tamanho: {len(segmento)})")

# analisar se há caracteres que não são . - ou u
caracteres_validos = ['.', '-', 'u']
caracteres_especiais = []
for char in mensagem_original:
    if char not in caracteres_validos and char != ' ':
        caracteres_especiais.append(char)

if caracteres_especiais:
    print(f"\ncaracteres especiais encontrados: {caracteres_especiais}")
else:
    print("\nnenhum caractere especial encontrado")

# verificar se a mensagem está correta
print("\nverificacao da mensagem:")
print("esperado: .- ..∪- .-.-.-∪.. ..−∪.. ..∪..−.-")
print("atual:    .- ..u- .-.-.-u.. ..-u.. ..u..-.-")
print("diferenca nos caracteres especiais:")
print("- posicao 4: esperado ∪, atual u")
print("- posicao 12: esperado ∪, atual u") 
print("- posicao 19: esperado ∪, atual u")
print("- posicao 25: esperado ∪, atual u")
