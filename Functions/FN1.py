# File Created By Python
# Write a Python function to find the Max of three numbers.


def MaxNumber(a, b, c):
    if(a > b) and (a > c):
        return f"The Greater number is {a}"
    elif(b > a) and (b > c):
        return f"The Greater number is {b}"
    else:
        return f"The Greater number is {c}"


print(MaxNumber(2, 3, 1))
