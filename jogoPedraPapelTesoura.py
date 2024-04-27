import random

empate = 0
vitoria_jogador = 0
vitoria_computador = 0

while True:
    print('========== PEDRA - PAPEL - TESOURA ==========')
    nome_jogador = input('Informe o seu nome: ')
    if nome_jogador == 'sair' or nome_jogador == 'Sair':
        print('Jogo encerrado!')
        break
    quantidade_partidas = int(input('Quantas partidas você vai jogar: '))
    
    for partida in range(quantidade_partidas):
        print('======= {}° PARTIDA ======'.format(partida + 1))
        print('1 - PEDRA')
        print('2 - PAPEL')
        print('3 - TESOURA')
        escolha_jogador = int(input('Faça a sua escolha: '))
        escolha_computador = random.randint(1,3)
        
        if escolha_jogador == escolha_computador:
            print('Deu empate')
            empate += 1
        elif escolha_jogador == 1 and escolha_computador == 2:
            print('Vitória do computador')
            vitoria_computador += 1
        elif escolha_jogador == 1 and escolha_computador == 3:
            print('Vitória do jogador')
            vitoria_jogador += 1
        elif escolha_jogador == 2 and escolha_computador == 1:
            print('Vitória do jogador')
            vitoria_jogador += 1
        elif escolha_jogador == 2 and escolha_computador == 3:
            print('Vitória do computador')
            vitoria_computador += 1
        elif escolha_jogador == 3 and escolha_computador == 1:
            print('Vitória do computador')
            vitoria_computador += 1
        elif escolha_jogador == 3 and escolha_computador == 2:
            print('Vitória do jogador')
            vitoria_jogador += 1
        else:
            print('Opção inválida!\nJogada não contada')
    print('====== PLACAR =====')
    print('EMPATE: ', empate)
    print('Vitorias do jogador: ', vitoria_jogador)
    print('Vitorias do computador: ', vitoria_computador)

    empate = 0
    vitoria_jogador = 0
    vitoria_computador = 0