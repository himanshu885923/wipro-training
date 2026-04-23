# 2. Write a program that takes a year as input and checks if it is a leap year or not.
# Print the result.

year = int(input("Enter Year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a leap year")