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


#This is an Example of While Loop with a Continue Statement

print('Entering the while loop with the continue statement')
value=0
while (value<=5):
	value+=1
	if (value==3):
		continue
	print('The Value is '+str(value))
print('Exiting the while loop')