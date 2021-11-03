L = [2,6,4,8,10,9,15]
a,b=0,1
s,e=-1,-1
while b != len(L):
    if L[a] > L[b]:
        s = a
    if s != -1:
        if L[a] < L[s]:
            e = a
    a+=1
    b+=1
print(s,e)
    