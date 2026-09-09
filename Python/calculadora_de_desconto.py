preco = float(input('Informe o preço: R$ '))
percentual = float(input('Escolha o percentual de desconto: '))

desconto = preco * (percentual / 100)
preco_final = preco - desconto

print(f'Preço original: R$ {preco:.2f}')
print(f'Desconto: R$ {desconto:.2f}')
print(f'Preço final: R$ {preco_final:.2f}')