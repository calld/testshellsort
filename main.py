import shellsort as ss
import random as ran

reverselist = [x for x in range(10000, 0, -1)]

randomlist = [ran.randrange(1000000) for x in range(10000)]

print("before: " + " ".join(map(lambda x: str(x), reverselist)) + "\n")
ss.shellsort(reverselist)
print("after: " + " ".join(map(lambda x: str(x), reverselist)) + "\n")

print("before: " + " ".join(map(lambda x: str(x), randomlist)) + "\n")
ss.shellsort(randomlist)
print("after: " + " ".join(map(lambda x: str(x), randomlist)) + "\n")
