# ques4 - Do the following in sequence and record the results in a single program
# Create a dictionary with your name, age, and favorite hobby as keys, and provide
# appropriate values. Print the dictionary.
# Access and print the value associated with your name in the dictionary.
# Add a new key-value pair for your favorite food, then update the value for your favorite
# hobby. Print the updated dictionary.
# Print all the keys and all the values in the dictionary separately.
# Remove the age key-value pair from the dictionary. Print the dictionary to see the
# change.


info = {
    "name" : "Himanshu",
    "age" : 22,
    "hobby" : "Gaming"
}
print("Intial data:", info)

print("Name value:", info.get("name"))

info["food"] = "Burger"
info["hobby"] = "Traveling"
print("After update:" , info)

print("All Keys:", list(info.keys()))
print("All values:", list(info.values()))

del info["age"]
print("Final data:", info)