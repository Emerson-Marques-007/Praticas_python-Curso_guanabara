# ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E 
# PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
# - 1 PARA BINÁRIO
# - 2 PARA OCTAL
# - 3 PARA HEXADECIMAL
import math

def inteiro():
    numero_int = int(input('Digite um Número Inteiro: '))
    return numero_int

def menu():
        print('[1] - Binário')
        print('[2] - Octal')
        print('[3] - Hexadecimal')
        print('[4] - Sair')

        opcao = int(input('Escolha uma opção para conversão: '))
        return opcao

while True:

    opcao = menu()

    if opcao == 1:
        numero = inteiro()
        print(f'O número binário de {numero} é {numero:b}')
    elif opcao == 2:
        numero = inteiro()
        octal = oct(numero)
        print(f'O número Octal de {numero} é {numero:o}')
    elif opcao == 3:
        numero = inteiro()
        hexadecimal = hex(numero)
        print(f'O número Hexadecimal de {numero} é {numero:x}')
    elif opcao == 4:
        print('Fim do Programa!')
        break
    else:
        print('Número Invalido!')
