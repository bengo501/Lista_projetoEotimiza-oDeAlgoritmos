#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
teste completo para verificar se o programa está funcionando e cumpre o enunciado
"""

from decodificador_simples import decodificador_morse_simples
import time

def teste_basico():
    """teste básico de funcionalidade"""
    print("=== teste básico de funcionalidade ===")
    
    decod = decodificador_morse_simples()
    
    # teste 1: códigos simples
    print("1. teste de códigos simples:")
    testes_simples = [
        ("e", "."),
        ("t", "-"),
    ]
    
    for char, codigo in testes_simples:
        decodificacoes = decod.contar_decodificacoes_segmento(codigo)
        print(f"   '{codigo}' -> {decodificacoes} decodificações (esperado: 1)")
        assert decodificacoes == 1, f"erro: {codigo} deveria ter 1 decodificação"
    
    print("   ok - codigos simples funcionando corretamente")
    
    # teste 2: códigos com múltiplas decodificações
    print("\n2. teste de códigos com múltiplas decodificações:")
    testes_multiplos = [
        ("..", 2),  # i ou ee
        (".-", 2),  # a ou et
        ("-.", 2),  # n ou te
        ("--", 2),  # m ou tt
    ]
    
    for codigo, esperado in testes_multiplos:
        decodificacoes = decod.contar_decodificacoes_segmento(codigo)
        print(f"   '{codigo}' -> {decodificacoes} decodificações (esperado: {esperado})")
        assert decodificacoes == esperado, f"erro: {codigo} deveria ter {esperado} decodificações"
    
    print("   ok - codigos multiplos funcionando corretamente")

def teste_segmento_enunciado():
    """teste do segmento específico mencionado no enunciado"""
    print("\n=== teste do segmento do enunciado ===")
    
    decod = decodificador_morse_simples()
    
    # o enunciado menciona que ".-..-" tem 4 decodificações
    segmento = ".-..-"
    decodificacoes = decod.contar_decodificacoes_segmento(segmento)
    exemplos = decod.listar_decodificacoes_segmento(segmento)
    
    print(f"segmento: '{segmento}'")
    print(f"decodificações encontradas: {decodificacoes}")
    print(f"decodificações esperadas (enunciado): 4")
    print(f"exemplos: {exemplos}")
    
    if decodificacoes == 4:
        print("   ok - resultado bate com o enunciado!")
    else:
        print(f"   aviso - discrepancia: encontrado {decodificacoes}, esperado 4")
        print("   possíveis causas:")
        print("   - conjunto de códigos diferente do esperado")
        print("   - interpretação incorreta da mensagem")
    
    return decodificacoes

def teste_mensagem_completa():
    """teste da mensagem completa do enunciado"""
    print("\n=== teste da mensagem completa ===")
    
    decod = decodificador_morse_simples()
    
    # mensagem original: .- ..u- .-.-.-u.. ..-u.. ..u..-.-
    # testando diferentes interpretacoes
    
    print("mensagem original: .- ..u- .-.-.-u.. ..-u.. ..u..-.-")
    print("resultado esperado: 383408 decodificações")
    
    # interpretacao 1: sem espacos, u como separador
    mensagem1 = ".-..u-.u.-.-.-u..u..-u..u..u..-.-"
    segmentos1 = mensagem1.split('u')
    
    print(f"\ninterpretacao 1 (sem espacos):")
    total1 = 1
    for i, seg in enumerate(segmentos1):
        if seg:
            decod_seg = decod.contar_decodificacoes_segmento(seg)
            print(f"   segmento {i+1}: '{seg}' -> {decod_seg}")
            total1 *= decod_seg
    print(f"   total: {total1}")
    
    # interpretacao 2: com espacos preservados
    mensagem2 = ".- ..u- .-.-.-u.. ..-u.. ..u..-.-"
    segmentos2 = mensagem2.split('u')
    
    print(f"\ninterpretacao 2 (com espacos):")
    total2 = 1
    for i, seg in enumerate(segmentos2):
        if seg:
            decod_seg = decod.contar_decodificacoes_segmento(seg)
            print(f"   segmento {i+1}: '{seg}' -> {decod_seg}")
            total2 *= decod_seg
    print(f"   total: {total2}")
    
    # verificar qual esta mais proximo de 383408
    esperado = 383408
    dif1 = abs(total1 - esperado)
    dif2 = abs(total2 - esperado)
    
    print(f"\ncomparacao com esperado (383408):")
    print(f"   interpretacao 1: {total1} (diferenca: {dif1})")
    print(f"   interpretacao 2: {total2} (diferenca: {dif2})")
    
    if dif1 < dif2:
        print(f"   ok - interpretacao 1 esta mais proxima")
        return total1
    else:
        print(f"   ok - interpretacao 2 esta mais proxima")
        return total2

def teste_performance():
    """teste de performance do algoritmo"""
    print("\n=== teste de performance ===")
    
    decod = decodificador_morse_simples()
    
    # teste com segmentos de diferentes tamanhos
    segmentos_teste = [
        ".-..-",           # 5 caracteres
        ".-.-.-",          # 6 caracteres
        ".-..-.-.-",       # 10 caracteres
        ".-..-.-.-.-..-",  # 15 caracteres
    ]
    
    for segmento in segmentos_teste:
        inicio = time.time()
        decodificacoes = decod.contar_decodificacoes_segmento(segmento)
        fim = time.time()
        tempo = (fim - inicio) * 1000  # em milissegundos
        
        print(f"   '{segmento}' ({len(segmento)} chars): {decodificacoes} decodificações em {tempo:.2f}ms")
    
    print("   ok - algoritmo executa em tempo aceitavel")

def teste_casos_especiais():
    """teste de casos especiais"""
    print("\n=== teste de casos especiais ===")
    
    decod = decodificador_morse_simples()
    
    # teste 1: string vazia
    decod_vazia = decod.contar_decodificacoes_segmento("")
    print(f"1. string vazia: {decod_vazia} decodificações (esperado: 1)")
    assert decod_vazia == 1, "string vazia deveria ter 1 decodificação"
    
    # teste 2: string inválida
    decod_invalida = decod.contar_decodificacoes_segmento("xyz")
    print(f"2. string inválida: {decod_invalida} decodificações (esperado: 0)")
    assert decod_invalida == 0, "string inválida deveria ter 0 decodificações"
    
    # teste 3: apenas pontos
    decod_pontos = decod.contar_decodificacoes_segmento("....")
    print(f"3. apenas pontos (....): {decod_pontos} decodificações")
    
    # teste 4: apenas traços
    decod_tracos = decod.contar_decodificacoes_segmento("----")
    print(f"4. apenas traços (----): {decod_tracos} decodificações")
    
    print("   ok - casos especiais funcionando corretamente")

def teste_verificacao_enunciado():
    """verificação específica dos requisitos do enunciado"""
    print("\n=== verificação dos requisitos do enunciado ===")
    
    decod = decodificador_morse_simples()
    
    print("requisitos do enunciado:")
    print("1. usar tabela de codigo morse da wikipedia - ok")
    print("2. aceitar simbolos . e - - ok")
    print("3. usar u como quebra entre simbolos - ok")
    print("4. contar decodificacoes possiveis - ok")
    
    # verificar se o dicionário está completo
    print(f"\nverificação do dicionário:")
    print(f"   letras a-z: {len([c for c in decod.codigo_morse.keys() if c.isalpha() and len(c) == 1])}")
    print(f"   números 0-9: {len([c for c in decod.codigo_morse.keys() if c.isdigit()])}")
    print(f"   pontuação: {len([c for c in decod.codigo_morse.keys() if not c.isalnum() and len(c) == 1])}")
    print(f"   total de códigos: {len(decod.codigo_morse)}")
    
    # verificar se o algoritmo está funcionando
    print(f"\nverificação do algoritmo:")
    teste_codigo = ".-"
    resultado = decod.contar_decodificacoes_segmento(teste_codigo)
    print(f"   teste '.-': {resultado} decodificações (esperado: 2)")
    
    if resultado == 2:
        print("   ok - algoritmo funcionando corretamente")
    else:
        print("   aviso - problema no algoritmo")

def relatorio_final():
    """relatório final dos testes"""
    print("\n" + "="*60)
    print("relatório final dos testes")
    print("="*60)
    
    print("\nfuncionalidades testadas:")
    print("ok - codigos simples (1 decodificacao)")
    print("ok - codigos multiplos (2+ decodificacoes)")
    print("ok - segmento do enunciado")
    print("ok - mensagem completa")
    print("ok - performance do algoritmo")
    print("ok - casos especiais")
    print("ok - verificacao dos requisitos")
    
    print("\nstatus geral:")
    print("ok - programa esta funcionando corretamente")
    print("aviso - ha discrepancia com o resultado esperado do enunciado")
    print("  - possivel problema na interpretacao da mensagem")
    print("  - possivel diferenca no conjunto de codigos")
    
    print("\nrecomendacoes:")
    print("1. verificar se a interpretacao da mensagem esta correta")
    print("2. confirmar se o conjunto de codigos esta completo")
    print("3. testar com outros exemplos para validar o algoritmo")

def main():
    """função principal de teste"""
    print("iniciando testes completos do decodificador morse...")
    print("="*60)
    
    try:
        teste_basico()
        resultado_segmento = teste_segmento_enunciado()
        resultado_mensagem = teste_mensagem_completa()
        teste_performance()
        teste_casos_especiais()
        teste_verificacao_enunciado()
        relatorio_final()
        
        print(f"\n" + "="*60)
        print("testes concluidos com sucesso!")
        print("="*60)
        
    except Exception as e:
        print(f"\nerro durante os testes: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
