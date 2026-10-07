# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
# - SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR.
# - SE É A HORA DE SE ALISTAR.
# - SE JÁ PASSOU DO TEMPO DE ALISTAMENTO.

# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.
import datetime

ano = datetime.datetime.now()

ano_nascimento = int(input('Digite seu ano do nascimento: '))
idade = ano.year - ano_nascimento

if idade == 18:
    print('Este ano você tem que se alistar!')
elif idade > 18:
    print(f'Ja passou {idade - 18} anos de você se alistar')
elif idade < 18:
    print(f'Falta {18 - idade} anos para você se alistar!')
