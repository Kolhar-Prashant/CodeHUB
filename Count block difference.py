# Problem statement
'''Given an array of positive integers, divide it into two sets such that the absolute difference between their sums is smallest.
Return the minimum difference.

Input: [3, 7, 2, 5]
Output: 1
Explanation: [2, 7], [3, 5]'''

from itertools import permutations

def div_array(L):
    start = 0
    mem = []
    for end in range(len(L)):
        a = L[start:end+1]
        b = L[end+1:len(L)+1]
        a_sum = 0
        b_sum = 0
        for indx in range(len(b)):
            if indx < len(a):
                a_sum += a[indx]
            if indx < len(b):
                b_sum += b[indx]
        diff = a_sum - b_sum
        if diff > 0:
            mem.append(a_sum - b_sum)
    return mem

L = [3, 7, 2, 5]
x = permutations(L)
min_diff = 0
for num in L:
    min_diff += num
for l in x:
    List = list(l)
    mem = div_array(List)
    if len(mem) > 0:
        mem = sorted(mem)
        diff = mem[0]
        if diff > 0:
            if diff < min_diff:
                min_diff = diff
print(min_diff)


