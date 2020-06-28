# Write a Python script to concatenate following dictionaries to create a new
# one.
# Sample Dictionary:
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# Expected Result: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}


def Clone(cloneList):
    return cloneList


finalList = Clone(dic1)


for keys, value in dic2.items():
    finalList[keys] = value
for keys, value in dic3.items():
    finalList[keys] = value

print(finalList)
