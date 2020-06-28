# File Created By Python
# Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number ( or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself

def IsPrime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print('Not')
                break
        else:
            print('Prime')
    else:
        print('Not a prime')


IsPrime(5)
