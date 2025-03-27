import time as t # Import time and make it t

# Varibles
points = 0

# Introduction
print("Welcome to the quiz!")

# Pause the program for 2 seconds
t.sleep(2)

# Get their name 
name = input("What is your name --> ")

# Say hello to them using their name, previously set in the last statement
print(f"Hello {name}, Welcome! This is an example quiz1")

# Ask Questions
print("What is the capital Of America?")
# Get the awnser and set it into a varibles
capital = input("Awnser --> ").lower()
# Check if their right
if capital == "washington":
  # Add a point
  points += 1
  print("You were correct!")
print("What colour is a fire hydrant?")
colour = input("Awnser --> ")
if colour == "red":
  points += 1
  print("You were corect")

# Use a f string to tell them their points
print(f"You have scored {points}! , Well done!")
