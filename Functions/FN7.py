# File Created By Python
# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String: 'The quick Brow Fox'
# Expected Output:
# No. of Upper case characters: 3
# No. of Lower case Characters: 12


def FindletterInfo(myString):
    uppercase = 0
    lowercase = 0
    for i in myString:
        if(i == ' '):
            continue
        elif(i.isupper()):
            uppercase += 1
        else:
            lowercase += 1
    return f"Uppercase {uppercase} \nLowercase {lowercase}"


print(FindletterInfo("The quick Brow Fox"))
