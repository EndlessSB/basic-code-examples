import random as r

# Varibles

game = True

number = r.randint(1,30)

# Introduction print statement
print("Welcome to the random number game! The number is between 1 and 30!")

# While the game is still going keep going
while game == True:
    # Get the guess from the user
    guess == input("Guess a number! --> ")
    # if guess is over number say its higher
    if guess > number:
      print("Your guess is higher then the number")
    # If guess is lower then number tell them
    elif guess < number:
      print("Your guess is lower then the number")
    # If the guess is correct tell them
    elif guess == number:
      print(f"Your correct! The number was {number}")
      # Stop the game [ref line #5 and line #13]
      game = False
  
