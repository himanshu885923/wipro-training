# ques 1 - Do the following in sequence and record the results in a single program
# Create a list with 5 different types of fruits. Print the list.
# Add two more fruits to the list, then remove one fruit from it. Print the updated list.
# Access the second and fourth fruits in the list. Print them.
# Slice the list to get the first three fruits and print the result.
# Find and print the length of your list.

fruit_items = ["Apple" , "Mango" , "Banana" , "Orange", "Guava"]
print("Inital fruits:", fruit_items)

fruit_items.extend(["kiwi", "Papaya"])
fruit_items.pop(2)
print("After modification: ", fruit_items)

print("2nd fruit:", fruit_items[1])
print("4th fruit:", fruit_items[3])

print("First 3 fruits:", fruit_items[0:3])

print("Total fruits: " , len(fruit_items))
