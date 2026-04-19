# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Em que cidade você nasceu? ')).strip()
comeca_com_santo = cidade[:5].upper() == 'SANTO'

print(f'A cidade começa com SANTO? {comeca_com_santo}')