'''
numero = int(input('Digite um número [999 para parar]: '))

contador = 0
soma = 0

while numero != 999:
    
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))

    contador += 1

print('Você digitou {} numeros e a soma entre eles foi {}'.format(contador,soma))
'''

num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont,soma))

