# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

formula = primeiro + (10 - 1) * razao

for c in range(primeiro, formula, razao):
    print(f"{c}", end= " -> ")
print("Fim")