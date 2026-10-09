# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:

# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def valor_produto():
    limpar_terminal()
    print('=' * 5, 'VALOR DO PRODUTO', 5 * '=')
    produto = float(input('Digite o valor do produto: R$'))
    return produto

def menu():
    limpar_terminal()
    print('-MÉTODO DE PAGAMENTO-')
    print('[1] - À vista dinheiro/Cheque (10% desconto)')
    print('[2] - À vista no cartão (5% desconto)')
    print('[3] - Em até 2x (Sem Juros), acima de 3X (20% Juros)')
    print('[4] - Sair')
    opcao = int(input('Qual opção de pagamento: '))
    return opcao

while True:
    produto = valor_produto()
    opcao = menu()
    
    if opcao == 1:
        limpar_terminal()
        valor_desconto = produto * (10 / 100)
        valor_final = produto - valor_desconto
        print(f'Valor a vista: R${valor_final:.2f}')
        input('\nPressione ENTER para voltar...')
    elif opcao == 2:
        limpar_terminal()
        valor_desconto = produto * (5 / 100)
        valor_final = produto - valor_desconto
        print(f'Valor a vista no cartão: R${valor_final:.2f}')
        input('\nPressione ENTER para voltar...')
    elif opcao == 3:
        limpar_terminal()
        vezes = int(input('Quantas vezes você quer Dividir?'))
        if vezes == 1 or vezes == 2:
            limpar_terminal()
            sem_juros = produto / vezes
            print(f'O valor da parcela é: R${sem_juros} sem juros')
            input('\nPressione ENTER para voltar...')
        elif vezes > 2:
            limpar_terminal()
            juros = produto * ( 20 / 100)
            valor_com_juros = produto + juros
            com_juros = valor_com_juros / vezes
            print(f'O valor dividido por {vezes}x é R$ {com_juros}')
            input('\nPressione ENTER para voltar...')
    elif opcao == 4:
        print('Fim do programa!')
        break
    else:
        limpar_terminal()
        print('Opção invalida')
        input('\nPressione ENTER para voltar...')
    
    
