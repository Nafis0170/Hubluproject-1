#dice rolling simulator
import random
#random module is a build in moduleimport random
DiceRolling=True
while DiceRolling:
    print(random.randint(1,6))

# Difference between randit and randrange is that
# randrange doesn't include endpoint of range but randint does.

    playagain=input("Do you want to play again[yes/no].\n Input valid option")
    if playagain=="yes":
        continue

    else:
        print("Game over")
        break
