# Crie um programa que receba como e
# um número natural n e exiba n!.

n = int(input('Digite um número: '))
f = 1
i = 1

while i <= n:
    f = f * i
    i += 1

print('%d! = %d' % (n, f))
