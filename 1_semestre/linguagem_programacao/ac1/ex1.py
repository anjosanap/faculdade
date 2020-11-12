import math

n = float(input())
e = math.e

print('i)', n**2)
print('ii)', n**e)
print('iii)', math.sqrt(n))
print('iv)', n**(1/3))
print('v)', n**(1/n))
print('vi)', e*n)
print('vii)', math.pi / n)
print('viii)', math.log(n, 7))
print('ix)', math.log(n, e))
print('x)', math.log(n, math.pi))
