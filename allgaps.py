
import itertools

def gaps(maxgap = 100, maxlen = 10):
    allgaps = [x for x in range(maxgap, 1, -1)]
    for leng in range(1, maxlen):
        for comb in itertools.combinations(allgaps, leng):
            yield list(comb) + [1]
