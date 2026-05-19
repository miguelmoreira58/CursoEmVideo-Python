n = str(input('Digite seu nome completo: ')).strip() #eliminando espaços antes e depois com strip
nome = n.split() #vai pegar o nome inteiro e dividir em pedaços separados por espaços

print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1])) #tamanho total menos um vai pegar o ultimo nome