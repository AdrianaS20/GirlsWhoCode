#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

#Create a variable to store the amount of guesses
guessTries = 0

#Build a loop to repeat the number of times
while guessTries < 3:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")
    else:
    	guess = int(guess) # converts a string to an integer

#code the logic to check to see if the code is right
    if guess == aRandomNumber:
        print("You win!")
        break
    elif guess < aRandomNumber:
        print("Guess higher.")
    else:
        print("Guess lower.")
    guessTries += 1

    if guessTries == 3:
        print("Sorry, the number was "+str(aRandomNumber)+".")
