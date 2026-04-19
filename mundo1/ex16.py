# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# A função trunc vem da palavra inglesa truncate (truncar). No contexto da matemática e da programação, truncar significa "cortar" a parte decimal de um número sem realizar nenhum tipo de arredondamento.

from math import trunc

num = float(input("Digite um número: "))

print(f"O valor digitado foi {num} e sua porção inteira é {trunc(num)}.")