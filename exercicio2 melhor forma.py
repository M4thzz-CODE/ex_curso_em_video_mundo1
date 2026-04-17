nome = 'Matheus Lemos'
altura = 1.83
peso = 76
imc = peso / (altura * altura)

linha_1 = f'{nome} tem: {altura:.2f} altura' 
linha_2 = f'Pesa {peso} quilos'
linha_3 = f'E seu IMC é : {imc:.2f}'

# o F no inicio precisa do {} para colocar a variável
# :.2f - quantidade de números após a virgula.
# F-strings

print(linha_1)
print(linha_2)
print(linha_3)
