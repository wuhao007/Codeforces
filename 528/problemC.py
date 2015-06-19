m = int(raw_input())
h1, a1 = map(lambda x : int(x), raw_input().split())
x1, y1 = map(lambda x : int(x), raw_input().split())
h2, a2 = map(lambda x : int(x), raw_input().split())
x2, y2 = map(lambda x : int(x), raw_input().split())
s = set()
s.add((h1, h2))
cnt = 0
while True:
    cnt += 1
    h1 = (x1 * h1 + y1) % m
    h2 = (x2 * h2 + y2) % m

    if h1 == a1 and h2 == a2:
        print cnt
        break
    elif (h1, h2) in s:
        print -1
        break
    else:
        s.add((h1, h2))
    
