# #File Created By Python
# Write a Python program to sort a list of dictionaries using Lambda.


myList = [
    {"name": 'ram', 'marks': 56},
    {"name": 'hari', 'marks': 54},
    {"name": 'gita', 'marks': 70},
    {"name": 'will', 'marks': 40},
]
sorted = sorted(myList, key=lambda x: x['marks'])
print('Sorted Dict :')

print(sorted)
