# . Write a program that takes a grade (A, B, C, D, F) as input and uses match-case
# to print a message corresponding to the grade (e.g., "Excellent" for A, "Good" for
# B, etc.).

grade = input("Enter grade: ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Poor")
    case "F":
        print("Fail")
    case _:
        print("invalid input")

