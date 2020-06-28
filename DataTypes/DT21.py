# Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)

myList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def quickSort(sequence):
    length = len(sequence)
    if(length <= 1):
        return sequence
    else:
        pivot = sequence.pop()
    item_larger = []
    item_small = []
    for item in sequence:
        if(sum(item) > sum(pivot)):
            item_larger.append(item)
        else:
            item_small.append(item)
    return quickSort(item_small) + [pivot] + quickSort(item_larger)


print(quickSort(myList))
