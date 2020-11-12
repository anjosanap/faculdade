"""
Receba o peso de uma pessoa, calcule e mostre:
a) o novo peso, se a pessoa engordar 5% sobre o peso digitado;
b) o novo peso, se a pessoa emagrecer 10% sobre o peso digitado.
"""

peso = float(input('Insira seu peso: '))
print('Peso atual: ', peso, 'kg', sep='')

a = peso + (peso * (5/100))
print('a) Se você engordar 5%, seu peso será:', a)

b = peso - (peso * (10/100))
print('b) Se você emagrecer 10%, seu peso será:', b)
