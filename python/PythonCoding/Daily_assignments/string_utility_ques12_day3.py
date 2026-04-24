# ques 12 - Create a Package for String Utilities:
# Create a package called string_utils with two modules: string_operations.py and
# string_validations.py.
# In string_operations.py, define functions for reversing a string, converting a string to
# uppercase, and finding the length of a string.
# In string_validations.py, define functions to check if a string is a palindrome and if it
# contains only alphabetic characters.
# Write a program that imports and uses these functions from the string_utils package.

from string_utils.string_operations import reverse_text, to_upper, text_length
from string_utils.string_validations import is_palindrome, is_alpha

word = input("Enter a word: ")

print("Reversed:", reverse_text(word))
print("Uppercase:", to_upper(word))
print("Length:", text_length(word))

if is_palindrome(word):
    print("It is a palindrome")
else:
    print("Not a palindrome")

if is_alpha(word):
    print("Only letters")
else:
    print("Contains other characters")