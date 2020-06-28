# File Created By Python
# Write a Python function to multiply all the numbers in a list.
# Sample List: (8, 2, 3, -1, 7)
# Expected Output: -336
def SumOfList(myList):
    sum = 1
    for i in myList:
        sum *= i
    return sum


print(SumOfList([1, 2, 3, 4]))
