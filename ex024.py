#cidade = str(input('Em que cidade você nasceu? '))
#print(cidade[:5] == 'Santo')

cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')