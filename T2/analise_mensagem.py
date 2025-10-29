#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
análise da mensagem morse do enunciado
"""

# mensagem original do enunciado: .- ..∪- .-.-.-∪.. ..−∪.. ..∪..−.-
# vou analisar cada parte separadamente

mensagem_original = ".- ..∪- .-.-.-∪.. ..−∪.. ..∪..−.-"

print("mensagem original:", mensagem_original)
print("tamanho:", len(mensagem_original))

# dividir por ∪
segmentos = mensagem_original.split('∪')
print(f"numero de segmentos: {len(segmentos)}")

for i, segmento in enumerate(segmentos):
    print(f"segmento {i+1}: '{segmento}' (tamanho: {len(segmento)})")

# analisar caracteres especiais
print("\nanalise de caracteres:")
for i, char in enumerate(mensagem_original):
    print(f"posicao {i}: '{char}' (unicode: {ord(char)})")

# verificar se há caracteres especiais que não são . - ou ∪
caracteres_especiais = []
for char in mensagem_original:
    if char not in ['.', '-', '∪', ' ']:
        caracteres_especiais.append(char)

if caracteres_especiais:
    print(f"\ncaracteres especiais encontrados: {caracteres_especiais}")
else:
    print("\nnenhum caractere especial encontrado")
