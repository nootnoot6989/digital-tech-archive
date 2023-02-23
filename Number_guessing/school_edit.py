# Introduction
print("Number Guessing Game")
print("Coded by Charlie Tournier for Western Heights College")
print("https://github.com/nootnoot6989")
print("")

import random

def player_guess():
  tries = 1

  numinput = int(input("Please input the number range: "))
  number = random.randint(1, numinput)
  
  while True:
      
      tries = 1

      # Asks user to guess a number.
      guess = int(input(f"Guess a number between 1 and {numinput}: "))

      # Output the results, hints to go higher or lower if the answer was wrong, ends the game if the number was right.
      # If the user got the answer wrong it adds 1 to the attempt count.
      if guess == number:
        print(f"You guessed {guess}. You got it right!")
        print(f"It took you {tries} attempts to get that number!")
        break
      elif guess > number:
        print(f"You guessed {guess}. You got it wrong, guess a bit lower!")
        tries += 1
      elif guess < number:
        print(f"You guessed {guess}. You got it wrong, guess a bit higher!")
        tries += 1

def computer_guess():
  tries = 0

  low = 1
  high = int(input("Please input the number range: "))
  feedback = ''
  
  while feedback != "C":
    tries += 1
    if low != high:
      guess = random.randint(low,high)
    else:
      guess = low
    
    feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").upper()

    if feedback == 'H':
      high = guess - 1
    elif feedback == 'L':
      low = guess + 1
  
  print(f"The computer gussed {guess}, it took the computer {tries} tries to get that number.")


game = ''

while game != "q":
  game = input("Select (P) to pick a number, (G) to guess a number or (Q) to quit the game: ").upper()
  if game == "P":
    computer_guess()
  elif game == "G":
    player_guess()
