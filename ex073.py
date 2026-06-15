tabela_campeonato_brasileiro = ('Palmeiras','Flamengo','Fluminense','Athletico-Paranaense',
                                'Red-Bull-Bragantino','Bahia','Coritiba','São-Paulo','Atlético-MG',
                                'Corinthians','Cruzeiro','Botafogo','Vitória','Internacional',
                                'Santos','Grêmio','Vasco-da-gama','Remo','Mirassol','Chapecoense')

print('=-'*30)
print(f'Lista de times do Brasileirão: {(tabela_campeonato_brasileiro)}')

print('=-'*30)
print(f'Os 5 primeiros são: {(tabela_campeonato_brasileiro[0:5])}')

print('=-'*30)
print(f'Os 4 últimos são: {(tabela_campeonato_brasileiro[-4:])}')

print('=-'*30)
print(f'Times em ordem alfabética: {sorted(tabela_campeonato_brasileiro)}')

print('=-'*30)
print(f'O Chapecoense está na {tabela_campeonato_brasileiro.index('Chapecoense')+1} posição')