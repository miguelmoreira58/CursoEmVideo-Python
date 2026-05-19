'''
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

# imc = peso / (altura ** 2)
imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal')
elif imc >= 25 and imc <= 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Você está em obesidade')
else:
    print('Você está em obesidade morbida')
'''

peso = float(input('Digite seu peso? (kg) '))
altura = float(input('Digite sua altura? (m) '))

imc = peso / (altura ** 2)

print('O IMC dessa pessoa é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABENS, você está na faixa do PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MÒRBIDA, cuidado!')