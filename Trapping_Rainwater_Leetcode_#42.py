def calculate(height):
    if len(height) > 0:
        L = []
        max = height[0]
        for e in height:
            if e > max:
                max = e
                L.append(max)
            else:
                L.append(max)
        # print(L)
        M = []
        max = height[-1]
        for e in reversed(height):
            if e > max:
                max = e
                M.append(max)
            else:
                M.append(max)
        M = list(reversed(M))
        # print(M)
        unit = 0
        for indx in range(len(height)):
            min_val = min(L[indx], M[indx])
            if (height[indx] > min_val):
                unit += height[indx] - min_val
            else:
                unit += min_val - height[indx]
        return unit
    else:
        return 0
L=[0,1,0,2,1,0,1,3,2,1,2,1]
unit = calculate(L)
print("Total units of water trapped : ",unit)