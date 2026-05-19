preco_normal = float(input('Digite o preço do produto: '))

print('''
Formas de pagamento:
[1] - a vista no dinheiro/cheque (10% de desconto)
[2] - a vista no cartão (5% de desconto)
[3] - em 2x no cartão (preço normal)
[4] - em 3x ou mais no cartão (20% de juros)''')

forma_de_pagamento = int(input('Qual a forma de pagamento? '))

if forma_de_pagamento == 1:
    valor_final = preco_normal - (preco_normal * 10/100)
    print('O valor a pagar será de R${:.2f}'.format(valor_final))
elif forma_de_pagamento == 2:
    valor_final = preco_normal - (preco_normal * 5/100)
    print('O valor a pagar será de R${:.2f}'.format(valor_final))
elif forma_de_pagamento == 3:
    valor_final = preco_normal
    print('O valor a pagar será de R${:.2f}'.format(valor_final))
elif forma_de_pagamento == 4:
    valor_final = preco_normal + (preco_normal * 20/100)
    print('O valor a pagar será de R${:.2f}'.format(valor_final))
else:
    print('Opção Inválida.')
