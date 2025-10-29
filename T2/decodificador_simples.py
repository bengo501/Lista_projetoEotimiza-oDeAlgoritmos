#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decodificador morse simplificado - apenas códigos básicos
"""

class decodificador_morse_simples:
    def __init__(self):
        # apenas códigos básicos: letras, números e pontuação essencial
        self.codigo_morse = {
            # letras a-z
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
            'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
            's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..',
            
            # números 0-9
            '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            
            # pontuação básica
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
            '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
            '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
            '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.'
        }
        
        # criar mapeamento reverso
        self.codigo_para_caracteres = {}
        for char, codigo in self.codigo_morse.items():
            if codigo not in self.codigo_para_caracteres:
                self.codigo_para_caracteres[codigo] = []
            self.codigo_para_caracteres[codigo].append(char)
    
    def contar_decodificacoes_segmento(self, segmento):
        """
        conta decodificações possíveis para um segmento sem ∪
        """
        n = len(segmento)
        if n == 0:
            return 1
        
        # dp[i] = número de decodificações possíveis para os primeiros i caracteres
        dp = [0] * (n + 1)
        dp[0] = 1  # string vazia tem 1 decodificação (vazia)
        
        for i in range(1, n + 1):
            # tentar todos os possíveis códigos que terminam na posição i-1
            for j in range(i):
                codigo_candidato = segmento[j:i]
                if codigo_candidato in self.codigo_para_caracteres:
                    dp[i] += dp[j]
        
        return dp[n]
    
    def listar_decodificacoes_segmento(self, segmento):
        """
        lista decodificações possíveis para um segmento sem ∪
        """
        if not segmento:
            return ['']
        
        decodificacoes = []
        n = len(segmento)
        
        def backtrack(pos, decodificacao_atual):
            if pos == n:
                decodificacoes.append(decodificacao_atual)
                return
            
            # tentar todos os possíveis códigos que começam na posição pos
            for i in range(pos + 1, n + 1):
                codigo_candidato = segmento[pos:i]
                if codigo_candidato in self.codigo_para_caracteres:
                    for char in self.codigo_para_caracteres[codigo_candidato]:
                        backtrack(i, decodificacao_atual + char)
        
        backtrack(0, '')
        return decodificacoes

def main():
    decod = decodificador_morse_simples()
    
    print("=== teste com segmento '.-..-' ===")
    segmento = ".-..-"
    decodificacoes = decod.contar_decodificacoes_segmento(segmento)
    exemplos = decod.listar_decodificacoes_segmento(segmento)
    
    print(f"segmento: {segmento}")
    print(f"numero de decodificacoes: {decodificacoes}")
    print(f"decodificacoes: {exemplos}")
    
    print(f"\nverificacao: o enunciado diz que '.-..-' tem 4 decodificacoes")
    print(f"nosso resultado: {decodificacoes} decodificacoes")
    print(f"diferenca: {abs(decodificacoes - 4)}")
    
    # verificar quais códigos estão sendo usados
    print(f"\nanalise das decodificacoes:")
    for decod_exemplo in exemplos:
        print(f"  '{decod_exemplo}' -> ", end="")
        # mostrar como foi decodificado
        pos = 0
        for char in decod_exemplo:
            # encontrar o código morse para este caractere
            for codigo, chars in decod.codigo_para_caracteres.items():
                if char in chars:
                    print(f"{codigo} ", end="")
                    break
        print()

if __name__ == "__main__":
    main()
