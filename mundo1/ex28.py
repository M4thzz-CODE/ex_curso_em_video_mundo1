import random

pensar = int(input("Digite um numero entre 0 e 5: "))

computador = random.randint(0, 5)
if pensar == computador and pensar:
    print("Venceu!")
else:
    print("Perdeu!")