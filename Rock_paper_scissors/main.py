# Introduction
print("Rock Paper & Scissors")
print("Coded by Charlie Tournier for Western Heights College")
print("https://github.com/nootnoot6989")
print("")

# Import modules
import random
import time

# Define the game funtion
def game():
    
    # Ask the user how many rounds of Rock, Paper and Scissors do they want to play
    roundcount = int(input("How many rounds do you want to play? "))
    
    # Set up variables
    playerscore = 0
    computerscore = 0
    
    # Set up choices for the user and the computer
    options = ["rock", "paper", "scissors"]
    
    # Start loop until the amount of rounds have finshed
    while True:
        
        # Ask the user to choose either Rock, Paper or Scissors
        playerinput = input("What will you draw? (Rock (R), Paper (P) or Scissors (S)) ").upper()

        # Assign the input with a variables
        if playerinput == 'R':
            playerchoice = "rock"
        elif playerinput == 'P':
            playerchoice = "paper"
        elif playerinput == 'S':
            playerchoice = "scissors"

        # Computer makes a choice
        computerchoice = random.choice(options)

        # Little text animiation for hype
        print("")
        print("ROCK")
        time.sleep(0.5)
        print("PAPER")
        time.sleep(0.5)
        print("SCISSORS")
        time.sleep(0.5)
        print("SHOOT")
        time.sleep(0.5)
        print("")

        # Print what the user and computer drew
        print(f"You drew {playerchoice}")
        print(f"Computer drew {computerchoice}")

        print("")
        
        # Rock beats Scissors, Paper beats Rock, Scissors beats Paper
        if computerchoice == "rock":
            if playerchoice == "rock":
                print("It's a Draw!")
            elif playerchoice == "paper":
                print("Paper beats Rock")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "scissors":
                print("Rock beats Scissors")
                print("You lost this round...")
                computerscore += 1
        elif computerchoice == "paper":
            if playerchoice == "paper":
                print("It's a Draw!")
            elif playerchoice == "scissors":
                print("Scissors beats Paper")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "rock":
                print("Paper beats Rock")
                print("Lose")
                computerscore += 1
        elif computerchoice == "scissors":
            if playerchoice == "scissors":
                print("It's a Draw!")
            elif playerchoice == "rock":
                print("Rock beats Scissors")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "paper":
                print("Scissors beats Paper")
                print("You lost this round...")
                computerscore += 1
        
        # A round passes
        roundcount -= 1

        print("")

        # Print the scoreboard
        print("Scoreborad:")
        print(f"Player: {playerscore}")
        print(f"CPU: {computerscore}")
        print("")

        # If roundcount reaches 0 stop the loop
        if roundcount == 0:
            break
    
    # Print endgame results
    if playerscore > computerscore:
        print("You Won the Game!")
    elif playerscore < computerscore:
        print("You Lost the game...")
    elif playerscore == computerscore:
        print("The game is a draw!")
    print("")

game()