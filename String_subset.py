def check_subset(s,t):
    si = len(s)-1
    ti = len(t)-1
    cnt = 0
    while si > -1:
        if s[si] == t[ti]:
            cnt+=1
            si-=1
            ti-=1
        else:
            si-=1
        
    if cnt == len(t):
        return "t is subset in s"
    return "t not a subset in s"

s = "cmxinutes"
t = "cinnes"
print(check_subset(s,t))        