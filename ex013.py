"""
salario = float(input('Digite o seu salário: '))

porcentagem_de_aumento = salario*15/100

salario_final = salario + porcentagem_de_aumento

print('O salario inicial é de {:.2f}, com 15% de aumento fica {:.2f}'.format(salario,salario_final))
"""

salario = float(input('Digite o seu salário: '))

salario_com_aumento = salario + (salario*15/100) #salario com 15% de aumento

print('Um funcionario que ganhava R${:.2f}, com 15% de aumento passa a receber R${:.2f}'.format(salario, salario_com_aumento))