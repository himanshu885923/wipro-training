# 8. Write a program that takes a number as input and uses a for loop to calculate its
# factorial. Print the result.

n = int(input("Enter a number: "))
fact = 1

for i in range(1 , n+1):
    fact *= i
print("Factorial =", fact)
