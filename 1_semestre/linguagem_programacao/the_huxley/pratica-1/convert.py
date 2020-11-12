"""
Faça um programa que receba um valor em polegadas, converta e imprima o resultado em milímetros.
A entrada será um número real e não deve ser impresso nenhum texto para pedi-la.
A saída deverá ser o valor em polegadas e o resultado em milímetros.
Os números devem ser exibidos sem nenhuma formatação explícita quanto ao número de casas decimais.
"""

polegadas = float(input())
milimetros = polegadas * 25.4

print(polegadas, 'polegada(s) eh o mesmo que', milimetros, 'mm')
