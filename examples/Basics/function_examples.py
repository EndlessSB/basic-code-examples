import time as t # import time and set it as t
import random as r # import random and set it as r

print("Welcome to a game!!!!")

def get_number(): # Iniital defintion of the function
    number = r.randint(1,100) # Set number , using random.randint(1,100) or in our case r.randint becaucase of line #2 , 
    return number # return the previously set number

while True: # Infinite loop
    number = get_number() # Use the get_number() function to set the varible number
    print(f"Your number is {number}!!") # print the number
    t.sleep(3) # Sleep so it isnt going too fast