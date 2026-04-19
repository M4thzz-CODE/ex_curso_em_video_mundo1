# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Qual é a frase? ")).upper().strip()

print(f"A letra 'A' aparece {frase.count('A')} vezes na frase.")
print(f"A primeira letra 'A' apareceu na posição {frase.find('A') + 1}")
print(f"A última letra 'A' apareceu na posição {frase.rfind('A') + 1}")

# .rfind('A'): O "r" vem de Right (direita). Ele começa a procurar do final da frase para o início, encontrando assim a última ocorrência.
# .count('A'): Conta exatamente quantas vezes o caractere aparece na string.
#.find('A'): Procura a partir do início da frase e retorna o índice (posição) da primeira ocorrência.