def max_unique_substring(s):
    a,b=0,0
    mem = []
    max_dict = {}
    while a != len(s)-1:
        if s[b] not in mem:
            mem.append(s[b])
            if b < len(s)-1:
                b+=1
            else:
                a+=1
                b=a
        else:
            max_dict[len(mem)]= "".join(mem)
            mem.clear()
            a+=1
            b=a
    return max_dict[max(max_dict)]
s = "abcadb"
print(max_unique_substring(s))
