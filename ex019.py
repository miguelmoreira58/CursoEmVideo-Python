'''
import random

alunos = int(input('Quantos alunos serão sorteados? '))

lista_alunos = []

for aluno in range(alunos):

    nome_aluno = str(input('Digite o nome do aluno: '))
    lista_alunos.append(nome_aluno)

sorteado = random.choice(lista_alunos)

print('O aluno sorteado foi {}'.format(sorteado))
'''

import random

nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)

print('\nO aluno escolhido foi {}'.format(escolhido))