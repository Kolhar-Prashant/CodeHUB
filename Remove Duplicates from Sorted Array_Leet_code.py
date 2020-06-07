def check (nums):
    curr=0
    next=1
    while(curr != next):
        if next > len(nums)-1:
            next=len(nums)-1
            continue
        if (nums[curr] == nums[next]):
            nums.remove(nums[next])
        else:
            curr+=1
            if curr != len(nums)-1:
                next=curr+1
            else:
                next=curr
    print(nums)
    print(len(nums))
L= [1,1,1,1,2]
check(L)