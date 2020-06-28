
def conv_Roman_to_Integer(str):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    L = list(str)
    a = 0
    b = 1
    sum = 0
    total_sum = 0

    while (b < len(L)):
        if d[L[a]] < d[L[b]]:
            total_sum += d[L[b]] - d[L[a]]
            L[a] = '-'
            L[b] = '-'
            a = b + 1
            b = a + 1
        else:
            a += 1
            b += 1

    for e in L:
        if e != '-':
            total_sum += d[e]
    return total_sum

s = "MCMXCVI"  #input roman value
v = conv_Roman_to_Integer(s)
print("Integer value :",v,"of Roman value :",s)