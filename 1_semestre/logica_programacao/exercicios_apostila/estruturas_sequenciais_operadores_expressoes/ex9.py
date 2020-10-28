"""
Modifique o programa de conversão de temperatura, construído anteriormente, para converter de Celsius para Fahrenheit.
A fórmula de conversão é: F = C ∙ 9/5 + 32
"""

celsius = float(input('Insira sua temperatura em graus Celsius: '))
fahrenheit = celsius * 9 / 5 + 32
print('Sua temperatura em Celsius é:', '%.1f' % fahrenheit, 'ºF')
