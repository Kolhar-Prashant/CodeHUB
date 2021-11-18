def first_non_rep_char(L):
    dict = {}
    for c in L:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
        Found = False
        for char, val in dict.items():
            if val == 1:
                print(char,end=" ")
                Found = True
                break
        if Found == False:
            print('-1',end=" ")
L = 'aabccbcd'
first_non_rep_char(L)