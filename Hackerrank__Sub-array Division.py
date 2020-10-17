def birthday(s, d, m):
    L = s
    tar = d
    if len(L) == 1:
        Len = 2
    else:
        Len = len(L)
    indx = 0
    cnt = 0
    while indx != Len-1:
        min_indx = indx
        sum = 0
        try:
            for _ in range(m):
                sum += L[min_indx]
                min_indx += 1
        except:
            return cnt        
        if sum == tar:
            cnt += 1
        indx += 1
    return cnt
