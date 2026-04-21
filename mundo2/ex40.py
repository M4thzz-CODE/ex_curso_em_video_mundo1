# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

total = (nota1 + nota2) / 2

if 5.0 <= total < 6.9:
    print("Recuperação")
elif total >= 7:
    print("Aprovado")
else:
    print("Reprovado")