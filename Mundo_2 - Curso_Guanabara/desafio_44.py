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
    produto = float(input('Digite o valor do produto: '))
    return produto

def menu():
    limpar_terminal()
    print('-MÉTODO DE PAGAMENTO-')
    print('[1] - À vista dinheiro/Cheque (10% desconto)')
    print('[2] - À vista no cartão (5% desconto)')
    print('[3] - Em até 2x no cartão (Sem Juros)')
    print('[4] - 3x ou mais no cartão (Com juros)')
    opcao = int(input('Digite qual opção de pagamento: '))
    return opcao

while True:

    opcao = menu()
    produto = valor_produto()

    if opcao == 1:
        limpar_terminal()
        valor_desconto = produto * (10 / 100)
        valor_final = produto - valor_desconto
        print(f'Valor a pagar: R${valor_final:.2f}')
        input('\nPressione ENTER para voltar...')
    elif:
    pass
