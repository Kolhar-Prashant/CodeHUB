L = [1,9,3,0,18,5,2,4,10,7,12,6]
for n in L:
    if n-1 not in L:
        cnt = 0
        r = range(n,max(L)+1)
        for num in r:
            if num in L:
                cnt+=1
            else:
                break
        print(n,cnt)
        