# #File Created By Python
# Write a Python program to find intersection of two given arrays using
# Lambda.

 
arr1 = [1,2,3,4,5]
arr2 = [1,3,5,6]

result =list(filter(lambda x:x in arr1,arr2))
print(result)