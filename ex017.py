#import math
from math import hypot

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

#hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2) # outra maneira de calcular a raiz quadrada é usar o ** (1/2)

#hipotenusa = math.sqrt((cateto_oposto ** 2) + (cateto_adjacente ** 2))

#hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print('A hipotenusa vai medir {:.2f}' .format(hipotenusa))