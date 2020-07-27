
def remove_triple():
    a=0
    b=1
    c=2
    if len(L) == 0:
        return 0
    if len(L) == 1:
        return 1
    if len(L) == 2:
        return 2
    while(b != len(L)-1):
        if L[a] == L[b]:
            if L[b] == L[c]:
                L.remove(L[c])
            else:
                a=b
                b=a+1
                c=b+1
        else:
            a=b
            b=a+1
            c=b+1
    return len(L)

L=[1,3,3,3,4,5,5,5,5,5,6,7,7,8]
Len = remove_triple()
print(Len)