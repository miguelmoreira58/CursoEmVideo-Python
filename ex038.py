val1 = float(input('Digite o primeiro valor: '))
val2 = float(input('Digite o segundo valor: '))

if val1 > val2:
    print('O primeiro valor é maior')
elif val1 < val2:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')