n = raw_input().strip()
A = map(lambda x : int(x), raw_input().split())
A_sort = sorted([(A[i], i) for i in range(len(A))], reverse=True)
result = [0 for i in range(len(A))]
rank = ''
sore = -1
for j in range(len(A_sort)):
    (a, i) = A_sort[j]
    if a == sore:
        result[i] = rank
    else:
        result[i] = str(j + 1)
        sore = a
        rank = str(j + 1)
print ' '.join(result)
