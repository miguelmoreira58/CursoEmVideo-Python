numero = int(input('Digite um número inteiro: '))

"""
if numero % 2 == 0:
    print('O número é PAR')
else:
    print('O número é IMPAR')
"""

resultado = numero % 2

if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))