# This is the Python file for week 2
import random
import time

choices = ["Rock", "Paper", "Scissors"]

playerChoice = int(input("Enter a number...\n1 > Rock\n2 > Paper\n3 > Scissors\n"))

if playerChoice not in [1,2,3]:
    print("Error: Choice must be between 1 and 3")
    exit(1)
else:
    print("Generating computer's choice", end='')
    for i in range(3):
        print(".", end='')
        time.sleep(0.5)
    computerChoice = random.randint(1,3)

    playerChoiceIndex = choices[playerChoice - 1]
    computerChoiceIndex = choices[computerChoice - 1]

    print(f"Player's choice: {playerChoiceIndex}")
    print(f"Computer's choice: {computerChoiceIndex}\n")

    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats Scissors - You win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock - You win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper - You win!")
    else:
        print("You lose!\n")

    if playerChoice != 1:
        print("You didn't choose the classic Rock...")

