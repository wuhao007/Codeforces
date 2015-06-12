a = raw_input().strip()
b = raw_input().strip()
c = raw_input().strip()
#print a, b, c
t_set = set("qwertyuiopasdfghjklzxcvbnm")
#print len(t_set)
def genDic(s):
    d = {k:0 for k in t_set}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

a_dic = genDic(a)
b_dic = genDic(b)
c_dic = genDic(c)

#print a_dic, b_dic, c_dic

def isOneOK(x, d):
    for k, v in a_dic.items():
        if x * d[k] > v:
            return False
    return True

def isBothOK(x, y):
    for k, v in a_dic.items():
        if x * b_dic[k] + y * c_dic[k] > v:
            return False
    return True
x = 0
max_x = 0
y = 0
max_y = 0
mx = 0
while isOneOK(x, b_dic):
    while isBothOK(x, y):
        if mx < x + y:
            max_x = x
            max_y = y
            mx = x + y
        y += 1
    x += 1
    y = 0

for k, v in a_dic.items():
    a_dic[k] -= (max_x * b_dic[k] + max_y * c_dic[k])
import string
print b * max_x + c * max_y + ''.join([ c * a_dic[c] for c in string.lowercase])
