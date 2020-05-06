
n = int(input())
s = str(input())

s = str(s).replace(" ", ",")
L = []
x = s.split(",")

for e in x:
    L.append(int(e))
print(L)
p=L
p=sorted(p)
p=list(set(p))
print(p)
max=p[-1]
base=p[-2]
print(max,base)
f=0
r=len(L)-1
F=0
R=0
wall_start=0
wall_end=0

for x in range(len(L)):
    if L[f] >= base and F != 1:
        wall_start=f
        F=1
        if F== 1 and R==1:
            break
    else:
        f+=1
    if L[r] >= base and R != 1:
        wall_end=r
        R=1
        if F== 1 and R==1:
            break
    else:
        r-=1

units=0
for e in L[wall_start:wall_end+1]:
    if e <= base:
        #print(e,base,base-e)
        units += base-e
print(units)