# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input("Digite a temperatura em °C: "))

print(f"A temperatura em {temperatura}°C é {temperatura * 9 / 5 + 32:.1f}°F.")