# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input("Qual a distancia da sua viagem? "))

if distancia <= 200:
    print(f"O valor da passagem será {distancia * 0.50:.2f}")
elif distancia > 200:
    print(f"O valor da passagem será {distancia * 0.45:.2f}")
else:
    print()