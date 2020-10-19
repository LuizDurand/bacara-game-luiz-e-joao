# EP - Design de Software
# Equipe: Joao Manoel Pasqua Filho e Luiz Felipe Borelli Durand
# Data: 18/10/2020



from random import randint
import math

# Sao 52 cartas por baralho, sendo 13 de cada naipe
naipe = 4
cartas_por_naipe = 13
cartas_por_baralho = naipe * cartas_por_naipe

# Essa função verifica se não houve repetição de carta 
def verifica_carta(carta_verificar,lista_cartas):
    carta_unica=True

    for cartas_jogador in lista_cartas:
        for carta_jogador in cartas_jogador:
            if carta_verificar==carta_jogador:
                carta_unica=False
    return carta_unica

# Distribuidor de carta
def carta_aleatoria (lista_cartas):
    while True:
        ndc = randint(1, cartas_por_baralho)

        baralho = int(ndc / cartas_por_baralho)
        naipe = int((ndc - cartas_por_baralho) / cartas_por_naipe)
        numero = ndc 

        while numero > cartas_por_naipe:
            numero -= cartas_por_naipe

        if numero >= 11:
            numero = 0
            
        carta=(ndc, numero)

        if verifica_carta(carta,lista_cartas):
            return carta


def soma_cartas (cartas_jogador):
    soma = 0 
    
    for carta in cartas_jogador:
        valor = carta[1]
        soma += valor
    
    while soma>=10:
        soma=soma-10


    return soma 


def cartas_aleatorias (numeros_grupos):
    lista_cartas = []

    for i in range (0, numeros_grupos):
        cartas_jogador = []

        cartas_jogador.append(carta_aleatoria(lista_cartas))
        cartas_jogador.append(carta_aleatoria(lista_cartas))       

        soma=soma_cartas(cartas_jogador)
        if soma<6:
            cartas_jogador.append(carta_aleatoria(lista_cartas))
        
        lista_cartas.append(cartas_jogador)

    return lista_cartas


    




