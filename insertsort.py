

def insertionsort(l, compare = lambda x, y: x <= y):
    for i in range(1, len(l)):
        pos = i
        temp = l[pos]
        while pos > 0 and not compare(l[pos - 1], temp):
            l[pos] = l[pos-1]
            pos = pos - 1
        l[pos] = temp
    return l
