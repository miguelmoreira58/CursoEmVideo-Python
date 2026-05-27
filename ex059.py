'''
val1 = float(input('Digite o primeiro valor: '))
val2 = float(input('Digite o segundo valor: '))

opcao = 0

while opcao != 5:

    print('-='*10)
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    print('-='*10)

    opcao = int(input('Escolha uma opção do menu: '))

    if opcao == 1:
        soma = val1+val2
        print('\nA Soma de {} e {} é de: {}'.format(val1,val2,soma))
    
    elif opcao == 2:
        multi = val1*val2
        print('\nA multiplicação de {} e {} é de: {}'.format(val1,val2,multi))

    elif opcao == 3:
        if val1 > val2:
            maior = val1
            print('O maior número entre {} e {} é {}'.format(val1,val2,maior))
        elif val2 > val1:
            maior = val2
            print('O maior número entre {} e {} é {}'.format(val1,val2,maior))

        else:
            print('Não há um número maior que o outro pois ambos são iguais')

    elif opcao == 4:
        print('Digite os dois novos números: ')

        val1 = float(input('Digite o primeiro valor: '))
        val2 = float(input('Digite o segundo valor: '))

    elif opcao == 5:
        
        print('Fim do programa')
        opcao = 5

    else:
        print('Opcao inválida. Tente novamente')
'''

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:

    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        soma = n1+n2
        print('A soma entre {} e {} é {}'.format(n1,n2,soma))
    elif opcao == 2:
        produto = n1*n2
        print('O resultado entre {} e {} é {}'.format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior número é {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior número é {}'.format(maior))
        else:
            print('Os numeros são iguais')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida. Tente novamente')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')