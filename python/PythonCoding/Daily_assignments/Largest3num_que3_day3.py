# ques3 - Write a user-defined function factorial(n) that takes a positive integer n as an argument
# and returns its factorial. Use the function in a program and print the factorial of a given
# number.

def find_largest(a,b,c):
    return max(a,b,c)

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

print("Largest num: ", find_largest(a,b,c))