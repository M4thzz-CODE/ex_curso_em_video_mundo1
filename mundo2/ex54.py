# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

menores = 0

for c in range(1, 8):
     pessoa = int(input(f"Digite o ano de nascimento da {c} pessoa: "))
     if date.today().year - pessoa < 18:
        menores += 1
print(f"{7 - menores} são maiores e {menores} são menores.")
