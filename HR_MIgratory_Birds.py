def migratoryBirds(arr):
    L = arr
    d = {}
    min = L[0]
    L = sorted(L)
    for num in L:
        if num not in d:
            if num < min:
                min = num
            d[num] = 1
        else:
            cnt = d[num]
            cnt += 1
            d[num] = cnt
    max = min
    max_rep_type = []

    for type, count in d.items():
        if count > max:
            max_rep_type.append(type)
            max = count
    return max_rep_type[-1]  