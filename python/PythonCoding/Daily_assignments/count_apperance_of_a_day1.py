# Count how many times "a" appears in a string using enumerate

text = input("Enter a string: ")

count = 0
for index, char in enumerate(text):
    if char == 'a':
        count += 1
print(count)