# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, 
# DE ACORDO COM A MÉDIA ATINGIDA:
# - MÉDIA ABAIXO DE 5.0: REPROVADO
# - MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
# - MÉDIA 7.0 OU SUPERIOR: APROVADO

nota_1 = float(input('Digite sua nota do 1º Bimestre: '))
nota_2 = float(input('Digite sua nota do 2º Bimestre: '))

media = (nota_1 + nota_2) / 2

if media < 5:
    print(f'Nota Final: {media}')
    print('Reprovado')
elif media >= 5 and media <= 6.9:
    print(f'Nota Final: {media}')
    print('Recuperação')
else:
    print(f'Nota Final: {media}')
    print('Aprovado!')
