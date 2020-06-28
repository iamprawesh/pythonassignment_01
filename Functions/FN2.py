# #File Created By Python
# Write a Python function to sum all the numbers in a list.
# Sample List: (8, 2, 3, 0, 7)
# Expected Output: 20

def SumOfList(myList):
    sum = 0
    for i in myList:
        sum += i
    return sum


print(SumOfList([1, 2, 3, 4]))
