# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

distancia = float(input("Digite a distância em metros: "))

print(f'''A medida que {distancia:.0f} corresponde á: 
      {1000 / distancia}km
      {100 / distancia}hm
      {10 / distancia}dam
      {10 * distancia:.0f}dm
      {100 * distancia:.0f}cm
      {1000 * distancia:.0f}mm''')