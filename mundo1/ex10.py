# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

valor = float(input("Digite quanto de dinheiro tens em sua carteira R$"))

# Objetivo é converter em dolar, considerando o valor do dolar em $6,00.

print(f"Com o seu valor de R${valor} você pode comprar U${valor / 6.00:.2f}.")