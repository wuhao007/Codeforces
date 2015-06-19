n, m, q = map(lambda x : int(x), raw_input().split())
mat = []
vec = [0 for i in range(n)]
def count_line(i, vec):
    cnt = 0
    mx = 0
    flag = True
    for j in range(m):
        if mat[i][j] == 1:
            if flag:
                cnt += 1
            else:
                flag = True
                cnt = 1
        else:
            flag = False
        mx = max(mx, cnt)
    vec[i] = mx
for i in range(n):
    mat += [map(lambda x : int(x), raw_input().split())]
    count_line(i, vec)
for _ in range(q):
    i, j = map(lambda x : int(x) - 1, raw_input().split())
    if mat[i][j] == 1:
        mat[i][j] = 0
    else:
        mat[i][j] = 1
    count_line(i, vec)
    print max(vec)
