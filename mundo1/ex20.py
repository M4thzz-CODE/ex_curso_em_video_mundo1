# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

pri = str(input("Primeiro aluno: "))
seg = str(input("Segundo aluno: "))
ter = str(input("Terceiro aluno: "))
qua = str(input("Quarto aluno: "))

alunos = [pri, seg, ter, qua]
random.shuffle(alunos)

print(f'''A ordem de apresentação será:
{alunos}''')