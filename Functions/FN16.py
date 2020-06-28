# #File Created By Python
# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

mynumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]

square = list(map(lambda n: n * n, mynumber))
cubes = list(map(lambda n: n*n*n, mynumber))

print(square)
print(cubes)
