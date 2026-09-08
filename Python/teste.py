idade = int(input('Digite sua Idade:  '))
carteira = input('Você tem carteira ? ')
e_verdadeiro = carteira.strip().lower() == 'sim'

tem_carteira = e_verdadeiro

if idade >= 18 and tem_carteira:
    print('Você pode Dirigir!')
else:
    print('Você não pode Dirigir!')

print(carteira)