import math

area = float(input())

lata_g = 24 * 7
preco_g = 91.00
quantidade_g = math.ceil(area / lata_g)
total_g = quantidade_g * preco_g

lata_p = 5.4 * 7
preco_p = 23.00
quantidade_p = math.ceil(area / lata_p)
total_p = quantidade_p * preco_p

mix_g, resto = divmod(area, lata_g)
if resto != 0:
    mix_p = math.ceil(resto / lata_p)
mix_g = math.ceil(mix_g)
total = (mix_g * preco_g) + (mix_p * preco_p)

print('a)', quantidade_g,'lata(s) de 24 litros: R$', "{:.2f}".format(total_g))
print('b)', quantidade_p,'lata(s) de 5.4 litros: R$', "{:.2f}".format(total_p))
print('c)', mix_g,'lata(s) de 24 litros e', mix_p,'lata(s) de 5.4 litros: R$', "{:.2f}".format(total))