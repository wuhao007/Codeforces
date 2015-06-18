n = int(raw_input())
s = 0
for i in range(n):
    x1, y1, x2, y2 = map(lambda x : int(x), raw_input().split())
    s += (x2 - x1 + 1) * (y2 - y1 + 1)
print s
