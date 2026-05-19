'''
maior_peso = 0
menor_peso = 0

for c in range(1, 6):
    peso_da_pessoa = float(input('Peso da {}ª pessoa '.format(c)))

    if c == 1:
        maior_peso = peso_da_pessoa
        menor_peso = peso_da_pessoa
    else:
        if peso_da_pessoa > maior_peso:
            maior_peso = peso_da_pessoa

        if peso_da_pessoa < menor_peso:
            menor_peso = peso_da_pessoa

print('O maior peso lido foi de {}'.format(maior_peso))
print('O menor peso lido foi de {}'.format(menor_peso))
'''

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(p)))

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))