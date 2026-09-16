# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então 
# o empréstimo será negado.

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos você deseja pagar: '))

meses = anos * 12
prestacao = valor_casa / meses

if prestacao > salario * 0.3:
    print(f'Empréstimo Negado! A prestação seria de R$ {prestacao:.2f}.')
else:
    print(f'Empréstimo Aprovado! Sua prestação mensal será de R$ {prestacao:.2f} durante {meses} meses.')