print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

qtd_termos = int(input('Quantos termos você quer mostrar? '))

t1 = 0
t2 = 1

print('~'*30)
print('{} -> {}'.format(t1,t2), end='')

cont = 3 #começa em três porque já mostramos o primeiro e segundo termo
while cont <= qtd_termos:
    t3 = t1 + t2
    print(' -> {}'.format(t3),end='')

    t1 = t2
    t2 = t3

    cont += 1
print(' -> FIM')
print('~'*30)