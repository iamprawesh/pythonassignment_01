# #File Created By Python
# Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number
import random


def MultiplyRandom(num):
    n = random.random() * 10
    return num * round(n)


print(MultiplyRandom(5))
