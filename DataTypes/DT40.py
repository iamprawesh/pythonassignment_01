# File Created By Python
# Write a Python program to add an item in a tuple.
t = (1, 2, 3)


def addTotuple(myTuple, item):
    myList = list(myTuple)
    myList.append(item)
    return tuple(myList)


print(addTotuple(t, 4))
