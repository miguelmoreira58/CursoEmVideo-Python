import random

numero = random.randint(0,5)

chute = int(input('Qual foi o número escolhido? '))

if chute == numero:
    print('Você venceu, o número é {}'.format(numero))
else:
    print('Você perdeu, o número é {}'.format(numero))