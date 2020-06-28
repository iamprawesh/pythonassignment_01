# File Created By Python
# Write a Python program to reverse a string.
# Sample String: "1234abcd"
# Expected Output: "dcba4321"
def ReverseString(myString):
    reverse = ''
    index = len(myString)
    print(index)
    while index > 0:
        reverse += myString[index-1]
        index = index-1
    return reverse


print(ReverseString('1234abcd'))
