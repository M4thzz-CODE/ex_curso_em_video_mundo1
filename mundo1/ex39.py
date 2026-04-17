nascimento = int(input("Digite o seu ano de nascimento: "))
ano = 2017
idade = ano - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em 2017.")

if idade == 18:
    print("Você deve se alistar este ano")
elif idade > 18:
    saldo = idade - 18
    print(f"Você já deveria ter se alistado há {saldo}.")
elif idade < 18:
    saldo = 18 - idade
    print(f"Você ainda não tem 18 anos. Ainda faltam {saldo} anos para  o alistamento.")