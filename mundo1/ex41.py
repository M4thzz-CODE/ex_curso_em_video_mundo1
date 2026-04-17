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