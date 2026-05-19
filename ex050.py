soma = 0

for n in range(1,7):
    numero = int(input('Digite o {} valor: '.format(n)))
    if numero % 2 == 0:
        soma += numero
print(soma)