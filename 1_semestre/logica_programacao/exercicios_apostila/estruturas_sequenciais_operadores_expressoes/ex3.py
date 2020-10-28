# Leia um número inteiro de 3 dígitos, determine e apresente o número invertido
# (exemplo: número informado = 345, número apresentado = 543).

n = int(input('Insira um número inteiro de 3 dígitos: '))
rev = 0

while n > 0:
    a = n % 10
    rev = rev * 10 + a
    n = n // 10

print(rev)
