
x=[6,7,8,10,12,16,12,8]
l=[]
for e in x:
    if e not in l:  #memoization concept.
        l.append(e)
    else:
        print("Dup ele",e)