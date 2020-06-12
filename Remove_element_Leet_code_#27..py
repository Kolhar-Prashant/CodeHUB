def removeElement(nums,val):
    first = 0
    while (first != len(nums)):
        if nums[first] == val:
            nums.remove(nums[first])
        else:
            first += 1
    return (len(nums))

L=[3,2,2,3]
val = 3
Len=removeElement(L,val)
print("Length : ",Len)