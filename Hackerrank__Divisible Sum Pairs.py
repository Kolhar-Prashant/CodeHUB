def divisibleSumPairs(n, k, ar):
    L = ar
    a = 0
    b = 1
    itr = 0
    cnt = 0
    while a != len(L)-1:
        if ((L[a]+L[b]) % k == 0):
            cnt += 1
        b+=1
        if b == len(L):
            itr += 1 
            a = itr
            b = a + 1
    return cnt