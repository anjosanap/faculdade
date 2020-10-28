"""
Elabore o fluxograma de um programa que leia dois números reais e
mostre o resultado da diferença do maior valor pelo menor.
"""

y = int(input('Insira o primeiro número: '))
x = int(input('Insira o segundo número: '))

if y > x:
    sub = y - x
    print('A diferença do maior valor pelo menor é:', sub)
else:
    if x > y:
        sub = x - y
        print('A diferença do maior valor pelo menor é:', sub)
    else:
        print("Shit! It's equal :P")
