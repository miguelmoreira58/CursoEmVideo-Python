'''
from datetime import date

ano_atual = date.today().year

maior_de_idade = 0
menor_de_idade = 0

for c in range(1, 8):
    ano_nascimento = int(input('Digite o ano de nascimento da {} pessoa: '.format(c)))

    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maior_de_idade += 1
    else:
        menor_de_idade += 1

print('Temos {} menores de idade e {} maiores de idade.'.format(menor_de_idade,maior_de_idade))
'''

from datetime import date

atual = date.today().year

totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '. format(pess)))
    idade = atual - nasc

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))