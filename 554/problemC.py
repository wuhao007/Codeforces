import math
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

k = int(raw_input())
balls = []
n = 0
for i in range(k):
    c = int(raw_input())
    n += c
    balls += [c]
n -= k
result = 1
for i in range(k, 0, -1):
    m = balls[k - 1]
    w = 0
    for j in range(m):
        w += nCk(n - j, m - j)

print result
