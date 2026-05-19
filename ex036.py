'''
val_casa = float(input('Qual o valor da casa? R$'))
val_salario = float(input('Qual o valor do salario? R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = val_casa / (anos * 12)

if prestacao <= val_salario * 30 / 100:
    print('Você pode financiar')
else:
    print('Salario muito baixo para o financiamento')
'''

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do salario? R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em  {} anos'.format(casa, anos))
print('A prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo aprovado')
else:
    print('Emprestimo NEGADO')