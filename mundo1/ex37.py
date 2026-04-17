numero = int(input("Digite um número: "))
escolha = int(input('''Para qual conversão deseja? 
1 Binario 
2 Octal 
3 Hexadecimal'''))

if escolha == 1:
    print(f"O valor {numero} em binario é {numero:b}.")
elif escolha == 2:
    print(f"O valor {numero} em octal é {numero:o}.")
elif escolha == 3:
    print(f"O valor {numero} em hexadecimal é {numero:x}.")
else:
    print("Você não escolheu uma das opções válidas!")