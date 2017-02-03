import random as ran
import shellsort as ss
import timeit

#globals
PopulationLimit = 200
time = {}
livingspecies = [[1]]
currentgaps = [1]
testsetup = 'testiter = createiter(testset); next(testiter)'
testcase = 'ss.shellsort(next(testiter), gaps = currentgaps)'

#generate testset
def ranlist(size = 1000, rang = 10000):
    return [ran.randrange(rang) for x in range(size)]

testset = [[]] + [ranlist() for x in range(8)] + [[x for x in range(1000)], [x for x in range(1000, 0, -1)]]

def createiter(lst):
    for x in [x[:] for x in lst]:
        yield x

def nextgen(val):
    for x in [[val] + y for y in livingspecies]:
        yield x

time[(1,)] = timeit.timeit(testcase, testsetup, number = len(testset)-1, globals = globals())

for gap in range(2, 101):
    for nw in nextgen(gap):
        #print(nw)
        currentgaps = nw
        time[tuple(nw)] = timeit.timeit(testcase, testsetup, number = len(testset)-1, globals = globals())
        livingspecies.append(nw)
    if(len(livingspecies) > PopulationLimit):
        livingspecies.sort(key = lambda x: time[tuple(x)])
        livingspecies = livingspecies[:PopulationLimit]


for species in livingspecies:
    print('{}: {}'.format(species, time[tuple(species)]))
