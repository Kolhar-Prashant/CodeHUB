x=[]
def botm_top(col):
    c=col
    for r in reversed(range(n)):
        x.append(L[r][c])
    curr = L[r][c]
    c+=1
    if curr % 2 != 0:
        if c < m:
            botm_top(c)
    else:
        if c < m:
            top_botm(c)

def top_botm(col):
    c=col
    for r in range(n):
        x.append(L[r][c])
    curr = L[r][c]
    c+=1
    if curr % 2 != 0:
        if c < m:
            botm_top(c)
    else:
        if c < m:
            top_botm(c)

if __name__=="__main__":

	L=[] #2D Matrix
	temp=[]
	m= int(input())  #enter input at runtime
	n= int(input())  #enter input at runtime
	if (m > 1 and  m < 10) and (n > 1 and  n < 10):
		for row in range(n):
			for ele in range(m):
				temp.append(int(input()))  #enter input at runtime
			L.append(temp)
			temp=[]
		Len=len(L[0])-1
		top_botm(0)
		x.append("END")
		x=str(x).replace("[","")
		x=str(x).replace("]","")
		x=str(x).replace("'","")
		print(x)
	else:
		print("Invalid matix values")