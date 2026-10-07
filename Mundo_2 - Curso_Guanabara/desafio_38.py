# ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
# - O PRIMEIRO VALOR É MAIOR
# - O SEGUNDO NÚMERO É MAIOR
# - NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS

numero_1 = int(input('Digite o 1º número: '))
numero_2 = int(input('Digite o 2º número: '))

if numero_1 > numero_2:
    print('O 1º número e MAIOR!')
elif numero_2 > numero_1:
    print('O 2º número e MAIOR!')
elif numero_1 == numero_2:
    print('Não existe valor MAIOR, Os dois são iguais!')
else:
    print('Tente Novamente!')
