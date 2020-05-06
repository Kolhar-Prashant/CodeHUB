def add_ele(start_indx):
    s = 0
    for e in L[start_indx:]:
        t = []
        s += e
        x.append(e)
        D.append(s)

        for i in x:
            t.append(i)
        D.append(t)
    x.clear()

L = [-2,1,-3,4,-1,2,1,-5,4]
s = 0
D = []
x=[]

for i in range(len(L)):
    add_ele(i)

count=[]
for i in range(len(D)):
    if i%2 == 0:
        count.append(D[i])

x=sorted(count)
indx=count.index(x[-1])*2+1

print(D[indx],x[-1])