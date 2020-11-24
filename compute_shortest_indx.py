def compute_nearst_indx(nums,val):
    if val not in nums:
        return -1
    indx = 0
    avail_indx = []

    while indx != len(nums):  # Storing the index of val
        if nums[indx] == val:
            avail_indx.append(indx)
        indx+=1

    indx = 0
    Fin_indx = []
    while indx != len(nums):  # looping from 0th to n-1
        if indx in avail_indx:   # if index is available in avail_indx list then putting 0 value
            Fin_indx.append(0)
        else:                       # else looping and check which index is nearest to indx and putting the nearest value
            min_indx = len(nums)
            for index in avail_indx:
                low = abs(indx - index)
                if low < min_indx:
                    min_indx = low
            Fin_indx.append(min_indx)
        indx += 1
    return (Fin_indx)

nums = [2, 1, 4, 5, 6, 2, 3]
value = 2

indx = compute_nearst_indx(nums,value)
print(indx)