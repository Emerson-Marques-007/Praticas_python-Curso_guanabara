# CALCULADORA

def numeros():
    numero_1 = float(input('Digite o 1° número: '))
    numero_2 = float(input('Digite o 2° número: '))
    return numero_1, numero_2

while('MENU'):
    print('MENU')
    print('[1] - SOMA')
    print('[2] - SUBTRAÇÃO')
    print('[3] - MULTIPLICAÇÃO')
    print('[4] - DIVISÃO')
    print('[5] - SAIR')
    print('')
    opcao = int(input('Digite um número para opção: '))

    if opcao == 1:
        n1, n2 = numeros()
        soma = n1 + n2
        print(f'A soma entre {n1:.0f} + {n2:.0f} é igual {soma}')
    elif opcao == 2:
        n1, n2 = numeros()
        subtracao = n1 - n2
        print(f'A subtração entre {n1:.0f} + {n2:.0f} é igual {subtracao}')
    elif opcao == 3:
        n1, n2 = numeros()
        multiplicacao = n1 * n2
        print(f'A soma entre {n1:.0f} X {n2:.0f} é igual {multiplicacao}')
    elif opcao == 4:
        n1, n2 = numeros()
        divisao = n1 / n2
        print(f'A divisão entre {n1:.0f} / {n2:.0f} é igual {divisao}')
    else:
        print('Fim')
        break