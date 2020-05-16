def convert(s):
    s=str(s)
    L=s.split(":")
    sec=L[2]
    if s == "12:00:00AM":
        s="00:00:00"
        return s
    elif s == "12:00:00PM":
        s="12:00:00"
        return s
    elif 'AM' in sec:
        L=s.split(":")
        h=int(L[0])
        if h == 12:
            h=int(L[0])-12
            h=str(h).replace('0','00')
        else:
            h=h*10        
            h=list(str(h))
            temp=h[1]
            h[1]=h[0]
            h[0]=temp
            h=str(h).replace(",","")
            h=str(h).replace("'","")
        L[0]=h
        L=str(L).replace("A","")
        L=str(L).replace("M","")
        L=str(L).replace("[","")
        L=str(L).replace("]","")
        L=str(L).replace(",",":")
        L=str(L).replace("'","")
        L=str(L).replace(" ","")
        return L
    else:
        L=s.split(":")
        h=int(L[0])
        if h != 12:
            h=int(L[0])+12
            L[0]=h
        L=str(L).replace("P","")
        L=str(L).replace("M","")
        L=str(L).replace("[","")
        L=str(L).replace("]","")
        L=str(L).replace(",",":")
        L=str(L).replace("'","")
        L=str(L).replace(" ","")
        return L
s="04:54:48AM"

print("Time in 12 hour format",s)
x=convert(s)
print("Time in 24 hour format",x)
