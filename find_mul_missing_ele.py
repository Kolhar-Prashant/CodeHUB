l=[]
for i in range(6,20):
    l.append(i)
x=[6,7,8,10,12,16,17,19]

for e in l:
    if e not in x:
        x.append(e)
x.sort()
print(x)