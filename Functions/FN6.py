# File Created By Python
# Write a Python function to check whether a number is in a given range.


def FindInrange(num, rangeNum):
    if num in range(rangeNum):
        return True
    else:
        return False


print(FindInrange(2, 3))
