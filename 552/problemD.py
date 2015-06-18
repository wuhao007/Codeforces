import math
n = int(raw_input())
points = []
for _ in range(n):
    points += [tuple(map(lambda x : int(x), raw_input().split()))]
def distance(i, j):
    return math.sqrt((points[i][1] - points[j][1])**2 + (points[i][0] - points[j][0])**2)
cnt = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            ij = distance(i, j)
            ik = distance(i, k)
            jk = distance(j, k)
            if (ij + ik - jk) <= 0.001 or (ij + jk - ik) <= 0.001 or (ik + jk - ij) <= 0.001: 
                continue
            else:
                cnt += 1
print cnt
                
