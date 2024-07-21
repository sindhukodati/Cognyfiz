import random

# Generate random number
hidden_number = random.randint(1, 10)

# Set number of attempts
attempts = 3

# Start game loop
while attempts > 0:
  # Get player guess
  try:
    guess = int(input("Guess a number between 1 and 10: "))
  except ValueError:
    print("Invalid input! Please enter a number.")
    continue  # Skip to the next iteration of the loop if input is not a number

  attempts -= 1  # Reduce attempts after each guess

  # Check guess
  if guess == hidden_number:
    print("Congratulations! You guessed the number!")
    break  # Exit loop on correct guess
  elif guess > hidden_number:
    print("Too high! Guess lower.")
  else:
    print("Too low! Guess higher.")

# Game over message
if attempts == 0:
  print("Out of attempts! The hidden number was:", hidden_number)
