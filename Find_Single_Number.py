L = [1,2,1,4,4,3,2,24,3]
x = []
y = []

for e in L:
    if e not in x:
        x.append(e)
    else:
        y.append(e)

for e in y:
    if e in x:
        x.remove(e)
print(x)
