# This is the Python file for week 2
choices = ["Rock", "Paper", "Scissors"]
test = [1,2,3]
playerChoice = int(input("Enter a number...\n1 > Rock\n2 > Paper\n3 > Scissors\n"))
if playerChoice not in [1,2,3]:
    print("Error: Choice must be between 1 and 3")
    exit(1)

