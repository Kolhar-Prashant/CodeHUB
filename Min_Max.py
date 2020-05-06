
L=[12,-950,13,150,-98,55,32]

max=L[0]
min=L[0]

for e in L:
    if e > max:
        max=e
    if e < min:
        min=e
print(max,min)