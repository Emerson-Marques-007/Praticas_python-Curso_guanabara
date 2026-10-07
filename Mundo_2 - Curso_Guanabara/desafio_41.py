# A confederação Nacional de Natação precisa de um programa que leia o ano atleta e mostre sua categoria, 
# de acordo com a idade:

# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

import datetime

def idade():
    print(f'Idade: {idade}')

ano = datetime.datetime.now()
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
idade = ano.year - ano_nascimento

if idade < 10:
    print(f'Idade: {idade}')
    print("Categoria: MIRIM!")
elif idade < 15:
    print(f'Idade: {idade}')
    print('Categoria: INFANTIL')
elif idade < 20:
    print(f'Idade: {idade}')
    print('Categoria: JUNIOR')
elif idade == 20:
    print(f'Idade: {idade}')
    print('Categoria: SÊNIOR')
else:
    print(f'Idade: {idade}')
    print('Categoria: MASTER')
