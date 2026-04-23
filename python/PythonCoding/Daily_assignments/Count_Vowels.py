# 11. Write a program that uses a for loop to count the number of vowels in a given
# string. Print the count.

txt = input("Enter text: ")
count = 0

for ch in txt.lower():
    if ch in "aeiou":
        count += 1
print("Total Vowels:", count)