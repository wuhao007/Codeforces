s = raw_input()
n = len(s)
st = set()
for i in range(n + 1):
    for c in "qwertyuiopasdfghjklzxcvbnm":
        st.add(s[:i] + c + s[i:])
print len(st)
