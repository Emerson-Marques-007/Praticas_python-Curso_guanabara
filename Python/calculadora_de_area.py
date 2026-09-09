import math
import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def quadrado():
    limpar_terminal()
    lado = float(input('Digite o lado do quadrado: '))
    limpar_terminal()
    area_quadrado = lado ** 2
    return area_quadrado

def retangulo():
    limpar_terminal()
    base_ret = float(input('Digite a base do retângulo: '))
    altura_ret = float(input('Digite a altura do retângulo: '))
    limpar_terminal()
    area_retangulo = base_ret * altura_ret
    return area_retangulo

def triangulo():
    limpar_terminal()
    base_tri = float(input('Digite a base do triângulo: '))
    altura_tri = float(input('Digite a altura do triângulo: '))
    limpar_terminal()
    area_triangulo = (base_tri * altura_tri) / 2
    return area_triangulo

def circulo():
    limpar_terminal()
    raio = float(input('Digite o raio do Círculo: '))
    limpar_terminal()
    area_circulo = math.pi * raio ** 2
    return area_circulo

def menu():
    limpar_terminal()
    print('=' * 5, 'CALCULADORA DE ÁREA', 5 * '=')
    print('[1] - Quadrado')
    print('[2] - Retângulo')
    print('[3] - Triângulo')
    print('[4] - Círculo')
    print('[5] - Sair')

    opcao = int(input('Digite o número da opção: '))
    return opcao

while True:

    opcao = menu()

    if opcao == 1:
        area = quadrado()
        print(f'A área do quadrado é: {area}')
        input('\nPressione ENTER para voltar...')
    elif opcao == 2:
        area = retangulo()
        print(f'A área do retângulo é: {area}')
        input('\nPressione ENTER para voltar...')
    elif opcao == 3:
        area = triangulo()
        print(f'A área do triângulo é: {area}')
        input('\nPressione ENTER para voltar...')
    elif opcao == 4:
        area = circulo()
        print(f'A área do Círculo é: {area}')
        input('\nPressione ENTER para voltar...')
    elif opcao == 5:
        limpar_terminal()
        print('Fim Do Programa!')
        break
    else:
        limpar_terminal()
        print('Opção Invalida!')
        input('\nPressione ENTER para voltar...')