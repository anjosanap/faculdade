"""
Faça um programa que receba a idade em segundos,
calcule e exiba a idade convertida em dias, horas e minutos.
"""


def convert(age):
    day = age // (24 * 3600)

    age = age % (24 * 3600)
    hour = age // 3600

    age %= 3600
    minutes = age // 60

    print('%d' % day, 'dias', hour, 'horas', minutes, 'minutos')


age = float(input('Insira sua idade em segundos: '))
convert(age)
