"""
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo')
"""

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')

    if r1 == r2 and r2 == r3:
        print('É um triangulo equilatero, pois todos os lados são iguais')
    elif r1 != r2 != r3 != r1:
        print('É um triangulo escaleno, pois todos os lados são diferentes')
    else:
        print('É um triangulo isósceles pois dois lados são iguais')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo')