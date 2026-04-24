
# ques2 - Write a user-defined function factorial(n) that takes a positive integer n as an argument
# and returns its factorial. Use the function in a program and print the factorial of a given
# number.


def factorial(n):
    result =1
    for i in range(1, n+1):
        result *= i
    return result

n= int(input("Enter number for factorial: "))
print("factorial:", factorial(n))


