
def square(L):
    sqr=0
    for e in L:
        sqr += e*e
    return sqr

def convert(n):
    s=str(n)
    L=[]
    for e in s:
        L.append(int(e))
    s=square(L)
    return s

n=124
s=convert(n)
print(s)
c=1

while s != 1:
    c+=1
    s=convert(s)
    print(s)
    if s == 1:
        print("Happy number got after",c,"repetations")






