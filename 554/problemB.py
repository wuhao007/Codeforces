n = int(raw_input())
room = []
for i in range(n):
    s = raw_input()
    room += [s]
room.sort()
mx = 1
c = 1
for i in range(1, n):
    if room[i] == room[i - 1]:
        c += 1
    else:
        c = 1
    mx = max(mx, c)
print mx
