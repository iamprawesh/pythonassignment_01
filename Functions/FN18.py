# #File Created By Python
# Write a Python program to check whether a given string is number or not
# using Lambda.
mynum=input("ENter the string")

is_num=lambda num:True if(num.isnumeric()) else False
print(is_num(mynum))