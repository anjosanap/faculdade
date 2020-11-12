r = int(input())
n = int(input())
c = 1

soma = 0

while c < n + r:
    count = c
    soma = soma + count

    c = c + r

print(f'A somatoria da PA eh: {soma}')
