def sockMerchant(n, ar):
    L = ar
    L = sorted(L)
    d = {}

    for sock in L:
        if sock not in d:
            cnt = 1
            d[sock] = cnt
        else:
            cnt = d[sock]
            cnt += 1
            d[sock] = cnt

    for sock, cnt in d.items():
        if cnt % 2 != 0:
            cnt = d[sock]
            d[sock] = cnt - 1
    sum = 0
    for sock , cnt in d.items():
        sum += cnt
    return(sum//2)