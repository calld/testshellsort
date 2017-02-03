import shellsort as ss
import quicksort as qs
import insertsort as ins
import random as ran
import timeit
from allgaps import gaps

'''compares shellsort to other '''

reverselist = [x for x in range(100, 0, -1)]

#randomlist = [ran.randrange(1000) for x in range(100)]

def ranlist(size = 1000, rang = 10000):
    return [ran.randrange(rang) for x in range(size)]

#print("before: " + " ".join(map(str, reverselist)) + "\n")
print("Reverselist:")
timeSS = timeit.timeit('ss.shellsort(reverselist[:])', number = 1, globals = globals())
#timeSort = timeit.timeit('sorted(reverselist)', number = 100, globals = globals())
timeQS = timeit.timeit('qs.quicksort(reverselist[:])', number = 1, globals = globals())
timeIS = timeit.timeit('ins.insertionsort(reverselist[:])', number = 1, globals = globals())
#print("after: " + " ".join(map(str, reverselist)) + "\n")
print("completion shellsort:\t\t" + str(timeSS) + "\ncompletion quicksort:\t\t" + str(timeQS) + "\ncompletion insertionsort:\t" + str(timeIS))
#print("before: " + " ".join(map(str, randomlist)) + "\n")
print("Randomlists:")
timeSS = timeit.timeit('ss.shellsort(ranlist())', number = 100, globals = globals())
#timeSort = timeit.timeit('sorted(randomlist)', number = 100, globals = globals())
timeQS = timeit.timeit('qs.quicksort(ranlist())', number = 100, globals = globals())
#timeIS = timeit.timeit('ins.insertionsort(ranlist())', number = 100, globals = globals())
#print("after: " + " ".join(map(str, randomlist)) + "\n")
print("completion shellsort:\t\t" + str(timeSS) + "\ncompletion quicksort:\t\t" + str(timeQS) + "\ncompletion insertionsort:\t" + str(timeIS))

def infiter(l):
    i = 0
    while True:
        yield l[i]
        i = (i+1)%len(l)

testcasecount = 5
testset = infiter([[x for x in range(1000)], [x for x in range(1000, 0, -1)], ranlist(), ranlist(), ranlist()])

testcase = 'ss.shellsort(next(testset)[:], gaps = currentgaps)'
currentgaps = [1]
topshellsorts = [(10, 0) for x in range(10)]
for gs in gaps():
    currentgaps = gs
    result = (timeit.timeit(testcase, number = testcasecount, globals = globals()), gs)
    for i in range(len(topshellsorts)):
        if result[0] < topshellsorts[i][0]:
            topshellsorts = topshellsorts[:i] + [result] + topshellsorts[i:-1]
            break



for x in range(10):
    print(topshellsorts[x])
