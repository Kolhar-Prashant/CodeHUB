
def calc (num,indx):
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

prime_fact = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
factor = []
no = 48
base_no = no
indx = 0

while no != 1:
    no, r = calc(no,indx)
    if r == -1:
        indx += 1

print("Prime factors of",base_no,"are",factor)
