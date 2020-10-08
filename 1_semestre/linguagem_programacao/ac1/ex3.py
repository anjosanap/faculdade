import math

l = float(input())

lado = l
area = ((l ** 2.) * (math.sqrt(3)) / 4) * 6
perimetro = l * 6.

print('Lado do hexagono:', lado,'metros,')
print('Area:', area,'metros quadrados,')
print('Perimetro:', perimetro,'metros.')