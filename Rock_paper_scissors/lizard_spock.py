# Introduction
print("Rock, Paper, Scissors, Lizard & Spock")
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
    options = ["rock", "paper", "scissors", "lizard", "spock"]
    
    # Start loop until the amount of rounds have finshed
    while True:
        
        # Show how many rounds are left
        print("")
        print(f"{roundcount} rounds left")
        print("")
        
        # Ask the user to choose either Rock, Paper or Scissors
        playerinput = input("What will you draw? (Rock (R), Paper (P), Scissors (S), Lizard (L), or Spock (K)) ").upper()

        # Assign the input with a variables
        if playerinput == 'R':
            playerchoice = "rock"
        elif playerinput == 'P':
            playerchoice = "paper"
        elif playerinput == 'S':
            playerchoice = "scissors"
        elif playerinput == 'L':
            playerchoice = "lizard"
        elif playerinput == "K":
            playerchoice = "spock"

        # Computer makes a choice
        computerchoice = random.choice(options)

        # Little text animiation for hype
        print("")
        print("ROCK")
        time.sleep(0.3)
        print("PAPER")
        time.sleep(0.3)
        print("SCISSORS")
        time.sleep(0.3)
        print("LIZARD")
        time.sleep(0.3)
        print("SPOCK")
        time.sleep(0.3)
        print("")

        # Print what the user and computer drew
        print(f"You drew {playerchoice}")
        print(f"Computer drew {computerchoice}")

        print("")
        
        # Nested loops to decide the outcome
        # Rock crushes Scissors, Paper cover Rock, Scissors cuts Paper, Lizard poisons Spock, Spock vaporizes Rock
        # Rock crushes Lizard, Paper disproves Spock, Scissors decapitates Lizard, Lizards eats Paper, Spock smashes Scissors
        if computerchoice == "rock":
            if playerchoice == "rock":
                print("It's a Draw!")
            elif playerchoice == "paper":
                print("Paper covers Rock")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "spock":
                print("Spock vaporizes Rock")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "scissors":
                print("Rock crushes Scissors")
                print("You lost this round...")
                computerscore += 1
            elif playerchoice == "lizard":
                print("Rock crushes Lizard")
                print("You lost this round...")
                computerscore += 1
        elif computerchoice == "paper":
            if playerchoice == "paper":
                print("It's a Draw!")
            elif playerchoice == "scissors":
                print("Scissors cuts Paper")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "lizard":
                print("Lizard eats Paper")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "rock":
                print("Paper covers Rock")
                print("You lost this round...")
                computerscore += 1
            elif playerchoice == "spock":
                print("Paper disproves Spock")
                print("You lost this round...")
                computerscore += 1
        elif computerchoice == "scissors":
            if playerchoice == "scissors":
                print("It's a Draw!")
            elif playerchoice == "rock":
                print("Rock crushes Scissors")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "spock":
                print("Spock smashes Scissors")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "paper":
                print("Scissors cuts Paper")
                print("You lost this round...")
                computerscore += 1
            elif playerchoice == "lizard":
                print("Scissors decapitates Lizard")
                print("You lost this round...")
                computerscore += 1
        elif computerchoice == "lizard":
            if playerchoice == "lizard":
                print("It's a Draw!")
            elif playerchoice == "scissors":
                print("Scissors decapitates Lizard")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "rock":
                print("Rock crushes Lizard")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "paper":
                print("Lizard eats Paper")
                print("You lost this round...")
                computerscore += 1
            elif playerchoice == "spock":
                print("Lizard poisons Spock")
                print("You lost this round...")
                computerscore += 1
        elif computerchoice == "spock":
            if playerchoice == "spock":
                print("It's a Draw!")
            elif playerchoice == "lizard":
                print("Lizard poisons Spock")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "paper":
                print("Paper disproves Spock")
                print("You won this round!")
                playerscore += 1
            elif playerchoice == "rock":
                print("Spock vaporizes Rock")
                print("You lost this round...")
                computerscore += 1
            elif playerchoice == "scissors":
                print("Spock smashes Scissors")
                print("You lost this round...")
                computerscore += 1
        
        # A round passes
        roundcount -= 1

        print("")

        # Print the scoreboard
        print("Scoreborad:")
        print(f"Player: {playerscore}")
        print(f"Computer: {computerscore}")

        # If roundcount reaches 0 stop the loop
        if roundcount == 0:
            break
    
    # Print endgame results
    print("")
    if playerscore > computerscore:
        print("You Won the Game!")
    elif playerscore < computerscore:
        print("You Lost the game...")
    elif playerscore == computerscore:
        print("The game is a draw!")
    print("")

game()

option = ''

while option != "N":
    option = input("Do you want play again? (Y/N) ").upper()
    if option == "Y":
        print("")
        game()