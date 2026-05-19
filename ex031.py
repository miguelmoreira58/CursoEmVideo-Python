distancia = int(input('Qual a distância da viagem em km? '))

if distancia <= 200:
    preco = distancia * 0.50
    print('Você vai viajar por {} km, pagando R${}'.format(distancia, preco))
else:
    preco = distancia * 0.45
    print('Você vai viajar por {} km, pagando R${}'.format(distancia, preco))