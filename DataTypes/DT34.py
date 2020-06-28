# Write a Python script to merge two Python dictionaries.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}


def CloneandMerge(dict1, dic2):
    for keys, value in dic2.items():
        dic1[keys] = value
    return dict1


dic = CloneandMerge(dic1, dic2)
print(dic)
