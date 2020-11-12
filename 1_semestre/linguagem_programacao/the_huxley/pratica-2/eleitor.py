"""
Faça um programa que leia a idade (valor inteiro) de uma pessoa e informe sua classe eleitoral.
"""

idade = int(input())

if idade < 16:
    print('nao eleitor')
else:
    if 18 <= idade <= 65:
        print('eleitor obrigatorio')
    else:
        if 16 <= idade < 18 or idade > 65:
            print('eleitor facultativo')
