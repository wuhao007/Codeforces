w, m = map(lambda x : int(x), raw_input().split())
wp = 1
while wp < m:
    wp *= w
nwp = 0
while wp > 0:
    if nwp > m:
        nwp -= wp
    elif nwp == m:
        break
    else:
        nwp += wp
    wp /= w
print 'YES' if nwp == m else 'NO'
