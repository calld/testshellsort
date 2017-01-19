import shellsort as ss
import random as ran
import timeit

reverselist = [x for x in range(10000, 0, -1)]

randomlist = [ran.randrange(1000000) for x in range(10000)]

print("before: " + " ".join(map(str, reverselist)) + "\n")
time = timeit.timeit('ss.shellsort(reverselist)', number = 1, globals = globals())
print("after: " + " ".join(map(str, reverselist)) + "\n")
print("completion: " + str(time) + "\n")

print("before: " + " ".join(map(str, randomlist)) + "\n")
time = timeit.timeit('ss.shellsort(randomlist)', number = 1, globals = globals())
print("after: " + " ".join(map(str, randomlist)) + "\n")
print("completion: " + str(time) + "\n")
