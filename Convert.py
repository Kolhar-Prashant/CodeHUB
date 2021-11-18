def convert(s):
    a,b=0,1
    mem = []
    while b != len(s):
        Even = None
        num1,num2 = int(s[a]),int(s[b])
        if num1 % 2 == 0 and num2 % 2 == 0:
            Even = True
        if num1 % 2 != 0 and num2 % 2 != 0:    
            Even = False
        if Even != None:
            mem.append(s[a])
            if Even == True:
                mem.append('*')
            elif Even == False:
                mem.append('-')
        else:
            mem.append(s[a])
        a+=1
        b+=1
    mem.append(s[b-1])
    return "".join(mem)
s = '21462675756'
print(convert(s))
        
