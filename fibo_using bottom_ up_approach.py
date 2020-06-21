#fibonacci series using bottom up approach
def fibo (a,b,cnt):
    cnt+=1
    sum = a+b
    if cnt != lim:
        fibo(b,sum,cnt)
    else:
        print("fib of",lim,"is",sum)
cnt=1
lim=6
fibo(0,1,cnt)