

def shellsort(l, gaps = [5, 3, 1], compare = lambda x, y: x <= y):
    def traverse(begin, step):
        for i in range(begin, len(l), step):
            pos = i
            temp = l[pos]
            while pos - step >= 0 and not compare(l[pos-step], temp):
                l[pos] = l[pos - step]
                pos = pos - step
            l[pos] = temp
    for gap in gaps:
        if gap >= len(l):
            continue
        for start in range(min(gap, len(l) - gap)):
            traverse(start, gap)
    return l
