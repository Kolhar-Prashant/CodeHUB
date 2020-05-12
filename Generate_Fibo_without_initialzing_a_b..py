
def gen_Fib(limit):
    a=0
    b=0
    for i in range(limit):
        if a == 0 and b==0:
            a=i
            b=a+1
        sum=a+b
        print(sum)
        a=sum-a
        b=sum
        if sum > limit:
            break

limit=int(input("Enter the limit of fibo series: "))
gen_Fib(limit)