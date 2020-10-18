from random import randint
import math

naipe = 4
cartas_por_naipe = 13
cartas_por_baralho = naipe * cartas_por_naipe
baralhos = int(input("Com quantos baralhos você quer jogar??"))
cartas_totais = baralhos * cartas_por_baralho

def carta_aleatoria():
    i = randint(1, cartas_totais)

    baralho = int(input(i / cartas_por_baralho))
    baralho_indice = baralho * cartas_por_baralho
    naipe = int(input(i - baralho_indice) / cartas_por_naipe)
    numero = i - baralho_indice

    while numero > 13:

        numero -= cartas_por_naipe


    return numero