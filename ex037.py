numero = int(input('Digite um numero inteiro: '))

print('''
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')

opcao = int(input('Escolha uma opcao: '))

if opcao == 1:
    print('O valor {} convertido para binario é {}'.format(numero, bin(numero)[2:]))

elif opcao == 2:
    print('O valor {} convertido para octal é {}'.format(numero, oct(numero)[2:]))

elif opcao == 3:
    print('O valor {} convertido para hexadecimal é {}'.format(numero, hex(numero)[2:]))

else:
    print('Opcao invalida')