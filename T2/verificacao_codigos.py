#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificação dos códigos morse utilizados
"""

from decodificador_morse import decodificador_morse

def verificar_codigo_morse():
    decod = decodificador_morse()
    
    print("=== verificação dos códigos morse ===")
    print("códigos de 1 caractere:")
    for char, codigo in decod.codigo_morse.items():
        if len(codigo) == 1:
            print(f"  {char}: {codigo}")
    
    print("\ncódigos de 2 caracteres:")
    for char, codigo in decod.codigo_morse.items():
        if len(codigo) == 2:
            print(f"  {char}: {codigo}")
    
    print("\ncódigos de 3 caracteres:")
    for char, codigo in decod.codigo_morse.items():
        if len(codigo) == 3:
            print(f"  {char}: {codigo}")
    
    print("\ncódigos de 4 caracteres:")
    for char, codigo in decod.codigo_morse.items():
        if len(codigo) == 4:
            print(f"  {char}: {codigo}")
    
    print("\ncódigos de 5 caracteres:")
    for char, codigo in decod.codigo_morse.items():
        if len(codigo) == 5:
            print(f"  {char}: {codigo}")

def testar_segmento_especifico():
    decod = decodificador_morse()
    
    print("\n=== teste específico do segmento '.-..-' ===")
    segmento = ".-..-"
    
    # verificar todas as possíveis decodificações passo a passo
    print(f"segmento: {segmento}")
    print("tamanho: 5 caracteres")
    
    # tentar todas as possíveis divisões
    print("\npossíveis divisões:")
    
    # divisão 1: 1 + 4
    parte1 = segmento[0:1]  # "."
    parte2 = segmento[1:5]  # "-..-"
    print(f"  divisão 1+4: '{parte1}' + '{parte2}'")
    if parte1 in decod.codigo_para_caracteres:
        print(f"    '{parte1}' -> {decod.codigo_para_caracteres[parte1]}")
    if parte2 in decod.codigo_para_caracteres:
        print(f"    '{parte2}' -> {decod.codigo_para_caracteres[parte2]}")
    
    # divisão 2: 2 + 3
    parte1 = segmento[0:2]  # ".-"
    parte2 = segmento[2:5]  # "..-"
    print(f"  divisão 2+3: '{parte1}' + '{parte2}'")
    if parte1 in decod.codigo_para_caracteres:
        print(f"    '{parte1}' -> {decod.codigo_para_caracteres[parte1]}")
    if parte2 in decod.codigo_para_caracteres:
        print(f"    '{parte2}' -> {decod.codigo_para_caracteres[parte2]}")
    
    # divisão 3: 3 + 2
    parte1 = segmento[0:3]  # ".-."
    parte2 = segmento[3:5]  # ".-"
    print(f"  divisão 3+2: '{parte1}' + '{parte2}'")
    if parte1 in decod.codigo_para_caracteres:
        print(f"    '{parte1}' -> {decod.codigo_para_caracteres[parte1]}")
    if parte2 in decod.codigo_para_caracteres:
        print(f"    '{parte2}' -> {decod.codigo_para_caracteres[parte2]}")
    
    # divisão 4: 4 + 1
    parte1 = segmento[0:4]  # ".-.."
    parte2 = segmento[4:5]  # "-"
    print(f"  divisão 4+1: '{parte1}' + '{parte2}'")
    if parte1 in decod.codigo_para_caracteres:
        print(f"    '{parte1}' -> {decod.codigo_para_caracteres[parte1]}")
    if parte2 in decod.codigo_para_caracteres:
        print(f"    '{parte2}' -> {decod.codigo_para_caracteres[parte2]}")
    
    # divisão 5: 5 + 0 (segmento completo)
    parte1 = segmento[0:5]  # ".-..-"
    print(f"  divisão 5+0: '{parte1}' + ''")
    if parte1 in decod.codigo_para_caracteres:
        print(f"    '{parte1}' -> {decod.codigo_para_caracteres[parte1]}")
    
    # verificar subdivisões mais complexas
    print("\nsubdivisões mais complexas:")
    
    # 1 + 1 + 3
    print(f"  1+1+3: '{segmento[0:1]}' + '{segmento[1:2]}' + '{segmento[2:5]}'")
    if segmento[0:1] in decod.codigo_para_caracteres:
        print(f"    '{segmento[0:1]}' -> {decod.codigo_para_caracteres[segmento[0:1]]}")
    if segmento[1:2] in decod.codigo_para_caracteres:
        print(f"    '{segmento[1:2]}' -> {decod.codigo_para_caracteres[segmento[1:2]]}")
    if segmento[2:5] in decod.codigo_para_caracteres:
        print(f"    '{segmento[2:5]}' -> {decod.codigo_para_caracteres[segmento[2:5]]}")
    
    # 1 + 2 + 2
    print(f"  1+2+2: '{segmento[0:1]}' + '{segmento[1:3]}' + '{segmento[3:5]}'")
    if segmento[0:1] in decod.codigo_para_caracteres:
        print(f"    '{segmento[0:1]}' -> {decod.codigo_para_caracteres[segmento[0:1]]}")
    if segmento[1:3] in decod.codigo_para_caracteres:
        print(f"    '{segmento[1:3]}' -> {decod.codigo_para_caracteres[segmento[1:3]]}")
    if segmento[3:5] in decod.codigo_para_caracteres:
        print(f"    '{segmento[3:5]}' -> {decod.codigo_para_caracteres[segmento[3:5]]}")

if __name__ == "__main__":
    verificar_codigo_morse()
    testar_segmento_especifico()
