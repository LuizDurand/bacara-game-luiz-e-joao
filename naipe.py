from random import randint
import math

naipe = 4
cartas_por_naipe = 13
cartas_por_baralho = naipe * cartas_por_naipe

def carta_aleatoria ():
    ndc = randint(1, cartas_por_baralho)

    baralho = int(ndc / cartas_por_baralho)
    naipe = int((ndc - cartas_por_baralho) / cartas_por_naipe)
    numero = ndc 

    while numero > cartas_por_naipe:
        numero -= cartas_por_naipe

    if numero >= 11:
        numero = 0
        
    
    return (ndc, numero)


def verifica_carta(carta_verificar,lista_cartas):
    carta_unica=True

    for cartas_jogador in lista_cartas:
        for carta_jogador in cartas_jogador:
            if carta_verificar==carta_jogador:
                carta_unica=False
    return carta_unica




def cartas_aleatorias (numeros_grupos):
    lista_c = []

    for i in range (0, numeros_grupos):
        cartas_jogador = []

        for j in range (0, 2):
            while True:
                carta_nova= carta_aleatoria()
                if verifica_carta(carta_nova,lista_c):
                    cartas_jogador.append(carta_nova)
                    break
        lista_c.append(cartas_jogador)
    return lista_c


def soma_cartas (cartas_jogador):
    soma = 0 
    
    for carta in cartas_jogador:
        valor = carta[1]
        soma += carta
    return soma 
        


    




