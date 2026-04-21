# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

compra = float(input("Digite o valor total da compra: "))

opcao = int(input(('''FORMAS DE PAGAMENTO
[ 1 ] Pagamento á vista em dinherio / cheque
[ 2 ] Pagamento á vista no cartão
[ 3 ] Pagamento em 2x no cartão
[ 4 ] Pagamento em 3x ou mais
Qual é a opção escolhida? ''')))

if opcao == 1:
  print(f"Sua compra de R${compra:.2f} vai custar R${compra - compra * 0.10:.2f}.")

elif opcao == 2:
  print(f"Sua compra de R${compra:.2f} vai custar R${compra - compra * 0.05:.2f}.")

elif opcao == 3:
  print(f"Sua compra de R${compra:.2f} vai custar R${compra:.2f} pois em até 2x no cartão não tem desconto ou acréscimo.")

elif opcao == 4:
  parcelas = int(input("Em quantas parcelas? "))
  total = compra + (compra * 0.20)
  valor_parcela = total / parcelas
  
  print(f"Cada parcela será de R${valor_parcela:.2f}.")
  print(f"A sua compra vai ser parcelada em {parcelas}x com o acréscimo no total de R${compra * 0.20:.2f} de juros.")
  print(f"A sua compra de R${compra:.2f} vai custar com o acréscimo de juros o total de R${total:.2f}.")
else:
  print("Opção inválida")