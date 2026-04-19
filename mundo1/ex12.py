# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite qual é o preço do produto R$ "))

print(f"O preço do produto é R${preco} e com o desconto fica R${preco - (preco * 0.05):.2f}.")