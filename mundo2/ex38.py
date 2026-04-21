# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: O primeiro valor é maior

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print("O primeiro valor é maior")
elif num1 < num2:
    print("O segundo valor é maior")
elif num1 == num2:
    print("Não existe valor maior, os dois são iguais")