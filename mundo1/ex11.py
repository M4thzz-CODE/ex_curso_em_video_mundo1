# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

print(f"A sua parede tem {largura}x{altura} e a área total é de: {largura * altura:.2f}m²")
print(f"Para pintar essa parede, você precisará em torno de {(largura * altura) / 2:.2f}l de tinta.")