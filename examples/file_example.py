import json

user_input = input("What do you want to be saved to the files --> ")

try:
  with open("example.txt", "w") as file:
    file.write(user_input)
