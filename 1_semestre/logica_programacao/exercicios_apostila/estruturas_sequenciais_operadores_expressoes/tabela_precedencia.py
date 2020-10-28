print('Desenvolva as expressões abaixo usando a tabela de precedência e calcule seu resultado:')

print('(a) 4 + 2 ** 5 // 10')
a = 2 ** 5
a = a + 4
a = a // 10
a = ((4 + (2 ** 5)) // 10)
print('Resposta:', a)
print('')

print('(b) 5 + 42 % 10')
b = (5 + 42) % 10
b = (5 + (42 % 10))
print('Resposta:', b)
print('')


print('(c) -3 * 2 + 2 / 5 * 10 + 3')
c = -3 * 2 + 2 / 5 * 10 + 3
print('Resposta:', c)
print('')

print('(d) 2 ** 4 / 2 + 2 % 5 * 3')
d = 2 ** 4 / 2 + 2 % 5 * 3
print('Resposta:', d)
