# File Created By Python
# . Write a Python program to unpack a tuple in several variables.
myDict = {1: 10, 2: 20}
multiply = 1
for key, value in myDict.items():
    multiply *= value
print(multiply)
