# ques-3 Do the following in sequence and record the results in a single program
# Create a set of 5 unique colors. Print the set.
# Add a new color to the set, then try removing an existing color. Print the updated set.
# Create another set with 3 different colors. Find the intersection, union, and difference
# between both sets.
# Check if a specific color is in the set and print the result.
# Convert a list of fruits (with some duplicates) into a set and print the unique fruits.


from multiprocessing.reduction import duplicate

color_set = {"Red" , "Green" , "Blue", "Black", "yellow"}
print("Original colors:", color_set)

color_set.add("White")
color_set.discard("Green")
print("Modified colors:", color_set)

other_colors = {"Blue", "Purple", "Black"}

print("Common colors:", color_set.intersection(other_colors))
print("All colors:", color_set.union(other_colors))
print("Unique to first set:", color_set.difference(other_colors))

print(("Is 'Red' present?", "Red" in color_set))

duplicate_list = ["Apple" , "Mango" , "Apple", "Grapes" , "Mango"]
print("Unique fruits:" , set(duplicate_list))
