
def check_next(index):
    index+=1
    if index < Len:
        e=m[index]
        return e
    else:
        index-=1
        e=m[index]
        return e

s='122233145555'
print(s)
m=[]
m=list(s)
Len=len(m)
D={}
c=1
indx=0
F=[]
for indx in range(len(m)-1):
    e=m[indx]
    ne=check_next(indx)
    if ne == e:
        c+=1
        D[e]=c
        F.append(e)
        F.append(c)
    else:
        D[e]=c
        c=1
        F.append(e)
        F.append(c)

print(D)
