n = int(input())

soma = 0

for d in range(1, n + 1):
    value = 1 / d

    if d % 2 != 0:
        soma -= value
    else:
        soma += value

print(f'{soma:.6f}')
