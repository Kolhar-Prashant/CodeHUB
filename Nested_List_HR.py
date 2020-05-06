#Nested list
if __name__ == '__main__':
    T = []
    L = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        T.append(name)
        T.append(score)
        L.append(T)
        T = []

    D = {}
    mark_l = []
    for e in L:
        D[e[0]] = e[1]
        mark_l.append(e[1])

    mark_l = sorted(mark_l)
    n_list = []
    smlest_el = mark_l[0]

    for e in mark_l:
        if e != smlest_el:
            n_list.append(e)

    secnd_small = n_list[0]
    Final_L = []

    for k, v in D.items():
        if v == secnd_small:
            Final_L.append(k)

    Final_L = sorted(Final_L)
    mark_l = []
    T = []
    L = []
    n_list = []
    for e in Final_L:
        print(e)

