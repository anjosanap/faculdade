"""
Receba a quantidade de dinheiro, em reais, que uma pessoa tem para fazer uma viagem ao exterior.
Receba, também, o valor da cotação do dólar do dia. Calcule e apresente o valor convertido em dólares.
"""

real = float(input('Insira o valor em reais: '))
dolar = float(input('Insira o valor da cotação em dólar: '))

cotacao = real * dolar
print('O valor em dólar é: US$', format(cotacao, '.2f'))
