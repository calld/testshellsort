import insertsort as ins
import shellsort as ss
import quicksort as qs
import random as ran

randomlist = [ran.randrange(1000) for x in range(100)]

def isSorted(l, compare = lambda x, y: x <= y):
    result = True
    return all(map(compare, l[:-1], l[1:]))

print("Insertionsort: {}".format(isSorted(ins.insertionsort(randomlist[:]))))
print("Shellsort: {}".format(isSorted(ss.shellsort(randomlist[:]))))
qsr = qs.quicksort(randomlist[:])
ans = sorted(randomlist)
print("Quicksort: {}".format(isSorted(qsr)))
for i in range(100):
    if not qsr[i] == ans[i]:
        print("{} {}".format(qsr[i], ans[i]))
