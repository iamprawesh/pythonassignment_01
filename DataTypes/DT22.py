# Write a Python program to remove duplicates from a list.
myList = [1, 2, 3, 4, 1, 2]
result = []
for item in myList:
    if item not in result:
        result.append(item)
print(f"The result is {result}")
