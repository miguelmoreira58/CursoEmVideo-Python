nome = str(input('Qual é seu nome completo? ')).strip()
#print('Seu nome tem silva? {}'.format(nome[:5] == 'Silva'))
print('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))