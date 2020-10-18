from carta import *

fichas_jogador = 1000

while fichas_jogador > 0:
    valor = int(input('Quanto você quer perder hoje??'))
    
    if valor == 0:
        break 

    aposta = input('Faça sua aposta, jogador, banco ou empate??')

    cartas_jogador, cartas_banco = cartas_aleatorias(2)

    soma_jogador = soma_cartas(cartas_jogador)
    soma_banco = soma_cartas(cartas_banco)

    print('Jogador marcou {0} pontos'.format(soma_jogador))
    print('Banco marcou {0} pontos'.format(soma_banco))

    if aposta == 'empate':
        if soma_jogador == soma_banco:
            fichas_jogador = fichas_jogador + 8 * valor
            print('Parabéns, você ganhou {0} fichas!!'.format( 8 * valor))
        else:
            fichas_jogador = fichas_jogador - valor
            print('Puts, que peninha você perdeu {0} fichas!!'.format(valor))

    if aposta == 'jogador':
        if soma_jogador > soma_banco:
            fichas_jogador = fichas_jogador +  valor
            print('Parabéns, você ganhou {0} fichas!!'.format( valor))
        else:
            fichas_jogador = fichas_jogador - valor
            print('Puts, que peninha você perdeu {0} fichas!!'.format(valor))

    if aposta == 'banco':
        if soma_jogador < soma_banco:
            fichas_jogador = fichas_jogador + int(0.95* valor)
            print('Parabéns, você ganhou {0:.0f} fichas!!'.format(0.95* valor))
        else:
            fichas_jogador = fichas_jogador - valor
            print('Puts, que peninha você perdeu {0} fichas!!'.format(valor))







    
