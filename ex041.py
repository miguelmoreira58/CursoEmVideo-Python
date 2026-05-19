'''
import datetime

ano_atual = datetime.datetime.now().year

ano_nasc = int(input('Qual o ano de nascimento? '))

idade = (ano_atual - ano_nasc)

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')
'''

from datetime import date

atual = date.today().year
nascimento = int(input('Qual o ano de nascimento? '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
