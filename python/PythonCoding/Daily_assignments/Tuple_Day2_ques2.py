# ques 2 -Do the following in sequence and record the results in a single program
# Create a tuple with the names of 3 different cities you’d like to visit. Print the tuple.:
# Access and print the first and last elements of the tuple.:
# Create another tuple with 2 more cities. Concatenate both tuples and print the result.
# Try changing one element of the tuple. What happens?
# Unpack the elements of the tuple into separate variables and print them.


places = ("Delhi" , "Paris" , "Sydeny")
print("Cities tuple:" , places)

print("First city: ", places[0])
print("Last city:" , places[-1])

extr_places = ("Rome" , "Dubai")
combined_places = places + extr_places
print("Combined tuple:", combined_places)

print("Tuples are immutable cannot be cahnged")

a , b, c = places
print("Unpacked:", a, b, c)