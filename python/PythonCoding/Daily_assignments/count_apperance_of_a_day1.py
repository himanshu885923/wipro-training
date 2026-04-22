text = input("Enter A str")

count = 0

for index, char in enumerate(text):
    if char == 'a':
        count += 1
print(count)