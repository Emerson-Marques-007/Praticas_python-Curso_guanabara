# Crie um programa que faça o computador jogar jokenpô com você.

import random
import os

def limpar_tela():
    pass

def menu():
    print('| VAMOS JOGAR - JOQUEMPÔ |')
    print('| [1] - Pedra')
    print('| [2] - Papel')
    print('| [3] - Tesoura')
    opcao = int(input('Faça uma jogada: '))
    return opcao

def maquina():
   jogadas = ['Pedra', 'Papel', 'Tesoura']
   resultado = random.choice(jogadas)


   return resultado

while True:
    opcao = menu()
    resultado_maquina = maquina()
    print(f'Jogada da maquina: {resultado_maquina}')

    if opcao == 1:
        if resultado_maquina == "Papel":
            print('Você perdeu, Tente Novamente!')
        elif resultado_maquina == "Pedra":
            print('EMPATE!!!, Joque novamente.')
        else:
            print('Parabens, você ganhou!!!')
