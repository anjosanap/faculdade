"""
Complete o código do programa em Python3 que recebe dois valores quaisquer, armazenando-os nas variáveis v1 e v2,
e em seguida troca os valores de v1 e v2 e imprime os valores trocados.
As entradas poderão ser quaisquer caracteres ou conjuntos de caracteres do teclado.
A saída devera ser as duas entradas impressas na ordem inversa. Serão impressos os valores armazenados em v1 e v2,
nessa ordem, mas o programa deverá ter trocado os valores recebidos em cada variável.
"""

v1 = input()
v2 = input()

aux = v2
v2 = v1
v1 = aux

print('valor em v1:', v1)
print('valor em v2:', v2)
