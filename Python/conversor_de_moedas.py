def money():
    cash = float(input('Digite o valor: '))
    return cash

while True:
    print(('-' * 5),'Conversor de Moedas',('-' * 5))
    print('[1] - Real --> Dólar')
    print('[2] - Dólar --> Real')
    print('[3] - Real --> Euro')
    print('[4] - Euro --> Real')
    print('[5] - Sair')

    opcao = int(input('Digite o número da opção: '))

    if opcao == 1:
        num = money()
        real_dolar = num / 5.13
        print(f'A conversão de Real para Dolar é ${real_dolar}')
    elif opcao == 2:
        num = money()
        dolar_real = num * 5.13
        print(f'A conversão de Dolar para Real é R${dolar_real}')
    elif opcao == 3:
        num = money()
        real_euro = num / 5.94
        print(f'A conversão de Real para Euro é ${real_euro}')
    elif opcao == 4:
        num = money()
        euro_real = num * 5.94
        print(f'A conversão de Euro para Real é R${euro_real}')
    elif opcao == 5:
        print('Fim')
        break
    else:
        print('Opção inválida!')