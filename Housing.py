L=[5,3,2,1,7]
a,b=0,0
tar = 8
while b != len(L):
    t = L[a:b+1]
    sum = 0
    for n in t:
        sum += n
    if sum == tar or sum > tar:
        if sum == tar:
            print(a,b)
        a+=1
        b=a+1
    elif sum < tar:
        b+=1