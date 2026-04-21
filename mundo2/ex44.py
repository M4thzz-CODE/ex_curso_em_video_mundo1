# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print(f'{" LOJA M4THZZ ":=^40}')
compras = float(input("Qual o preço das compras? R$"))

print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque (10% desc)
[ 2 ] à vista no cartão (5% desc)
[ 3 ] 2x no cartão (Preço normal)
[ 4 ] 3x ou mais no cartão (20% juros)''')
opcao = int(input("Qual é a opção? "))

if opcao == 1:
    total = compras - (compras * 10 / 100)
elif opcao == 2:
    total = compras - (compras * 5 / 100)
elif opcao == 3:
    total = compras
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS.")
elif opcao == 4:
    total = compras + (compras * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print(f"Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS.")
else:
    total = compras
    print("OPÇÃO INVÁLIDA de pagamento. Tente novamente!")

print(f"Sua compra de R${compras:.2f} vai custar R${total:.2f} no final.")