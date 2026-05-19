"""
numero = int(input('Digite um número: '))

dobro = numero*2
triplo = numero*3
raiz_quadrada = numero**(1/2)

print('O dobro de {} é {}' .format(numero, dobro))
print('O triplo de {} é {}' .format(numero, triplo))
print('A raiz quadrada de {} é {:.2f}' .format(numero, raiz_quadrada))
"""

numero = int(input('Digite um número: '))

print('O dobro de {} vale {}.'.format(numero, (numero*2)))
#print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(numero, (numero*3), numero, (numero**(1/2))))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(numero, (numero*3), numero, pow(numero, (1/2)))) #usando pow()