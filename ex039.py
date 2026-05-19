'''
import datetime

ano_atual = datetime.datetime.now().year

ano_nascimento = int(input('Qual o ano de nascimento? '))

ano_de_alistamento = ano_nascimento + 18

if ano_de_alistamento > ano_atual:
    print('Você ainda vai se alistar')
    print('Ainda faltam {} anos para o seu alistamento'.format(ano_de_alistamento - ano_atual))

elif ano_de_alistamento == ano_atual:
    print('Está na hora de se alistar')

else:
    print('Você já passou do tempo de alistamento')
    print('Já se passaram {} anos desde a sua época de alistamento'.format(ano_atual - ano_de_alistamento))
'''

from datetime import date

atual = date.today().year
nasci = int(input('Qual o ano de nascimento? '))

idade = atual - nasci
print('Quem nasceu em {} tem {} anos em {}'.format(nasci, idade, atual))

if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))