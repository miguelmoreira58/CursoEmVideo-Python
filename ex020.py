'''
import random

lista_alunos = []

for aluno in range(4):

    nome_aluno = str(input('Digite o nome do aluno: '))
    lista_alunos.append(nome_aluno)

sorteado1 = random.choice(lista_alunos)
lista_alunos.remove(sorteado1)

sorteado2 = random.choice(lista_alunos)
lista_alunos.remove(sorteado2)

sorteado3 = random.choice(lista_alunos)
lista_alunos.remove(sorteado3)

sorteado4 = random.choice(lista_alunos)
lista_alunos.remove(sorteado4)

print('\nO primeiro aluno sorteado foi {}, o segundo {}, o terceiro {} e o quarto {}.'.format(sorteado1, sorteado2, sorteado3, sorteado4))
'''

#import random
from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]

shuffle(lista) #shuffle = Embaralhar

print('A ordem de apresentação será: ')
print(lista)

