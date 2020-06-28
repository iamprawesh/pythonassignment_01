# Write a Python script to add a key to a dictionary.
# Sample Dictionary: {0: 10, 1: 20}
# Expected Result: {0: 10, 1: 20, 2: 30}

def addToDict(myDict):
    lastkey = list(myDict.keys())[-1]
    lastValue = list(myDict.values())[-1] + 10
    myDict[lastkey+1] = lastValue
    return myDict


myDict = {0: 10, 1: 20}
print(addToDict(myDict))
