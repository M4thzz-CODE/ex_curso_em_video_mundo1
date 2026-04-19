# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite qual é o salário do funcinário R$"))

print(f"O salário do funcionário é de R${salario} com o reajuste de 15% será de R${salario + (salario * 0.15):.2f}.")