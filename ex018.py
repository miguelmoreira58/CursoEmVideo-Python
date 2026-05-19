"""
import math

angulo = float(input('Digite o ângulo que você deseja: '))

'''lembrando que estamos entregando o angulo que ainda NÃO está em graus centigrados, portanto ele tem 
que estar representado em radianos para que o calculo seja feito corretamente'''

#Apenas o "seno = math.sin(angulo)" NAO FUNCIONARIA pois o angulo ainda não está convertido para radians
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno de {} é {:.2f}'.format(angulo, seno))
print('O cosseno de {} é {:.2f}'.format(angulo, cosseno))
print('A tangente de {} é {:.2f}'.format(angulo, tangente))
"""

from math import sin,cos,tan,radians

angulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O seno de {} é {:.2f}'.format(angulo, seno))
print('O cosseno de {} é {:.2f}'.format(angulo, cosseno))
print('A tangente de {} é {:.2f}'.format(angulo, tangente))