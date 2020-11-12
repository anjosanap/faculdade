"""
Escreva um programa que leia dois valores inteiros da entrada padrão e informe qual é o maior.
Se os números forem iguais, imprima qualquer um deles.
"""

n1 = int(input())
n2 = int(input())

if n1 == n2:
    print(n1)

else:
    if n2 > n1:
        print(n2)
    else:
        print(n1)
