'''
import math

numero = int(input('Digite um número: '))

factorial_do_numero = math.factorial(numero)

print(factorial_do_numero)
'''

'''
numero = int(input('Digite um número: '))

factorial = 1

for c in range(numero, 1, -1):
    
    factorial *= c

    print(factorial)
'''
'''
numero = int(input('Digite um número: '))

factorial = 1
contador = numero

while contador > 0:
    print(contador,end='')

    if contador > 1:
        print('x', end='')

    factorial *= contador
    contador -= 1

print(f'={factorial}')
'''

'''
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n,f))
'''

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1 #ao invez de começar por zero, começa pelo 1 lidando com multiplicadores
print('Calculando {}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c #o mesmo que f *= c
    c -= 1 #estamos tirando 1 do c
print('{}'.format(f))
