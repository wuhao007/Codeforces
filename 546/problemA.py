k, n, w = map(lambda x : int(x), raw_input().split())
r = (1 + w) * w / 2 * k - n
print r if r > 0 else 0
