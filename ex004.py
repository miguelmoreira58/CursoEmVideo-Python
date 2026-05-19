texto = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(texto))
print('Só tem espaços? ', texto.isspace())
print('É um número?', texto.isnumeric())
print('É alfabético?', texto.isalpha())
print('É alfanumérico?', texto.isalnum())
print('Está em maiúsculas?', texto.isupper()) #PYTHON
print('Está em minusculas?', texto.islower()) #python
print('Está capitalizada?', texto.istitle()) #capitalizado = Python, Título, etc...