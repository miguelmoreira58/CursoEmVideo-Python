import random

contador = 0
while True:

    print('=-'*10)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-'*10)

    computador = random.randint(1,10)
    
    jogador = int(input('Diga um valor: '))
    par_ou_impar = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]

    soma = (computador + jogador)

    if par_ou_impar == 'P':
        if soma % 2 == 0:
            contador += 1
            
            print('-'*10)
            print(f'Você jogou {jogador} e o computador {computador}. O total de {soma} deu PAR')
            print('-'*10)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
        else:
            print('-'*10)
            print(f'Você jogou {jogador} e o computador {computador}. O total de {soma} deu IMPAR')
            print('-'*10)
            print('Você PERDEU!')
            break
    if par_ou_impar == 'I':
        if soma % 2 == 0:
            print('-'*10)
            print(f'Você jogou {jogador} e o computador {computador}. O total de {soma} deu PAR')
            print('-'*10)
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
    