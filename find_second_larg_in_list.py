
def find_max(temp,l,max_list):

    n_max=temp
    for e in l:
        if e > n_max and e not in max_list:
            n_max=e
    max_list.append(n_max)
    return 0,n_max,max_list

x=[879,-98756,6,7,8,10,12,5,17,19,4,-998,3657,124,24,2124]
max=min=x[0]
n=int(input("Enter which largest to be search : "))
if n > 0:
    if n <= len(x):
        for e in x:
            if e > max:
                max=e
            elif e < min:
                min=e
        t_max=min
        max_list=[max]

        for _ in range(0,n-1):
            t,max,max_list=find_max(t_max,x,max_list)

        if n == 1:
            print("1st largest in a list",str(max),str(max_list))
        elif n == 2:
            print("2nd largest in a list", str(max),str(max_list))
        elif n == 3:
            print("3rd largest in a list", str(max),str(max_list))
        else:
            print(str(n),"th largest in a list", str(max),str(max_list))
    else:
        print("Sorry value greater than list length !!")
else:
    print("Invalid input!",n)