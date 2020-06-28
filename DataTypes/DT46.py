# File Created By Python
# Write a Python program to find the length of a tuple

t = (1, 2, 3)


def findlength(myTuple):
    length = 0
    for _ in t:
        length += 1
    return length


print(findlength(t))
