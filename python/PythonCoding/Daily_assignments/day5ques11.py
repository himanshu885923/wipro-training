try:
    f = open("output.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("Error: File not found")

finally:
    print("Program completed")