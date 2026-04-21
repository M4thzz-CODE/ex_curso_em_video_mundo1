# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

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