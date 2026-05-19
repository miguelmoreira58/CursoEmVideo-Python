'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Reprovado')
elif media >= 5 and media <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print('Tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, media))

if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÂO')
elif media < 5:
    print('O aluno está REPROVADO')
elif media >= 7:
    print('O aluno está APROVADO')