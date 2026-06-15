tupla_numeros = ('zero','um','dois','tres','quatro',
                 'cinco','seis','sete','oito','nove',
                 'dez','onze','doze','treze','quatorze',
                 'quinze','dezesseis','dezesete',
                 'dezoito','dezenove','vinte')

numero = int(input('Digite um número entre 0 e 20: '))

while True:
    if numero >= 0 and numero < 21:
        print(f'Você digitou o número {tupla_numeros[numero]}')
        break
    else:
        numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
