'''
soma = 0

for n in range(1, 501):
    if n % 2 != 0 and n % 3 == 0:
        soma += n

print(soma)
'''

soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador = contador + 1
        soma += c
print('A soma de todos os {} valores solicitados é {}'.format(contador,soma))