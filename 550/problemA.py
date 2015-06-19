s = raw_input().strip()
min_ab = s.find("AB")
max_ba = s.rfind("BA")
if abs(max_ba - min_ab) >=2:
    print "YES"
else: 
    max_ab = s.rfind("AB") 
    min_ba = s.find("BA")
    if abs(max_ab - min_ba) >=2:
        print "YES"
    else:
        print "NO"
