'''
#PROGRESSÂO ARITMÉTICA
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo_termo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
'''

'''
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 0
termo = primeiro_termo

while contador < 10:
    
    print(termo)
    
    termo += razao
    contador += 1
'''

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont += 1
print('FIM')