s = raw_input().strip()
k = int(raw_input())
n = len(s)
step = n / k
def palindrome(i, j):
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
if n % k != 0:
    print "NO"
else:
    res = "YES"
    for i in range(0, n, step):
        if not palindrome(i, i + step - 1):
            res = "NO"
            break
    print res
        
