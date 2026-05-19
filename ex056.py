soma_da_idade = 0
media_da_idade = 0

maior_idade_homem = 0
nome_velho = ''

tot_mulher_20 = 0

for p in range(1,5):
    print('----- {} PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    soma_da_idade += idade

    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        tot_mulher_20 += 1

media_da_idade = soma_da_idade / 4
print('A média da idade do grupo é de {} anos'.format(media_da_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(tot_mulher_20))