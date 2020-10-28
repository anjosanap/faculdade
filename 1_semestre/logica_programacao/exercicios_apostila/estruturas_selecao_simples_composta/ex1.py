from math import sqrt

print('Determine os resultados obtidos na avaliação das expressões lógicas a seguir sabendo que: ')

a = 2
b = 7
c = 3.5
m = True
n = False

print('i)', b == a * c and (m or n))
print('ii)', b > a or b == pow(a, a))
print('iii)', m and b // a >= c or not a <= c)
print('iv)', not m or n and sqrt(a + b) >= c)
print('v)', b/a == c or b/a != c)
print('vi)', m or pow(b, a) <= c * 10 + a * b)
