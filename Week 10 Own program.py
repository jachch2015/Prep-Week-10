#This program rolls a 12 sided dice, if you roll equal or less than 6 you lose else you win.

import random
roll=random.randint(1,12)
if roll < 6:
    print(roll)
    print("You won, your roll was greater than 6")
elif roll >=6:
    print(roll)
    print("You lost, your number was less/equal to 6")

    
