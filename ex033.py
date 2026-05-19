numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 > numero2 and numero1 > numero3:
    print('{} é o maior'.format(numero1))
elif numero2 > numero3 and numero2 > numero3:
    print('{} é o maior'.format(numero2))
else:
    print('{} é o maior'.format(numero3))
##############
if numero1 < numero2 and numero1 < numero3:
    print('{} é o menor'.format(numero1))
elif numero2 < numero3 and numero2 < numero3:
    print('{} é o menor'.format(numero2))
else:
    print('{} é o menor'.format(numero3))