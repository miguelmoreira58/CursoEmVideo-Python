soma = 0
contador = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))

    if num == 999:
        break

    soma += num #embaixo do break não conta o 999
    contador += 1
print(f'A soma dos {contador} valores foi {soma}')