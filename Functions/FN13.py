# # File Created By Python
# Write a Python program to sort a list of tuples using Lambda.
myList = [('ram', 58), ('hari', 50), ('gita', 69), ('Will', 92)]
myList.sort(key=lambda x: x[1])
print(myList)
