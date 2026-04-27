from multiprocessing.pool import worker

from Daily_assignments.day5_ques1 import content

with open("output.txt" , "r") as f:
    content = f.read()

line = content .split("\n")
words = content.split()
characters = len(content)

print("Number fo lines:", len(line))
print("Number of words:", len(words))
print("Number of characters:", characters)

