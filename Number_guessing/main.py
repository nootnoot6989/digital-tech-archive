import random

# Introduction
print("Number Guessing Game")
print("Coded by Charlie Tournier for Western Heights College")
print("https://github.com/nootnoot6989")
print("")

# Difficulty screen
print("Choose a difficulty:")
print("")
print("Easy - Between 1 - 10")
print("Normal - Between 1 - 25")
print("Hard - Between 1 - 50")
print("Insane - Between 1 - 100")
print("Lunatic - Between 1 - 250")
print("Custom - Between 1 - your choice of number")
print("")
diff = input("Please input first letter of diffculty: ").upper()
if diff == "E":
  numran = 10
elif diff == "N":
  numran = 25
elif diff == "H":
  numran = 50
elif diff == "I":
  numran = 100
elif diff == "L":
  numran = 250
elif diff == "C":
  custom = int(input("Please input a number range: "))
  numran = custom
elif diff == "G":
  numran = 1000
  print("")
  print("ENTERING GOD MODE")
else:
  print("")
  print(f"Input {diff} is invaild please try again.")
  exit()

# Generate random based on the difficulty the user has selected.
number = random.randint(1, numran)

print("")

# Set up attempt count.
tries = 0

while True:

  # Asks user to guess a number.
  guess = int(input(f"Guess a number between 1 and {numran}: "))

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
