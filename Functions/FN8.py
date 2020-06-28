# File Created By Python
# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List: [1, 2, 3, 3, 3, 3, 4, 5]
# Unique List: [1, 2, 3, 4, 5]

def UniqueList(myList):
    resuly = []
    for i in myList:
        if i not in resuly:
            resuly.append(i)
    return resuly


print(UniqueList([1, 2, 3, 3, 3, 3, 4, 5]))
