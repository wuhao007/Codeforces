n = int(raw_input())
s = 0
t = 1
while t <= n:
    s += (n - (t - 1))
    t *= 10
print s
