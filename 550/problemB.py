import itertools
n,l,r,x = map(lambda x : int(x), raw_input().split())
c = map(lambda x : int(x), raw_input().split())
c.sort()
cnt = 0
for L in range(0, len(c)+1):
    for subset in itertools.combinations(c, L):
        if l <= sum(subset) <= r and (subset[-1] - subset[0]) >= x:
            cnt += 1
print cnt 
            
