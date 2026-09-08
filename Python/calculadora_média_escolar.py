def notas():
    nota_1 = float(input('Digite a nota do 1° Bimestre: '))
    nota_2 = float(input('Digite a nota do 2° Bimestre: '))
    nota_3 = float(input('Digite a nota do 3° Bimestre: '))
    return nota_1, nota_2, nota_3

def media():
    nota_1, nota_2, nota_3 = notas()
    soma = nota_1 + nota_2 + nota_3
    divisao = soma / 3
    return divisao

situacao = media()


if situacao < 5:
    print('Situação Escolar')
    print(f'Reprovado {situacao:.2f}')
elif situacao < 6:
    print('Situação Escolar')
    print(f'Recuperação {situacao:.2f}')
else:
    print(f'Aprovado {situacao:.2f}')