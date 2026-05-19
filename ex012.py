"""
preco_produto = float(input('Digite o preço do produto: '))

desconto = preco_produto*5/100 #5% do preço total

valor_final = preco_produto - desconto

print('O preço original era {}, com 5% de desconto ficou {:.2f}'.format(preco_produto,valor_final))
"""

preco_produto = float(input('Digite o preço do produto: '))

preco_com_desconto = preco_produto - (preco_produto*5/100) #5% do preço total

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco_produto, preco_com_desconto))