from random import randint
import math

naipe = 4
cartas_por_naipe = 13
cartas_por_baralho = naipe * cartas_por_naipe

def carta_aleatoria():
    ndc = randint(1, cartas_por_baralho)

    baralho = int(input(ndc / cartas_por_baralho))
    naipe = int(input(ndc - cartas_por_baralho) / cartas_por_naipe)
    numero = ndc - cartas_por_baralho

    while numero > 13:
        numero -= cartas_por_naipe
        return numero