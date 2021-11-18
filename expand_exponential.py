def expand_exponential(L):
    start,exp,mem = 0,0,[]        
    while start < len(L):
        end = start + 2**exp
        mem.append(L[start:end])
        exp+=1
        start = end
    return mem
L = list(range(1,12))
print(expand_exponential(L))