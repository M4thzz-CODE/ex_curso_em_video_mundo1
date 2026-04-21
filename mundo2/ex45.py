# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

print("Bem-vindo ao jogo Pedra Papel e Tesoura!")

opcoes = int(input('''OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua escolha? '''))

itens = ["PEDRA", "PAPEL", "TESOURA"]
computador = choice([0, 1, 2])

print("PEDRA")
sleep(1)
print("PAPEL")
sleep(1)
print("TESOURA")
sleep(1)

print("-=" * 15)
print(f"Você escolheu {itens[opcoes]}")
print(f"O computador escolheu {itens[computador]}")
print("-=" * 15)

if opcoes == computador:
    print("Empate!")
elif (opcoes == 0 and computador == 2) or \
     (opcoes == 1 and computador == 0) or \
     (opcoes == 2 and computador == 1):
    print("O jogador venceu!")
else:
    print("O computador venceu!")