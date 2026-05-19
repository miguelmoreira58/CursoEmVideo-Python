salario = float(input('Qual o salário do funcionário? '))

if salario < 1250:
    novo_salario = salario + (salario * 15 / 100)

else:
    novo_salario = salario + (salario * 10 / 100)

aumento = novo_salario - salario

print('O seu salario de R${:.2f} receberá um aumento de R${:.2f} indo para R${:.2f}'.format(salario, aumento, novo_salario))