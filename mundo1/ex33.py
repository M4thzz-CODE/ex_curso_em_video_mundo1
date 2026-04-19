# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

numeros = [num1, num2, num3]

print(f'O maior valor digitado foi {max(numeros)}')
print(f'O menor valor digitado foi {min(numeros)}')