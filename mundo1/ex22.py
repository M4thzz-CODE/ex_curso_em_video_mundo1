# Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas.

nome = str(input('Qual o seu nome completo? ')).strip()

nomes_separados = nome.split()

print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')

total_letras = len(nome) - nome.count(' ')
print(f'Seu nome tem {total_letras} letras ao todo.')

print(f'Seu primeiro nome é {nomes_separados[0]} e ele tem {len(nomes_separados[0])} letras.')