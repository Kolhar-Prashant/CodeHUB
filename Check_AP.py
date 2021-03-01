'''
Given an array of positive integers, check if all its distinct values can be rearranged to form an arithmetic progression and return its difference. Otherwise return 0.
Input: [180, 30, 180, 80, 130, 130]
Output: 50
'''
from itertools import permutations

def check_AP(L):
    a=0
    b=1
    diff = 0
    while b != len(L):
        diff = L[b] - L[a]
        if a != 0:
            if diff != last_diff:
                return -1
        a+=1
        b+=1
        last_diff = diff
    return diff

L = [180, 30, 180, 80, 130, 130]
L = list(sorted(set(L)))
New_list = permutations(L)

MyList = []
for arr in New_list:
    MyList.append(list(arr))

diff=0
mem = []
for array in (MyList):
    diff = check_AP(array)
    mem.append(diff)
AP = 0
for diff in mem:
    if diff > 0:
        AP = diff
print(AP)