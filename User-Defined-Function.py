# This is a Sample Program to show how to Define a Function

print("Sample Program to show how to Define a Function")

myValue = 1

def myFunction():
	global myValue
	print('This print statement is printed from inside a normal user-defined function')
	print('I have been called '+str(myValue)+' times')
	myValue = myValue +1

myFunction()
myFunction()
myFunction()

# This is a Sample Program to show Functions accepting Parameters

print("A Sample Program to show functions accepting arguments")

def anotherFunction(name):
	print('Hello There ! '+name)

anotherFunction('Jiby')
anotherFunction('Joje')