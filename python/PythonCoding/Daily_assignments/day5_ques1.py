user_text = input("Enter some text: ")

with open("output.txt", "w") as file:
    file.write(user_text)

with open("output.txt", "r") as file:
    content = file.read()

print("\nContents of output.txt:")
print(content)