#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
teste do decodificador de código morse
"""

from decodificador_morse import decodificador_morse

def main():
    decodificador = decodificador_morse()
    
    print("=== teste com mensagem do enunciado ===")
    # mensagem original: .- ..∪- .-.-.-∪.. ..−∪.. ..∪..−.-
    mensagem_exemplo = ".- ..u- .-.-.-u.. ..-u.. ..u..-.-"
    
    total = decodificador.contar_decodificacoes(mensagem_exemplo)
    print(f"mensagem: {mensagem_exemplo}")
    print(f"total de decodificacoes possiveis: {total}")
    
    # verificar se bate com o enunciado (383408)
    print(f"resultado esperado no enunciado: 383408")
    print(f"diferenca: {abs(total - 383408)}")
    
    print("\n=== teste com segmento simples ===")
    # teste com ".-..-" que deveria ter 4 decodificações segundo o enunciado
    segmento_teste = ".-..-"
    decodificacoes = decodificador._contar_decodificacoes_segmento(segmento_teste)
    print(f"segmento: {segmento_teste}")
    print(f"decodificacoes: {decodificacoes}")
    
    # listar as decodificações
    exemplos = decodificador._listar_decodificacoes_segmento(segmento_teste)
    print(f"exemplos: {exemplos}")
    
    print("\n=== analise detalhada da mensagem ===")
    segmentos = mensagem_exemplo.split('u')
    for i, segmento in enumerate(segmentos):
        if segmento:
            decod = decodificador._contar_decodificacoes_segmento(segmento)
            print(f"segmento {i+1}: '{segmento}' -> {decod} decodificacoes")

if __name__ == "__main__":
    main()
