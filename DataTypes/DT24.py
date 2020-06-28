# Write a Python program to clone or copy a list.

def Clone(x):
    return x[:]


x = [1, 2, 3]
y = Clone(x)
print(y)
