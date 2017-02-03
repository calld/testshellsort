
import itertools

def gaps(maxgap = 25, maxlen = 7):
    allgaps = [x for x in range(maxgap, 1, -1)]
    for leng in range(1, maxlen):
        for comb in itertools.combinations(allgaps, leng):
            yield list(comb) + [1]
