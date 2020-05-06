
def check(front, next_f, rear, i):
    joint_sum = L[next_f] + L[rear]
    sum = L[front] + joint_sum
    if rear - next_f <= 0:
        if rear - front <= 2:
            i = 0
            return (front, next_f, rear, i)
        else:
            front += 1
            next_f = front + 1
            rear = len(L) - 1
            i = -1
            return (front, next_f, rear, i)
    if sum == tar:
        print("{}, {} and {}".format(L[front], L[next_f], L[rear]))
        next_f = front + 1
        rear -= 1
        i = -1
        return (front, next_f, rear, i)
    elif sum > tar:
        rear -= 1
        i = -1
        return (front, next_f, rear, i)
    elif sum < tar:
        next_f += 1
        i = -1
        return (front, next_f, rear, i)


if __name__ == "__main__":

    n = int(input())
    s = str(input())

    s = str(s).replace(" ", ",")
    L = []
    x = s.split(",")
    for e in x:
        L.append(int(e))
    L = sorted(L)
    Len=len(L)

    if Len > 1 and Len < 1000:
        tar = int(input())
        front = 0
        rear = len(L) - 1
        next_f = front + 1
        joint_sum = 0
        sum = 0
        i = -1

        while (i != 0):
            front, next_f, rear, i = check(front, next_f, rear, i)

