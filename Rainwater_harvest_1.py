def calculate(L):
    left = 0
    center = 1
    right = 2
    unit = 0
    level = 1
    x = sorted(L)
    highest = x[-1]
    cnt = L.count(highest)
    if cnt > 1:
        highest += 1
    temp_inc = 1
    FLAG = 0
    short_pillar = 0
    last_pillar = len(L)
    temp = 0
    pit_to_be_fill = []

    while (level != highest):
        while (right != last_pillar):
            # print(L[left], L[center], L[right])
            if L[center] < level:
                if L[left] > L[center] and L[right] > L[center]:
                    unit += 1
                    L[center] = level  # filling pit
                    left += 1
                    center += 1
                    right += 1
                    continue
            if L[left] > L[center] and L[center] == L[right]:  # filling pit till the wall hits
                temp = right
                pit_to_be_fill.append(center)
                while (L[right] <= L[center]):
                    temp_inc += 1
                    pit_to_be_fill.append(right)
                    if right == last_pillar and last_pillar <= L[center]:
                        FLAG = 0
                    right += 1
                    FLAG = 1
                right = temp
                if FLAG == 1:
                    unit += temp_inc
                    temp_inc = 1
                    FLAG = 0
                    left += 1
                    center += 1
                    right += 1
                for indx in pit_to_be_fill:  # filling pit
                    L[indx] = level
                pit_to_be_fill = []
                # print(L)
            else:
                left += 1
                center += 1
                right += 1
                # print("At level",level,"unit incremented",unit)
        level += 1
        left = 0
        center = 1
        right = 2
    print(unit)
    
n = int(input())
L = list(map(int, input().split()))
calculate(L)