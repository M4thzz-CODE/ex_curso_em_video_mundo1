velocidade = float(input("Qual foi a velocidade do carro: "))
limite = 80

if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * 7
    print(f"Voce foi multado! E passou a {velocidade} e teve uma multa de: {multa}")

else:
    print("Voce não foi multado!, Parabéns!")
