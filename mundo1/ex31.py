distancia = int(input("Qual a distancia da sua viagem? "))

if distancia <= 200:
    print(f"O valor da passagem será {distancia * 0.50:.2f}")
elif distancia > 200:
    print(f"O valor da passagem será {distancia * 0.45:.2f}")
else:
    print()