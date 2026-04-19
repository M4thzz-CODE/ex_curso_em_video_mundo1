# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salário do funcionário: "))
aumento = salario * 1.10
aumento2 = salario * 1.15
if salario >= 1.250:
    print(f"O seu salario de R${salario:.2f} apartir de agora vai ser {aumento:.2f}.")
else:
    print(f"O seu salario de R${salario:.2f} apartir de agora vai ser {aumento2:.2f}.")