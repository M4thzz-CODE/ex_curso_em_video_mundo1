# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = int(input("Primeira reta: "))
r2 = int(input("Segunda reta: "))
r3 = int(input("Terceira reta:"))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Pode formar um triangulo")
else:
    print("Não pode formar um triangulo")