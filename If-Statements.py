# This block of code is sample for If-Statements


print('Testing If Condition')
myName='Jiby'
if (myName=='Jiby'):
	print('Nice to meet you '+myName)
print('Exiting the "If" Block')

# This block of code is sample for If-Else Statements

print('Testing If-Else Condition')
print ('Choose any value between "Jiby" or "Joje"')
myName=input()
if (myName=='Jiby'):
	print('You Chose '+myName)
else:
	print('You chose '+myName)
print('Exiting the "If-Else" Block')


# This block of code is sample for If-Elif Statements

print('Testing If-Elif Condition')
print('Choose any value between 1 and 10')
number = input()
if (int(number)<5):
	print('You chose the value '+str(number)+' which is less than 5')
elif (int(number) > 5 and int(number) <=10):
	print('You chose the valu0e '+str(number)+' which is greater than 5')
elif (int(number)==5):
	print('You chose the number 5')
else:
	print('You chose a value greater than 10')
print('Exiting the "If-Elif" block'	)