#import math
from math import trunc

numero = float(input('Digite um numero: '))

#print('O número é {:.0f}'.format(numero))
#print('O valor digitado foi {} e a sua porção inteira é {}' .format(numero, math.trunc(numero)))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(numero, trunc(numero)))

# OU fazer sem importar nada, usando o conversor inteiro

print('O valor digitado foi {} e a sua porção inteira é {}' .format(numero, int(numero)))
