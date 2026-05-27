sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF': #enquanto sexo nao estiver igual a "M" ou "F", continue...
    sexo = str(input('Resposta inválida. Digite apenas M ou F: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso!'.format(sexo))