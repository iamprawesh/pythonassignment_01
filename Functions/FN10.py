# File Created By Python
# Write a Python program to print the even numbers from a given list.
# Sample List:
# Expected Result: [2, 4, 6, 8]

def IsEven(myList):
    result = []
    for i in myList:
        if i % 2 == 0:
            result.append(i)
    print(result)


IsEven([1, 2, 3, 4, 5, 6, 7, 8, 9])
