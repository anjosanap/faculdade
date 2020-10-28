"""
Faça um programa que peça a temperatura em grausFahrenheit,
transforme e mostre a temperatura em graus Celsius.
"""

fahrenheit = float(input('Insira sua temperatura em graus Fahrenheit: '))
celsius = (fahrenheit - 32) * 5 / 9
print('Sua temperatura em Celsius é:', '%.1f' % celsius, 'ºC')
