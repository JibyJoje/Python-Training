# This is an Example for While Loops

print('Entering the While Loop')
print('Enter the Password:')
Password = input()
while (Password != "Password"): #This is where the condition of the while loop is checked
	print('You entered the wrong password. Access Denied')
	print('Please retry: ')
	Password = input()
print('Welcome, Nice to have you back')

#This is a Example of a Infinite While Loop which is forced to Exit with a Break Statement

print('Entering the Infinite While Loop which exits with a Break Statement')
while True:
	print("Inside the Infinite While Loop")
	print ("Type in 'Break' if you want to break the Infinite Loop")
	userInput = input()
	if (userInput=='Break'):
		break
print('Exiting the Infinite While Loop')

