#optimized
def check(amt,indx):
    for coin in reversed(L[:indx]):
        if coin <= amt:
            x.append(coin)
            amt-=coin
            indx=L.index(coin)+1
            return amt,indx

L=[1,2,5,10,20,50,100,200,500,2000]
amt=2010
amt1=amt
if amt in L:
    print("To generate Rs", amt1, "minimum change required is :",amt)
else:
    x=[]
    indx=len(L)+1
    while amt != 0:
        amt,indx=check(amt,indx)
    print("To generate Rs",amt1,"minimum change required is :",x)

