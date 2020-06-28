# #File Created By Python
# . Write a Python program to create Fibonacci series upto n using Lambda.
num = 10
myfibo = [0,1]
any(map(lambda _:myfibo.append(sum(myfibo[-2:])),range(2,num)))
print(myfibo)