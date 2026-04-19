# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input("Digite o nome completo: ")).strip()
nome = nome_completo.split()

print(f"Seu primeiro nome é: {nome[0]}")
print(f"Seu último nome é: {nome[-1]}")