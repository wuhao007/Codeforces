n = int(raw_input())
A = map(lambda a : int(a), raw_input().split())
mn = min(A)
sm = sum(A) 
print mn * n + (n - 1) * n / 2 - sm
