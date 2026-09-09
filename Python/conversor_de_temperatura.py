import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    limpar_terminal()
    print('=' * 10, 'CONVERSOR', '=' * 10)
    print('[1] Celsius --> Fahrenheit')
    print('[2] Fahrenheit --> Celsius')
    print('[3] Celsius --> Kelvin')
    print('[4] Kelvin --> Celsius')
    print('[5] Sair')



    opcao = int(input('\nDigite o número: '))
    return opcao

while True:

    opcao = menu()

    if opcao == 1:
        limpar_terminal()
        valor_celsius = float(input('Digite a temperatura em Celsius: '))
        fahrenheit = (valor_celsius * 9/5) + 32
        limpar_terminal()
        print(f'A temperatura de Celsius {valor_celsius:.1f}°C para Fahrenheit é {fahrenheit:.1f}°F')
        input('\nPressione ENTER para voltar...')
    elif opcao == 2:
        limpar_terminal()
        valor_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
        celsius = (valor_fahrenheit - 32) * 5/9
        limpar_terminal()
        print(f'A temperatura de Fahrenheit {valor_fahrenheit:.1f}°F para Celsius é {celsius:.1f}°C')
        input('\nPressione ENTER para voltar...')
    elif opcao == 3:
        limpar_terminal()
        valor_celsius = float(input('Digite a temperatura em Celsius: '))
        kelvin = valor_celsius + 273.15
        limpar_terminal()
        print(f'A temperatura de Celsius {valor_celsius:.1f}°C para Kelvin é {kelvin:.2f}°K')
        input('\nPressione ENTER para voltar...')
    elif opcao == 4:
        limpar_terminal()
        valor_kelvin = float(input('Digite a temperatura em Kelvin: '))
        celsius = valor_kelvin - 273.15
        limpar_terminal()
        print(f'A temperatura de Kelvin {valor_kelvin:.2f}°K para Celsius é {celsius:.2f}°C')
        input('\nPressione ENTER para voltar...')
    elif opcao == 5:
        limpar_terminal()
        print('Fim do Programa!')
        break
    else:
        limpar_terminal()
        print('Opção invalida!')
        input('\nPressione ENTER para voltar...')