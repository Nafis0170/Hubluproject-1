# Number guesing game
# For this purpose first we have to import a build in module name "random" to generate random number
import random
Randomnumber= random.randrange(1,200)
# We will generate a random number from 1 to 200 by randrange function
Userinput=int(input(" Guess your number:"))
if Userinput>Randomnumber:
    print(" The number is high")
    print(f" Real Number is {Randomnumber}")
elif Userinput<Randomnumber:
    print(" The number is low")
    print(f"The real number is {Randomnumber}")
else:
    print(" your number is right")
