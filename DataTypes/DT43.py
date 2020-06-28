# File Created By Python
# Write a Python program to remove an item from a tuple.

t = (1, 2, 3)


def removeTuple(myTuple):
    myList = list(myTuple)
    while len(myList) != 0:
        myList.pop()
    return tuple(myList)


print(removeTuple(t))
