#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
decodificador de código morse - conta decodificações possíveis
baseado no enunciado do t2 e nas observações fornecidas
"""

class decodificador_morse:
    def __init__(self):
        # dicionário completo de código morse baseado nas observações
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
            
            # pontuação
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
            '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
            '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
            '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.',
            
            # prosigns (sinais operacionais)
            'k': '-.-',  # convite geral para transmitir
            'ct': '-.-.-',  # início de transmissão
            'rn': '.-.-.',  # próxima mensagem
            'sk': '...-.-',  # fim de trabalho
            'hh': '........',  # erro
            'verified': '...-.',  # verificado
            'as': '.-...'  # aguarde
        }
        
        # criar mapeamento reverso: código -> caracteres possíveis
        self.codigo_para_caracteres = {}
        for char, codigo in self.codigo_morse.items():
            if codigo not in self.codigo_para_caracteres:
                self.codigo_para_caracteres[codigo] = []
            self.codigo_para_caracteres[codigo].append(char)
    
    def contar_decodificacoes(self, mensagem):
        """
        conta quantas decodificações diferentes são possíveis para uma mensagem morse
        """
        # remover espaços e dividir por u (substituindo ∪)
        segmentos = mensagem.replace(' ', '').split('u')
        
        total_decodificacoes = 1
        
        for segmento in segmentos:
            if segmento:  # se o segmento não estiver vazio
                decodificacoes_segmento = self._contar_decodificacoes_segmento(segmento)
                total_decodificacoes *= decodificacoes_segmento
        
        return total_decodificacoes
    
    def _contar_decodificacoes_segmento(self, segmento):
        """
        conta decodificações possíveis para um segmento sem ∪
        usa programação dinâmica para eficiência
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
    
    def listar_decodificacoes(self, mensagem, max_decodificacoes=100):
        """
        lista as decodificações possíveis (limitado para evitar explosão)
        """
        segmentos = mensagem.replace(' ', '').split('u')
        decodificacoes = ['']
        
        for segmento in segmentos:
            if segmento:
                novas_decodificacoes = []
                decodificacoes_segmento = self._listar_decodificacoes_segmento(segmento)
                
                for decod_anterior in decodificacoes:
                    for decod_segmento in decodificacoes_segmento:
                        if len(novas_decodificacoes) >= max_decodificacoes:
                            break
                        novas_decodificacoes.append(decod_anterior + decod_segmento)
                    if len(novas_decodificacoes) >= max_decodificacoes:
                        break
                
                decodificacoes = novas_decodificacoes
        
        return decodificacoes
    
    def _listar_decodificacoes_segmento(self, segmento):
        """
        lista decodificações possíveis para um segmento sem ∪
        """
        if not segmento:
            return ['']
        
        decodificacoes = []
        n = len(segmento)
        
        # usar backtracking para encontrar todas as decodificações
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
    
    def mostrar_estatisticas(self, mensagem):
        """
        mostra estatísticas detalhadas da decodificação
        """
        print(f"mensagem morse: {mensagem}")
        print(f"total de decodificações possíveis: {self.contar_decodificacoes(mensagem)}")
        
        segmentos = mensagem.replace(' ', '').split('u')
        print(f"número de segmentos: {len(segmentos)}")
        
        for i, segmento in enumerate(segmentos):
            if segmento:
                decodificacoes = self._contar_decodificacoes_segmento(segmento)
                print(f"segmento {i+1}: '{segmento}' -> {decodificacoes} decodificações")
                
                # mostrar algumas decodificações de exemplo
                exemplos = self._listar_decodificacoes_segmento(segmento)[:5]
                if exemplos:
                    print(f"  exemplos: {', '.join(exemplos)}")
                    if len(exemplos) == 5 and decodificacoes > 5:
                        print(f"  ... e mais {decodificacoes - 5} decodificações")


def main():
    """
    função principal para testar o decodificador
    """
    decodificador = decodificador_morse()
    
    # testar com a mensagem do enunciado
    mensagem_exemplo = ".- ..u- .-.-.-u.. ..-u.. ..u..-.-"
    print("=== teste com mensagem do enunciado ===")
    decodificador.mostrar_estatisticas(mensagem_exemplo)
    
    print("\n=== teste com mensagem simples ===")
    mensagem_simples = ".-..-"
    decodificador.mostrar_estatisticas(mensagem_simples)
    
    print("\n=== teste interativo ===")
    print("digite uma mensagem morse (use u para separar símbolos):")
    print("exemplo: .-..- ou .- u ..-")
    
    while True:
        try:
            entrada = input("\nmensagem morse (ou 'sair' para terminar): ").strip()
            if entrada.lower() == 'sair':
                break
            if entrada:
                decodificador.mostrar_estatisticas(entrada)
        except KeyboardInterrupt:
            print("\n\nprograma encerrado.")
            break


if __name__ == "__main__":
    main()
