import copy
import math  # Only used to calculate square root of the limit

def generate_Prime_List(limit):    # Generating Prime numbers list

    def prime_sieve(n,sqrt):

        for e in range(2,sqrt+1):
            for i in range(e,n+1):
                c=i*e
                if c > n:
                    break
                else:
                    L[c]=False

        for num in range(2, n+1):
            if L[num] == True:
                prime_List.append(num)

    prime_List=[]
    n= limit
    sqrt=int(math.sqrt(n))
    L=[True for i in range(n+1)]
    prime_sieve(n,sqrt)
    return prime_List


def calc(num,indx):           # Performing Prime factorization.
    p_fact = prime_fact[indx]
    if num % p_fact == 0:
        num //= p_fact
        factor.append(p_fact)
        return num, 0
    elif num in prime_fact:
        factor.append(num)
        return 1, 0
    else:
        return no, -1

numbers = []
indx = 0

no = int(input("for how may numbers you want to calculate LCM: "))
for _ in range(no):
    numbers.append(int(input("Enter the number: ")))

limit = max(numbers)
prime_fact = generate_Prime_List(limit)

Super = []
factor = []

for no in numbers:
    while no != 1:
        no, r = calc(no,indx)
        if r == -1:
            indx += 1
    indx = 0

    Super.append(copy.deepcopy(factor))
    factor.clear()

L = Super
indx = len(L)-1

for _ in range(indx):      # Merging the highest powers.
    cnt = 0
    while cnt != len (L[indx-1]):
        if L[indx-1].count(L[indx-1][cnt]) < L[indx].count(L[indx-1][cnt]):
            L[indx-1].remove(L[indx-1][cnt])
        else:
            diff = abs(L[indx-1].count(L[indx-1][cnt]) - L[indx].count(L[indx-1][cnt]))
            for _ in range(diff):
                L[indx].append(L[indx-1][cnt])
            cnt += 1
    L.remove(L[indx-1])
    indx -= 1
L = L[0]

LCM = 1
for factors in L:
    LCM *= factors
print("LCM of numbers",numbers,"is:",LCM)