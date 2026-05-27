'''
soma = 0
contador = 1
media = 0

numero = int(input('Digite um número: '))
continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()

while continuar not in 'Nn':
    
    numero = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()

    soma += numero
    contador += 1
    media = (soma)/contador

print('Você digitou {} numeros e a média foi {}'.format(contador,media))
print('')
'''

resp = 'S'
soma = quantidade = media = 0
maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    
    soma += num
    quantidade += 1

    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} numeros e a media foi {}'.format(quantidade,media))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))
