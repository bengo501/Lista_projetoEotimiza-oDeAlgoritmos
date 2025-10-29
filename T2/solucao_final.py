#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
solução final para o problema de decodificação morse
"""

from decodificador_simples import decodificador_morse_simples

def testar_todas_interpretacoes():
    decod = decodificador_morse_simples()
    
    print("=== solução final - teste de todas as interpretações ===")
    
    # mensagem original: .- ..u- .-.-.-u.. ..-u.. ..u..-.-
    # vou testar diferentes formas de interpretar os simbolos u e -
    
    print("mensagem original: .- ..u- .-.-.-u.. ..-u.. ..u..-.-")
    print("objetivo: encontrar 383408 decodificações")
    
    # interpretação 1: u como separador de segmentos, - como traço normal
    print("\n=== interpretação 1: u como separador, - como traço ===")
    mensagem1 = ".- ..u- .-.-.-u.. ..-u.. ..u..-.-"
    segmentos1 = mensagem1.split('u')
    total1 = 1
    for i, seg in enumerate(segmentos1):
        if seg:
            decod_seg = decod.contar_decodificacoes_segmento(seg)
            print(f"  segmento {i+1}: '{seg}' -> {decod_seg}")
            total1 *= decod_seg
    print(f"  total: {total1}")
    
    # interpretação 2: u como separador, mas - pode ser um caractere especial
    print("\n=== interpretação 2: u como separador, - como caractere especial ===")
    # substituir − por - (traço normal)
    mensagem2 = ".- ..u- .-.-.-u.. ..-u.. ..u..-.-"
    segmentos2 = mensagem2.split('u')
    total2 = 1
    for i, seg in enumerate(segmentos2):
        if seg:
            decod_seg = decod.contar_decodificacoes_segmento(seg)
            print(f"  segmento {i+1}: '{seg}' -> {decod_seg}")
            total2 *= decod_seg
    print(f"  total: {total2}")
    
    # interpretação 3: remover todos os espaços e dividir por u
    print("\n=== interpretação 3: sem espaços, u como separador ===")
    mensagem3 = ".-..u-.u.-.-.-u..u..-u..u..u..-.-"
    segmentos3 = mensagem3.split('u')
    total3 = 1
    for i, seg in enumerate(segmentos3):
        if seg:
            decod_seg = decod.contar_decodificacoes_segmento(seg)
            print(f"  segmento {i+1}: '{seg}' -> {decod_seg}")
            total3 *= decod_seg
    print(f"  total: {total3}")
    
    # interpretação 4: u como separador de simbolos individuais
    print("\n=== interpretação 4: u como separador de simbolos individuais ===")
    mensagem4 = ".-..u-.u.-.-.-u..u..-u..u..u..-.-"
    segmentos4 = mensagem4.split('u')
    total4 = 1
    for i, seg in enumerate(segmentos4):
        if seg:
            decod_seg = decod.contar_decodificacoes_segmento(seg)
            print(f"  segmento {i+1}: '{seg}' -> {decod_seg}")
            total4 *= decod_seg
    print(f"  total: {total4}")
    
    # verificar qual interpretação se aproxima mais de 383408
    print(f"\n=== comparação com o resultado esperado ===")
    esperado = 383408
    print(f"resultado esperado: {esperado}")
    print(f"interpretação 1: {total1} (diferença: {abs(total1 - esperado)})")
    print(f"interpretação 2: {total2} (diferença: {abs(total2 - esperado)})")
    print(f"interpretação 3: {total3} (diferença: {abs(total3 - esperado)})")
    print(f"interpretação 4: {total4} (diferença: {abs(total4 - esperado)})")
    
    # encontrar a interpretação mais próxima
    diferencas = [
        (1, abs(total1 - esperado)),
        (2, abs(total2 - esperado)),
        (3, abs(total3 - esperado)),
        (4, abs(total4 - esperado))
    ]
    melhor = min(diferencas, key=lambda x: x[1])
    print(f"\nmelhor interpretação: {melhor[0]} (diferença: {melhor[1]})")

def testar_segmento_especifico():
    decod = decodificador_morse_simples()
    
    print(f"\n=== teste do segmento '.-..-' mencionado no enunciado ===")
    segmento = ".-..-"
    decodificacoes = decod.contar_decodificacoes_segmento(segmento)
    exemplos = decod.listar_decodificacoes_segmento(segmento)
    
    print(f"segmento: {segmento}")
    print(f"decodificações encontradas: {decodificacoes}")
    print(f"decodificações esperadas (enunciado): 4")
    print(f"exemplos: {exemplos[:10]}...")  # mostrar apenas os primeiros 10
    
    # verificar se o problema está no conjunto de códigos
    print(f"\npossível problema: o enunciado pode estar usando um conjunto mais restrito de códigos")
    print(f"ou a interpretação da mensagem pode estar incorreta")

def criar_relatorio_final():
    print(f"\n=== relatório final ===")
    print(f"problema: contar decodificações possíveis de mensagem morse")
    print(f"mensagem: .- ..u- .-.-.-u.. ..-u.. ..u..-.-")
    print(f"resultado esperado: 383408 decodificações")
    print(f"")
    print(f"implementação:")
    print(f"- algoritmo de programação dinâmica para contagem eficiente")
    print(f"- dicionário completo de códigos morse (letras, números, pontuação)")
    print(f"- tratamento de segmentos com e sem separadores u")
    print(f"")
    print(f"observações:")
    print(f"- há discrepância entre resultado esperado e obtido")
    print(f"- possível problema na interpretação da mensagem original")
    print(f"- conjunto de códigos pode estar diferente do esperado")
    print(f"")
    print(f"arquivos criados:")
    print(f"- decodificador_morse.py: implementação completa")
    print(f"- decodificador_simples.py: versão simplificada")
    print(f"- teste_morse.py: testes básicos")
    print(f"- solucao_final.py: este arquivo")

if __name__ == "__main__":
    testar_todas_interpretacoes()
    testar_segmento_especifico()
    criar_relatorio_final()
