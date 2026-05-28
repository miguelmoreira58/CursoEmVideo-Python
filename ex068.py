'''
import random

contador = 0
while True:

    print('=-'*15)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-'*15)

    computador = random.randint(0,10)
    
    jogador = int(input('Diga um valor: '))
    par_ou_impar = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]

    soma = (computador + jogador)

    if par_ou_impar == 'P':
        if soma % 2 == 0:
            contador += 1
            
            print('-'*20)
            print(f'Você jogou {jogador} e o computador {computador}. O total de {soma} deu PAR')
            print('-'*20)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        else:
            print('-'*20)
            print(f'Você jogou {jogador} e o computador {computador}. O total de {soma} deu IMPAR')
            print('-'*20)
            print('Você PERDEU!')
            break
    if par_ou_impar == 'I':
        if soma % 2 == 0:
            print('-'*20)
            print(f'Você jogou {jogador} e o computador {computador}. O total de {soma} deu PAR')
            print('-'*20)
            print('Você PERDEU!')
            break
        else:
            contador += 1
            
            print('-'*10)
            print(f'Você jogou {jogador} e o computador {computador}. O total de {soma} deu IMPAR')
            print('-'*10)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {contador} vezes')
'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador+computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par um impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')