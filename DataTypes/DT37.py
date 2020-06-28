# File Created By Python
# . Write a Python program to multiply all the items in a dictionary.
myDict = {1: 10, 2: 20}
multiply = 1
for key, value in myDict.items():
    multiply *= value
print(multiply)
