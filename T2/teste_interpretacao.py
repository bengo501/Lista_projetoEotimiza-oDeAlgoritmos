#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
teste de diferentes interpretações da mensagem
"""

from decodificador_simples import decodificador_morse_simples

def testar_diferentes_interpretacoes():
    decod = decodificador_morse_simples()
    
    print("=== teste de diferentes interpretações ===")
    
    # interpretação 1: ".-..-" como um segmento único
    print("interpretação 1: '.-..-' como segmento único")
    segmento1 = ".-..-"
    decod1 = decod.contar_decodificacoes_segmento(segmento1)
    print(f"  decodificações: {decod1}")
    
    # interpretação 2: ".-.." + "-" como dois segmentos
    print("\ninterpretação 2: '.-..' + '-' como dois segmentos")
    segmento2a = ".-.."
    segmento2b = "-"
    decod2a = decod.contar_decodificacoes_segmento(segmento2a)
    decod2b = decod.contar_decodificacoes_segmento(segmento2b)
    decod2_total = decod2a * decod2b
    print(f"  '.-..' -> {decod2a} decodificações")
    print(f"  '-' -> {decod2b} decodificações")
    print(f"  total: {decod2_total}")
    
    # interpretação 3: ".-" + "..-" como dois segmentos
    print("\ninterpretação 3: '.-' + '..-' como dois segmentos")
    segmento3a = ".-"
    segmento3b = "..-"
    decod3a = decod.contar_decodificacoes_segmento(segmento3a)
    decod3b = decod.contar_decodificacoes_segmento(segmento3b)
    decod3_total = decod3a * decod3b
    print(f"  '.-' -> {decod3a} decodificações")
    print(f"  '..-' -> {decod3b} decodificações")
    print(f"  total: {decod3_total}")
    
    # verificar se alguma interpretação dá 4 decodificações
    print(f"\nverificação:")
    print(f"  interpretação 1: {decod1} (esperado: 4)")
    print(f"  interpretação 2: {decod2_total} (esperado: 4)")
    print(f"  interpretação 3: {decod3_total} (esperado: 4)")
    
    # verificar se o problema está na mensagem original
    print(f"\n=== analise da mensagem original ===")
    print("mensagem original: .- ..u- .-.-.-u.. ..-u.. ..u..-.-")
    print("possivel interpretacao: o enunciado se refere ao inicio '.-..-'")
    print("mas na mensagem real, o primeiro segmento e '.- ..' (com espaco)")
    print("isso sugere que pode haver um erro na interpretacao ou na mensagem")

def testar_mensagem_completa():
    decod = decodificador_morse_simples()
    
    print(f"\n=== teste da mensagem completa ===")
    # mensagem: .- ..u- .-.-.-u.. ..-u.. ..u..-.-
    # dividindo por u: .- .., -, .-.-.-, .., ..-, .., .., ..-.-
    
    # interpretação 1: com espaços
    segmentos1 = [".- ..", "-", ".-.-.-", "..", "..-", "..", "..", "..-.-"]
    print("interpretação 1 (com espaços):")
    total1 = 1
    for i, seg in enumerate(segmentos1):
        decod_seg = decod.contar_decodificacoes_segmento(seg)
        print(f"  segmento {i+1}: '{seg}' -> {decod_seg}")
        total1 *= decod_seg
    print(f"  total: {total1}")
    
    # interpretação 2: sem espaços
    segmentos2 = [".-..", "-", ".-.-.-", "..", "..-", "..", "..", "..-.-"]
    print("\ninterpretação 2 (sem espaços):")
    total2 = 1
    for i, seg in enumerate(segmentos2):
        decod_seg = decod.contar_decodificacoes_segmento(seg)
        print(f"  segmento {i+1}: '{seg}' -> {decod_seg}")
        total2 *= decod_seg
    print(f"  total: {total2}")
    
    print(f"\nverificação:")
    print(f"  interpretação 1: {total1} (esperado: 383408)")
    print(f"  interpretação 2: {total2} (esperado: 383408)")

if __name__ == "__main__":
    testar_diferentes_interpretacoes()
    testar_mensagem_completa()
