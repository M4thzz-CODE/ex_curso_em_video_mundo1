# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

pensar = int(input("Digite um numero entre 0 e 5: "))

computador = random.randint(0, 5)
if pensar == computador and pensar:
    print("Venceu!")
else:
    print("Perdeu!")