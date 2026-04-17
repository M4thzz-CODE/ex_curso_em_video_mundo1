nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

total = (nota1 + nota2) / 2

if 5.0 <= total < 6.9:
    print("Recuperação")
elif total >= 7:
    print("Aprovado")
else:
    print("Reprovado")