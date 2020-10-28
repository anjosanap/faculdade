"""
Leia dois números inteiros e exiba o quadrado da diferença do primeiro valor pelo segundo.
"""

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

diferenca = (n1 ** 2) - (n2 ** 2)
quadrado = (n1-n2) ** 2

print('Diferença dos quadrados:', diferenca)
print('Quadrado da diferença:', quadrado)
