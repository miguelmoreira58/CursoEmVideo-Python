"""
import random

numero = random.randint(0,5)

chute = int(input('Qual foi o número escolhido? '))

if chute == numero:
    print('Você venceu, o número é {}'.format(numero))
else:
    print('Você perdeu, o número é {}'.format(numero))
    """

'''
import random

numero_sorteado = random.randint(0,10)

chute_do_usuario = int(input('Qual foi o número escolhido? '))

qtd_tentativas = 1 #começando com 1, adicionando a cada erro


while chute_do_usuario != numero_sorteado:
    
    print('Você perdeu, o número não é {}'.format(chute_do_usuario))

    chute_do_usuario = int(input('Qual foi o número escolhido? '))

    qtd_tentativas += 1

print('Você venceu em {} tentativas, o número é {}'.format(qtd_tentativas, numero_sorteado))
'''

from random import randint

computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False
palpites = 0

while not acertou:
    
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
