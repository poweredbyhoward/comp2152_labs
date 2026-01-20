# This is the Python file for week 2
import random
import time

choices = ["Rock", "Paper", "Scissors"]
playerScore = 0

while True:
    playerChoice = int(input("Enter a number...\n\t1 > Rock\n\t2 > Paper\n\t3 > Scissors\n\t0 > EXIT\n"))

    if playerChoice == 0:
        exit(0)
    elif playerChoice not in [1,2,3]:
        print("Error: Choice must be between 1 and 3")
        exit(1)
    else:
        print("Generating computer's choice", end='')
        for i in range(3):
            print(".", end='')
            time.sleep(0.7)
        computerChoice = random.randint(1,3)

        playerChoiceIndex = choices[playerChoice - 1]
        computerChoiceIndex = choices[computerChoice - 1]

        print(f"Player's choice: {playerChoiceIndex}")
        print(f"Computer's choice: {computerChoiceIndex}\n")
        time.sleep(1)

        if playerChoice == computerChoice:
            print("It's a tie!\n")
        elif playerChoice == 1 and computerChoice == 3:
            print("Rock beats Scissors - You win!\n")
            playerScore += 1
        elif playerChoice == 2 and computerChoice == 1:
            print("Paper beats Rock - You win!\n")
            playerScore += 1
        elif playerChoice == 3 and computerChoice == 2:
            print("Scissors beats Paper - You win!\n")
            playerScore += 1
        else:
            print("You lose!\n")
            playerScore -= 1
        print(f"Current score: {playerScore}\n")

        if playerChoice != 1:
            print("**You didn't choose the classic Rock...**\n")

        input("Press ENTER to continue...\n")
