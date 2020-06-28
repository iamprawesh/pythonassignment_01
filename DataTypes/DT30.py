# Write a Python script to check whether a given key already exists in a
# dictionary.


def CheckKeyExist(myDict, key):
    if key in myDict:
        return True
    return False


dic1 = {1: 10, 2: 20}

print(CheckKeyExist(dic1, 1))
