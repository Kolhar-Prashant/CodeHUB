def pair_of_mindiff(n):
    l = sorted(n)
    a,b=0,1
    min_diff = max(l)*10
    while b != len(l):
        if l[b]-l[a] < min_diff:
            min_diff = l[b] - l[a]
        a+=1
        b+=1
    a,b=0,1
    while b != len(l):
        if l[b]-l[a] == min_diff:
            print(l[a],l[b])
        a+=1
        b+=1
n=[4,2,6,10,33,11,99,54,3]
pair_of_mindiff(n)