"""
Faça um programa que receba uma temperatura em Fahrenheit, calcule e imprima o valor convertido para a
escala Celsius e para a escala Kelvin, de acordo com as equações de conversão
"""

t_fahrenheit = float(input())

t_celsius = (t_fahrenheit - 32) * 5/9
t_kelvin = t_celsius + 273.15

print(f'Convertendo {t_fahrenheit} graus Fahrenheit temos:\n{t_celsius} graus Celsius e {t_kelvin} Kelvin')
