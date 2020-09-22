
x=[4586,7,8,10,12,5,17,19,4]

min=x[0]
max=x[0]
for e in x:    
    if e < min:
        min = e
    if e > max:
        max=e
print(min,max)
