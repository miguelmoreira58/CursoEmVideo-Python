'''
valor_final=0
mais_de_mil=0

produto_mais_barato = ''
preco_mais_barato = 0

while True:

    produto = str(input('Nome do produto: ')).strip()

    if produto.replace(' ', '').isalpha():

        preco_produto = float(input('Preço: R$'))

        if preco_produto > 0:

            valor_final += preco_produto

             # verifica o produto mais barato
            if preco_mais_barato == 0 or preco_produto < preco_mais_barato:
                preco_mais_barato = preco_produto
                produto_mais_barato = produto

            if preco_produto > 1000:

                mais_de_mil += 1

            continuar_ou_parar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

            if continuar_ou_parar in 'S':
                print('\nContinuando!')
            elif continuar_ou_parar in 'N':
                print(f'\nO total da compra foi de R${valor_final}')
                print(f'Temos {mais_de_mil} produtos custando mais de R$1000.00')
                print(f'O produto mais barato é {produto_mais_barato} que custa R${preco_mais_barato}')
                print('\n\nEncerrando...')
                break
            else:
                print('Opção inválida')
        else:
            print('Preço de produto inválido.')
    else:
        print('Nome de Produto inválido.')
'''
total = 0
totmil = 0

menor = cont = 0
barato = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    
    if preco > 1000:
        totmil += 1
    
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')