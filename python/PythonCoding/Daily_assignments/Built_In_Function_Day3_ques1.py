# ques1-
# Do the following in a single program using built-in functions
# Take a list of numbers as input and print the largest and smallest numbers in the list.
# Take a string as input and print the length of the string.
# Take a list of names as input and print the list in alphabetical order.
# Take a list of numbers as input and print the total sum of the elements in the list.
# Takes a string as input and print the string in uppercase.

nums = list(map(int, input("Enter numbers: ").split()))
print("Largest:", max(nums))
print("Smallest:", min(nums))

text = input("Enter a string: ")
print("Length:", len(text))

names = input("Enter names: ").split()
print("Sorted names: ", sorted(names))

nums2 = list(map(int, input("Enter numbers again: ").split()))
print("Sum:", sum(nums2))

text2 = input("Enter string:")
print("Uppercase:", text2.upper())
