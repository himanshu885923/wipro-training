# 5. Write a program that takes a password as input and checks if it is strong (at least
# 8 characters). Print a message based on the result.


pwd = input("Enter a password: ")

if len(pwd) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
