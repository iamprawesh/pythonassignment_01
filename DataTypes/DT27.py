# Write a Python program to replace the last element in a list with another list.
# Sample data: [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]


def replaceLastElement(myList, addToLast):
    myList = myList[:-1] + addToLast
    return(myList)


myList = [1, 3, 5, 7, 9, 10]
addtoLast = [12, 13, 14, 15]

print(replaceLastElement(myList, addtoLast))
