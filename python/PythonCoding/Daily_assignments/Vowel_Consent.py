# 4. Write a program that takes a character as input and checks if it is a vowel or
# consonant. Print the result.

char = input("Enter a letter: ").lower()

if char in "aeiou":
    print("Vowel")
else:
    print("Constant")