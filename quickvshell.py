import quicksort as qs
import shellsort as ss
import random as ran
import timeit

gaps = [100, 59, 39, 27, 21, 16, 13, 11, 9, 4, 1] #best result from evolution search


def ranlist(size = 1000, rang = 10000):
    return [ran.randrange(rang) for x in range(size)]

n = 1000

testset = [[]] + [ranlist() for x in range(n)]

def testiter(inp):
    for x in [y[:] for y in inp]:
        yield x

testsetup = 'ti = testiter(testset); next(ti)'

qtime = timeit.timeit('qs.quicksort(next(ti))', testsetup, number = n, globals = globals())
stime = timeit.timeit('ss.shellsort(next(ti), gaps = gaps)', testsetup, number = n, globals = globals())

print("quicksort time: {}".format(qtime))
print("shellsort time: {}".format(stime))
