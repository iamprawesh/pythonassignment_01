# #File Created By Python
# . Write a Python program to filter a list of integers using Lambda.
mynumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = list(filter(lambda n: n % 2 == 0, mynumber))
print(evens)
