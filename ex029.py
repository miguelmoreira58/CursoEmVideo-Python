velocidade_carro = float(input('Qual a velocidade do carro? '))

if velocidade_carro > 80:
    print('Você foi multado')
    multa = (velocidade_carro - 80) * 7

    print('Por estar a {} km/h, você pagará uma multa de R${}'.format(velocidade_carro, multa))
else:
    print('Você não foi multado')