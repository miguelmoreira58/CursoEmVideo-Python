lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
for item in lista:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
