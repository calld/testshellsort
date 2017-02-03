#for the putpose of comparison, first value split
#
# def quicksort(l, compare = lambda x, y: x <= y):
#     def Divide(unsort):
#         if not unsort:
#             return unsort
#         partition = unsort.pop()
#         left = [element for element in unsort if not compare(partition, element)]
#         right = [element for element in unsort if compare(partition, element)]
#         result = Divide(left)
#         result.append(partition)
#         result.extend(Divide(right))
#         return result
#     return Divide(l)

def quicksort(l, compare = lambda x, y: x <= y):
    def sort(left, right):
        def Partition(left, right, ppos):
            '''partitions the list l around the value at ppos and return ppos's new postion'''
            #ppos = pivot position
            pivot = l[ppos]
            if right - left < 1:
                return ppos
            def exchange(i, j):
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
            exchange(ppos, right)
            i = left
            for j in range(left, right):
                if compare(l[j], l[right]):
                    exchange(i, j)
                    i = i + 1
            exchange(i, right)
            return i

        def median(a, b, c):
            """return the median of three elements"""
            if compare(l[a], l[b]):
                if compare(l[b], l[c]):
                    return b
                elif compare(l[a], l[c]):
                    return c
                else:
                    return a
            else:
                if compare(l[a], l[c]):
                    return a
                elif compare(l[c], l[b]):
                    return b
                else:
                    return c

        if left < right:
            part = median(left, right, (right+left)//2)
            part = Partition(left, right, part)
            sort(left, part-1)
            sort(part+1, right)
    sort(0, len(l)-1)
    return l
