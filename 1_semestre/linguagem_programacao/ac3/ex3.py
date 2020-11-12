n = int(input())

i = 1
soma = 0

while i <= n:
    d = (i * i)
    i = i + 1
    soma = soma + (1 / d)

print(f'{soma:.6f}')
