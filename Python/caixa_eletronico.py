import os


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def consultar_saldo(saldos):
    limpar_terminal()
    print("-" * 32)
    print("|       CONSULTAR SALDO       |")
    print("-" * 32)
    print(f"|        R$ {saldos:.2f}         |")
    print("-" * 32)


def menu():
    limpar_terminal()

    print("-" * 32)
    print("|       CAIXA ELETRONICO       |")
    print("-" * 32)
    print("| 1. Sacar                     |")
    print("| 2. Depositar                 |")
    print("| 3. Consultar Saldo           |")
    print("| 4. Sair                      |")
    print("-" * 32)

    return int(input('\nDigite o número da opção: '))


saldos = 1000


while True:

    opcao = menu()

    if opcao == 1:

        limpar_terminal()

        print(f'Valor disponível para saque: R${saldos:.2f}')

        valor = float(input('Digite o valor para saque: '))

        if valor <= 0:
            print('Digite um valor válido!')

        elif valor > saldos:
            print('Saldo insuficiente!')

        else:
            saldos -= valor
            print(f'Saque realizado no valor de R${valor:.2f}')
            print(f'Seu novo saldo: R${saldos:.2f}')

        input('\nPressione ENTER para voltar...')


    elif opcao == 2:

        limpar_terminal()

        valor = float(input('Digite o valor para depósito: '))

        if valor <= 0:
            print('Digite um valor válido!')

        else:
            saldos += valor

            print('Depósito realizado com sucesso!')
            print(f'Seu novo saldo: R${saldos:.2f}')

        input('\nPressione ENTER para voltar...')


    elif opcao == 3:

        consultar_saldo(saldos)

        input('\nPressione ENTER para voltar...')


    elif opcao == 4:

        print('Obrigado por utilizar o Caixa Eletrônico!')
        break


    else:

        print('Opção inválida!')

        input('\nPressione ENTER para voltar...')