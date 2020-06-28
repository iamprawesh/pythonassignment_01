# Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list: [{}, {}, {}]
# Return value: True
# Sample list: [{1, 2}, {}, {}]
# Return value: False


myDict = [{1, 2}, {}, {}]


def checkEmpty(myDict):
    for item in myDict:
        if(sum(item) > 0):
            return False
    return True


print(checkEmpty(myDict))
