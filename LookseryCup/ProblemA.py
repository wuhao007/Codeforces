n, m = map(lambda x : int(x), raw_input().split())
image = [raw_input() for i in range(n)]
count = 0    
for i in range(n - 1):
    for j in range(m - 1):
        if ''.join(sorted([image[i][j], image[i][j + 1], image[i + 1][j], image[i + 1][j + 1]])) == "acef":
            count += 1
print count
