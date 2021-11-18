import re
def licenseKeyFormatting(s: str, k: int) -> str:
    if re.search('[a-zA-Z0-9]',s) == None:
        return ""
    s = list(reversed(s.upper()))
    f = 0
    while True:
        if s[f] == '-':
            s.pop(0)
            continue
        else:
            break
        f+=1
    l = len(s)-1
    while True:
        if s[l] == '-':
            s.pop(-1)
        else:
            break
        l-=1
    cnt = 0
    mem, temp = [], []
    indx=0
    while indx != len(s):
        char = s[indx]
        if cnt != k:
            if char != '-':
                temp.append(char)
                cnt+=1
        else:
            temp.append('-')
            mem.append(''.join(list(reversed(temp))))
            temp.clear()
            cnt=0
            continue
        indx+=1
    if len(temp) > 0:
        mem.append(''.join(list(reversed(temp))))
    return("".join(list(reversed(mem))))
s = "5F3Z-2e-9-w"
k = 4
print(licenseKeyFormatting(s,k))