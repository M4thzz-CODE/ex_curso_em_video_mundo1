#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

idade = int(input("Digite a idade do aluno para saber a sua categoria: "))

if idade <= 9:
    print("Mirim")
elif 10 <= idade <= 14:
    print("Infantil")
elif 15 <= idade <= 19:
    print("Junior")
elif 20 <= idade <= 25:
    print("Sênior")
else:
    print("Master")