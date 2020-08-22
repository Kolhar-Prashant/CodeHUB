nums = [5, 7, 9, 1, 2, 4, 6, 8, 3] # Provide array here.
nums = sorted(nums)
a = 0
b = 1
c = len(nums) - 1
Tri_set = []
tar = 21                           # Provide target.
while (a != len(nums) - 2):
    mem = []
    sum = nums[a] + (nums[b] + nums[c])
    if sum == tar:
        mem.append(nums[a])
        mem.append(nums[b])
        mem.append(nums[c])
        b += 1
        if mem not in Tri_set:
            Tri_set.append(mem)
    elif sum > tar:
        c -= 1
    elif sum < tar:
        b += 1
    if b == c:
        a += 1
        b = a + 1
        c = len(nums) - 1
print(Tri_set)