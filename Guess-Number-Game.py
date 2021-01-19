# This is a random Number guessing game

import random

print ('This is a random number guessing game')

print('Please enter your name: ')
myName = input()

print ('Hi There '+ myName + '! I am guessing a number between 1 and 20')
secretNumber =  random.randint(1,20)

for guessesTaken in range (1, 7):
	print('Take a Guess')
	myGuess = input()

	if (int(myGuess) < secretNumber):
		print('Your Guess is too low')
	elif (int(myGuess) > secretNumber):
		print ('Your Guess is too high')
	else:
		break

if int(myGuess) ==  secretNumber:
	print('Congrats '+ myName + ', You guessed the correct number in '+str(guessesTaken)+' guesses. And the number is '+ str(secretNumber))
else:
	print('You have used all the 6 guesses and the correct number is '+ str(secretNumber))