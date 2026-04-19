# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Qual foi a velocidade do carro: "))
limite = 80

if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * 7
    print(f"Voce foi multado! E passou a {velocidade} e teve uma multa de: {multa}.")

else:
    print("Voce não foi multado!, Parabéns!")