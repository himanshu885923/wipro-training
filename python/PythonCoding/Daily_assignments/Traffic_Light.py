# 7. Write a program that takes a traffic light color (Red, Yellow, Green) as input and
# uses match-case to print the corresponding action (e.g., "Stop" for Red, "Wait"
# for Yellow, etc.).


color = input("Enter color: ").lower()

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid color")
