#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
análise final da mensagem morse
"""

# mensagem original do enunciado: .- ..∪- .-.-.-∪.. ..−∪.. ..∪..−.-
# substituindo ∪ por u para evitar problemas de codificação

mensagem_original = ".- ..u- .-.-.-u.. ..-u.. ..u..-.-"

print("mensagem original (u substituindo o simbolo de uniao):", mensagem_original)
print("tamanho:", len(mensagem_original))

# dividir por u
segmentos = mensagem_original.split('u')
print(f"numero de segmentos: {len(segmentos)}")

for i, segmento in enumerate(segmentos):
    print(f"segmento {i+1}: '{segmento}' (tamanho: {len(segmento)})")

print("\nanalise da mensagem do enunciado:")
print("mensagem: .- ..u- .-.-.-u.. ..-u.. ..u..-.-")
print("segmentos:")
print("1: .- ..")
print("2: - .-.-.-") 
print("3: .. ..-")
print("4: .. ..")
print("5: ..-.-")

print("\nobservacao: o enunciado menciona que apenas o inicio '.-..-' pode ser decodificado de 4 formas diferentes")
print("mas na mensagem completa, o primeiro segmento e '.- ..' (com espaco), nao '.-..-'")
print("isso sugere que pode haver um erro na interpretacao da mensagem")
