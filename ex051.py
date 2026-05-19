'''
primeiro_termo = int(input('Qual é o primeiro termo? '))
razao = int(input('Qual é a razão? '))

qtd = 10
for n in range(primeiro_termo, 11, razao):
    print(n)
'''

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo_termo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')