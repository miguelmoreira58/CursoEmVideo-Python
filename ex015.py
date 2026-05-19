"""
dias = int(input('Quantos dias alugados? '))
km_rodado = float(input('Quantos Km rodados? '))

custo_carro_diaria = (60*dias)
custo_carro_km = (0.15*km_rodado)

total_a_pagar = custo_carro_diaria + custo_carro_km

print('O total a pagar é R${:.2f} reais.'.format(total_a_pagar))
"""

dias = int(input('Quantos dias alugados? '))
km_rodado = float(input('Quantos Km rodados? '))

total_a_pagar = (dias*60) + (0.15*km_rodado)

print('O total a pagar é de R${:.2f} reais.' .format(total_a_pagar))