# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é: {imc:.2f}')
    print(f'Abaixo do Peso')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu IMC é: {imc:.2f}')
    print(f'Peso Ideal')
elif imc < 30:
    print(f'Seu IMC é: {imc:.2f}')
    print(f'Sobrepeso')
elif imc < 40:
    print(f'Seu IMC é: {imc:.2f}')
    print(f'Obesidade')
else:
    print(f'Seu IMC é: {imc:.2f}')
    print('Obesidade mórbida')
